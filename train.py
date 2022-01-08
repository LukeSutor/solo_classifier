import torch
import torchaudio
from torch import nn
import torch.optim as optim
from torch.utils.data import WeightedRandomSampler
from torch.utils.data import DataLoader
from torch.cuda.amp import GradScaler, autocast
from collections import Counter
from torch.utils.tensorboard import SummaryWriter
from SolosDataset import SolosDataset
# from cnn import CNNNetwork
import timm

BATCH_SIZE = 32
ACCUMULATE_STEPS = 4
EPOCHS = 300
USE_AUTOCAST = True
LEARNING_RATE = 1e-4

ANNOTATIONS_FILE = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv"
AUDIO_DIR = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"
SAMPLE_RATE = 22050
NUM_SAMPLES = 220500

if __name__ == "__main__":
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    print(f"Using {device}")

    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate=SAMPLE_RATE,
        n_fft=1024,
        hop_length=512,
        n_mels=64
    )

    sd = SolosDataset(ANNOTATIONS_FILE,
                      AUDIO_DIR,
                      mel_spectrogram,
                      SAMPLE_RATE,
                      NUM_SAMPLES,
                      device)

    # Get the number of samples for each guitarist
    trainclasses = [label for _, label in sd]
    counter = Counter(trainclasses)

    class_weights = [0] * 4
    sample_weights = torch.zeros(len(sd))

    for i in range(len(counter)):
        class_weights[i] = 1 / counter.pop(i)

    for i, (_, label) in enumerate(sd):
        class_weight = class_weights[label]
        sample_weights[i] = class_weight

    sampler = WeightedRandomSampler(
        sample_weights, num_samples=len(sample_weights), replacement=True)

    train_dataloader = DataLoader(
        sd, batch_size=BATCH_SIZE, sampler=sampler)

    # Construct model and assign it to device
    cnn = timm.create_model('efficientnetv2_s', num_classes=4)
    cnn.conv_stem = nn.Conv2d(1, 24, 3, 2, 1, bias=False)
    cnn.to(device)
    cnn.train()
    # print(cnn.modules)

    # Initialize loss function (Cross Entropy) and optimiser (Adam)
    criterion = nn.CrossEntropyLoss()
    optimiser = optim.AdamW(cnn.parameters(), lr=LEARNING_RATE)
    scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(optimiser, 5)
    scaler = GradScaler()
    writer = SummaryWriter(
        f"runs/bs{BATCH_SIZE}_as{ACCUMULATE_STEPS}_e{EPOCHS}_lr{LEARNING_RATE}_UAC={USE_AUTOCAST}_weightedSample")

    iter = 0
    for i in range(EPOCHS):
        print(f"Epoch {i+1}")
        running_loss = []
        running_correct = 0
        index = 0
        for input, target in train_dataloader:
            with autocast(USE_AUTOCAST):
                input, target = input.to(device), target.to(device)
                # calculate loss
                prediction = cnn(input)
                loss = criterion(prediction, target)

                predicted_index = prediction[0].argmax(0)
                if predicted_index.item() == target[0]:
                    running_correct += 1

            iter += 1
            index += 1

            if (iter % ACCUMULATE_STEPS == 0):
                # backpropagate error and update weights
                optimiser.zero_grad(set_to_none=True)
                loss.backward()
                optimiser.step()
                running_loss.append(loss.item())

        accuracy = running_correct / index

        print(f"accuracy: {accuracy}")
        print(f"loss: {sum(running_loss) / len(running_loss)}")
        writer.add_scalar("Loss", sum(running_loss) / len(running_loss), i+1)
        writer.add_scalar("Accuracy", accuracy, i+1)
        scheduler.step()
    print("---------------------------")
    print("Finished training")

    # Save model
    torch.save(cnn.state_dict(), "cnn_2.pth")
    print("Trained convolutional neural network saved at cnn_2.pth")
