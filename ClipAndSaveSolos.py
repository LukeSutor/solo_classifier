from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Download the youtube videos as .wav files at https://loader.to/en18/youtube-wav-converter.html 
# Save the video as its name under the full_solos directory

# Transposer: https://transposr.com/songs/new
# Converter: https://www.freeconvert.com/audio-converter

FILENAME = 'Custard_Pie_Up_Half'
SONG_NUMBER = 2.1

# This is where you input the start and end time of the solo, and it's chopped up into 10 second segments and saved
# in the correct solos folder to be accessed by the annotations.csv file
start_minutes = 1
start_seconds = 45

end_minutes = 2
end_seconds = 16

start_time = start_minutes * 60 + start_seconds
end_time = end_minutes * 60 + end_seconds

clips = ((end_time - start_time) // 10)

for i in range(clips):
    ffmpeg_extract_subclip(
        "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/"+FILENAME+".wav", 
        start_time+(i*10), 
        start_time+((i+1)*10), 
        targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos/{SONG_NUMBER}_{i}.wav"
        )
    print(f"clip {i} complete")
