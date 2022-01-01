import os
import pandas as pd

from songs import get_songs

directory = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"

csv = pd.read_csv(
    "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv")

songs = get_songs()


def get_solo_number(solo):
    i = 0
    while True:
        try:
            s = int(solo[i])
            i += 1
        except:
            return int(solo[:i])


def get_guitarist_id(solo_number):
    if solo_number <= 46:
        return 0
    elif solo_number <= 144:
        return 1
    elif solo_number <= 192:
        return 2
    elif solo_number <= 273:
        return 3
    else:
        return -1


def get_guitarist(solo_number):
    if solo_number <= 46:
        return "jimmy_page"
    elif solo_number <= 144:
        return "eddie_van_halen"
    elif solo_number <= 193:
        return "david_gilmour"
    elif solo_number <= 273:
        return "eric_clapton"
    else:
        return "unknown"


additions = 0
for filename in os.listdir(directory):
    solo_number = get_solo_number(filename)
    print([filename, get_guitarist_id(solo_number),
          get_guitarist(solo_number), songs[solo_number]])
    csv.loc[additions] = [filename, get_guitarist_id(
        solo_number), get_guitarist(solo_number), songs[solo_number]]
    additions += 1

print(f"annotated {additions} files")
csv.to_csv(
    "C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv", index=False)
