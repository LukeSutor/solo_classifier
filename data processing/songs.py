# In this file, all the songs for each artist are saved in their own array, then all the arrays are
# combined into one large "songs" array
# This array is used by UpdateCSV.py to add all of the proper song names
# Each comment on the guitarist arrays denotes an album

# Download the youtube videos as _wav files at https://loader_to/en18/youtube-wav-converter_html 
# Save the video as its name under the full_solos directory
# Transposer: https://transposr_com/songs/new
# Converter: https://www_freeconvert_com/audio-converter
# Wav converter https://songsurgeon_com/engine/ssweb/

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
    # van halen
    "runnin_with_the_devil",
    "eruption",
    "you_really_got_me",
    "aint_talkin_bout_love",
    "im_the_one",
    "atomic_punk",
    "feel_your_love_tonight",
    "little_dreamer",
    "ice_cream_man",
    "on_fire",

    # van halen ii
    "youre_no_good",
    "somebody_get_me_a_doctor",
    "bottoms_up",
    "outta_love_again",
    "light_up_the_sky",
    "d.o.a.",
    "women_in_love",
    "beautiful_girls",

    # women and children first
    "and_the_cradle_will_rock",
    "everybody_wants_some",
    "fools",
    "romeo_delight",
    "take_your_whiskey_home",
    "in_a_simple_rhyme",

    # fair warning
    "mean_street",
    "sinners_swing",
    "hear_about_it_later",
    "unchained",
    "push_comes_to_shove",
    "so_this_is_love",
    "one_foot_out_the_door",
    
    # diver down
    "where_have_all_the_good_times_gone",
    "hang_em_high",
    "secrets",
    "dancing_in_the_street",
    "the_full_bug",

    # 1984
    "jump",
    "panama",
    "top_jimmy",
    "drop_dead_legs",
    "hot_for_teacher",
    "ill_wait",
    "girl_gone_bad",
    "house_of_pain",

    # 5150
    "good_enough",
    "why_cant_this_be_love",
    "get_up",
    "dreams",
    "summer_nights",
    "best_of_both_worlds",
    "love_walks_in",
    "5150",
    "inside",

    # ou812
    "mine_all_mine",
    "when_its_love",
    "a.f.u.",
    "cabo_wabo",
    "source_of_infection",
    "feels_so_good",
    "black_and_blue",
    "sucker_in_a_3_piece",

    # for unlawful carnal knowledge
    "poundcake",
    "judgement_day",
    "spanked",
    "runaround",
    "pleasure_dome",
    "in_n_out",
    "man_on_a_mission",
    "the_dream_is_over",
    "right_now",
    "top_of_the_world",

    # balance
    "cant_stop_lovin_you",
    "dont_tell_me",
    "amsterdam",
    "not_enough",
    "aftershock",
    "baluchiteherium",
    "feelin",

    # van halen iii
    "without_you",
    "one_i_want",
    "from_afar",
    "fire_in_the_hole",
    "josephina",
    "year_to_the_day",
    "ballot_or_the_bullet",

    # a different kind of truth
    "tattoo",
    "you_and_your_blues",
    "china_town",
    "blood_and_fire",
    "bullethead",
    "as_is",
    "honeybabysweetiedoll",
    "the_trouble_with_never",
    "outta_space",
    "stay_frosty",
    "big_river",
    "beats_workin",
    "shes_the_woman"
]

def get_songs():
    songs = []

    for jimmy_song in jimmy_page:
        songs.append(jimmy_song)

    for eddit_song in eddie_van_halen:
        songs.append(eddit_song)

    return songs