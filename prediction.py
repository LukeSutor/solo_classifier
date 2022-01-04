import torch
from torch import random
import torchaudio
import random

from SolosDataset import SolosDataset
from torch import nn


import timm

ANNOTATIONS_FILE = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv"
AUDIO_DIR = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"
SAMPLE_RATE = 22050
NUM_SAMPLES = 220500

class_mappings = [
    "Jimmy Page",
    "Eddie Van Halen",
    "David Gilmour",
    "Eric Clapton"
]

if __name__ == "__main__":
    # if torch.cuda.is_available():
    #     device = "cuda"
    # else:
    device = "cpu"
    print(f"Using {device}")

    cnn = timm.create_model('efficientnetv2_s', num_classes=4)
    cnn.conv_stem = nn.Conv2d(1, 24, 3, 2, 1, bias=False)
    cnn.load_state_dict(torch.load("cnn_2.pth"))
    # cnn.to(device)

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
    correct = 0
    for i in range(300):

        index = random.randint(0, 1199)
        # print(index)

        input, target = sd[index][0], sd[index][1]
        input.unsqueeze_(0)
        # input, target = input.to(device), target.cuda()

        cnn.eval()
        with torch.no_grad():
            predictions = cnn(input)
            predicted_index = predictions[0].argmax(0)
            predicted_guitarist = class_mappings[predicted_index]
            actual_guitarist = class_mappings[target]

            if predicted_index == target:
                correct += 1

    print(f"{correct} right out of 300, {correct / 300}% accuracy")

    # print(
    #     f"predicted: {predicted_guitarist} actual: {actual_guitarist}")
