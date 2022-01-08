import os
import torchaudio
import torch
from torch.utils.data import Dataset
import pandas as pd


class SolosDataset(Dataset):

    def __init__(self, annotations_file, audio_dir, transformation,
                 target_sample_rate, num_samples, device):
        self.annotations = pd.read_csv(annotations_file)
        self.audio_dir = audio_dir
        self.device = device
        self.transformation = transformation.to(self.device)
        self.target_sample_rate = target_sample_rate
        self.num_samples = num_samples

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        audio_sample_path = self._get_audio_sample_path(index)
        label = self._get_audio_sample_label(index)
        signal, sr = torchaudio.load(audio_sample_path)
        signal = signal.to(self.device)
        # Resample to make all sample rates the same
        signal = self._resample_if_necessary(signal, sr)

        # Make the signal mono if it isn't already
        signal = self._mix_down_if_necessary(signal)

        # These next two transformations either add or subtract
        # from the signal if it's too big or small.
        # These shouldn't be needed as all audio files are
        # 10 seconds long, but they're added just in case.
        signal = self._cut_if_necessary(signal)
        signal = self._right_pad_if_necessary(signal)

        # Mel spectrogram transformation
        signal = self.transformation(signal)
        return signal, label

    def _cut_if_necessary(self, signal):
        if signal.shape[1] > self.num_samples:
            signal = signal[:, :self.num_samples]
        return signal

    def _right_pad_if_necessary(self, signal):
        length_signal = signal.shape[1]
        if length_signal < self.num_samples:
            num_missing_samples = self.num_samples - length_signal
            last_dimension_padding = (0, num_missing_samples)
            signal = torch.nn.functional.pad(signal, last_dimension_padding)
        return signal

    def _resample_if_necessary(self, signal, sr):
        if sr != self.target_sample_rate:
            resampler = torchaudio.transforms.Resample(
                sr, self.target_sample_rate).to(self.device)
            signal = resampler(signal)
        return signal

    def _mix_down_if_necessary(self, signal):
        if signal.shape[0] > 1:
            signal = torch.mean(signal, dim=0, keepdim=True)
        return signal

    def _get_audio_sample_path(self, index):
        path = os.path.join(self.audio_dir, self.annotations.iloc[index, 0])
        return path

    def _get_audio_sample_label(self, index):
        return self.annotations.iloc[index, 1]


if __name__ == "__main__":
    ANNOTATIONS_FILE = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv"
    AUDIO_DIR = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"
    SAMPLE_RATE = 48000  # 22050
    NUM_SAMPLES = 480000  # 220500

    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    print(f"using device {device}")

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

    signal, label = sd[1199]

    page = 0
    gilmour = 0
    van_halen = 0
    clapton = 0

    # for i in range(len(sd)):
    #     guitarist = sd[i][1]
    #     if guitarist == 0:
    #         page += 1
    #     elif guitarist == 1:
    #         gilmour += 1
    #     elif guitarist == 2:
    #         van_halen += 1
    #     else:
    #         clapton += 1

    # print(
    #     f"Page: {page}, Gilmour: {gilmour}, Van Halen: {van_halen}, Clapton: {clapton}")

    ids = ImbalancedDatasetSampler(sd)
