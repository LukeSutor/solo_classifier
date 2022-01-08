import os
import torchaudio
import torch

SAMPLE_RATE = 22050
NUM_SAMPLES = 220500


def Transform(audio_dir, device):
    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate=SAMPLE_RATE,
        n_fft=1024,
        hop_length=512,
        n_mels=64
    )

    signal, sr = torchaudio.load(audio_dir)
    signal = signal.to(device)
    # Resample to make all sample rates the same
    signal = _resample_if_necessary(signal, sr, device)

    # Make the signal mono if it isn't already
    signal = _mix_down_if_necessary(signal)

    # These next two transformations either add or subtract
    # from the signal if it's too big or small.
    # These shouldn't be needed as all audio files are
    # 10 seconds long, but they're added just in case.
    signal = _cut_if_necessary(signal)
    signal = _right_pad_if_necessary(signal)

    # Mel spectrogram transformation
    signal = mel_spectrogram(signal)
    return signal


def _cut_if_necessary(signal):
    if signal.shape[1] > NUM_SAMPLES:
        signal = signal[:, :NUM_SAMPLES]
    return signal


def _right_pad_if_necessary(signal):
    length_signal = signal.shape[1]
    if length_signal < NUM_SAMPLES:
        num_missing_samples = NUM_SAMPLES - length_signal
        last_dimension_padding = (0, num_missing_samples)
        signal = torch.nn.functional.pad(signal, last_dimension_padding)
    return signal


def _resample_if_necessary(signal, sr, device):
    if sr != SAMPLE_RATE:
        resampler = torchaudio.transforms.Resample(
            sr, SAMPLE_RATE).to(device)
        signal = resampler(signal)
    return signal


def _mix_down_if_necessary(signal):
    if signal.shape[0] > 1:
        signal = torch.mean(signal, dim=0, keepdim=True)
    return signal
