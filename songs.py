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
    "your_time_is_gonna_come",
    "black_mountain_side",
    "communication_breakdown",
    "i_cant_Quit_you_baby",
    "how_many_more_times",

    # led zeppelin ii
    "whole_lotta_love",
    "what_is_and_what_should_never_be",
    "the_lemon_song",
    "thank_you",
    "heartbreaker",
    "living_loving_maid",
    "ramble_on",
    "moby_dick",
    "bring_it_on_home",

    # led zeppelin iii
    "immigrant_song",
    "friends",
    "celebration_day",
    "since_ive_been_loving_you",
    "out_on_the_tiles",
    "gallows_pole",
    "tangerine",
    "thats_the_way",
    "bron-y-aur_stomp",
    "hats_off_to_roy_harper",

    # led zeppelin iv
    "black_dog",
    "rock_and_roll",
    "the_battle_of_evermore",
    "stairway_to_heaven",
    "misty_mountain_hop",
    "four_sticks",
    "going_to_california",
    "when_the_levee_breaks",

    # houses of the holy
    "the_song_remains_the_same",
    "the_rain_song",
    "over_the_hills_and_far_away",
    "the_crunge",
    "dancing_days",
    "dyer_maker",
    "no_quarter",
    "the_ocean",

    # physical graffiti
    "custard_pie",
    "the_rover"
    "in_my_time_dying",
    "houses_of_the_holy",
    "trampled_under_foot",
    "kashmir",
    "in_the_light",
    "bron-y-aur",
    "down_by_the_seaside",
    "ten_years_gone",
    "night_flight",
    "the_wanton_song",
    "boogie_with_stu",
    "black_country_woman",
    "sick_again",

    # Presence
    "achilles_last_stand",
    "for_your_life",
    "royal_orleans",
    "nobodys_fault_but_mine",
    "candy_store_rock",
    "hots_on_for_nowhere",
    "tea_for_one"

    # in through the out door
    "in_the_evening",
    "south_bound_suarez",
    "fool_in_the_rain",
    "hot_dog",
    "carouselambra",
    "all_my_love",
    "im_gonna_crawl",

    # coda
    "poor_tom",
    "walters_walk",
    "ozone_baby",
    "darlene",
    "bonzos_montreux",
    "wearing_and_tearing"
]

def get_songs():
    songs = []

    for song in jimmy_page:
        songs.append(song)

    return songs