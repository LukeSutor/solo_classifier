from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from ClipAndSaveSolos import ClipAndSave

# This file is for trimming the original song down to just the solo to save space

FILENAME = 'shes_the_woman'

def Minimize():
        start_minutes = 2
        start_seconds = 3

        end_minutes = 2
        end_seconds = 20

        start_time = start_minutes * 60 + start_seconds
        end_time = end_minutes * 60 + end_seconds

        ffmpeg_extract_subclip(
                "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/eddie_van_halen/"+FILENAME+".wav", 
                start_time, 
                end_time, 
                targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/eddie_van_halen/{FILENAME}_solo.wav"
                )

        print(f"subclip extracted for {FILENAME}")

        print("clipping...")

        ClipAndSave(FILENAME)

Minimize()