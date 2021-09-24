import wave
import contextlib
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from songs import get_songs

# Download the youtube videos as .wav files at https://loader.to/en18/youtube-wav-converter.html 
# Save the video as its name under the full_solos directory

# Transposer: https://transposr.com/songs/new
# Converter: https://www.freeconvert.com/audio-converter
# Wav converter https://songsurgeon.com/engine/ssweb/

FILENAME = "live_at_msg"


def get_song_number():
    songs = get_songs()
    for i in range(len(songs)):
        print(songs[i])
        if(songs[i] == FILENAME):
            return i
    return 'SONG NOT FOUND'

SONG_NUMBER = int(get_song_number())


# The minimized solo clip is automatically chopped down into 10 second segments

def get_duration():
    with contextlib.closing(wave.open("C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/jimmy_page/"+FILENAME+"_solo.wav",'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration + 1 # add 1 just in case the duration is just under 20 seconds (i.e. 19.995) so it doesn't mess up clipping

for i in range(int(get_duration()) // 10):
    ffmpeg_extract_subclip(
    "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/jimmy_page/"+FILENAME+"_solo.wav", 
    i*10, 
    (i+1)*10, 
    targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos/{SONG_NUMBER}_{i}.wav"
    )