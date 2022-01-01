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
# mark knopfler
# brian may
# carlos santana

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

david_gilmour = [
    # a saucerful of secrets
    "let_there_be_more_light",

    # more
    "the_nile_song",
    "more_blues",

    # atom heart mother
    "fat_old_sun",

    # meddle
    "one_of_these_days",
    "echoes",

    # obscured by clouds
    "the_gold_its_in_the",
    "mudmen",
    "childhoods_end",
    "free_four",
    "stay",

    # the dark side of the moon
    "time",
    "money",
    "any_colour_you_like",

    # wish you were here
    "shine_on_you_crazy_diamond",  # all parts
    "have_a_cigar",

    # animals
    "dogs",
    "pigs",

    # the wall
    "the_thin_ice",
    "another_brick_in_the_wall",  # part 2
    "mother",
    "young_lust",
    "one_of_my_turns",
    "hey_you",
    "comfortably_numb",

    # the final cut
    "your_possible_pasts",
    "the_fletcher_memorial_home",
    "the_final_cut",
    "not_now_john",

    # a momentary lapse of reason
    "learning_to_fly",
    "the_dogs_of_war",
    "on_the_turning_away",
    "yet_another_movie",
    "sorrow",

    # the division bell
    "cluster_one",
    "what_do_you_want_from_me",
    "poles_apart",
    "marooned",
    "a_great_day_for_freedom",
    "wearing_the_inside_out",
    "coming_back_to_life",
    "keep_talking",
    "high_hopes",

    # the endless river
    "its_what_we_do",
    "louder_than_words",

    # the later years
    "davids_blues",
    "nervana",

    # delicate sound of thunder (live)
    # four mninute solo at end, exclude normal part start clip at 5:37
    "comfortably_numb_live",

    # live at knebworth 1990
    "sorrow_live",  # last solo
]

eric_clapton = [
    # for your love
    "im_not_talking",
    "i_aint_got_you",
    "got_to_hurry",
    "a_certain_girl",
    "good_morning_little_schoolgirl",

    # layla and other assorted love songs
    "bell_bottom_blues",
    "keep_on_growing",
    "nobody_knows_you_when_youre_down_and_out",
    "i_am_yours",
    "anyday",
    "key_to_the_highway",
    "tell_the_truth",
    "why_does_love_got_to_be_so_sad",
    "have_you_ever_loved_a_woman",
    "little_wing",
    "its_too_late",
    "layla",

    # 461 Ocean Blvd.
    "motherless_children",
    "i_cant_hold_out",
    "let_it_grow",
    "steady_rollin_man",
    "aint_that_lovin_you",
    "meet_me",
    "eric_after_hours_blues",
    "b_minor_jam",

    # theres one in every crowd
    "swing_low_sweet_chariot",
    "the_sky_is_crying",
    "better_make_it_through_today",
    "high",

    # no reason to cry
    "beautiful_thing",
    "county_jail_blues",
    "all_our_past_times",
    "double_trouble",
    "hungry",
    "black_summer_rain",
    "last_night",

    # slowhand
    "cocaine",
    "lay_down_sally",
    "next_time_you_see_her",
    "mean_old_frisco",
    "peaches_and_diesel",

    # backless
    "walk_out_in_the_rain",
    "watch_out_for_lucy",
    "ill_make_love_to_you_anytime",
    "roll_it",
    "if_i_dont_be_there_by_morning",
    "early_in_the_morning",

    # another ticket
    "blow_wind_blow",
    "hold_me_lord",
    "floating_bridge",
    "catch_me_if_you_can",
    "rita_mae",

    # timepieces
    "after_midnight",

    # money and cigarettes
    "everybody_oughta_make_a_change",
    "the_shape_youre_in",
    "aint_going_down",
    "ive_got_a_rock_n_roll_heart",
    "man_overboard",
    "pretty_girl",
    "crosscut_saw",
    "slow_down_linda",

    # CREAM

    # fresh cream
    "n.s.u",
    "sleepy_time_time",
    "sweet_wine",
    "spoonful",
    "cats_squirrel",
    "im_so_glad",

    # wheels of fire
    "white_room",
    "sitting_on_top_of_the_world",
    "politician",
    "those_were_the_days",
    "born_under_a_bad_sign",
    "deserted_cities_of_the_heart",

    # goodbye
    "badge",
    "crossroads",

    # disraeli gears
    "strange_brew",
    "sunshine_of_your_love",
    "tales_of_brave_ulysses",
    "swlabr",
    "outside_woman_blues",

    # Weird bug with 1 more eric clapton song than is showing up, all other songs are correctly labeled, though
    # it funks out at around song 249
    "idk_1",
]

jimi_hendrix = [

]


def get_songs():
    songs = []

    for jimmy_song in jimmy_page:
        songs.append(jimmy_song)

    for eddie_song in eddie_van_halen:
        songs.append(eddie_song)

    for gilmour_song in david_gilmour:
        songs.append(gilmour_song)

    for clapton_song in eric_clapton:
        songs.append(clapton_song)

    for jimi_song in jimi_hendrix:
        songs.append(jimi_song)

    return songs


print(len(get_songs()))

x = get_songs()

print(x[200])
