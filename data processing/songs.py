# In this file, all the songs for each artist are saved in their own array, then all the arrays are
# combined into one large "songs" array.
# This array is used by UpdateCSV.py to add all of the proper song names.
# Each comment on the guitarist arrays denotes an album

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
    # van halen
    "runnin.with.the.devil",
    "eruption",
    "you.really.got.me",
    "aint.talkin.bout.love",
    "im.the.one",
    "atomic.punk",
    "feel.your.love.tonight",
    "little.dreamer",
    "ice.cream.man",
    "on.fire",

    # van halen ii
    "youre.no.good",
    "somebody.get.me.a.doctor",
    "bottoms.up",
    "outta.love.again",
    "light.up.the.sky",
    "d.o.a.", # fix periods
    "woman.in.love",
    "beautiful.girls",

    # women and children first
    "and.the.cradle.will.rock",
    "everybody.wants.some",
    "fools",
    "romeo.delight",
    "take.your.whiskey.home",
    "in.a.simple.rhyme",

    # fair warning
    "mean.street",
    "dirty.movies",
    "sinners.swing",
    "hear.about.it.later",
    "unchained",
    "push.comes.to.shove",
    "so.this.is.love",
    "one.foot.out.the.door",
    
    # diver down
    "where.have.all.the.good.times.gone",
    "hang.em.high",
    "secrets",
    "dancing.in.the.street",
    "litte.guitars",
    "the.full.bug",

    # 1984
    "jump",
    "panama",
    "top.jimmy",
    "drop.dead.legs",
    "hot.for.teacher",
    "ill.wait",
    "girl.gone.bad",
    "house.of.pain",

    # 5150
    "good.enough",
    "why.cant.this.be.love",
    "get.up",
    "dreams",
    "summer.nights",
    "best.of.both.worlds",
    "love.walks.in",
    "5150",
    "inside",

    # ou812
    "mine.all.mine",
    "when.its.love",
    "a.f.u.", # fix periods
    "cabo.wabo",
    "source.of.infection",
    "feels.so.good",
    "black.and.blue",
    "sucker.in.a.3.piece",

    # for unlawful carnal knowledge
    "poundcake",
    "judgement.day",
    "spanked",
    "runaround",
    "pleasure.dome",
    "in.n.out",
    "man.on.a.mission",
    "the.dream.is.over",
    "right.now",
    "top.of.the.world",

    # balance
    "cant.stop.lovin.you",
    "dont.tell.me",
    "amsterdam",
    "not.enough",
    "aftershock",
    "baluchiteherium",
    "feelin",

    # van halen iii
    "without.you",
    "one.i.want",
    "from.afar",
    "dirty.water.dog",
    "fire.in.the.hole",
    "josephina",
    "year.to.the.day",
    "ballot.or.the.bullet",

    # a different kind of truth
    "tattoo",
    "you.and.your.blues",
    "china.town",
    "blood.and.fire",
    "bullethead",
    "as.is",
    "honeybabysweetiedoll",
    "the.trouble.with.never",
    "outta.space",
    "stay.frosty",
    "big.river",
    "beats.workin"
]

def get_songs():
    songs = []

    for jimmy_song in jimmy_page:
        songs.append(jimmy_song)

    for eddit_song in eddie_van_halen:
        songs.append(eddit_song)

    return songs

print(get_songs())