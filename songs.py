# In this file, all the songs for each artist are saved in their own array, then all the arrays are
# combined into one large "songs" array.
# This array is used by UpdateCSV.py to add all of the proper song names.

# Download the youtube videos as .wav files at https://loader.to/en18/youtube-wav-converter.html 
# Save the video as its name under the full_solos directory
# Transposer: https://transposr.com/songs/new
# Converter: https://www.freeconvert.com/audio-converter
# Wav converter https://songsurgeon.com/engine/ssweb/

# artists: 
# jimmy page
# eddie van halen
# david gilmour
# eric clapton
# jimi hendrix
# slash
# randy rhoades
# mark knopfler
# brian may
# prince
# carlos santana
# j mascis

jimmy_page = [
    # led zeppelin 
    "good_times_bad_times",
    "dazed_and_confused",
    "communication_breakdown",
    "i_cant_quit_you_baby",
    "how_many_more_times",

    # led zeppelin ii
    "whole_lotta_love",
    "what_is_and_what_should_never_be",
    "the_lemon_song",
    "heartbreaker",
    "living_loving_maid",
    "ramble_on",
    "moby_dick",

    # led zeppelin iii
    "celebration_day",
    "since_ive_been_lovin_you",
    "tangerine",

    # led zeppelin iv
    "black_dog",
    "rock_and_roll",
    "stairway_to_heaven",
    "misty_mountain_hop",
    "when_the_levee_breaks",

    # houses of the holy
    "the_song_remains_the_same",
    "over_the_hills_and_far_away",
    "dyer_maker",
    "no_quarter",
    "the_ocean",

    # physical graffiti
    "custard_pie",
    "the_rover",
    "in_my_time_of_dying",
    "ten_years_gone",
    "the_wanton_song",
    "sick_again",

    # Presence
    "achilles_last_stand",
    "for_your_life",
    "royal_orleans",
    "nobodys_fault_but_mine",
    "hots_on_for_nowhere",
    "tea_for_one",

    # in through the out door
    "in_the_evening",
    "south_bound_suarez",
    "fool_in_the_rain",
    "hot_dog",
    "all_my_love",
    "im_gonna_crawl",

    # coda
    "walters_walk",
    "ozone_baby",
    "darlene",

    # live solos
    "live_at_msg"
]


eddie_van_halen = [

]

def get_songs():
    songs = []

    for jimmy_song in jimmy_page:
        songs.append(jimmy_song)

    for eddit_song in eddie_van_halen:
        songs.append(eddit_song)

    return songs