import torch
import torchaudio
from torch import nn
from torch.utils.data import DataLoader

from SolosDataset import SolosDataset
from cnn import CNNNetwork

BATCH_SIZE = 128
EPOCHS = 10
LEARNING_RATE = 0.001

ANNOTATIONS_FILE = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv"
AUDIO_DIR = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"
SAMPLE_RATE = 22050
NUM_SAMPLES = 220500

def create_data_loader(train_data, batch_size):
    train_dataloader = DataLoader(train_data, batch_size=batch_size)
    return train_dataloader


def train_single_epoch(model, data_loader, loss_fn, optimiser, device):
    for input, target in data_loader:
        input, target = input.to(device), target.to(device)        

        # calculate loss
        prediction = model(input)
        loss = loss_fn(prediction, target)

        # backpropagate error and update weights
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()

    print(f"loss: {loss.item()}")


def train(model, data_loader, loss_fn, optimiser, device, epochs):
    for i in range(epochs):
        print(f"Epoch {i+1}")
        train_single_epoch(model, data_loader, loss_fn, optimiser, device)
        print("---------------------------")
    print("Finished training")


if __name__ == "__main__":
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    print(f"Using {device}")


    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate = SAMPLE_RATE,
        n_fft = 1024,
        hop_length = 512,
        n_mels = 64
    )

    sd = SolosDataset(ANNOTATIONS_FILE, 
    AUDIO_DIR, 
    mel_spectrogram, 
    SAMPLE_RATE,
    NUM_SAMPLES,
    device)


    train_dataloader = create_data_loader(sd, BATCH_SIZE)

    # Construct model and assign it to device (GPU)
    cnn = CNNNetwork().to(device)

    # Initialize loss function (Cross Entropy) and optimiser (Adam)
    loss_fn = nn.CrossEntropyLoss()
    optimiser = torch.optim.Adam(cnn.parameters(), lr=LEARNING_RATE)

    # Train model
    train(cnn, train_dataloader, loss_fn, optimiser, device, EPOCHS)

    # Save model
    torch.save(cnn.state_dict(), "cnn.pth")
    print("Trained convolutional neural network saved at cnn.pth")