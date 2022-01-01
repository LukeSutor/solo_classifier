from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from ClipAndSaveSolos import ClipAndSave

# This file is for trimming the original song down to just the solo to save space

GUITARIST = 'eric_clapton'

FILENAME = "outside_woman_blues"

# check for "i_aint_done_wrong" after


def Minimize():
    solo_times = ["1:29-1:49"]

    for i in range(len(solo_times)):

        start_and_end = solo_times[i].split("-")

        start_time = (
            60 * int(start_and_end[0].split(":")[0])) + (int(start_and_end[0].split(":")[1]))

        end_time = (
            60 * int(start_and_end[1].split(":")[0])) + (int(start_and_end[1].split(":")[1]))

        ffmpeg_extract_subclip(
            "C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/" +
            GUITARIST+"/"+FILENAME+".wav",
            start_time,
            end_time,
            targetname=f"C:/Users/Luke/Desktop/coding/solo_classifier/audio/full_solos/{GUITARIST}/{FILENAME}_solo_{i}.wav"
        )

        print(f"subclip extracted for {FILENAME}_solo_{i}")

        print("clipping...")

        ClipAndSave(FILENAME, GUITARIST, i)


Minimize()
