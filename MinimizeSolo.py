from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# This file is for trimming the original song down to just the solo to save space

FILENAME = 'dazed_and_confused'

# dazed and confused: 3:34 to 4:44

start_minutes = 3
start_seconds = 34

end_minutes = 4
end_seconds = 44

start_time = start_minutes * 60 + start_seconds
end_time = end_minutes * 60 + end_seconds

ffmpeg_extract_subclip(
        "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/"+FILENAME+".wav", 
        start_time, 
        end_time, 
        targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/{FILENAME}_minimized.wav"
        )

print(f"subclip extracted for {FILENAME}")