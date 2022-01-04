import torchaudio

import librosa


def pitch_shift(data, sampling_rate, pitch_factor):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)


if __name__ == "__main__":
    SOLO_DIR = "audio/solos/1_5.wav"

    audio, sr = torchaudio.load(SOLO_DIR)

    print(audio)

    audio[0] = librosa.effects.pitch_shift(audio[0], sr, 1)

    print(audio)
