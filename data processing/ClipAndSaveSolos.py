import wave
import contextlib
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from songs import get_songs

# Download the youtube videos as .wav files at https://loader.to/en18/youtube-wav-converter.html 
# Save the video as its name under the full_solos directory

# Transposer: https://transposr.com/songs/new
# Converter: https://www.freeconvert.com/audio-converter
# Wav converter https://songsurgeon.com/engine/ssweb/


def ClipAndSave(songname):
    def get_song_number():
        songs = get_songs()
        for i in range(len(songs)):
            if(songs[i] == songname):
                return i
        return 'SONG NOT FOUND'

    SONG_NUMBER = int(get_song_number())
    FILENAME = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/eddie_van_halen/"+songname+"_solo.wav"

    def get_duration():
        with contextlib.closing(wave.open(FILENAME,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            return duration

    # The minimized solo clip is automatically chopped down into 10 second segments
    for i in range(int(get_duration()) // 10):
        ffmpeg_extract_subclip(
        FILENAME, 
        i*10, 
        (i+1)*10, 
        targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos/{SONG_NUMBER}_{i}.wav"
        )