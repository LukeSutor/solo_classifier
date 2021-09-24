from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# This file is for trimming the original song down to just the solo to save space

FILENAME = 'live_at_msg'


start_minutes = 0
start_seconds = 30

end_minutes = 1
end_seconds = 50

start_time = start_minutes * 60 + start_seconds
end_time = end_minutes * 60 + end_seconds

ffmpeg_extract_subclip(
        "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/jimmy_page/"+FILENAME+".wav", 
        start_time, 
        end_time, 
        targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/jimmy_page/{FILENAME}_solo.wav"
        )

print(f"subclip extracted for {FILENAME}")