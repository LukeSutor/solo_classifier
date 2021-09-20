import os
import pandas as pd

directory = "C:/Users/Luke/Desktop/coding/solo_classifier/audio/solos"

csv = pd.read_csv("C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv")

# Artists: 
# Jimmy Page
# Eddie Van Halen
# David Gilmour
# Eric Clapton
# Jimi Hendrix
# Slash
# Randy Rhoades
# Mark Knopfler
# Brian May
# Prince
# Carlos Santana
# J Mascis

songs = [
    "Stairway_To_Heaven",
    "Whole_Lotta_Love",
    "Custard_Pie",
    ""
]

def get_solo_number(solo):
    i = 0
    while True:
        try:
            s = int(solo[i])
            i += 1
        except:
            return int(solo[:i])

def get_guitarist_id(solo_number):
    if(solo_number < 10): return 0
    else: return -1

def get_guitarist(solo_number):
    if(solo_number < 10): return "Jimmy_Page"
    else: return "unknown"


additions = 0
for filename in os.listdir(directory):
    solo_number = get_solo_number(filename)
    print([filename, get_guitarist_id(solo_number), get_guitarist(solo_number), songs[solo_number]])
    csv.loc[additions] = [filename, get_guitarist_id(solo_number), get_guitarist(solo_number), songs[solo_number]]
    additions += 1

print(f"annotated {additions} files")
csv.to_csv("C:/Users/Luke/Desktop/coding/solo_classifier/audio/annotations.csv", index=False)