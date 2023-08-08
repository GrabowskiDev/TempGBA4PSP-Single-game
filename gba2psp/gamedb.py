

# Gameid is stored at offset 0xa0 into the GBA file and is 12 bytes in size
# plus 4 bytes for UTTD.
# The key in this dict is the 12 byte id plus the 4 bytes uttd
# (so that we can distinguish between different regions/releases of the game)
# Convert any 0x00 bytes in the id to 0x20 before looking it up in the dict.
#
# See https://www.youtube.com/watch?v=Sqr8lq79jsU&list=PL4sZJNxKabvlY-Fp3ozv7S290bbvvLNQD&index=1
# for more information about the header structure
#
#
# Commerical games follow the format UTTD, where:
#
# ==== =================================== =============================== ==== =====================
# U (game type)                   TT (shorthand game title)     D (destination/language)
# ---------------------------------------- ------------------------------- --------------------------
# Code Meaning                             Meaning                         Code Destination/language
# ==== =================================== =============================== ==== =====================
# A    Normal game (usually 2001 to 2003)  An arbitrary abbreviation for   D    German
# B    Normal game (year 2003 onwards)     the game title (eg. "PM" for    E    USA/English
# C    Normal game (not yet used)          "Pac Man").                     F    French
# F    Famicom/NES                                                         I    Italian
# K    Acceleration sensor                                                 J    Japan
# P    For e-Reader (dot-code scanner)                                     P    Europe/elsewhere
# R    Rumble and Z-axis gyro sensor                                       S    Spanish
# U    RTC and solar sensor
# V    Rumble motor
        
games = {
    "01:TBC@2960 AZKJ": {
        'uttd': "AZKJ",
        'title': "Simple 2960 Tomodachi Series Vol. 1 - The Table Game Collection",
    },
    "02:BK@2960  AZ9J": {
        'uttd': "AZ9J",
        'title': "Simple 2960 Tomodachi Series Vol. 2 - The Block Kuzushi",
    },
    "03:IP@2960  BS3J": {
        'uttd': "BS3J",
        'title': "Simple 2960 Tomodachi Series Vol. 3 - The Itsudemo Puzzle",
    },
    "04:TP@2960  BS4J": {
        'uttd': "BS4J",
        'title': "Simple 2960 Tomodachi Series Vol. 4 - The Trump - Minna de Asoberu 12 Shurui no Trump Game",
    },
    "2IN1_ADV_BTLBW4J": {
        'uttd': "BW4J",
        'title': "2 Games in 1 - Sonic Battle + Sonic Advance",
    },
    "2IN1_ADV_BTLBW4P": {
        'uttd': "BW4P",
        'title': "2 Games in 1 - Sonic Advance + Sonic Battle",
    },
    "2IN1_ADV_CHUBW3J": {
        'uttd': "BW3J",
        'title': "2 Games in 1 - Sonic Advance + Chu Chu Rocket!",
    },
    "2IN1_ADV_CHUBW3P": {
        'uttd': "BW3P",
        'title': "2 Games in 1 - Sonic Advance + Chu Chu Rocket!",
    },
    "2IN1_ADV_PINBW5E": {
        'uttd': "BW5E",
        'title': "2 Games in 1 - Sonic Pinball Party + Sonic Advance",
    },
    "2IN1_ADV_PINBW5P": {
        'uttd': "BW5P",
        'title': "2 Games in 1 - Sonic Pinball Party + Sonic Advance",
    },
    "2IN1_BTL_CHUBW7P": {
        'uttd': "BW7P",
        'title': "2 Games in 1 - Sonic Battle + Chu Chu Rocket!",
    },
    "2IN1_BTL_PINBW6J": {
        'uttd': "BW6J",
        'title': "2 Games in 1 - Sonic Battle + Sonic Pinball Party",
    },
    "2IN1_BTL_PINBW6P": {
        'uttd': "BW6P",
        'title': "2 Games in 1 - Sonic Battle + Sonic Pinball Party",
    },
    "2IN1_COL_CHUBW9P": {
        'uttd': "BW9P",
        'title': "2 Games in 1 - Columns Crown + Chu Chu Rocket!",
    },
    "3IN1 RECROOMBRQP": {
        'uttd': "BRQP",
        'title': "Rec Room Challenge",
    },
    "3N1SPORTSPAKB3NE": {
        'uttd': "B3NE",
        'title': "3 in 1 Sports Pack - Paintball Splat! + Dodgeball - Dodge This! + Big Alley Bowling",
    },
    "3N1SPORTSPAKB3NP": {
        'uttd': "B3NP",
        'title': "3 in 1 Sports Pack - Paintball Splat! + Dodgeball - Dodge This! + Big Alley Bowling",
    },
    "3 STOOGES   A3TE": {
        'uttd': "A3TE",
        'title': "Three Stooges, The",
    },
    "4V4 ARASHI  A4VJ": {
        'uttd': "A4VJ",
        'title': "Yuujou no Victory Goal 4v4 Arashi - Get the Goal!!",
    },
    "ACE COMBAT  BAEE": {
        'uttd': "BAEE",
        'title': "Ace Combat Advance",
    },
    "ACE LIGHTNINALXP": {
        'uttd': "ALXP",
        'title': "Ace Lightning",
    },
    "ACTANTHOLOGYBAVE": {
        'uttd': "BAVE",
        'title': "Activision Anthology",
    },
    "ACTION MAN  BACP": {
        'uttd': "BACP",
        'title': "Action Man - Robot Attack",
    },
    "ADVANCE GH  BAGJ": {
        'uttd': "BAGJ",
        'title': "Advance Guardian Heroes",
    },
    "ADVANCE GH  BGCE": {
        'uttd': "BGCE",
        'title': "Advance Guardian Heroes",
    },
    "ADVANCE GH  BGCP": {
        'uttd': "BGCP",
        'title': "Advance Guardian Heroes",
    },
    "ADVANCE GT2 A2GJ": {
        'uttd': "A2GJ",
        'title': "Advance GT2",
    },
    "ADVANCE GTA AG7J": {
        'uttd': "AG7J",
        'title': "Advance GTA",
    },
    "ADVANCE RALLAR7J": {
        'uttd': "AR7J",
        'title': "Advance Rally",
    },
    "ADVANCEWARS2AW2E": {
        'uttd': "AW2E",
        'title': "Advance Wars 2 - Black Hole Rising",
    },
    "ADVANCEWARS2AW2P": {
        'uttd': "AW2P",
        'title': "Advance Wars 2 - Black Hole Rising",
    },
    "ADVANCEWARS AWRE": {
        'uttd': "AWRE",
        'title': "Advance Wars",
        'icon0': 'https://images.launchbox-app.com/0d283a33-c5f3-429d-a1f1-3d6aa6a33553.jpg',
        'pic0': 'https://images.launchbox-app.com/73022111-ee1f-42ce-a7fe-471e55b2e010.png',
        'pic1': 'https://images.launchbox-app.com/4a4c39c1-9048-4570-ba6f-3079954f3a9c.jpg',
        'snd0': 'https://www.youtube.com/watch?v=Uhw3n1p-Tlk&list=PLph1rKwgi-5gfdUX6DWt3PCyk982DFzuL&index=1',
    },
    "ADVANCEWARSPAWRP": {
        'uttd': "AWRP",
        'title': "Advance Wars",
        'icon0': 'https://images.launchbox-app.com/0d283a33-c5f3-429d-a1f1-3d6aa6a33553.jpg',
        'pic0': 'https://images.launchbox-app.com/73022111-ee1f-42ce-a7fe-471e55b2e010.png',
        'pic1': 'https://images.launchbox-app.com/4a4c39c1-9048-4570-ba6f-3079954f3a9c.jpg',
        'snd0': 'https://www.youtube.com/watch?v=Uhw3n1p-Tlk&list=PLph1rKwgi-5gfdUX6DWt3PCyk982DFzuL&index=1',
    },
    "AEROACROBATXAAOE": {
        'uttd': "AAOE",
        'title': "Aero the Acro-Bat - Rascal Rival Revenge",
    },
    "AEROACROBATXAAOP": {
        'uttd': "AAOP",
        'title': "Aero the Acro-Bat - Rascal Rival Revenge",
    },
    "AEROMXXXXXXXAAOJ": {
        'uttd': "AAOJ",
        'title': "Acrobat Kid",
    },
    "AGASSI TENNIACEP": {
        'uttd': "ACEP",
        'title': "Agassi Tennis Generation",
    },
    "AGASSITENNISACEE": {
        'uttd': "ACEE",
        'title': "Agassi Tennis Generation",
    },
    "AGB-BSMP    BSMP": {
        'uttd': "BSMP",
        'title': "Metal Slug Advance",
        'icon0': 'https://images.launchbox-app.com/83c4fe37-2773-495f-bb70-aa58839e3fae.jpg',
        'pic0': 'https://images.launchbox-app.com/e9a2f52c-25b4-4184-8ef0-0e3785d4d1ce.png',
        'pic1': 'https://images.launchbox-app.com/158d45de-507b-4124-9917-a4c90d6cca91.jpg',
    },
    "AGB-DOOM    ADME": {
        'uttd': "ADME",
        'title': "Doom",
    },
    "AGB KIRBY AMB8KE": {
        'uttd': "B8KE",
        'title': "Kirby & The Amazing Mirror",
    },
    "AGB KIRBY AMB8KJ": {
        'uttd': "B8KJ",
        'title': "Hoshi no Kirby - Kagami no Daimeikyuu",
    },
    "AGB KIRBY AMB8KP": {
        'uttd': "B8KP",
        'title': "Kirby & The Amazing Mirror",
    },
    "AGB KIRBY DXA7KE": {
        'uttd': "A7KE",
        'title': "Kirby - Nightmare in Dream Land",
    },
    "AGB KIRBY DXA7KJ": {
        'uttd': "A7KJ",
        'title': "Hoshi no Kirby - Yume no Izumi Deluxe",
    },
    "AGB KIRBY DXA7KP": {
        'uttd': "A7KP",
        'title': "Kirby - Nightmare in Dream Land",
    },
    "AGB-P-A52J  A52J": {
        'uttd': "A52J",
        'title': "Koukou Juken Advance Series Eitango Hen - 2000 Words Shuuroku",
    },
    "AGB-P-A53J  A53J": {
        'uttd': "A53J",
        'title': "Koukou Juken Advance Series Eijukugo Hen - 650 Phrases Shuuroku",
    },
    "AGB-P-A54J  A54J": {
        'uttd': "A54J",
        'title': "Koukou Juken Advance Series Eigo Koubun Hen - 26 Units Shuuroku",
    },
    "AGB-P-A8CJ  A8CJ": {
        'uttd': "A8CJ",
        'title': "Card Party",
    },
    "AGB-P-AZ3J  AZ3J": {
        'uttd': "AZ3J",
        'title': "Cyberdrive Zoids - Kijuu no Senshi Hyuu",
    },
    "AGB-P-BSMJ  BSMJ": {
        'uttd': "BSMJ",
        'title': "Metal Slug Advance",
    },
    "AGB-TORNEKO3BD3J": {
        'uttd': "BD3J",
        'title': "Dragon Quest Characters - Torneco no Daibouken 3 Advance - Fushigi no Dungeon",
    },
    "AGGRESSIVE IAILE": {
        'uttd': "AILE",
        'title': "Aggressive Inline",
    },
    "AGGRESSIVE IAILP": {
        'uttd': "AILP",
        'title': "Aggressive Inline",
    },
    "AIRFORCEDELTAAKE": {
        'uttd': "AAKE",
        'title': "Airforce Delta Storm",
    },
    "AIRFORCEDELTAAKJ": {
        'uttd': "AAKJ",
        'title': "Airforce Delta II",
    },
    "AKAGI       BZWJ": {
        'uttd': "BZWJ",
        'title': "Akagi",
    },
    "AKATHAN     BAZJ": {
        'uttd': "BAZJ",
        'title': "Aka-chan Doubutsuen",
    },
    "ALADDIN     AJ6J": {
        'uttd': "AJ6J",
        'title': "Aladdin",
    },
    "ALADDIN     BADE": {
        'uttd': "BADE",
        'title': "Aladdin",
    },
    "ALADDIN     BADP": {
        'uttd': "BADP",
        'title': "Aladdin",
    },
    "ALEDERMANNEUBPVX": {
        'uttd': "BPVX",
        'title': "Pippa Funnell - Stable Adventure",
    },
    "ALEX RIDER  BAWE": {
        'uttd': "BAWE",
        'title': "Alex Rider - Stormbreaker",
    },
    "ALEX RIDER  BAWX": {
        'uttd': "BAWX",
        'title': "Alex Rider - Stormbreaker",
    },
    "ALICE       AF4J": {
        'uttd': "AF4J",
        'title': "Fushigi no Kuni no Alice",
    },
    "ALIENATORS  AEVE": {
        'uttd': "AEVE",
        'title': "Alienators - Evolution Continues",
    },
    "ALIENHOMINIDBAHP": {
        'uttd': "BAHP",
        'title': "Alien Hominid",
    },
    "ALLGROWNUP01MGUE": {
        'uttd': "MGUE",
        'title': "Game Boy Advance Video - All Grown Up! - Volume 1",
    },
    "ALLGROWNUP  BALX": {
        'uttd': "BALX",
        'title': "All Grown Up! - Express Yourself",
    },
    "ALLGROWNUPEYBALE": {
        'uttd': "BALE",
        'title': "All Grown Up! - Express Yourself",
    },
    "ALLSTAR 2003AA3E": {
        'uttd': "AA3E",
        'title': "All-Star Baseball 2003",
    },
    "ALLSTAR 2004AA7E": {
        'uttd': "AA7E",
        'title': "All-Star Baseball 2004",
    },
    "ALTERED BEASAARP": {
        'uttd': "AARP",
        'title': "Altered Beast - Guardian of the Realms",
    },
    "ALTEREDBEASTAARE": {
        'uttd': "AARE",
        'title': "Altered Beast - Guardian of the Realms",
    },
    "AM 3D POOL  BPLE": {
        'uttd': "BPLE",
        'title': "Archer Maclean's - 3D Pool",
    },
    "AM DRAGON   BAPE": {
        'uttd': "BAPE",
        'title': "American Dragon - Jake Long - Rise of the Huntsclan!",
    },
    "AMDRIVERBTLPBGPJ": {
        'uttd': "BGPJ",
        'title': "Get Ride! AMDriver - Shuggeki! Battle Party",
    },
    "AMDRIVERHEROBGIJ": {
        'uttd': "BGIJ",
        'title': "Get Ride! AMDriver - Senkou no Hero Tanjou!",
    },
    "AMERICA_BASSAABE": {
        'uttd': "AABE",
        'title': "American Bass Challenge",
    },
    "AMERICANTAILAFGE": {
        'uttd': "AFGE",
        'title': "American Tail, An - Fievel's Gold Rush",
    },
    "AMERICANTAILAFGP": {
        'uttd': "AFGP",
        'title': "American Tail, An - Fievel's Gold Rush",
    },
    "A.M.TURFWARSAY3E": {
        'uttd': "AY3E",
        'title': "Army Men - Turf Wars",
    },
    "ANGELICLAYERAALJ": {
        'uttd': "AALJ",
        'title': "Kidou Tenshi Angelic Layer - Misaki to Yume no Tenshi-tachi",
    },
    "ANGELIQUE   AAGJ": {
        'uttd': "AAGJ",
        'title': "Angelique",
    },
    "ANICENAFRICABFRP": {
        'uttd': "BFRP",
        'title': "My Animal Centre in Africa",
    },
    "ANIMALMANIA1AANJ": {
        'uttd': "AANJ",
        'title': "Animal Mania - Dokidoki Aishou Check",
    },
    "ANIMAL SNAP AAQE": {
        'uttd': "AAQE",
        'title': "Animal Snap - Rescue Them 2 by 2",
    },
    "ANIMAL SNAP AAQP": {
        'uttd': "AAQP",
        'title': "Animal Snap - Rescue Them 2 by 2",
    },
    "ANIMANIACS: ANIP": {
        'uttd': "ANIP",
        'title': "Animaniacs - Lights, Camera, Action!",
    },
    "ANISNOATORIEANSJ": {
        'uttd': "ANSJ",
        'title': "Marie, Elie & Anis no Atelier - Soyokaze Kara no Dengon",
    },
    "ANIYOKO2    BAXJ": {
        'uttd': "BAXJ",
        'title': "Animal Yokochou - Dokidoki Shinkyu Shiken",
    },
    "ANIYOKO     BAYJ": {
        'uttd': "BAYJ",
        'title': "Animal Yokochou - Dokidoki Kyushutsu Daisakusen! no Maki",
    },
    "ANSTOSS     BAQP": {
        'uttd': "BAQP",
        'title': "Premier Action",
    },
    "ANTZ RACING ANUE": {
        'uttd': "ANUE",
        'title': "Antz - Extreme Racing",
    },
    "ANTZ RACING ANZP": {
        'uttd': "ANZP",
        'title': "Antz - Extreme Racing",
    },
    "AOZORA      AAZJ": {
        'uttd': "AAZJ",
        'title': "Ao-Zoura to Nakamatachi - Yume no Bouken",
    },
    "ARMY MEN ADVASAE": {
        'uttd': "ASAE",
        'title': "Army Men Advance",
    },
    "ARMY MEN OG AMEE": {
        'uttd': "AMEE",
        'title': "Army Men - Operation Green",
    },
    "ARMY WAR    BG6E": {
        'uttd': "BG6E",
        'title': "Super Army War",
    },
    "AROUND THE WB8DE": {
        'uttd': "B8DE",
        'title': "Around the World in 80 Days",
    },
    "AROUND THE WB8DP": {
        'uttd': "B8DP",
        'title': "Around the World in 80 Days",
    },
    "ARTHUR      B2NE": {
        'uttd': "B2NE",
        'title': "Arthur and the Invisibles",
    },
    "ARTHUR      B2NP": {
        'uttd': "B2NP",
        'title': "Arthur and the Minimoys",
    },
    "ASOT        A3QE": {
        'uttd': "A3QE",
        'title': "Sound of Thunder, A",
    },
    "ASTERIX     BLXP": {
        'uttd': "BLXP",
        'title': "Asterix & Obelix XXL",
    },
    "ASTERIX & OBAOBP": {
        'uttd': "AOBP",
        'title': "Asterix & Obelix - Bash Them All!",
    },
    "ASTEROIDPONGB64P": {
        'uttd': "B64P",
        'title': "Pong - Asteroids - Yars' Revenge",
    },
    "ASTROBOY    BTAE": {
        'uttd': "BTAE",
        'title': "Astro Boy - Omega Factor",
        'icon0': 'https://images.launchbox-app.com/8dc7dee2-3ac0-4905-a362-f269f3079846.jpg',
        'pic0': 'https://images.launchbox-app.com/d9090e02-4373-40cc-a4d2-bf67e113b91a.png',
        'pic1': 'https://images.launchbox-app.com/7516f500-4e6c-4d92-801d-7feb8dcab322.jpg',
        'snd0': 'https://www.youtube.com/watch?v=W63cvvBFbOI&list=PL8C60229988A2CB28&index=1',
    },
    "ASTROBOY    BTAJ": {
        'uttd': "BTAJ",
        'title': "Astro Boy - Tetsuwan Atom - Atom Heart no Himitsu",
        'icon0': 'https://images.launchbox-app.com/97fdf958-c48a-4e6f-af90-129d4debf5e0.png',
        'pic0': 'https://images.launchbox-app.com/d9090e02-4373-40cc-a4d2-bf67e113b91a.png',
        'pic1': 'https://images.launchbox-app.com/7516f500-4e6c-4d92-801d-7feb8dcab322.jpg',
        'snd0': 'https://www.youtube.com/watch?v=W63cvvBFbOI&list=PL8C60229988A2CB28&index=1',
    },
    "ASTRO BOY-OMBTAP": {
        'uttd': "BTAP",
        'title': "Astro Boy - Omega Factor",
        'icon0': 'https://images.launchbox-app.com/8dc7dee2-3ac0-4905-a362-f269f3079846.jpg',
        'pic0': 'https://images.launchbox-app.com/d9090e02-4373-40cc-a4d2-bf67e113b91a.png',
        'pic1': 'https://images.launchbox-app.com/7516f500-4e6c-4d92-801d-7feb8dcab322.jpg',
        'snd0': 'https://www.youtube.com/watch?v=W63cvvBFbOI&list=PL8C60229988A2CB28&index=1',
    },
    "ATARI_ANNIVEAAVE": {
        'uttd': "AAVE",
        'title': "Atari Anniversary Advance",
    },
    "ATARI ANNIVEAAVP": {
        'uttd': "AAVP",
        'title': "Atari Anniversary Advance",
    },
    "ATLANTIS    ATLE": {
        'uttd': "ATLE",
        'title': "Atlantis - The Lost Empire",
    },
    "ATLANTIS    ATLX": {
        'uttd': "ATLX",
        'title': "Atlantis - The Lost Empire",
    },
    "ATOMIC BETTYBETE": {
        'uttd': "BETE",
        'title': "Atomic Betty",
    },
    "ATV QUAD POWAQRE": {
        'uttd': "AQRE",
        'title': "ATV Quad Power Racing",
    },
    "ATV THUNDER B3BE": {
        'uttd': "B3BE",
        'title': "ATV Thunder Ridge Riders",
    },
    "ATV THUNDER B3BP": {
        'uttd': "B3BP",
        'title': "ATV Thunder Ridge Riders",
    },
    "AV 7111     AGBJ": {
        'uttd': "AGBJ",
        'title': "Game Boy Advance SP AV Adaptor",
    },
    "AVATAR      BQZE": {
        'uttd': "BQZE",
        'title': "Avatar - The Last Airbender",
    },
    "AVATAR      BQZP": {
        'uttd': "BQZP",
        'title': "Avatar - The Legend of Aang",
    },
    "AZUMANGALINKAZAJ": {
        'uttd': "AZAJ",
        'title': "Azumanga Daiou Advance",
    },
    "BABAR_TTR   BBVE": {
        'uttd': "BBVE",
        'title': "Babar to the Rescue",
    },
    "BABAR_TTR   BBVP": {
        'uttd': "BBVP",
        'title': "Babar to the Rescue",
    },
    "BACKTOSTONE BBCE": {
        'uttd': "BBCE",
        'title': "Back to Stone",
    },
    "BACKTRACK   ABKE": {
        'uttd': "ABKE",
        'title': "BackTrack",
    },
    "BACKYARDFBL AYFE": {
        'uttd': "AYFE",
        'title': "Backyard Football",
    },
    "BACKYARD HCYBYHE": {
        'uttd': "BYHE",
        'title': "Backyard Hockey",
    },
    "BAD APPLE   BZTE": {
        'uttd': "BZTE",
        'title': "VeggieTales - LarryBoy and the Bad Apple",
    },
    "BALDURSGATE BGDE": {
        'uttd': "BGDE",
        'title': "Baldur's Gate - Dark Alliance",
    },
    "BALDURSGATE BGDP": {
        'uttd': "BGDP",
        'title': "Baldur's Gate - Dark Alliance",
    },
    "BALLISTIC ECAEEE": {
        'uttd': "AEEE",
        'title': "Ballistic - Ecks vs. Sever",
    },
    "BALLOONFIGHTFBFJ": {
        'uttd': "FBFJ",
        'title': "Famicom Mini Vol. 13 - Balloon Fight",
    },
    "BANJOKAZOOIEBKZE": {
        'uttd': "BKZE",
        'title': "Banjo-Kazooie - Grunty's Revenge",
    },
    "BANJOKAZOOIEBKZI": {
        'uttd': "BKZI",
        'title': "Banjo-Kazooie - La Vendetta di Grunty",
    },
    "BANJOKAZOOIEBKZS": {
        'uttd': "BKZS",
        'title': "Banjo-Kazooie - La Venganza de Grunty",
    },
    "BANJOKAZOOIEBKZX": {
        'uttd': "BKZX",
        'title': "Banjo-Kazooie - Grunty's Revenge",
    },
    "BANJO PILOT BAJE": {
        'uttd': "BAJE",
        'title': "Banjo Pilot",
    },
    "BANJO PILOT BAJP": {
        'uttd': "BAJP",
        'title': "Banjo Pilot",
    },
    "BARBIE12PRCSBB3E": {
        'uttd': "BB3E",
        'title': "Barbie in the 12 Dancing Princesses",
    },
    "BARBIE12PREUBB3P": {
        'uttd': "BB3P",
        'title': "Barbie in the 12 Dancing Princesses",
    },
    "BARBIE      AI8E": {
        'uttd': "AI8E",
        'title': "Barbie Horse Adventures - Blue Ribbon Race",
    },
    "BARBIE      AI8P": {
        'uttd': "AI8P",
        'title': "Barbie Horse Adventures",
    },
    "BARBIE AS THBAUP": {
        'uttd': "BAUP",
        'title': "Barbie - The Princess and the Pauper",
    },
    "BARBIE DM   BBIE": {
        'uttd': "BBIE",
        'title': "Barbie Diaries, The - High School Mystery",
    },
    "BARBIE DM   BBIP": {
        'uttd': "BBIP",
        'title': "Barbie Diaries, The - High School Mystery",
    },
    "BARBIE PEGASBE5P": {
        'uttd': "BE5P",
        'title': "Barbie and the Magic of Pegasus",
    },
    "BARBIEPEGASUBE5E": {
        'uttd': "BE5E",
        'title': "Barbie and the Magic of Pegasus",
    },
    "BARBIE P&P  BAUE": {
        'uttd': "BAUE",
        'title': "Barbie - The Princess and the Pauper",
    },
    "BARNYARD    BBYE": {
        'uttd': "BBYE",
        'title': "Barnyard",
    },
    "BARNYARD    BBYX": {
        'uttd': "BBYX",
        'title': "Barnyard",
    },
    "BASEBALL2003ACKE": {
        'uttd': "ACKE",
        'title': "Backyard Baseball",
    },
    "BASEBALL2006BCYE": {
        'uttd': "BCYE",
        'title': "Backyard Baseball 2006",
    },
    "BASEBALL2007BC7E": {
        'uttd': "BC7E",
        'title': "Backyard Sports - Baseball 2007",
    },
    "BASEBALL ADVABPE": {
        'uttd': "ABPE",
        'title': "Baseball Advance",
    },
    "BASS ADVANCEAABJ": {
        'uttd': "AABJ",
        'title': "Super Black Bass Advance",
    },
    "BASS ADVANCEAABP": {
        'uttd': "AABP",
        'title': "Super Black Bass Advance",
    },
    "BATMANBEGINSBBGE": {
        'uttd': "BBGE",
        'title': "Batman Begins",
    },
    "BATMAN-RISE BATE": {
        'uttd': "BATE",
        'title': "Batman - Rise of Sin Tzu",
    },
    "BATMAN-VENGEABTE": {
        'uttd': "ABTE",
        'title': "Batman Vengeance",
    },
    "BATMAN-VENGEABTP": {
        'uttd': "ABTP",
        'title': "Batman Vengeance",
    },
    "BATTLEBOTS  ABEE": {
        'uttd': "ABEE",
        'title': "BattleBots - Beyond the BattleBox",
    },
    "BATTLEBOTS  ABEP": {
        'uttd': "ABEP",
        'title': "BattleBots - Beyond the BattleBox",
    },
    "BATTLEBOTSDDBBDE": {
        'uttd': "BBDE",
        'title': "BattleBots - Design & Destroy",
    },
    "BATTLECHIPGPA89E": {
        'uttd': "A89E",
        'title': "Megaman - Battle Chip Challenge",
    },
    "BATTLECHIPGPA89J": {
        'uttd': "A89J",
        'title': "Rockman EXE Battle Chip GP",
    },
    "BATTLECHIPGPA89P": {
        'uttd': "A89P",
        'title': "Megaman - Battle Chip Challenge",
    },
    "BATTLEMASTERBQBJ": {
        'uttd': "BQBJ",
        'title': "Konchu Monster - Battle Master",
    },
    "BATTLE X2   BBFJ": {
        'uttd': "BBFJ",
        'title': "Battle X Battle - Kyodai Gyo Densetsu",
    },
    "BAYBLADE_1  AHEJ": {
        'uttd': "AHEJ",
        'title': "Bakuten Shoot Beyblade - Gekitou! Saikyou Blader",
    },
    "BAYBLADE_2  AB8J": {
        'uttd': "AB8J",
        'title': "Bakuten Shoot Beyblade 2002 - Ikuze! Bakutou! Chou Jiryoku Battle!!",
    },
    "BAYBLADE_3D A3EJ": {
        'uttd': "A3EJ",
        'title': "Bakuten Shoot Beyblade 2002 - Gekisen! Team Battle!! Kouryuu no Shou - Daichi Hen",
    },
    "BAYBLADE_3T A3WJ": {
        'uttd': "A3WJ",
        'title': "Bakuten Shoot Beyblade 2002 - Gekisen! Team Battle!! Seiryuu no Shou - Takao Hen",
    },
    "BBASKET2007 BB7E": {
        'uttd': "BB7E",
        'title': "Backyard Sports - Basketball 2007",
    },
    "BBASKETBALL AYBE": {
        'uttd': "AYBE",
        'title': "Backyard Basketball",
    },
    "BBBALL      A8LJ": {
        'uttd': "A8LJ",
        'title': "BB Booru",
    },
    "BBC         AB6P": {
        'uttd': "AB6P",
        'title': "Black Belt Challenge",
    },
    "BB-DAMA2FIREBBME": {
        'uttd': "BBME",
        'title': "Battle B-Daman - Fire Spirits!",
    },
    "BB-DAMA2FIREBBMJ": {
        'uttd': "BBMJ",
        'title': "B-Legends! Battle B-Daman - Fire Spirits!",
    },
    "BB-DAMAN    BDXE": {
        'uttd': "BDXE",
        'title': "Battle B-Daman",
    },
    "BB-DAMANFIREBDXJ": {
        'uttd': "BDXJ",
        'title': "B-Legends! Battle B-Daman - Moero! B-Damashii!!",
    },
    "BB_&_DP_FRE_BWBF": {
        'uttd': "BWBF",
        'title': "2 Games in 1 - Disney Princesse + Frere des Ours",
    },
    "BB_&_DP_GER_BWBD": {
        'uttd': "BWBD",
        'title': "2 Games in 1 - Disneys Prinzessinnen + Baren Bruder",
    },
    "BB_&_DP_ITALBWBI": {
        'uttd': "BWBI",
        'title': "2 Games in 1 - Disney Principesse + Koda, Fratello Orso",
    },
    "BB_&_DP_SPANBWBS": {
        'uttd': "BWBS",
        'title': "2 Games in 1 - Disney Princesas + Hermano Oso",
    },
    "B-DASH EX   ABDE": {
        'uttd': "ABDE",
        'title': "Boulder Dash EX",
    },
    "B-DASH EX   ABDJ": {
        'uttd': "ABDJ",
        'title': "Boulder Dash EX",
    },
    "B-DASH EX   ABDP": {
        'uttd': "ABDP",
        'title': "Boulder Dash EX",
    },
    "BEASTSHOOTERAH5J": {
        'uttd': "AH5J",
        'title': "Beast Shooter - Mezase Beast King!",
    },
    "BESTFRIENDS BHBP": {
        'uttd': "BHBP",
        'title': "Hunde & Katzen Best Friends",
    },
    "BEYBLADEGREVBB2E": {
        'uttd': "BB2E",
        'title': "Beyblade G-Revolution",
    },
    "BEYBLADEGREVBB2P": {
        'uttd': "BB2P",
        'title': "Beyblade G-Revolution",
    },
    "BEYBLADE: ULBEYE": {
        'uttd': "BEYE",
        'title': "Beyblade V-Force - Ultimate Blader Jam",
    },
    "BEYBLADE: ULBEYP": {
        'uttd': "BEYP",
        'title': "Beyblade V-Force - Ultimate Blader Jam",
    },
    "BIBIBLOCKSB2BBXD": {
        'uttd': "BBXD",
        'title': "Bibi Blocksberg - Der Magische Hexenkreis",
    },
    "BIBITINA01  BUXD": {
        'uttd': "BUXD",
        'title': "Bibi und Tina - Ferien auf dem Martinshof",
    },
    "BIBLE GAME  BIBE": {
        'uttd': "BIBE",
        'title': "Bible Game, The",
    },
    "BIENEMAJA   BKFX": {
        'uttd': "BKFX",
        'title': "Biene Maja, Die - Klatschmohnwiese in Gefahr",
    },
    "BIGMTRUCKER B63E": {
        'uttd': "B63E",
        'title': "Big Mutha Truckers",
    },
    "BIGMTRUCKER B63P": {
        'uttd': "B63P",
        'title': "Big Mutha Truckers",
    },
    "BILLY BLAZESAQHE": {
        'uttd': "AQHE",
        'title': "Rescue Heroes - Billy Blazes!",
    },
    "BIONICLE    BILE": {
        'uttd': "BILE",
        'title': "Bionicle - Maze of Shadows",
    },
    "BIONICLEGAMEBIOE": {
        'uttd': "BIOE",
        'title': "Bionicle",
    },
    "BIONICLEGAMEBIOP": {
        'uttd': "BIOP",
        'title': "Bionicle",
    },
    "BIONICLEH   BIHE": {
        'uttd': "BIHE",
        'title': "Bionicle Heroes",
    },
    "BIONICLEH   BIHP": {
        'uttd': "BIHP",
        'title': "Bionicle Heroes",
    },
    "BIONICLE MATA5AE": {
        'uttd': "A5AE",
        'title': "Bionicle - Matoran Adventures",
    },
    "BIONICLE_MOSBILP": {
        'uttd': "BILP",
        'title': "Bionicle - Maze of Shadows",
    },
    "BKM BATTLES ABWE": {
        'uttd': "ABWE",
        'title': "Butt-Ugly Martians - B.K.M. Battles",
    },
    "BKM BATTLES AUQP": {
        'uttd': "AUQP",
        'title': "Butt-Ugly Martians - B.K.M. Battles",
    },
    "BLACK BLACK AWEJ": {
        'uttd': "AWEJ",
        'title': "Black Black - Bura Bura",
    },
    "BLACKMATRIX0AXBJ": {
        'uttd': "AXBJ",
        'title': "Black Matrix Zero",
    },
    "BLACKTHORNE AQXE": {
        'uttd': "AQXE",
        'title': "Blackthorne",
    },
    "BLACKTHORNE AQXP": {
        'uttd': "AQXP",
        'title': "Blackthorne",
    },
    "BLADESOFTHDRBBHE": {
        'uttd': "BBHE",
        'title': "Blades of Thunder",
    },
    "BLEACH ADV1 BLEJ": {
        'uttd': "BLEJ",
        'title': "Bleach Advance",
    },
    "BLENDER BROSABRE": {
        'uttd': "ABRE",
        'title': "Blender Bros.",
    },
    "B-MAX2BOM   AMHJ": {
        'uttd': "AMHJ",
        'title': "Bomberman Max 2 - Bomberman Version",
    },
    "B-MAX2MAX   AMYJ": {
        'uttd': "AMYJ",
        'title': "Bomberman Max 2 - Max Version",
    },
    "BMAX2-RED   AMYP": {
        'uttd': "AMYP",
        'title': "Bomberman Max 2 - Red Advance",
    },
    "BMX TRICK RAAT9E": {
        'uttd': "AT9E",
        'title': "BMX Trick Racer",
    },
    "BOARDGAMES  B6EE": {
        'uttd': "B6EE",
        'title': "Board Game Classics",
    },
    "BOARDGAMES  B6EP": {
        'uttd': "B6EP",
        'title': "Board Game Classics",
    },
    "BO_BOBO2_GBABOBJ": {
        'uttd': "BOBJ",
        'title': "Boboboubo Boubobo - Maji de!! Shinken Battle",
    },
    "BO_BOBO3_GBABB9J": {
        'uttd': "BB9J",
        'title': "Boboboubo Boubobo - 9 Kyoku Senshi Gag Yuugou",
    },
    "BO_BOBO4_GBABOSJ": {
        'uttd': "BOSJ",
        'title': "Boboboubo Boubobo - Bakutou Hajike Taisen",
    },
    "BO_BOBO_GBA A8VJ": {
        'uttd': "A8VJ",
        'title': "Boboboubo Boubobo - Ougi 87.5 Bakuretsu Hanage Shinken",
    },
    "BOF1        ABFE": {
        'uttd': "ABFE",
        'title': "Breath of Fire",
    },
    "BOF1        ABFJ": {
        'uttd': "ABFJ",
        'title': "Breath of Fire - Ryuu no Senshi",
    },
    "BOF1        ABFP": {
        'uttd': "ABFP",
        'title': "Breath of Fire",
    },
    "BOF2        AB2E": {
        'uttd': "AB2E",
        'title': "Breath of Fire II",
    },
    "BOF2        AB2J": {
        'uttd': "AB2J",
        'title': "Breath of Fire II - Shimei no Ko",
    },
    "BOF2        AB2P": {
        'uttd': "AB2P",
        'title': "Breath of Fire II",
    },
    "BOF EUR     ABFX": {
        'uttd': "ABFX",
        'title': "Breath of Fire",
    },
    "BOKENJIMA 1 FTBJ": {
        'uttd': "FTBJ",
        'title': "Famicom Mini Vol. 17 - Takahashi Meijin no Bouken Shima",
    },
    "BOKTAI2     U32E": {
        'uttd': "U32E",
        'title': "Boktai 2 - Solar Boy Django",
    },
    "BOKTAI2     U32P": {
        'uttd': "U32P",
        'title': "Boktai 2 - Solar Boy Django",
    },
    "BOKTAI3     U33J": {
        'uttd': "U33J",
        'title': "Shin Bokura no Taiyou - Gyakushuu no Sabata",
    },
    "BOKTAI      U3IE": {
        'uttd': "U3IE",
        'title': "Boktai - The Sun is in Your Hand",
    },
    "BOKTAI      U3IP": {
        'uttd': "U3IP",
        'title': "Boktai - The Sun is in Your Hand",
    },
    "BOKUKAN AGB ABCJ": {
        'uttd': "ABCJ",
        'title': "Boku ha Koukuu Kanseikan",
    },
    "BOKUMONOGBA A4NJ": {
        'uttd': "A4NJ",
        'title': "Bokujou Monogatari - Mineral Town no Nakamatachi",
    },
    "BOKUMONOGBA BFGJ": {
        'uttd': "BFGJ",
        'title': "Bokujou Monogatari - Mineral Town no Nakamatachi for Girl",
    },
    "BOKUTAI     U3IJ": {
        'uttd': "U3IJ",
        'title': "Bokura no Taiyou - Taiyou Action RPG",
    },
    "BOMBER MAN  FBME": {
        'uttd': "FBME",
        'title': "Classic NES Series - Bomberman",
    },
    "BOMBER MAN  FBMJ": {
        'uttd': "FBMJ",
        'title': "Famicom Mini Vol. 09 - Bomberman",
    },
    "BOMBERMANJGCBOMJ": {
        'uttd': "BOMJ",
        'title': "Bomberman Jetters - Game Collection",
    },
    "BOMBERMAN MAAMHP": {
        'uttd': "AMHP",
        'title': "Bomberman Max 2 - Blue Advance",
    },
    "BOM_JET.JPN AJZJ": {
        'uttd': "AJZJ",
        'title': "Bomberman Jetters - Densetsu no Bomberman",
    },
    "BOMSTORY    ABSJ": {
        'uttd': "ABSJ",
        'title': "Bomberman Story",
    },
    "BOMSTORYUSA ABSE": {
        'uttd': "ABSE",
        'title': "Bomberman Tournament",
    },
    "BOND EON    BJBE": {
        'uttd': "BJBE",
        'title': "007 - Everything or Nothing",
    },
    "BOND EON    BJBJ": {
        'uttd': "BJBJ",
        'title': "007 - Everything or Nothing",
    },
    "BOOKWORM    BKWE": {
        'uttd': "BKWE",
        'title': "Book Worm",
    },
    "BOUKYAKU    BBSJ": {
        'uttd': "BBSJ",
        'title': "Boukyaku no Senritsu - The Melody of Oblivion",
    },
    "BOUNDISH    BVDJ": {
        'uttd': "BVDJ",
        'title': "bit Generations - Boundish",
    },
    "BOXEM       ABOE": {
        'uttd': "ABOE",
        'title': "Boxing Fever",
    },
    "BOYSSOCCER#2A2ZJ": {
        'uttd': "A2ZJ",
        'title': "Zen-Nippon Shounen Soccer Taikai 2 - Mezase Nippon-ichi!",
    },
    "BP-BASEBALL A8YJ": {
        'uttd': "A8YJ",
        'title': "Best Play Pro Yakyuu",
    },
    "BRATZ       A2RE": {
        'uttd': "A2RE",
        'title': "Bratz",
    },
    "BRATZ       A2RP": {
        'uttd': "A2RP",
        'title': "Bratz",
    },
    "BRATZ BABYZ BBZE": {
        'uttd': "BBZE",
        'title': "Bratz - Babyz",
    },
    "BRATZ BABYZ BBZP": {
        'uttd': "BBZP",
        'title': "Bratz - Babyz",
    },
    "BRATZDIAMONDBXFD": {
        'uttd': "BXFD",
        'title': "Bratz - Forever Diamondz",
    },
    "BRATZDIAMONDBXFE": {
        'uttd': "BXFE",
        'title': "Bratz - Forever Diamondz",
    },
    "BRATZDIAMONDBXFP": {
        'uttd': "BXFP",
        'title': "Bratz - Forever Diamondz",
    },
    "BRATZ ROCK ABRRD": {
        'uttd': "BRRD",
        'title': "Bratz - Rock Angelz",
    },
    "BRATZ ROCK ABRRE": {
        'uttd': "BRRE",
        'title': "Bratz - Rock Angelz",
    },
    "BRATZ ROCK ABRRF": {
        'uttd': "BRRF",
        'title': "Bratz - Rock Angelz",
    },
    "BRATZ ROCK ABRRS": {
        'uttd': "BRRS",
        'title': "Bratz - Rock Angelz",
    },
    "BREAKOUTCENTB6ZP": {
        'uttd': "B6ZP",
        'title': "Centipede - Breakout - Warlords",
    },
    "BROKENSWORD ABJE": {
        'uttd': "ABJE",
        'title': "Broken Sword - The Shadow of the Templars",
    },
    "BROKENSWORD ABJP": {
        'uttd': "ABJP",
        'title': "Broken Sword - The Shadow of the Templars",
    },
    "BROTHER BEARBBRE": {
        'uttd': "BBRE",
        'title': "Brother Bear",
    },
    "BROTHER BEARBBRP": {
        'uttd': "BBRP",
        'title': "Brother Bear",
    },
    "BROTHER BEARBBRX": {
        'uttd': "BBRX",
        'title': "Brother Bear",
    },
    "BRUCE LEE   ALEE": {
        'uttd': "ALEE",
        'title': "Bruce Lee - Return of the Legend",
    },
    "BRUCE LEE   ALEP": {
        'uttd': "ALEP",
        'title': "Bruce Lee - Return of the Legend",
    },
    "B STADIUM   BQSJ": {
        'uttd': "BQSJ",
        'title': "Konchu Monster - Battle Stadium",
    },
    "BUBBLE BOBBLAONE": {
        'uttd': "AONE",
        'title': "Bubble Bobble - Old & New",
    },
    "BUBBLEBOBBLEA2BJ": {
        'uttd': "A2BJ",
        'title': "Bubble Bobble - Old & New",
    },
    "BUBBLEBOBBLEAONP": {
        'uttd': "AONP",
        'title': "Bubble Bobble - Old & New",
    },
    "BUFFY       AVYD": {
        'uttd': "AVYD",
        'title': "Buffy - Im Bann der Damonen - Koenig Darkhuls Zorn",
    },
    "BUFFY       AVYE": {
        'uttd': "AVYE",
        'title': "Buffy - The Vampire Slayer - Wrath of the Darkhul King",
    },
    "BUFFY       AVYF": {
        'uttd': "AVYF",
        'title': "Buffy Contre les Vampires - La Colere de Darkhul",
    },
    "BUKKAZOOM   AZHP": {
        'uttd': "AZHP",
        'title': "Hugo - Bukkazoom!",
    },
    "BURABURADNKYBBKJ": {
        'uttd': "BBKJ",
        'title': "Bura Bura Donkey",
    },
    "BURNIN RUBBEAHWP": {
        'uttd': "AHWP",
        'title': "Hot Wheels - Burnin' Rubber",
    },
    "BUSTAMOVEGBAABME": {
        'uttd': "ABME",
        'title': "Super Bust-A-Move",
    },
    "BUSTAMOVEGBAABMP": {
        'uttd': "ABMP",
        'title': "Super Bust-A-Move",
    },
    "BUUGTCOLLECTBUFE": {
        'uttd': "BUFE",
        'title': "2 Games in 1 - Dragon Ball Z - Buu's Fury + Dragon Ball GT - Transformation",
    },
    "BYF 2006    BYFE": {
        'uttd': "BYFE",
        'title': "Backyard Football 2006",
    },
    "BYF 2007    BF7E": {
        'uttd': "BF7E",
        'title': "Backyard Sports - Football 2007",
    },
    "BYSK8NG2006 BS6E": {
        'uttd': "BS6E",
        'title': "Backyard Skateboarding",
    },
    "CABBAGE PATCBCGE": {
        'uttd': "BCGE",
        'title': "Cabbage Patch Kids - The Patch Puppy Rescue",
    },
    "CABBAGE PATCBCGP": {
        'uttd': "BCGP",
        'title': "Cabbage Patch Kids - The Patch Puppy Rescue",
    },
    "CABELAS BGH A8HE": {
        'uttd': "A8HE",
        'title': "Cabela's Big Game Hunter",
    },
    "CABELA'S BIGBG5E": {
        'uttd': "BG5E",
        'title': "Cabela's Big Game Hunter - 2005 Adventures",
    },
    "CAESARPALACEACPE": {
        'uttd': "ACPE",
        'title': "Caesars Palace Advance",
    },
    "CAKECASTLE  BLIJ": {
        'uttd': "BLIJ",
        'title': "Little Patissier - Cake no Oshiro",
    },
    "CAKE STORY  AAXJ": {
        'uttd': "AAXJ",
        'title': "Fantastic Maerchen - Cake-yasan Monogatari",
    },
    "CALCIOBIT01 BIXJ": {
        'uttd': "BIXJ",
        'title': "Calciobit",
    },
    "CAMP LAZLO  BLCE": {
        'uttd': "BLCE",
        'title': "Camp Lazlo - Leaky Lake Games",
    },
    "CANDYLAND CHBC4E": {
        'uttd': "BC4E",
        'title': "Candy Land - Chutes and Ladders - Memory",
    },
    "CANEPLATFR00MCNF": {
        'uttd': "MCNF",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Edition Platinum",
    },
    "CANEPREMFR00MCPF": {
        'uttd': "MCPF",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Edition Premium",
    },
    "CANESPECFR00MCSF": {
        'uttd': "MCSF",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Edition Speciale",
    },
    "CAPCOMINIMIXBC6E": {
        'uttd': "BC6E",
        'title': "Capcom Classics - Mini Mix",
    },
    "CARBATTLERGOACBJ": {
        'uttd': "ACBJ",
        'title': "Gekitou! Car Battler Go!!",
    },
    "CARBATTLERJOACBE": {
        'uttd': "ACBE",
        'title': "Car Battler Joe",
    },
    "CARDE READERPEAJ": {
        'uttd': "PEAJ",
        'title': "Card e-Reader",
    },
    "CARDE READERPSAE": {
        'uttd': "PSAE",
        'title': "e-Reader",
    },
    "CARDEREADER+PSAJ": {
        'uttd': "PSAJ",
        'title': "Card e-Reader+",
    },
    "CARE_BEARS  BEAE": {
        'uttd': "BEAE",
        'title': "Care Bears - The Care Quests",
    },
    "CARE_BEARS  BEAP": {
        'uttd': "BEAP",
        'title': "Care Bears - The Care Quests",
    },
    "CARRERA POWEAEDP": {
        'uttd': "AEDP",
        'title': "Carrera Power Slide",
    },
    "CARSAGB     BCAJ": {
        'uttd': "BCAJ",
        'title': "Cars",
    },
    "CARTONETW002MC2E": {
        'uttd': "MC2E",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Volume 2",
    },
    "CARTONETW003MCPE": {
        'uttd': "MCPE",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Premium Edition",
    },
    "CARTONETW004MCSE": {
        'uttd': "MCSE",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Special Edition",
    },
    "CARTONETW005MCME": {
        'uttd': "MCME",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Limited Edition",
    },
    "CARTONETW006MCNE": {
        'uttd': "MCNE",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Platinum Edition",
    },
    "CARTOONNET01MCTE": {
        'uttd': "MCTE",
        'title': "Game Boy Advance Video - Cartoon Network Collection - Volume 1",
    },
    "CASINO/HOLDMBWCE": {
        'uttd': "BWCE",
        'title': "2 Games in 1 - Golden Nugget Casino + Texas Hold'em Poker",
    },
    "CASPER      ACSE": {
        'uttd': "ACSE",
        'title': "Casper",
    },
    "CASPER      ACSP": {
        'uttd': "ACSP",
        'title': "Casper",
    },
    "CASTLECAPERSARGE": {
        'uttd': "ARGE",
        'title': "Rugrats - Castle Capers",
    },
    "CASTLECAPERSARGF": {
        'uttd': "ARGF",
        'title': "Razmoket, Les - Voler n'est pas Jouer",
    },
    "CASTLECAPERSARGS": {
        'uttd': "ARGS",
        'title': "Rugrats - Travesuras en el Castillo",
    },
    "CASTLEVANIA1ACHE": {
        'uttd': "ACHE",
        'title': "Castlevania - Harmony of Dissonance",
    },
    "CASTLEVANIA1ACHJ": {
        'uttd': "ACHJ",
        'title': "Castlevania - Byakuya no Concerto",
    },
    "CASTLEVANIA1ACHP": {
        'uttd': "ACHP",
        'title': "Castlevania - Harmony of Dissonance",
    },
    "CASTLEVANIA2A2CE": {
        'uttd': "A2CE",
        'title': "Castlevania - Aria of Sorrow",
        'icon0': 'https://images.launchbox-app.com/23588e39-184c-4b82-8c7a-5c46d1868013.jpg',
        'pic0': 'https://images.launchbox-app.com/9e11fc8f-6df7-4ceb-ac9d-f09c20ffca98.png',
        'pic1': 'https://images.launchbox-app.com/434d0e00-59c9-405f-9c85-ae8fb2f1bb07.jpg',
        'snd0': 'https://www.youtube.com/watch?v=IlVOomZcv0Q&list=PL6E9hVlff2TGFs9fVmsNIeuSpciQ9eKgi&index=1',
    },
    "CASTLEVANIA2A2CJ": {
        'uttd': "A2CJ",
        'title': "Castlevania - Akatsuki no Minuet",
        'icon0': 'https://images.launchbox-app.com/297f69a9-40aa-49db-a31a-ad79154feabd.png',
        'pic0': 'https://images.launchbox-app.com/9e11fc8f-6df7-4ceb-ac9d-f09c20ffca98.png',
        'pic1': 'https://images.launchbox-app.com/434d0e00-59c9-405f-9c85-ae8fb2f1bb07.jpg',
        'snd0': 'https://www.youtube.com/watch?v=IlVOomZcv0Q&list=PL6E9hVlff2TGFs9fVmsNIeuSpciQ9eKgi&index=1',
    },
    "CASTLEVANIA2A2CP": {
        'uttd': "A2CP",
        'title': "Castlevania - Aria of Sorrow",
        'icon0': 'https://images.launchbox-app.com/42f3dffe-05db-4020-9914-3f8446178611.jpg',
        'pic0': 'https://images.launchbox-app.com/a103d387-a59e-47ab-8afa-6adf73cb32c5.png',
        'pic1': 'https://images.launchbox-app.com/434d0e00-59c9-405f-9c85-ae8fb2f1bb07.jpg',
        'snd0': 'https://www.youtube.com/watch?v=IlVOomZcv0Q&list=PL6E9hVlff2TGFs9fVmsNIeuSpciQ9eKgi&index=1',
    },
    "CASTLEVANIA FADE": {
        'uttd': "FADE",
        'title': "Classic NES Series - Castlevania",
    },
    "CASTLEWEEN  AWNP": {
        'uttd': "AWNP",
        'title': "Castleween",
    },
    "CATINTHEHAT AQTE": {
        'uttd': "AQTE",
        'title': "Dr. Seuss' The Cat in the Hat",
    },
    "CATWOMAN    BCWE": {
        'uttd': "BCWE",
        'title': "Catwoman",
    },
    "CATZ        AN3E": {
        'uttd': "AN3E",
        'title': "Catz",
    },
    "CATZ        AN3X": {
        'uttd': "AN3X",
        'title': "Catz",
    },
    "CENTIPEDECOMB6ZE": {
        'uttd': "B6ZE",
        'title': "Centipede - Breakout - Warlords",
    },
    "CHAILIEN NO BKRJ": {
        'uttd': "BKRJ",
        'title': "No no no Puzzle Chailien",
    },
    "CHARLIE AND BCFE": {
        'uttd': "BCFE",
        'title': "Charlie and the Chocolate Factory",
    },
    "CHARLIE AND BCFP": {
        'uttd': "BCFP",
        'title': "Charlie and the Chocolate Factory",
    },
    "CHARLOTTE   BCJE": {
        'uttd': "BCJE",
        'title': "Charlotte's Web",
    },
    "CHARLOTTE   BCJP": {
        'uttd': "BCJP",
        'title': "Charlotte's Web",
    },
    "CHEETAHGIRLSBCQE": {
        'uttd': "BCQE",
        'title': "Cheetah Girls, The",
    },
    "CHESSMASTER ACYD": {
        'uttd': "ACYD",
        'title': "Chessmaster",
    },
    "CHESSMASTER ACYE": {
        'uttd': "ACYE",
        'title': "Chessmaster",
    },
    "CHESSMASTER ACYF": {
        'uttd': "ACYF",
        'title': "Chessmaster",
    },
    "CHESSMASTER ACYP": {
        'uttd': "ACYP",
        'title': "Chessmaster",
    },
    "CHICKENSHOOTB6FP": {
        'uttd': "B6FP",
        'title': "Chicken Shoot",
    },
    "CHICKENSHOT1B6FE": {
        'uttd': "B6FE",
        'title': "Chicken Shoot",
    },
    "CHICKENSHOT2B6GE": {
        'uttd': "B6GE",
        'title': "Chicken Shoot 2",
    },
    "CHICKENSHOT2B6GP": {
        'uttd': "B6GP",
        'title': "Chicken Shoot 2",
    },
    "CHIMP CHASE AWTE": {
        'uttd': "AWTE",
        'title': "Wild Thornberrys, The - Chimp Chase",
    },
    "CHIMP CHASE AWTF": {
        'uttd': "AWTF",
        'title': "Famille Delajungle, La - A la Poursuite de Darwin",
    },
    "CHINESE1&2  BSAJ": {
        'uttd': "BSAJ",
        'title': "Super Chinese Advance 1 & 2",
    },
    "CHINMOKU-ESTAGDJ": {
        'uttd': "AGDJ",
        'title': "Chinmoku no Iseki - Estpolis Gaiden",
    },
    "CHOBIGURUMI2BDCJ": {
        'uttd': "BDCJ",
        'title': "Doubutsujima no Chobi Gurumi 2 - Tamachan Monogatari",
    },
    "CHOBIGURUMI A8DJ": {
        'uttd': "A8DJ",
        'title': "Doubutsu Shima no Chobi Gurumi",
    },
    "CHOBITS-MMV1AOCJ": {
        'uttd': "AOCJ",
        'title': "Chobits - Atashi Dake no Hito",
    },
    "CHOCOBOLAND A5BJ": {
        'uttd': "A5BJ",
        'title': "Chocobo Land - A Game of Dice",
    },
    "CHOCO VADER AUCJ": {
        'uttd': "AUCJ",
        'title': "Uchuu Daisakusen Choco Vader - Uchuu Kara no Shinryakusha",
    },
    "CHOHMAKAI R ACJJ": {
        'uttd': "ACJJ",
        'title': "Chou Makaimura R",
    },
    "CHUCHU ROCKEACRP": {
        'uttd': "ACRP",
        'title': "Chu Chu Rocket!",
    },
    "CHUCHUROCKETACRE": {
        'uttd': "ACRE",
        'title': "Chu Chu Rocket!",
    },
    "CHUCHUROCKETACRJ": {
        'uttd': "ACRJ",
        'title': "Chu Chu Rocket!",
    },
    "CIMATHEENEMYBCME": {
        'uttd': "BCME",
        'title': "CIMA - The Enemy",
    },
    "CINDBCDE    BCDE": {
        'uttd': "BCDE",
        'title': "Cinderella - Magical Dreams",
    },
    "CINDBCDE    BCDP": {
        'uttd': "BCDP",
        'title': "Cinderella - Magical Dreams",
    },
    "CINNAMON2-YDB2SJ": {
        'uttd': "B2SJ",
        'title': "Cinnamon - Yume no Daibouken",
    },
    "CINNAMON A  BPSJ": {
        'uttd': "BPSJ",
        'title': "Cinnamoroll Kokoniiruyo",
    },
    "CINNAMOROLL3B43J": {
        'uttd': "B43J",
        'title': "Cinnamon - Fuwafuwa Daisakusen",
    },
    "CLITTLEE    BCHE": {
        'uttd': "BCHE",
        'title': "Chicken Little",
    },
    "CLITTLEJ    BCHJ": {
        'uttd': "BCHJ",
        'title': "Chicken Little",
    },
    "CLU CLU LANDFCLJ": {
        'uttd': "FCLJ",
        'title': "Famicom Mini Vol. 12 - Clu Clu Land",
    },
    "CNBLOCKPARTYAC9E": {
        'uttd': "AC9E",
        'title': "Cartoon Network - Block Party",
    },
    "CNDOUBLEGAMEBW2E": {
        'uttd': "BW2E",
        'title': "2 Games in 1 - Cartoon Network - Block Party + Cartoon Network - Speedway",
    },
    "CN SPEED&BLKBW2P": {
        'uttd': "BW2P",
        'title': "2 Games in 1 - Cartoon Network - Block Party + Cartoon Network - Speedway",
    },
    "CN SPEEDWAY ANRE": {
        'uttd': "ANRE",
        'title': "Cartoon Network - Speedway",
    },
    "COCOTO KART BC5P": {
        'uttd': "BC5P",
        'title': "Cocoto Kart Racer",
    },
    "COLORIS     BVAJ": {
        'uttd': "BVAJ",
        'title': "bit Generations - Coloris",
    },
    "COLUMNS CROWACGP": {
        'uttd': "ACGP",
        'title': "Columns Crown",
    },
    "COLUMNSCROWNACGE": {
        'uttd': "ACGE",
        'title': "Columns Crown",
    },
    "COLUMNSCROWNACGJ": {
        'uttd': "ACGJ",
        'title': "Columns Crown",
    },
    "COMBATCQ    AQCJ": {
        'uttd': "AQCJ",
        'title': "Combat Choro Q - Advance Daisakusen",
    },
    "COMIX ZONE  ACZP": {
        'uttd': "ACZP",
        'title': "Comix Zone",
    },
    "COMPILATION1BCSP": {
        'uttd': "BCSP",
        'title': "2 Games in 1 - V-Rally 3 + Stuntman",
    },
    "COMPILATION2B2AP": {
        'uttd': "B2AP",
        'title': "2 Games in 1 - Asterix & Obelix - Bash Them All! + Asterix & Obelix XXL",
    },
    "CONNECT4COMPB65E": {
        'uttd': "B65E",
        'title': "Connect Four - Perfection - Trouble",
    },
    "CONTRAADVANCAAWE": {
        'uttd': "AAWE",
        'title': "Contra Advance - The Alien Wars EX",
    },
    "CONTRAADVANCAAWJ": {
        'uttd': "AAWJ",
        'title': "Contra Hard Spirits",
    },
    "CONTRAADVANCAAWP": {
        'uttd': "AAWP",
        'title': "Contra Advance - The Alien Wars EX",
    },
    "COOKIE PIE  ABGJ": {
        'uttd': "ABGJ",
        'title': "Sweet Cookie Pie",
    },
    "CORVETTE    AVCE": {
        'uttd': "AVCE",
        'title': "Corvette",
    },
    "CQADVANCE2  AQ2J": {
        'uttd': "AQ2J",
        'title': "Choro Q Advance 2",
    },
    "CQADVANCE   AQAJ": {
        'uttd': "AQAJ",
        'title': "Choro Q Advance",
    },
    "CRAFTSWORD2 BSKJ": {
        'uttd': "BSKJ",
        'title': "Summon Night - Craft Sword Monogatari 2",
    },
    "CRAFTSWORD HB3CJ": {
        'uttd': "B3CJ",
        'title': "Summon Night - Craft Sword Monogatari Hajimari no Ishi",
    },
    "CRASH2      AC8E": {
        'uttd': "AC8E",
        'title': "Crash Bandicoot 2 - N-Tranced",
        'icon0': 'https://images.launchbox-app.com/5ab5e584-1aa4-4de5-a28c-625247156590.jpg',
        'pic1': 'https://images.launchbox-app.com/bf3c3253-21ca-41b1-858f-6cfc0faea960.jpg',
        'snd0': 'https://www.youtube.com/watch?v=Sqr8lq79jsU&list=PL4sZJNxKabvlY-Fp3ozv7S290bbvvLNQD&index=1',
    },
    "CRASH2      AC8J": {
        'uttd': "AC8J",
        'title': "Crash Bandicoot Advance 2 - Gurugurusaimin Dai Panic!",
    },
    "CRASH2      AC8P": {
        'uttd': "AC8P",
        'title': "Crash Bandicoot 2 - N-Tranced",
    },
    "CRASH       ACQE": {
        'uttd': "ACQE",
        'title': "Crash Bandicoot - The Huge Adventure",
    },
    "CRASH       ACQP": {
        'uttd': "ACQP",
        'title': "Crash Bandicoot XS",
    },
    "CRASH       ACUJ": {
        'uttd': "ACUJ",
        'title': "Crash Bandicoot Advance",
    },
    "CRASH PURPLEBD4E": {
        'uttd': "BD4E",
        'title': "Crash Bandicoot Purple - Ripto's Rampage",
    },
    "CRASH PURPLEBD4P": {
        'uttd': "BD4P",
        'title': "Crash Bandicoot Fusion",
    },
    "CRASH PURPLEBKDJ": {
        'uttd': "BKDJ",
        'title': "Crash Bandicoot Advance - Wakuwaku Tomodachi Daisakusen!",
    },
    "CRASH S PACKB8AE": {
        'uttd': "B8AE",
        'title': "2 Games in 1 - Crash Bandicoot 2 - N-Tranced + Crash Nitro Kart",
    },
    "CRASH & SPYRB53P": {
        'uttd': "B53P",
        'title': "2 Games in 1 - Spyro Fusion + Crash Bandicoot Fusion",
    },
    "CRA&SPYSPACKB53E": {
        'uttd': "B53E",
        'title': "2 Games in 1 - Spyro Orange - The Cortex Conspiracy + Crash Bandicoot Purple - Ripto's Rampage",
    },
    "CRAZY CHASE ACCE": {
        'uttd': "ACCE",
        'title': "Crazy Chase",
    },
    "CRAZY CHASE ACCP": {
        'uttd': "ACCP",
        'title': "Crazy Chase",
    },
    "CRAZY FROG KBCRP": {
        'uttd': "BCRP",
        'title': "Crazy Frog Racer",
    },
    "CRAZY TAXI CA3CE": {
        'uttd': "A3CE",
        'title': "Crazy Taxi - Catch a Ride",
    },
    "CRAZY TAXI CA3CP": {
        'uttd': "A3CP",
        'title': "Crazy Taxi - Catch a Ride",
    },
    "CREATURESAGBACTX": {
        'uttd': "ACTX",
        'title': "Creatures",
    },
    "CREATURESAGBACTY": {
        'uttd': "ACTY",
        'title': "Creatures",
    },
    "CROKET!2    BK2J": {
        'uttd': "BK2J",
        'title': "Croket! 2 - Yami no Bank to Banqueen",
    },
    "CROKET!3    B3KJ": {
        'uttd': "B3KJ",
        'title': "Croket! 3 - Guranyuu Oukoku no Nazo",
    },
    "CROKET!4    BK4J": {
        'uttd': "BK4J",
        'title': "Croket! 4 - Bank no Mori no Mamorigami",
    },
    "CROKET!5    BK5J": {
        'uttd': "BK5J",
        'title': "Korokke Great - Toki no Boukensha",
    },
    "CROKET!     A6CJ": {
        'uttd': "A6CJ",
        'title': "Croket! - Yume no Banker Survival!",
    },
    "CROUCHING TIAQDE": {
        'uttd': "AQDE",
        'title': "Crouching Tiger, Hidden Dragon",
    },
    "CROUCHING TIAQDP": {
        'uttd': "AQDP",
        'title': "Crouching Tiger, Hidden Dragon",
    },
    "CRUISN VELOCACFE": {
        'uttd': "ACFE",
        'title': "Cruis'n Velocity",
    },
    "CRUSHED BASEBCBE": {
        'uttd': "BCBE",
        'title': "Crushed Baseball",
    },
    "CT SPECIAL FA9CE": {
        'uttd': "A9CE",
        'title': "CT Special Forces 2 - Back in the Trenches",
    },
    "CT SPECIAL FA9CP": {
        'uttd': "A9CP",
        'title': "CT Special Forces - Back to Hell",
    },
    "CT SPECIAL FAC7E": {
        'uttd': "AC7E",
        'title': "CT Special Forces",
    },
    "CT SPECIAL FAC7P": {
        'uttd': "AC7P",
        'title': "CT Special Forces",
    },
    "CT SPECIAL FBC3P": {
        'uttd': "BC3P",
        'title': "CT Special Forces 3 - Bioterror",
    },
    "CUBIX_GBA   ACXE": {
        'uttd': "ACXE",
        'title': "Cubix - Robots for Everyone - Clash 'N Bash",
    },
    "CURIOUS GEORB3JP": {
        'uttd': "B3JP",
        'title': "Curious George",
    },
    "CV 2 PACK   BXKE": {
        'uttd': "BXKE",
        'title': "2 Games in 1 - Castlevania - Harmony of Dissonance + Castlevania - Aria of Sorrow",
    },
    "CV 2 PACK   BXKP": {
        'uttd': "BXKP",
        'title': "2 Games in 1 - Castlevania - Harmony of Dissonance + Castlevania - Aria of Sorrow",
    },
    "DAI-MA-JANG AHMJ": {
        'uttd': "AHMJ",
        'title': "Dai-Mahjong",
    },
    "DAISENRYAKU ADSJ": {
        'uttd': "ADSJ",
        'title': "Daisenryaku",
    },
    "DANCE BEAT  ABYE": {
        'uttd': "ABYE",
        'title': "Britney's Dance Beat",
    },
    "DANCE BEAT  ABYP": {
        'uttd': "ABYP",
        'title': "Britney's Dance Beat",
    },
    "DANCE BEAT  ABYX": {
        'uttd': "ABYX",
        'title': "Britney's Dance Beat",
    },
    "DANCE BEAT  ABYY": {
        'uttd': "ABYY",
        'title': "Britney's Dance Beat",
    },
    "DANCINGSWORDA9SJ": {
        'uttd': "A9SJ",
        'title': "Dancing Sword - Senkou",
    },
    "DAN DOH!! TOBDNJ": {
        'uttd': "BDNJ",
        'title': "Dan Doh!! - Tobase Shouri no Smile Shot!!",
    },
    "DANDOHXI    AXHJ": {
        'uttd': "AXHJ",
        'title': "Dan Doh!! Xi",
    },
    "DANGEROUS-G2BZ2J": {
        'uttd': "BZ2J",
        'title': "Zettaizetsumei Dangerous Jiisan - Tsuu Ikari no Oshioki Blues",
    },
    "DANGEROUS-G3BJ3J": {
        'uttd': "BJ3J",
        'title': "Zettaizetsumei Dangerous Jiisan 3 - Hateshinaki Mamonogatari",
    },
    "DANGEROUS-G BZDJ": {
        'uttd': "BZDJ",
        'title': "Zettaizetsumei Dangerous Jiisan - Shijou Saikyou no Dogeza",
    },
    "DANNYPHANTOMBQYD": {
        'uttd': "BQYD",
        'title': "Danny Phantom - Dschungelstadt",
    },
    "DANNYPHANTOMBQYE": {
        'uttd': "BQYE",
        'title': "Danny Phantom - Urban Jungle",
    },
    "DANNYPHANTOMBUEE": {
        'uttd': "BUEE",
        'title': "Danny Phantom - The Ultimate Enemy",
    },
    "DANNYPHANTOMBUEP": {
        'uttd': "BUEP",
        'title': "Danny Phantom - The Ultimate Enemy",
    },
    "DANNYPHANTOMBUEX": {
        'uttd': "BUEX",
        'title': "Danny Phantom - The Ultimate Enemy",
    },
    "DAREDEVIL   AVLD": {
        'uttd': "AVLD",
        'title': "Daredevil",
    },
    "DAREDEVIL   AVLE": {
        'uttd': "AVLE",
        'title': "Daredevil",
    },
    "DAREDEVIL   AVLX": {
        'uttd': "AVLX",
        'title': "Daredevil",
    },
    "DARIUS R    A2DJ": {
        'uttd': "A2DJ",
        'title': "Darius R",
    },
    "DARK ARENA  ADAE": {
        'uttd': "ADAE",
        'title': "Dark Arena",
    },
    "DAVE MIRRA 3AB3E": {
        'uttd': "AB3E",
        'title': "Dave Mirra Freestyle BMX 3",
    },
    "DAVE MIRRA FAX2E": {
        'uttd': "AX2E",
        'title': "Dave Mirra Freestyle BMX 2",
    },
    "DAVE MIRRA FAX2P": {
        'uttd': "AX2P",
        'title': "Dave Mirra Freestyle BMX 2",
    },
    "DAVID BECKHAABQE": {
        'uttd': "ABQE",
        'title': "David Beckham Soccer",
    },
    "DAVIDBECKHAMABQP": {
        'uttd': "ABQP",
        'title': "David Beckham Soccer",
    },
    "DAVIS CUP   AD6E": {
        'uttd': "AD6E",
        'title': "Davis Cup",
    },
    "DAVIS CUP   AD6P": {
        'uttd': "AD6P",
        'title': "Davis Cup",
    },
    "DBGTTRANSFORBT4E": {
        'uttd': "BT4E",
        'title': "Dragon Ball GT - Transformation",
    },
    "DBZBUUSFURY BG3E": {
        'uttd': "BG3E",
        'title': "Dragon Ball Z - Buu's Fury",
    },
    "DBZCARDGAME1ADZE": {
        'uttd': "ADZE",
        'title': "Dragon Ball Z - Collectible Card Game",
    },
    "DBZLEGACY1&2BLFE": {
        'uttd': "BLFE",
        'title': "2 Games in 1 - Dragon Ball Z I & II",
    },
    "DBZLGCYGOKU2ALFE": {
        'uttd': "ALFE",
        'title': "Dragon Ball Z - The Legacy of Goku II",
    },
    "DBZLGCYGOKU2ALFJ": {
        'uttd': "ALFJ",
        'title': "Dragon Ball Z - The Legacy of Goku II International",
    },
    "DBZ LGCYGOKUALGE": {
        'uttd': "ALGE",
        'title': "Dragon Ball Z - The Legacy of Goku",
    },
    "DBZ TAIKETSUBDBE": {
        'uttd': "BDBE",
        'title': "Dragon Ball Z - Taiketsu",
    },
    "DC2         BDKJ": {
        'uttd': "BDKJ",
        'title': "Digi Communication 2 - Datou! Black Gemagema Dan",
    },
    "DDEOTB      AD4E": {
        'uttd': "AD4E",
        'title': "Dungeons & Dragons - Eye of the Beholder",
    },
    "DDS_1       AAUJ": {
        'uttd': "AAUJ",
        'title': "Shin Megami Tensei",
    },
    "DDS_2       A5TJ": {
        'uttd': "A5TJ",
        'title': "Shin Megami Tensei II",
    },
    "DEADLYSKIES AAKP": {
        'uttd': "AAKP",
        'title': "Deadly Skies",
    },
    "DEADTORIGHTSBDEE": {
        'uttd': "BDEE",
        'title': "Dead to Rights",
    },
    "DEADTORIGHTSBDEP": {
        'uttd': "BDEP",
        'title': "Dead to Rights",
    },
    "DEBITIRUFLAMBDHJ": {
        'uttd': "BDHJ",
        'title': "Shin Megami Tensei Devil Children - Honoo no Sho",
    },
    "DEBITIRUHIKAAL4E": {
        'uttd': "AL4E",
        'title': "DemiKids - Light Version",
    },
    "DEBITIRUHIKAAL4J": {
        'uttd': "AL4J",
        'title': "Shin Megami Tensei Devil Children - Hikari no Sho",
    },
    "DEBITIRUICE BDYJ": {
        'uttd': "BDYJ",
        'title': "Shin Megami Tensei Devil Children - Koori no Sho",
    },
    "DEBITIRUPUZLA8ZJ": {
        'uttd': "A8ZJ",
        'title': "Shin Megami Tensei Devil Children - Puzzle de Call!",
    },
    "DEBITIRUYAMIAC5E": {
        'uttd': "AC5E",
        'title': "DemiKids - Dark Version",
    },
    "DEBITIRUYAMIAC5J": {
        'uttd': "AC5J",
        'title': "Shin Megami Tensei Devil Children - Yami no Sho",
    },
    "DEFENDER    A2FE": {
        'uttd': "A2FE",
        'title': "Defender",
    },
    "DEFENDER    A2FP": {
        'uttd': "A2FP",
        'title': "Defender",
    },
    "DEMON DRIVERA9AE": {
        'uttd': "A9AE",
        'title': "Demon Driver - Time to Burn Rubber!",
    },
    "DEMON DRIVERA9AP": {
        'uttd': "A9AP",
        'title': "Demon Driver - Time to Burn Rubber!",
    },
    "DENDOHMAJANGASMJ": {
        'uttd': "ASMJ",
        'title': "Saibara Rieko no Dendou Mahjong",
    },
    "DENKIBLOCKS!ADBE": {
        'uttd': "ADBE",
        'title': "Denki Blocks!",
    },
    "DENKIBLOCKS!ADBJ": {
        'uttd': "ADBJ",
        'title': "Denki Blocks!",
    },
    "DENKIBLOCKS!ADBP": {
        'uttd': "ADBP",
        'title': "Denki Blocks!",
    },
    "DEPATIKA    ADYJ": {
        'uttd': "ADYJ",
        'title': "Hanafuda Trump Mahjong - Depachika Wayouchuu",
    },
    "DESERTSTRIKEADIE": {
        'uttd': "ADIE",
        'title': "Desert Strike Advance",
    },
    "DETECTIVE C2BQAJ": {
        'uttd': "BQAJ",
        'title': "Meitantei Conan - Atasuki no Monument",
    },
    "DETECTIVE COAC4J": {
        'uttd': "AC4J",
        'title': "Meitantei Conan - Nerawareta Tantei",
    },
    "DEXTER CHESSADXE": {
        'uttd': "ADXE",
        'title': "Dexter's Laboratory - Chess Challenge",
    },
    "DEXTER CHESSADXP": {
        'uttd': "ADXP",
        'title': "Dexter's Laboratory - Chess Challenge",
    },
    "DIADROIDSWLDADDJ": {
        'uttd': "ADDJ",
        'title': "Diadroids World - Evil Teikoku no Yabou",
    },
    "DIALHEX     BVBJ": {
        'uttd': "BVBJ",
        'title': "bit Generations - Dial Hex",
    },
    "DIEMONSTERAGAMXD": {
        'uttd': "AMXD",
        'title': "Monster AG, Die",
    },
    "DIG DUG     FDDJ": {
        'uttd': "FDDJ",
        'title': "Famicom Mini Vol. 16 - Dig Dug",
    },
    "DIGICOM     A3OJ": {
        'uttd': "A3OJ",
        'title': "Di Gi Charat - DigiCommunication",
    },
    "DIGIDRIVE   BVHJ": {
        'uttd': "BVHJ",
        'title': "bit Generations - Digidrive",
    },
    "DIGIMON BATTA8SP": {
        'uttd': "A8SP",
        'title': "Digimon - Battle Spirit",
    },
    "DIGIMON BATTBDSP": {
        'uttd': "BDSP",
        'title': "Digimon - Battle Spirit 2",
    },
    "DIGIMON BS2 BDSE": {
        'uttd': "BDSE",
        'title': "Digimon - Battle Spirit 2",
    },
    "DIGIMON BTSPA8SE": {
        'uttd': "A8SE",
        'title': "Digimon - Battle Spirit",
    },
    "DIGIMONRACINBDGE": {
        'uttd': "BDGE",
        'title': "Digimon Racing",
    },
    "DIGIMONRACINBDGP": {
        'uttd': "BDGP",
        'title': "Digimon Racing",
    },
    "DIGIMONRACINBDJJ": {
        'uttd': "BDJJ",
        'title': "Digimon Racing",
    },
    "DINO2 DRAGONA4XJ": {
        'uttd': "A4XJ",
        'title': "Gachasute! Dino Device 2 - Dragon",
    },
    "DINO2 PHOENIA4WJ": {
        'uttd': "A4WJ",
        'title': "Gachasute! Dino Device 2 - Phoenix",
    },
    "DINODEVICE BABIJ": {
        'uttd': "ABIJ",
        'title': "Gachasute! Dino Device - Blue",
    },
    "DINODEVICE RAAIJ": {
        'uttd': "AAIJ",
        'title': "Gachasute! Dino Device - Red",
    },
    "DINOTOPIA   AD3E": {
        'uttd': "AD3E",
        'title': "Dinotopia - The Timestone Pirates",
    },
    "DISNEY FB SBBFBP": {
        'uttd': "BFBP",
        'title': "2 Games in 1 - Disney Sports - Football + Disney Sports - Skateboarding",
    },
    "DISNEY HOTR BHME": {
        'uttd': "BHME",
        'title': "Home on the Range",
    },
    "DISNEY HOTR BHMP": {
        'uttd': "BHMP",
        'title': "Home on the Range",
    },
    "DISNEY PARTYBD8E": {
        'uttd': "BD8E",
        'title': "Disney's Party",
    },
    "DISNEY PRINCAQDS": {
        'uttd': "AQDS",
        'title': "Disney Princesas",
    },
    "DISNEY PRINCAQPD": {
        'uttd': "AQPD",
        'title': "Disneys Prinzessinnen",
    },
    "DISNEY PRINCAQPE": {
        'uttd': "AQPE",
        'title': "Disney Princess",
    },
    "DISNEY PRINCAQPF": {
        'uttd': "AQPF",
        'title': "Disney Princesse",
    },
    "DISNEY PRINCAQPI": {
        'uttd': "AQPI",
        'title': "Disney Principesse",
    },
    "DISNEY'S DONAADJ": {
        'uttd': "AADJ",
        'title': "Donald Duck Advance",
    },
    "DISNEY'S DONADKE": {
        'uttd': "ADKE",
        'title': "Donald Duck Advance",
    },
    "DISNEYSEA   ADEJ": {
        'uttd': "ADEJ",
        'title': "Adventure of Tokyo Disney Sea",
    },
    "DISNEY SKATEBESE": {
        'uttd': "BESE",
        'title': "Extreme Skate Adventure",
    },
    "DISNEY SKATEBESX": {
        'uttd': "BESX",
        'title': "Extreme Skate Adventure",
    },
    "DISNEY'S LILBLSP": {
        'uttd': "BLSP",
        'title': "Lilo & Stitch 2",
    },
    "DISNEY'S TARAJGD": {
        'uttd': "AJGD",
        'title': "Tarzan - Ruckkehr in den Dschungel",
    },
    "DISNEY TARZAAJGF": {
        'uttd': "AJGF",
        'title': "Tarzan - L'Appel de la Jungle",
    },
    "DISNEYVOL001MDCE": {
        'uttd': "MDCE",
        'title': "Game Boy Advance Video - Disney Channel Collection - Volume 1",
    },
    "DIS PIX CARSBCAD": {
        'uttd': "BCAD",
        'title': "Cars",
    },
    "DIS PIX CARSBCAE": {
        'uttd': "BCAE",
        'title': "Cars",
    },
    "DIS PIX CARSBCAI": {
        'uttd': "BCAI",
        'title': "Cars",
    },
    "DIS PIX CARSBCAX": {
        'uttd': "BCAX",
        'title': "Cars",
    },
    "DIS PIX CARSBCAY": {
        'uttd': "BCAY",
        'title': "Cars",
    },
    "DIS PIX CARSBCAZ": {
        'uttd': "BCAZ",
        'title': "Cars",
    },
    "DIS T PLANETAZQE": {
        'uttd': "AZQE",
        'title': "Treasure Planet",
    },
    "DIS T PLANETAZQP": {
        'uttd': "AZQP",
        'title': "Treasure Planet",
    },
    "DLDEESASTER ADLE": {
        'uttd': "ADLE",
        'title': "Dexter's Laboratory - Deesaster Strikes!",
    },
    "DLDEESASTER ADLP": {
        'uttd': "ADLP",
        'title': "Dexter's Laboratory - Deesaster Strikes!",
    },
    "DM KAIJUDO  BD6E": {
        'uttd': "BD6E",
        'title': "Duel Masters - Kaijudo Showdown",
    },
    "DM KAIJUDO  BD6P": {
        'uttd': "BD6P",
        'title': "Duel Masters - Kaijudo Showdown",
    },
    "DM SEMPAI   AA9E": {
        'uttd': "AA9E",
        'title': "Duel Masters - Sempai Legends",
    },
    "DM SEMPAI   AA9P": {
        'uttd': "AA9P",
        'title': "Duel Masters - Sempai Legends",
    },
    "DM SHADOW   BDUE": {
        'uttd': "BDUE",
        'title': "Duel Masters - Shadow of the Code",
    },
    "DM SHADOW   BDUP": {
        'uttd': "BDUP",
        'title': "Duel Masters - Shadow of the Code",
    },
    "DOCTORSUDOKUBUOE": {
        'uttd': "BUOE",
        'title': "Dr. Sudoku",
    },
    "DODGEBALL   BG8J": {
        'uttd': "BG8J",
        'title': "Ganbare Dodge Fighters",
    },
    "DODGEBALL F ADFJ": {
        'uttd': "ADFJ",
        'title': "Bakunetsu Dodge Ball Fighters",
    },
    "DOGWONDERFULB82J": {
        'uttd': "B82J",
        'title': "Kawaii Koinu Wonderful",
    },
    "DOGZ2       BIME": {
        'uttd': "BIME",
        'title': "Dogz 2",
    },
    "DOGZ2       BIMP": {
        'uttd': "BIMP",
        'title': "Dogz 2",
    },
    "DOGZ        B82E": {
        'uttd': "B82E",
        'title': "Dogz",
    },
    "DOGZ        B82P": {
        'uttd': "B82P",
        'title': "Dogz",
    },
    "DOGZ        B82Y": {
        'uttd': "B82Y",
        'title': "Dogz",
    },
    "DOGZ FASHIONBFEE": {
        'uttd': "BFEE",
        'title': "Dogz - Fashion",
    },
    "DOGZ FASHIONBFEP": {
        'uttd': "BFEP",
        'title': "Dogz - Fashion",
    },
    "DOKAPON     ADQE": {
        'uttd': "ADQE",
        'title': "Dokapon",
    },
    "DOKAPON     ADQP": {
        'uttd': "ADQP",
        'title': "Dokapon",
    },
    "DOKAPON-Q   ADQJ": {
        'uttd': "ADQJ",
        'title': "Dokapon Q - Monster Hunter!",
    },
    "DOMOKUN     ADOJ": {
        'uttd': "ADOJ",
        'title': "Domo-kun no Fushigi Terebi",
    },
    "DONALD DUCK ADKP": {
        'uttd': "ADKP",
        'title': "Donald Duck Advance",
    },
    "DONKEY KONG FDKE": {
        'uttd': "FDKE",
        'title': "Classic NES Series - Donkey Kong",
    },
    "DONKEY KONG FDKJ": {
        'uttd': "FDKJ",
        'title': "Famicom Mini Vol. 02 - Donkey Kong",
    },
    "DOOM II     A9DE": {
        'uttd': "A9DE",
        'title': "Doom II",
    },
    "DOOM II     A9DP": {
        'uttd': "A9DP",
        'title': "Doom II",
    },
    "DORA DBL PAKB2EE": {
        'uttd': "B2EE",
        'title': "2 Games in 1 - Dora the Explorer - The Search for the Pirate Pig's Treasure + Dora the Explorer - Super Star Adventures!",
    },
    "DORADORAWDBKA5GJ": {
        'uttd': "A5GJ",
        'title': "Dragon Drive - World D Break",
    },
    "DORAEMON    ADRJ": {
        'uttd': "ADRJ",
        'title': "Doraemon - Midori no Wakusei Dokidoki Daikyuushutsu!",
    },
    "DORA SPR STRBDOE": {
        'uttd': "BDOE",
        'title': "Dora the Explorer - Super Star Adventures!",
    },
    "DORA SPR STRBDOP": {
        'uttd': "BDOP",
        'title': "Dora the Explorer - Super Star Adventures!",
    },
    "DORA SUPER SBERE": {
        'uttd': "BERE",
        'title': "Dora the Explorer - Super Spies",
    },
    "DORA THE EXPAERE": {
        'uttd': "AERE",
        'title': "Dora the Explorer - The Search for the Pirate Pig's Treasure",
    },
    "DORA WALKER ADPJ": {
        'uttd': "ADPJ",
        'title': "Doraemon - Dokodemo Walker",
    },
    "DORA WORLD ABXPE": {
        'uttd': "BXPE",
        'title': "Dora the Explorer - Dora's World Adventure!",
    },
    "DOREXPLOR 01MDRE": {
        'uttd': "MDRE",
        'title': "Game Boy Advance Video - Dora the Explorer - Volume 1",
    },
    "DOTC        ADHE": {
        'uttd': "ADHE",
        'title': "Defender of the Crown",
    },
    "DOTC        ADHP": {
        'uttd': "ADHP",
        'title': "Defender of the Crown",
    },
    "DOTSTREAM   BVCJ": {
        'uttd': "BVCJ",
        'title': "bit Generations - Dotstream",
    },
    "DOUBLEDRAGONBDDE": {
        'uttd': "BDDE",
        'title': "Double Dragon Advance",
    },
    "DOUBLEDRAGONBDDJ": {
        'uttd': "BDDJ",
        'title': "Double Dragon Advance",
    },
    "DOUBUTU     BWDJ": {
        'uttd': "BWDJ",
        'title': "Wan Nyan Doubutsu Byouin",
    },
    "DOWNFORCEAGBADWE": {
        'uttd': "ADWE",
        'title': "Downforce",
    },
    "DOWNTOWN    BDTJ": {
        'uttd': "BDTJ",
        'title': "Downtown - Nekketsu Monogatari EX",
    },
    "DQM-CARAVANHA9HJ": {
        'uttd': "A9HJ",
        'title': "Dragon Quest Monsters - Caravan Heart",
    },
    "DRACULA 1   FADJ": {
        'uttd': "FADJ",
        'title': "Famicom Mini Vol. 29 - Akumajou Dracule",
    },
    "DRACULA AGB1AAME": {
        'uttd': "AAME",
        'title': "Castlevania - Circle of the Moon",
    },
    "DRACULA AGB1AAMJ": {
        'uttd': "AAMJ",
        'title': "Akumajou Dracula - Circle of the Moon",
    },
    "DRACULA AGB1AAMP": {
        'uttd': "AAMP",
        'title': "Castlevania - Circle of the Moon",
    },
    "DRAGONBALL01MDBE": {
        'uttd': "MDBE",
        'title': "Game Boy Advance Video - Dragon Ball GT - Volume 1",
    },
    "DRAGONBALLAABDVE": {
        'uttd': "BDVE",
        'title': "Dragon Ball - Advanced Adventure",
    },
    "DRAGONBALLAABDVJ": {
        'uttd': "BDVJ",
        'title': "Dragon Ball - Advanced Adventure",
    },
    "DRAGONBALLAABDVK": {
        'uttd': "BDVK",
        'title': "Dragon Ball - Advanced Adventure",
    },
    "DRAGONBALLAABDVP": {
        'uttd': "BDVP",
        'title': "Dragon Ball - Advanced Adventure",
    },
    "DRAGONBALL ZALFP": {
        'uttd': "ALFP",
        'title': "Dragon Ball Z - The Legacy of Goku II",
    },
    "DRAGONBALL ZALGP": {
        'uttd': "ALGP",
        'title': "Dragon Ball Z - The Legacy of Goku",
    },
    "DRAGON BALLZBDBP": {
        'uttd': "BDBP",
        'title': "Dragon Ball Z - Taiketsu",
    },
    "DRAGONBLBKTGAZJJ": {
        'uttd': "AZJJ",
        'title': "Dragon Ball Z - Bukuu Tougeki",
    },
    "DRAGONBLSSWEAZJP": {
        'uttd': "AZJP",
        'title': "Dragon Ball Z - Supersonic Warriors",
    },
    "DRAGONBLSSWUAZJE": {
        'uttd': "AZJE",
        'title': "Dragon Ball Z - Supersonic Warriors",
    },
    "DRAGONDREAM BIPJ": {
        'uttd': "BIPJ",
        'title': "One Piece - Dragon Dream",
    },
    "DRAGONS ROCKBJDP": {
        'uttd': "BJDP",
        'title': "Dragon's Rock",
    },
    "DRAGONTALES BD9E": {
        'uttd': "BD9E",
        'title': "Dragon Tales - Dragon Adventures",
    },
    "DRAKEANDJOSHAJYE": {
        'uttd': "AJYE",
        'title': "Drake & Josh",
    },
    "DREAMSCHEME ARKE": {
        'uttd': "ARKE",
        'title': "Rocket Power - Dream Scheme",
    },
    "DRGBALLZBUKOAZJK": {
        'uttd': "AZJK",
        'title': "Dragon Ball Z - Moogongtoogeuk",
    },
    "DRILL DOZER V49E": {
        'uttd': "V49E",
        'title': "Drill Dozer",
    },
    "DRIVEN      ADVE": {
        'uttd': "ADVE",
        'title': "Driven",
    },
    "DRIVEN AGB  ADVP": {
        'uttd': "ADVP",
        'title': "Driven",
    },
    "DRIVER2ADV  ADUE": {
        'uttd': "ADUE",
        'title': "Driver 2 Advance",
    },
    "DRIVER 2 ADVADUP": {
        'uttd': "ADUP",
        'title': "Driver 2 Advance",
    },
    "DRIVER3     B3RE": {
        'uttd': "B3RE",
        'title': "Driver 3",
    },
    "DRIVER3     B3RP": {
        'uttd': "B3RP",
        'title': "Driver 3",
    },
    "DR. MARIO   FDME": {
        'uttd': "FDME",
        'title': "Classic NES Series - Dr. Mario",
    },
    "DR. MARIO   FDMJ": {
        'uttd': "FDMJ",
        'title': "Famicom Mini Vol. 15 - Dr. Mario",
    },
    "DRMARIO&PONEBZPE": {
        'uttd': "BZPE",
        'title': "Dr. Mario & Puzzle League",
    },
    "DRMARIO&PONJBZPJ": {
        'uttd': "BZPJ",
        'title': "Dr. Mario & Panel de Pon",
    },
    "DRMARIO&PONPBZPP": {
        'uttd': "BZPP",
        'title': "Dr. Mario & Puzzle League",
    },
    "DR. MUTO    A6TP": {
        'uttd': "A6TP",
        'title': "Dr. Muto",
    },
    "DROME RACERSAOEX": {
        'uttd': "AOEX",
        'title': "Drome Racers",
    },
    "DROOPYS TENNAD7P": {
        'uttd': "AD7P",
        'title': "Droopy's Tennis Open",
    },
    "DRSEUSSCITHTBCTE": {
        'uttd': "BCTE",
        'title': "The Cat in the Hat by Dr. Seuss",
    },
    "DR. SUDOKU  BUOP": {
        'uttd': "BUOP",
        'title': "Dr. Sudoku",
    },
    "DS_BASKET   A2AJ": {
        'uttd': "A2AJ",
        'title': "Disney Sports - Basketball",
    },
    "DS_BASKET_E A2AP": {
        'uttd': "A2AP",
        'title': "Disney Sports - Basketball",
    },
    "DS_BASKET_U A2AE": {
        'uttd': "A2AE",
        'title': "Disney Sports - Basketball",
    },
    "DS_FOOTBALL A3DJ": {
        'uttd': "A3DJ",
        'title': "Disney Sports - American Football",
    },
    "DS-FOOTBALLUA3DE": {
        'uttd': "A3DE",
        'title': "Disney Sports - Football",
    },
    "DS_MOTOCROSSAOME": {
        'uttd': "AOME",
        'title': "Disney Sports - Motocross",
    },
    "DS_MOTOCROSSAOMJ": {
        'uttd': "AOMJ",
        'title': "Disney Sports - Motocross",
    },
    "DS_MOTOCROSSAOMP": {
        'uttd': "AOMP",
        'title': "Disney Sports - Motocross",
    },
    "DS_SKATE    A4DJ": {
        'uttd': "A4DJ",
        'title': "Disney Sports - Skateboarding",
    },
    "DS-SKATE-E  A4DP": {
        'uttd': "A4DP",
        'title': "Disney Sports - Skateboarding",
    },
    "DS-SKATE-U  A4DE": {
        'uttd': "A4DE",
        'title': "Disney Sports - Skateboarding",
    },
    "DS_SNOWBD   A5DJ": {
        'uttd': "A5DJ",
        'title': "Disney Sports - Snowboarding",
    },
    "DS_SNOWBD_E A5DP": {
        'uttd': "A5DP",
        'title': "Disney Sports - Snowboarding",
    },
    "DS_SNOWBD_U A5DE": {
        'uttd': "A5DE",
        'title': "Disney Sports - Snowboarding",
    },
    "DS_SOCCER   A6DJ": {
        'uttd': "A6DJ",
        'title': "Disney Sports - Soccer",
    },
    "DS_SOCCER_E A6DP": {
        'uttd': "A6DP",
        'title': "Disney Sports - Football",
    },
    "DS_SOCCER_U A6DE": {
        'uttd': "A6DE",
        'title': "Disney Sports - Soccer",
    },
    "DUAL BLADES AB9E": {
        'uttd': "AB9E",
        'title': "Dual Blades",
    },
    "DUAL BLADES AB9J": {
        'uttd': "AB9J",
        'title': "Dual Blades",
    },
    "DUELMASTER25BD5J": {
        'uttd': "BD5J",
        'title': "Duel Masters 2 - Kirifuda Shoubu Version",
    },
    "DUELMASTERS2BD2J": {
        'uttd': "BD2J",
        'title': "Duel Masters 2 - Invisible Advance",
    },
    "DUELMASTERS3BDUJ": {
        'uttd': "BDUJ",
        'title': "Duel Masters 3",
    },
    "DUEL MASTERSAA9J": {
        'uttd': "AA9J",
        'title': "Duel Masters",
    },
    "DUKE NUKEM AAD9E": {
        'uttd': "AD9E",
        'title': "Duke Nukem Advance",
    },
    "DUKENUKEMUS AD9P": {
        'uttd': "AD9P",
        'title': "Duke Nukem Advance",
    },
    "DUNGEONS ANDAD4P": {
        'uttd': "AD4P",
        'title': "Dungeons & Dragons - Eye of the Beholder",
    },
    "DYNAMIC     AVDJ": {
        'uttd': "AVDJ",
        'title': "Legend of Dynamic Goushouden - Houkai no Rondo",
    },
    "DYN WARS ADVB36E": {
        'uttd': "B36E",
        'title': "Dynasty Warriors Advance",
    },
    "DYN WARS ADVB36P": {
        'uttd': "B36P",
        'title': "Dynasty Warriors Advance",
    },
    "EARTHWORM J2AJ4E": {
        'uttd': "AJ4E",
        'title': "Earthworm Jim 2",
    },
    "EARTHWORM JIAJ4P": {
        'uttd': "AJ4P",
        'title': "Earthworm Jim 2",
    },
    "EC2PICHIMO  BECJ": {
        'uttd': "BECJ",
        'title': "Angel Collection 2 - Pichimo ni Narou",
    },
    "ECKS VSE SEVAESE": {
        'uttd': "AESE",
        'title': "Ecks vs. Sever",
    },
    "ECKS VSE SEVAESP": {
        'uttd': "AESP",
        'title': "Ecks vs. Sever",
    },
    "ECKS VS SEV2AEEP": {
        'uttd': "AEEP",
        'title': "Ecks vs. Sever II - Ballistic",
    },
    "ED EDD EDDY AE3E": {
        'uttd': "AE3E",
        'title': "Ed, Edd n Eddy - Jawbreakers!",
    },
    "ED EDD EDDY AE3P": {
        'uttd': "AE3P",
        'title': "Ed, Edd n Eddy - Jawbreakers!",
    },
    "EEE2        BEDE": {
        'uttd': "BEDE",
        'title': "Ed, Edd n Eddy - The Mis-EDventures",
    },
    "EEE2        BEDP": {
        'uttd': "BEDP",
        'title': "Ed, Edd n Eddy - The Mis-EDventures",
    },
    "EGGOMANIA   AEME": {
        'uttd': "AEME",
        'title': "Egg Mania",
    },
    "EGGOMANIA   AEMJ": {
        'uttd': "AEMJ",
        'title': "Egg Mania",
    },
    "EGGOMANIA   AEMP": {
        'uttd': "AEMP",
        'title': "Eggo Mania",
    },
    "EIKETSUDEN  B3EJ": {
        'uttd': "B3EJ",
        'title': "Sangokushi - Eiketsuden",
    },
    "ELEMIX!     AEKJ": {
        'uttd': "AEKJ",
        'title': "Elemix!",
    },
    "ELEVATORACT ANWJ": {
        'uttd': "ANWJ",
        'title': "Elevator Action - Old & New",
    },
    "ELF         BELE": {
        'uttd': "BELE",
        'title': "Elf - The Movie",
    },
    "ELF         BELP": {
        'uttd': "BELP",
        'title': "Elf - The Movie",
    },
    "ELFBOWL     BEBE": {
        'uttd': "BEBE",
        'title': "Elf Bowling 1 & 2",
    },
    "ERAGON      BENE": {
        'uttd': "BENE",
        'title': "Eragon",
    },
    "ERAGON      BENP": {
        'uttd': "BENP",
        'title': "Eragon",
    },
    "EREMENTAR G BEJJ": {
        'uttd': "BEJJ",
        'title': "Erementar Gerad",
    },
    "ESL_SOCCER  AELP": {
        'uttd': "AELP",
        'title': "European Super League",
    },
    "ESPN FISHNG1AMGE": {
        'uttd': "AMGE",
        'title': "ESPN Great Outdoor Games - Bass 2002",
    },
    "ESPN FISHNG2AMGP": {
        'uttd': "AMGP",
        'title': "ESPN Great Outdoor Games - Bass Tournament",
    },
    "ESPN FISHNG3AMGJ": {
        'uttd': "AMGJ",
        'title': "Exciting Bass",
    },
    "ESPN GOLF   AGRE": {
        'uttd': "AGRE",
        'title': "ESPN Final Round Golf 2002",
    },
    "ESPN GOLF   AGRP": {
        'uttd': "AGRP",
        'title': "ESPN Final Round Golf",
    },
    "ESPN XG SK8BAXSE": {
        'uttd': "AXSE",
        'title': "ESPN X-Games Skateboarding",
    },
    "ESPN XG SK8BAXSJ": {
        'uttd': "AXSJ",
        'title': "ESPN X-Games Skateboarding",
    },
    "ESPN XG SK8BAXSP": {
        'uttd': "AXSP",
        'title': "ESPN X-Games Skateboarding",
    },
    "ESPN XG SNOWAWXE": {
        'uttd': "AWXE",
        'title': "ESPN Winter X-Games Snowboarding 2002",
    },
    "ESPN XG SNOWAWXJ": {
        'uttd': "AWXJ",
        'title': "ESPN Winter X-Games Snowboarding 2002",
    },
    "ESPN XG SNOWAWXP": {
        'uttd': "AWXP",
        'title': "ESPN Winter X-Games Snowboarding 2",
    },
    "ETTHEEXTRAT AETE": {
        'uttd': "AETE",
        'title': "E.T. - The Extra-Terrestrial",
    },
    "ETTHEEXTRAT AETP": {
        'uttd': "AETP",
        'title': "E.T. - The Extra-Terrestrial",
    },
    "EVERGIRL    BEVE": {
        'uttd': "BEVE",
        'title': "Ever Girl",
    },
    "EVILMIRROR  AHJE": {
        'uttd': "AHJE",
        'title': "Hugo - The Evil Mirror Advance",
    },
    "EVILMIRROR  AHJP": {
        'uttd': "AHJP",
        'title': "Hugo - The Evil Mirror Advance",
    },
    "EWJ         AEJE": {
        'uttd': "AEJE",
        'title': "Earthworm Jim",
    },
    "EXCITEBIKE  FEBE": {
        'uttd': "FEBE",
        'title': "Classic NES Series - Excitebike",
    },
    "EXCITEBIKE  FEBJ": {
        'uttd': "FEBJ",
        'title': "Famicom Mini Vol. 04 - Excitebike",
    },
    "EX MONOPOLY AMOJ": {
        'uttd': "AMOJ",
        'title': "EX Monopoly",
    },
    "EXTREME GHOSAEGE": {
        'uttd': "AEGE",
        'title': "Extreme Ghostbusters - Code Ecto-1",
    },
    "EXTREME GHOSAEGP": {
        'uttd': "AEGP",
        'title': "Extreme Ghostbusters - Code Ecto-1",
    },
    "EYESHIELDGBABE4J": {
        'uttd': "BE4J",
        'title': "Eyeshield 21 - Devilbats Devildays",
    },
    "EZ-TALK     A22J": {
        'uttd': "A22J",
        'title': "EZ-Talk - Shokyuu Hen 1",
    },
    "EZ-TALK     A23J": {
        'uttd': "A23J",
        'title': "EZ-Talk - Shokyuu Hen 2",
    },
    "EZ-TALK     A24J": {
        'uttd': "A24J",
        'title': "EZ-Talk - Shokyuu Hen 3",
    },
    "EZ-TALK     A25J": {
        'uttd': "A25J",
        'title': "EZ-Talk - Shokyuu Hen 4",
    },
    "EZ-TALK     A26J": {
        'uttd': "A26J",
        'title': "EZ-Talk - Shokyuu Hen 5",
    },
    "EZ-TALK     A27J": {
        'uttd': "A27J",
        'title': "EZ-Talk - Shokyuu Hen 6",
    },
    "F1 2002     AF8E": {
        'uttd': "AF8E",
        'title': "F1 2002",
    },
    "F1 2002     AF8X": {
        'uttd': "AF8X",
        'title': "F1 2002",
    },
    "F14-TOMCAT  AFTE": {
        'uttd': "AFTE",
        'title': "F-14 Tomcat",
    },
    "F-18 HORNET BF8E": {
        'uttd': "BF8E",
        'title': "Super Hornet - FA 18F",
    },
    "F24 STEALTH BYAE": {
        'uttd': "BYAE",
        'title': "F24 Stealth Fighter",
    },
    "F4 FLAME ON BH4E": {
        'uttd': "BH4E",
        'title': "Fantastic 4 - Flame On",
    },
    "F4 FLAME ON BH4P": {
        'uttd': "BH4P",
        'title': "Fantastic 4 - Flame On",
    },
    "FAIRLYODD 01MFOE": {
        'uttd': "MFOE",
        'title': "Game Boy Advance Video - Fairly Odd Parents!, The - Volume 1",
    },
    "FAIRLYODD 02MF2E": {
        'uttd': "MF2E",
        'title': "Game Boy Advance Video - Fairly Odd Parents!, The - Volume 2",
    },
    "FAIRLYODDAGBAF6E": {
        'uttd': "AF6E",
        'title': "Fairly Odd Parents!, The - Breakin' da Rules",
    },
    "FAIRLYODDAGBBF2D": {
        'uttd': "BF2D",
        'title': "Cosmo & Wanda - Wenn Elfen Helfen! - Das Schatten-Duell",
    },
    "FAIRLYODDAGBBF2E": {
        'uttd': "BF2E",
        'title': "Fairly Odd Parents!, The - Shadow Showdown",
    },
    "FAIRLYODDAGBBF2P": {
        'uttd': "BF2P",
        'title': "Fairly Odd Parents!, The - Shadow Showdown",
    },
    "FAIRLYODDPARAFVE": {
        'uttd': "AFVE",
        'title': "Fairly Odd Parents!, The - Enter the Cleft",
    },
    "FAMILY FEUD B2FE": {
        'uttd': "B2FE",
        'title': "Family Feud",
    },
    "FAMISTA     AN7J": {
        'uttd': "AN7J",
        'title': "Famista Advance",
    },
    "FANCYPOCKET AJEJ": {
        'uttd': "AJEJ",
        'title': "Fancy Pocket",
    },
    "FANTASTIC4  BF4E": {
        'uttd': "BF4E",
        'title': "Fantastic 4",
    },
    "FANTASTIC4  BF4I": {
        'uttd': "BF4I",
        'title': "I Fantastici 4",
    },
    "FANTASTIC4  BF4P": {
        'uttd': "BF4P",
        'title': "Fantastic 4",
    },
    "FANTASTIC4  BF4X": {
        'uttd': "BF4X",
        'title': "Fantastic 4",
    },
    "FANTCHILDRENBFCJ": {
        'uttd': "BFCJ",
        'title': "Fantastic Children",
    },
    "FASHION     AFNJ": {
        'uttd': "AFNJ",
        'title': "Angel Collection - Mezase! Gakuen no Fashion Leader",
    },
    "FEARFACTORULBFUE": {
        'uttd': "BFUE",
        'title': "Fear Factor - Unleashed",
    },
    "FF1&2ADVANCEBFFJ": {
        'uttd': "BFFJ",
        'title': "Final Fantasy I & II Advance",
    },
    "FF1&2DAWNOFSBFFE": {
        'uttd': "BFFE",
        'title': "Final Fantasy I & II - Dawn of Souls",
    },
    "FF1&2DAWNOFSBFFP": {
        'uttd': "BFFP",
        'title': "Final Fantasy I & II - Dawn of Souls",
    },
    "FF4ADVANCE  BZ4E": {
        'uttd': "BZ4E",
        'title': "Final Fantasy IV Advance",
    },
    "FF4ADVANCE  BZ4J": {
        'uttd': "BZ4J",
        'title': "Final Fantasy IV Advance",
    },
    "FF4ADVANCE  BZ4P": {
        'uttd': "BZ4P",
        'title': "Final Fantasy IV Advance",
    },
    "FF5ADVANCE  BZ5E": {
        'uttd': "BZ5E",
        'title': "Final Fantasy V Advance",
    },
    "FF5ADVANCE  BZ5J": {
        'uttd': "BZ5J",
        'title': "Final Fantasy V Advance",
    },
    "FF5ADVANCE  BZ5P": {
        'uttd': "BZ5P",
        'title': "Final Fantasy V Advance",
    },
    "FF6ADVANCE  BZ6E": {
        'uttd': "BZ6E",
        'title': "Final Fantasy VI Advance",
    },
    "FF6ADVANCE  BZ6J": {
        'uttd': "BZ6J",
        'title': "Final Fantasy VI Advance",
    },
    "FFT_ADVANCE AFXJ": {
        'uttd': "AFXJ",
        'title': "Final Fantasy Tactics Advance",
    },
    "FFTA_INTER. AFXP": {
        'uttd': "AFXP",
        'title': "Final Fantasy Tactics Advance",
    },
    "FFTA_USVER. AFXE": {
        'uttd': "AFXE",
        'title': "Final Fantasy Tactics Advance",
    },
    "FG2 THE LOSTAFBE": {
        'uttd': "AFBE",
        'title': "Frogger's Adventures 2 - The Lost Wand",
    },
    "FG2 THE LOSTAFBJ": {
        'uttd': "AFBJ",
        'title': "Frogger - Mahou no Kuni no Daibouken",
    },
    "FG2 THE LOSTAFBP": {
        'uttd': "AFBP",
        'title': "Frogger's Adventures 2 - The Lost Wand",
    },
    "FIFA 06     BF6E": {
        'uttd': "BF6E",
        'title': "FIFA 06",
    },
    "FIFA 07     B7FE": {
        'uttd': "B7FE",
        'title': "FIFA 07",
    },
    "FIFA 2004   BFIE": {
        'uttd': "BFIE",
        'title': "FIFA 2004",
    },
    "FIFA 2005   BF5E": {
        'uttd': "BF5E",
        'title': "FIFA Football 2005",
    },
    "FIFA        AFJE": {
        'uttd': "AFJE",
        'title': "FIFA",
    },
    "FIFA WC     B6WE": {
        'uttd': "B6WE",
        'title': "FIFA World Cup",
    },
    "FIGHTBOX    BOXP": {
        'uttd': "BOXP",
        'title': "FightBox",
    },
    "FILA DECATHLAFLP": {
        'uttd': "AFLP",
        'title': "FILA Decathlon",
    },
    "FINAL FIGHT AFFE": {
        'uttd': "AFFE",
        'title': "Final Fight One",
    },
    "FINAL FIGHT AFFJ": {
        'uttd': "AFFJ",
        'title': "Final Fight One",
    },
    "FINAL FIGHT AFFP": {
        'uttd': "AFFP",
        'title': "Final Fight One",
    },
    "FINAL FP    AFWJ": {
        'uttd': "AFWJ",
        'title': "Final Fire Pro Wrestling - Yume no Dantai Unei!",
    },
    "FINDET NEMO AZID": {
        'uttd': "AZID",
        'title': "Findet Nemo",
    },
    "FINDINGNEMO2BZIE": {
        'uttd': "BZIE",
        'title': "Finding Nemo - The Continuing Adventures",
    },
    "FINDINGNEMO2BZIJ": {
        'uttd': "BZIJ",
        'title': "Finding Nemo - Arata na Bouken",
    },
    "FINDINGNEMO2BZIX": {
        'uttd': "BZIX",
        'title': "Finding Nemo - The Continuing Adventures",
    },
    "FINDINGNEMO2BZIY": {
        'uttd': "BZIY",
        'title': "Finding Nemo - The Continuing Adventures",
    },
    "FINDING NEMOAZIE": {
        'uttd': "AZIE",
        'title': "Finding Nemo",
    },
    "FINDING NEMOAZIX": {
        'uttd': "AZIX",
        'title': "Finding Nemo",
    },
    "FINDING NEMOAZIY": {
        'uttd': "AZIY",
        'title': "Finding Nemo",
    },
    "FINDING NEMOBFNJ": {
        'uttd': "BFNJ",
        'title': "Finding Nemo",
    },
    "FIREEMBLEM2EBE8E": {
        'uttd': "BE8E",
        'title': "Fire Emblem - The Sacred Stones",
    },
    "FIREEMBLEM2PBE8P": {
        'uttd': "BE8P",
        'title': "Fire Emblem - The Sacred Stones",
    },
    "FIREEMBLEM6 AFEJ": {
        'uttd': "AFEJ",
        'title': "Fire Emblem - Fuuin no Tsurugi",
    },
    "FIREEMBLEM7 AE7J": {
        'uttd': "AE7J",
        'title': "Fire Emblem - Rekka no Ken",
    },
    "FIREEMBLEM8 BE8J": {
        'uttd': "BE8J",
        'title': "Fire Emblem - Seima no Kouseki",
    },
    "FIREEMBLEME AE7E": {
        'uttd': "AE7E",
        'title': "Fire Emblem",
        'icon0': 'https://images.launchbox-app.com/a3cf209e-7ad6-4d6a-b314-7c1e59400c64.jpg',
        'pic0': 'https://images.launchbox-app.com/88cd133b-578e-4517-8b73-1d1dc06746a0.png',
        'pic1': 'https://images.launchbox-app.com/89982137-a0fc-4833-89bd-5f73201f155e.jpg',
        'snd0': 'https://www.youtube.com/watch?v=NEStaXflg3o&list=PLA0005A166A014EF4&index=1',
    },
    "FIREEMBLEMX AE7X": {
        'uttd': "AE7X",
        'title': "Fire Emblem",
        'icon0': 'https://images.launchbox-app.com/a3cf209e-7ad6-4d6a-b314-7c1e59400c64.jpg',
        'pic0': 'https://images.launchbox-app.com/88cd133b-578e-4517-8b73-1d1dc06746a0.png',
        'pic1': 'https://images.launchbox-app.com/89982137-a0fc-4833-89bd-5f73201f155e.jpg',
        'snd0': 'https://www.youtube.com/watch?v=NEStaXflg3o&list=PLA0005A166A014EF4&index=1',
    },
    "FIREEMBLEMY AE7Y": {
        'uttd': "AE7Y",
        'title': "Fire Emblem",
        'icon0': 'https://images.launchbox-app.com/a3cf209e-7ad6-4d6a-b314-7c1e59400c64.jpg',
        'pic0': 'https://images.launchbox-app.com/88cd133b-578e-4517-8b73-1d1dc06746a0.png',
        'pic1': 'https://images.launchbox-app.com/89982137-a0fc-4833-89bd-5f73201f155e.jpg',
        'snd0': 'https://www.youtube.com/watch?v=NEStaXflg3o&list=PLA0005A166A014EF4&index=1',
    },
    "FLUSHED AWAYBLHE": {
        'uttd': "BLHE",
        'title': "Flushed Away",
    },
    "FLUSHED AWAYBLHP": {
        'uttd': "BLHP",
        'title': "Flushed Away",
    },
    "FMS METROID FMRJ": {
        'uttd': "FMRJ",
        'title': "Famicom Mini Vol. 23 - Metroid",
    },
    "FO9DG01A    AF9J": {
        'uttd': "AF9J",
        'title': "Field of Nine - Digital Edition 2001",
    },
    "FORDRACING3 BF3E": {
        'uttd': "BF3E",
        'title': "Ford Racing 3",
    },
    "FORDRACING3 BF3P": {
        'uttd': "BF3P",
        'title': "Ford Racing 3",
    },
    "FORTRESS    AFOE": {
        'uttd': "AFOE",
        'title': "Fortress",
    },
    "FORTRESS    AFOP": {
        'uttd': "AFOP",
        'title': "Fortress",
    },
    "FOSTERS HOMEBFYE": {
        'uttd': "BFYE",
        'title': "Foster's Home for Imaginary Friends",
    },
    "FP2 NA      AFYE": {
        'uttd': "AFYE",
        'title': "Fire Pro Wrestling 2",
    },
    "FPA         AFPJ": {
        'uttd': "AFPJ",
        'title': "Fire Pro Wrestling A",
    },
    "FP US       AFPE": {
        'uttd': "AFPE",
        'title': "Fire Pro Wrestling",
    },
    "FRANKLIN    BFKE": {
        'uttd': "BFKE",
        'title': "Franklin the Turtle",
    },
    "FRANKLIN    BFKP": {
        'uttd': "BFKP",
        'title': "Franklin the Turtle",
    },
    "FRANKLIN    BFLE": {
        'uttd': "BFLE",
        'title': "Franklin's Great Adventures",
    },
    "FRANKLIN    BFLP": {
        'uttd': "BFLP",
        'title': "Franklin's Great Adventures",
    },
    "FREEKSTYLE  BFSE": {
        'uttd': "BFSE",
        'title': "Freekstyle",
    },
    "FREEKSTYLE  BFSP": {
        'uttd': "BFSP",
        'title': "Freekstyle",
    },
    "FREESTYLE SCARFP": {
        'uttd': "ARFP",
        'title': "Freestyle Scooter",
    },
    "FROGGER RPG BFJE": {
        'uttd': "BFJE",
        'title': "Frogger's Journey - The Forgotten Relic",
    },
    "FROGGER RPG BFJJ": {
        'uttd': "BFJJ",
        'title': "Frogger - Kodaibunmei no Nazo",
    },
    "FROGQST     AFQE": {
        'uttd': "AFQE",
        'title': "Frogger Advance - The Great Quest",
    },
    "FROGQST     AFQP": {
        'uttd': "AFQP",
        'title': "Frogger Advance - The Great Quest",
    },
    "FROG: TEMPLEAFRE": {
        'uttd': "AFRE",
        'title': "Frogger's Adventures - Temple of the Frog",
    },
    "FROG: TEMPLEAFRP": {
        'uttd': "AFRP",
        'title': "Frogger's Adventures - Temple of the Frog",
    },
    "FRONTIERST  BCMJ": {
        'uttd': "BCMJ",
        'title': "Frontier Stories",
    },
    "FRUITMURA   BFDJ": {
        'uttd': "BFDJ",
        'title': "Fruit Mura no Doubutsutachi",
    },
    "F-SOCCER2002AFMJ": {
        'uttd': "AFMJ",
        'title': "Formation Soccer 2002",
    },
    "FSTONES BTIBAFSE": {
        'uttd': "AFSE",
        'title': "Flintstones, The - Big Trouble in Bedrock",
    },
    "FSTONES BTIBAFSP": {
        'uttd': "AFSP",
        'title': "Flintstones, The - Big Trouble in Bedrock",
    },
    "F TENNIS    AATJ": {
        'uttd': "AATJ",
        'title': "Family Tennis Advance",
    },
    "FUJUHOUROKU BTFJ": {
        'uttd': "BTFJ",
        'title': "Tokyo Majin Gakuen - Fuju Houroku",
    },
    "FUSHIGIANGE AFAJ": {
        'uttd': "AFAJ",
        'title': "Fushigi no Kuni no Angelique",
    },
    "F-ZERO2     BFZE": {
        'uttd': "BFZE",
        'title': "F-Zero - GP Legend",
    },
    "F-ZERO2     BFZJ": {
        'uttd': "BFZJ",
        'title': "F-Zero - Falcon Densetsu",
    },
    "F-ZERO2     BFZP": {
        'uttd': "BFZP",
        'title': "F-Zero - GP Legend",
    },
    "F-ZERO ADVANAFZE": {
        'uttd': "AFZE",
        'title': "F-Zero - Maximum Velocity",
    },
    "F-ZERO ADVANAFZJ": {
        'uttd': "AFZJ",
        'title': "F-Zero",
    },
    "F-ZEROCLIMAXBFTJ": {
        'uttd': "BFTJ",
        'title': "F-Zero - Climax",
    },
    "GACHINKOPRO ANYJ": {
        'uttd': "ANYJ",
        'title': "Gachinko Pro Yakyuu",
    },
    "GADGETRACERSAQ2P": {
        'uttd': "AQ2P",
        'title': "Gadget Racers",
    },
    "GADGETRACERSAQAE": {
        'uttd': "AQAE",
        'title': "Gadget Racers",
    },
    "GAKENALICE_1BASJ": {
        'uttd': "BASJ",
        'title': "Gakuen Alice - Dokidoki Fushigi Taiken",
    },
    "GAKKOAGB-1  AYSJ": {
        'uttd': "AYSJ",
        'title': "Gakkou wo Tsukurou!! Advance",
    },
    "GAKUENMURYOUBGSJ": {
        'uttd': "BGSJ",
        'title': "Gakuen Senki Muryou",
    },
    "GALAXY ANGELAGZJ": {
        'uttd': "AGZJ",
        'title': "Galaxy Angel - Moridakusan Tenshi no Full-Course - Okawari Jiyuu",
    },
    "GALIDOR     AG8E": {
        'uttd': "AG8E",
        'title': "Galidor - Defenders of the Outer Dimension",
    },
    "GAMEEXPLSIONBG7E": {
        'uttd': "BG7E",
        'title': "Games Explosion!",
    },
    "GARFIELD    BG9E": {
        'uttd': "BG9E",
        'title': "Garfield and His Nine Lives",
    },
    "GARFIELD    BG9P": {
        'uttd': "BG9P",
        'title': "Garfield and His Nine Lives",
    },
    "GARFIELDTSFPBGOE": {
        'uttd': "BGOE",
        'title': "Garfield - The Search for Pooky",
    },
    "GARFIELDTSFPBGOP": {
        'uttd': "BGOP",
        'title': "Garfield - The Search for Pooky",
    },
    "GASHBOOKMARKBKBJ": {
        'uttd': "BKBJ",
        'title': "Konjiki no Gashbell!! - Makai no Bookmark",
    },
    "GASH-CARDGBABKEJ": {
        'uttd': "BKEJ",
        'title': "Konjiki no Gashbell!! - The Card Battle for GBA",
    },
    "GASH-ZAKERU2BGYJ": {
        'uttd': "BGYJ",
        'title': "Konjiki no Gashbell!! - Unare! Yuujou no Zakeru 2",
    },
    "GASH-ZAKERU3BUDJ": {
        'uttd': "BUDJ",
        'title': "Konjiki no Gashbell!! Yuujou no Zakeru Dream Tag Tournament",
    },
    "GASH-ZAKERU A4GJ": {
        'uttd': "A4GJ",
        'title': "Konjiki no Gashbell!! - Unare! Yuujou no Zakeru",
    },
    "GAUNTLETCOMPB69E": {
        'uttd': "B69E",
        'title': "Gauntlet - Rampart",
    },
    "GAUNTLET_DL AYGE": {
        'uttd': "AYGE",
        'title': "Gauntlet - Dark Legacy",
    },
    "GAUNTLETRAMPB69P": {
        'uttd': "B69P",
        'title': "Gauntlet - Rampart",
    },
    "GBA_Capture tvap": {
        'uttd': "tvap",
        'title': "TV Tuner PAL",
    },
    "GBA_SENGOKU1A7GJ": {
        'uttd': "A7GJ",
        'title': "Sengoku Kakumei Gaiden",
    },
    "GBAZELDA    AZLE": {
        'uttd': "AZLE",
        'title': "Legend of Zelda, The - A Link to the Past & Four Swords",
    },
    "GBAZELDA    AZLJ": {
        'uttd': "AZLJ",
        'title': "Zelda no Densetsu - Kamigami no Triforce & 4tsu no Tsurugi",
    },
    "GBAZELDA    AZLP": {
        'uttd': "AZLP",
        'title': "Legend of Zelda, The - A Link to the Past & Four Swords",
    },
    "GBAZELDA MC BZME": {
        'uttd': "BZME",
        'title': "Legend of Zelda, The - The Minish Cap",
        'icon0': 'https://images.launchbox-app.com/0fe2ca8b-4307-4913-a1b2-46720c1a82d1.jpg',
        'pic0': 'https://images.launchbox-app.com/f5d37c8b-60cc-45c1-b459-27055dbe98e7.png',
        'pic1': 'https://images.launchbox-app.com/4827e856-0ee9-46df-81fe-d83f72225588.jpg',
        'snd0': 'https://www.youtube.com/watch?v=B7T9t5Swu0c&list=PL66C3A99730C3F3F2&index=1',
    },
    "GBAZELDA MC BZMJ": {
        'uttd': "BZMJ",
        'title': "Zelda no Densetsu - Fushigi no Boushi",
        'icon0': 'https://images.launchbox-app.com/aa436fc7-6b34-4cb7-87e7-dec315f71573.jpg',
        'pic0': 'https://images.launchbox-app.com/751983ec-eb5d-4456-ad1f-7a8f8000eb35.png',
        'pic1': 'https://images.launchbox-app.com/4827e856-0ee9-46df-81fe-d83f72225588.jpg',
        'snd0': 'https://www.youtube.com/watch?v=B7T9t5Swu0c&list=PL66C3A99730C3F3F2&index=1',
    },
    "GBAZELDA MC BZMP": {
        'uttd': "BZMP",
        'title': "Legend of Zelda, The - The Minish Cap",
        'icon0': 'https://images.launchbox-app.com/0fe2ca8b-4307-4913-a1b2-46720c1a82d1.jpg',
        'pic0': 'https://images.launchbox-app.com/f5d37c8b-60cc-45c1-b459-27055dbe98e7.png',
        'pic1': 'https://images.launchbox-app.com/4827e856-0ee9-46df-81fe-d83f72225588.jpg',
        'snd0': 'https://www.youtube.com/watch?v=B7T9t5Swu0c&list=PL66C3A99730C3F3F2&index=1',
    },
    "GB JYAGAN   BGFJ": {
        'uttd': "BGFJ",
        'title': "GetBackers Dakkanya - Jagan Fuuin!",
    },
    "GB METRO    A8GJ": {
        'uttd': "A8GJ",
        'title': "GetBackers Dakkanya - Metropolis Dakkan Sakusen!",
    },
    "GBWARS1+2   BGWJ": {
        'uttd': "BGWJ",
        'title': "Game Boy Wars Advance 1+2",
    },
    "GEKIDO      AGEE": {
        'uttd': "AGEE",
        'title': "Gekido Advance - Kintaro's Revenge",
    },
    "GEKIDO      AGEP": {
        'uttd': "AGEP",
        'title': "Gekido Advance - Kintaro's Revenge",
    },
    "GEKITOU NOAHANNJ": {
        'uttd': "ANNJ",
        'title': "Gekitou Densetsu Noah - Dream Management",
    },
    "GEM SMASHERSAZSE": {
        'uttd': "AZSE",
        'title': "Gem Smashers",
    },
    "GENSOU-CARD1AGKJ": {
        'uttd': "AGKJ",
        'title': "Gensou Suikoden - Card Stories",
    },
    "GEORGE      B3JE": {
        'uttd': "B3JE",
        'title': "Curious George",
    },
    "GET! AGB    BGBJ": {
        'uttd': "BGBJ",
        'title': "Get! - Boku no Mushi Tsukamaete",
    },
    "GETBACKERS  AGBJ": {
        'uttd': "AGBJ",
        'title': "GetBackers Dakkanya - Jigoku no Scaramouche",
    },
    "GET PHAT!   AGPE": {
        'uttd': "AGPE",
        'title': "No Rules - Get Phat",
    },
    "GGENE A     BGAJ": {
        'uttd': "BGAJ",
        'title': "SD Gundam G-Generation Advance",
    },
    "GGXAE       AGXE": {
        'uttd': "AGXE",
        'title': "Guilty Gear X - Advance Edition",
    },
    "GGXAE       AGXJ": {
        'uttd': "AGXJ",
        'title': "Guilty Gear X - Advance Edition",
    },
    "GGXAE       AGXP": {
        'uttd': "AGXP",
        'title': "Guilty Gear X - Advance Edition",
    },
    "GHOST RIDER BR8E": {
        'uttd': "BR8E",
        'title': "Ghost Rider",
    },
    "GHOSTTRAP   AGVJ": {
        'uttd': "AGVJ",
        'title': "Ghost Trap",
    },
    "GHTP MAXD   BGQE": {
        'uttd': "BGQE",
        'title': "Greg Hastings' Tournament Paintball Max'D",
    },
    "GLORY DAYS  BG6P": {
        'uttd': "BG6P",
        'title': "Glory Days - The Essence of War",
    },
    "GOASTHOUSE24AUYJ": {
        'uttd': "AUYJ",
        'title': "Yuureiyashiki no Nijuuyojikan",
    },
    "GODZILLADOMIAG4E": {
        'uttd': "AG4E",
        'title': "Godzilla - Domination!",
    },
    "GODZILLADOMIAG4P": {
        'uttd': "AG4P",
        'title': "Godzilla - Domination!",
    },
    "GODZILLA KDAAG4J": {
        'uttd': "AG4J",
        'title': "Godzilla - Kaijuu Dairantou Advance",
    },
    "GOEMON1&2   BG2J": {
        'uttd': "BG2J",
        'title': "Kessakusen! Ganbare Goemon 1+2",
    },
    "GOEMON 1    FGGJ": {
        'uttd': "FGGJ",
        'title': "Famicom Mini Vol. 20 - Ganbare Goemon! Karakuri Douchuu",
    },
    "GOEMONNEW   AGNJ": {
        'uttd': "AGNJ",
        'title': "Goemon - New Age Shutsudou!",
    },
    "GOGOBECKHAM!AGQP": {
        'uttd': "AGQP",
        'title': "Go! Go! Beckham! - Adventure on Soccer Island",
    },
    "GOLDENNUGGETBGGE": {
        'uttd': "BGGE",
        'title': "Golden Nugget Casino",
    },
    "GOLDEN_SUN_AAGSD": {
        'uttd': "AGSD",
        'title': "Golden Sun",
    },
    "Golden_Sun_AAGSE": {
        'uttd': "AGSE",
        'title': "Golden Sun",
    },
    "GOLDEN_SUN_AAGSF": {
        'uttd': "AGSF",
        'title': "Golden Sun",
    },
    "GOLDEN_SUN_AAGSI": {
        'uttd': "AGSI",
        'title': "Golden Sun",
    },
    "GOLDEN_SUN_AAGSS": {
        'uttd': "AGSS",
        'title': "Golden Sun",
    },
    "GOLDEN_SUN_BAGFD": {
        'uttd': "AGFD",
        'title': "Golden Sun 2 - Die Vergessene Epoche",
    },
    "GOLDEN_SUN_BAGFE": {
        'uttd': "AGFE",
        'title': "Golden Sun - The Lost Age",
    },
    "GOLDEN_SUN_BAGFF": {
        'uttd': "AGFF",
        'title': "Golden Sun - L'Age Perdu",
    },
    "GOLDEN_SUN_BAGFI": {
        'uttd': "AGFI",
        'title': "Golden Sun - L'Era Perduta",
    },
    "GOLDEN_SUN_BAGFS": {
        'uttd': "AGFS",
        'title': "Golden Sun - La Edad Perdida",
    },
    "GOLFMASTER  AGRJ": {
        'uttd': "AGRJ",
        'title': "JGTO Kounin Golf Master - Japan Golf Tour Game",
    },
    "GOLFMASTER MAGMJ": {
        'uttd': "AGMJ",
        'title': "JGTO Kounin Golf Master Mobile - Japan Golf Tour Game",
    },
    "GRADIUSADVANAGAP": {
        'uttd': "AGAP",
        'title': "Gradius Advance",
    },
    "GRADIUSGALAXAGAE": {
        'uttd': "AGAE",
        'title': "Gradius Galaxies",
    },
    "GRADIUSGENERAGAJ": {
        'uttd': "AGAJ",
        'title': "Gradius Generation",
    },
    "GREATESTNINEAG9J": {
        'uttd': "AG9J",
        'title': "Greatest Nine",
    },
    "GREENEGGSHAMBUSE": {
        'uttd': "BUSE",
        'title': "Green Eggs and Ham by Dr. Seuss",
    },
    "GREMLINS    AGGP": {
        'uttd': "AGGP",
        'title': "Gremlins - Stripe vs. Gizmo",
    },
    "GREMLINS STRAGGE": {
        'uttd': "AGGE",
        'title': "Gremlins - Stripe vs. Gizmo",
    },
    "GREMLINS STRAGGP": {
        'uttd': "AGGP",
        'title': "Gremlins - Stripe vs. Gizmo",
    },
    "GROOVY GAMESAVBE": {
        'uttd': "AVBE",
        'title': "Barbie Groovy Games",
    },
    "GROOVY GAMESAVBP": {
        'uttd': "AVBP",
        'title': "Barbie Groovy Games",
    },
    "GTA3MGP     BARP": {
        'uttd': "BARP",
        'title': "2 Games in 1 - GT Advance 3 + Moto GP",
    },
    "GTA ADVANCE BGTP": {
        'uttd': "BGTP",
        'title': "Grand Theft Auto Advance",
    },
    "GTA         BGTE": {
        'uttd': "BGTE",
        'title': "Grand Theft Auto Advance",
    },
    "GT ADVANCE 2AGWE": {
        'uttd': "AGWE",
        'title': "GT Advance 2 - Rally Racing",
    },
    "GT ADVANCE 2AGWP": {
        'uttd': "AGWP",
        'title': "GT Advance 2 - Rally Racing",
    },
    "GT ADVANCE 3A2GE": {
        'uttd': "A2GE",
        'title': "GT Advance 3 - Pro Concept Racing",
    },
    "GT ADVANCE 3A2GP": {
        'uttd': "A2GP",
        'title': "GT Advance 3 - Pro Concept Racing",
    },
    "GT ADVANCE CACAE": {
        'uttd': "ACAE",
        'title': "GT Advance - Championship Racing",
    },
    "GT-CHAMP    AGTJ": {
        'uttd': "AGTJ",
        'title': "Zen-Nippon GT Senshuken",
    },
    "GT-CHAMP    ATCX": {
        'uttd': "ATCX",
        'title': "GT Championship",
    },
    "GTRACERS    BJAP": {
        'uttd': "BJAP",
        'title': "GT Racers",
    },
    "GUMBY       BGVE": {
        'uttd': "BGVE",
        'title': "Gumby vs. the Astrobots",
    },
    "GUNDAMSEED-BBGNE": {
        'uttd': "BGNE",
        'title': "Mobile Suit Gundam Seed - Battle Assault",
    },
    "GUNDAMSEED  BGNJ": {
        'uttd': "BGNJ",
        'title': "Kidou Senshi Gundam Seed - Tomo to Kimi to koko de.",
    },
    "GUNSTAR FH  BHGP": {
        'uttd': "BHGP",
        'title': "Gunstar Future Heroes",
    },
    "GUNSTAR SH  BGXJ": {
        'uttd': "BGXJ",
        'title': "Gunstar Super Heroes",
    },
    "GUNSTAR SH  BHGE": {
        'uttd': "BHGE",
        'title': "Gunstar Super Heroes",
    },
    "GURANBO     AIBJ": {
        'uttd': "AIBJ",
        'title': "Guranbo",
    },
    "GURULOGI_C  AGCJ": {
        'uttd': "AGCJ",
        'title': "Guru Logic Champ",
    },
    "GURUMI      A2VJ": {
        'uttd': "A2VJ",
        'title': "Kisekko Gurumi - Chesty to Nuigurumi-tachi no Mahou no Bouken",
    },
    "G&W GALLERY4AQWE": {
        'uttd': "AQWE",
        'title': "Game & Watch Gallery 4",
    },
    "G&W GALLERYAAQWP": {
        'uttd': "AQWP",
        'title': "Game & Watch Gallery Advance",
    },
    "GYAKUTEN_SA2A3GJ": {
        'uttd': "A3GJ",
        'title': "Gyakuten Saiban 2",
    },
    "GYAKUTEN_SA3A3JJ": {
        'uttd': "A3JJ",
        'title': "Gyakuten Saiban 3",
    },
    "GYAKUTEN_SAIASBJ": {
        'uttd': "ASBJ",
        'title': "Gyakuten Saiban",
    },
    "HACHIEMON   A8EJ": {
        'uttd': "A8EJ",
        'title': "Hachiemon",
    },
    "HAGANERONDO BHRJ": {
        'uttd': "BHRJ",
        'title': "Hagane no Renkinjutsushi - Meisou no Rondo",
    },
    "HAGANESONATABH2J": {
        'uttd': "BH2J",
        'title': "Hagane no Renkinjutsushi - Omoide no Soumeikyoku",
    },
    "HAJIMENOIPPOA2HJ": {
        'uttd': "A2HJ",
        'title': "Hajime no Ippo - The Fighting!",
    },
    "HAM-CLUB3   AJHJ": {
        'uttd': "AJHJ",
        'title': "Hamster Club 3",
    },
    "HAM-CLUB4   A4KJ": {
        'uttd': "A4KJ",
        'title': "Hamster Club 4",
    },
    "HAMMYGOSNUTSBH7E": {
        'uttd': "BH7E",
        'title': "Over the Hedge - Hammy Goes Nuts!",
    },
    "HAMMYGOSNUTSBH7P": {
        'uttd': "BH7P",
        'title': "Over the Hedge - Hammy Goes Nuts!",
    },
    "HAMSPORTS   B85A": {
        'uttd': "B85A",
        'title': "Hamtaro - Ham-Ham Games",
    },
    "HAMSPORTS   B85P": {
        'uttd': "B85P",
        'title': "Hamtaro - Ham-Ham Games",
    },
    "HAMSTAR2    AHBJ": {
        'uttd': "AHBJ",
        'title': "Hamster Monogatari 2 GBA",
    },
    "HAMSTAR3    A83J": {
        'uttd': "A83J",
        'title': "Hamster Monogatari 3 GBA",
    },
    "HAMSTAR3EX4 BHSJ": {
        'uttd': "BHSJ",
        'title': "Hamster Monogatari 3EX + 4 Special",
    },
    "HAMSTAR COLLBHCJ": {
        'uttd': "BHCJ",
        'title': "Hamster Monogatari Collection",
    },
    "HAMSTER     AH7J": {
        'uttd': "AH7J",
        'title': "Nakayoshi Pet Advance Series 1 - Kawaii Hamster",
    },
    "HAMUPARAAGB AHAJ": {
        'uttd': "AHAJ",
        'title': "Hamster Paradise Advanchu",
    },
    "HAMUPARAPUREA82J": {
        'uttd': "A82J",
        'title': "Hamster Paradise - Pure Heart",
    },
    "HAMUTARO3   AH3E": {
        'uttd': "AH3E",
        'title': "Hamtaro - Ham-Ham Heartbreak",
    },
    "HAMUTARO3   AH3J": {
        'uttd': "AH3J",
        'title': "Tottoko Hamutarou 3 - Love Love Daibouken Dechu",
    },
    "HAMUTARO3   AH3P": {
        'uttd': "AH3P",
        'title': "Hamtaro - Ham-Ham Heartbreak",
    },
    "HAMUTARO4   A84J": {
        'uttd': "A84J",
        'title': "Tottoko Hamutarou 4 - Nijiiro Daikoushin Dechu",
    },
    "HAMUTARO4   A84P": {
        'uttd': "A84P",
        'title': "Hamtaro - Rainbow Rescue",
    },
    "HANADON     BDAJ": {
        'uttd': "BDAJ",
        'title': "Donchan Puzzle Hanabi de Dohn Advance",
    },
    "HANAYA      A87J": {
        'uttd': "A87J",
        'title': "Ohanaya-san Monogatari GBA - Iyashikei Ohanaya-san Ikusei Game",
    },
    "HANAYANINAROAF7J": {
        'uttd': "AF7J",
        'title': "Tokimeki Yume Series 1 - Ohanaya-san ni Narou!",
    },
    "HAPPYCAKE   A56J": {
        'uttd': "A56J",
        'title': "Dokidoki Cooking Series 1 - Komugi-chan no Happy Cake",
    },
    "HAPPY FEET  BH3E": {
        'uttd': "BH3E",
        'title': "Happy Feet",
    },
    "HAPPY FEET EBH3P": {
        'uttd': "BH3P",
        'title': "Happy Feet",
    },
    "HAPPYPANECHUKHPJ": {
        'uttd': "KHPJ",
        'title': "Koro Koro Puzzle - Happy Panechu!",
    },
    "HAPPYTRUMP20BTLJ": {
        'uttd': "BTLJ",
        'title': "Minna no Soft Series - Happy Trump 20",
    },
    "HARDCOREPOOLBHOP": {
        'uttd': "BHOP",
        'title': "Hardcore Pool",
    },
    "HARLEMGLOBE BHNP": {
        'uttd': "BHNP",
        'title': "Original Harlem Globetrotters, The",
    },
    "HARLEMTROTERBHNE": {
        'uttd': "BHNE",
        'title': "Original Harlem Globetrotters, The",
    },
    "HAROBOTSADVNAHQJ": {
        'uttd': "AHQJ",
        'title': "Harobots - Robo Hero Battling!!",
    },
    "HARONOPUYOPUBH6J": {
        'uttd': "BH6J",
        'title': "Haro no Puyo Puyo",
    },
    "HARRY POTTERAHRE": {
        'uttd': "AHRE",
        'title': "Harry Potter and the Sorcerer's Stone",
    },
    "HARRY POTTERAHRJ": {
        'uttd': "AHRJ",
        'title': "Harry Potter to Kenja no Ishi",
    },
    "HARRY POTTERBHTE": {
        'uttd': "BHTE",
        'title': "Harry Potter and the Prisoner of Azkaban",
    },
    "HARRY POTTERBHTJ": {
        'uttd': "BHTJ",
        'title': "Harry Potter to Azkaban no Shuujin",
    },
    "HARUKANARU  ARNJ": {
        'uttd': "ARNJ",
        'title': "Harukanaru Toki no Naka de",
    },
    "HARVESTMOGBAA4NE": {
        'uttd': "A4NE",
        'title': "Harvest Moon - Friends of Mineral Town",
    },
    "HARVESTMOGBAA4NP": {
        'uttd': "A4NP",
        'title': "Harvest Moon - Friends of Mineral Town",
    },
    "HARVESTMOGERA4ND": {
        'uttd': "A4ND",
        'title': "Harvest Moon - Friends of Mineral Town",
    },
    "HATENASATENAAHSJ": {
        'uttd': "AHSJ",
        'title': "Hatena Satena",
    },
    "HCPINBALL   AH6E": {
        'uttd': "AH6E",
        'title': "Hardcore Pinball",
    },
    "HEIDI       BHJP": {
        'uttd': "BHJP",
        'title': "Heidi - The Game",
    },
    "HELLO       BHDJ": {
        'uttd': "BHDJ",
        'title': "Hello! - Idol Debut",
    },
    "HELLOKITTY  B86E": {
        'uttd': "B86E",
        'title': "Hello Kitty - Happy Party Pals",
    },
    "HELLOKITTY  B86P": {
        'uttd': "B86P",
        'title': "Hello Kitty - Happy Party Pals",
    },
    "HELLOKITTY  B86X": {
        'uttd': "B86X",
        'title': "Hello Kitty - Happy Party Pals",
    },
    "HE-MAN POWERAGUE": {
        'uttd': "AGUE",
        'title': "Masters of the Universe - He-Man Power of Grayskull",
    },
    "HERBIE FL   B8FE": {
        'uttd': "B8FE",
        'title': "Herbie - Fully Loaded",
    },
    "HERBIE FL   B8FP": {
        'uttd': "B8FP",
        'title': "Herbie - Fully Loaded",
    },
    "HEXCITE AGB AJSJ": {
        'uttd': "AJSJ",
        'title': "Space Hexcite - Maetel Legend EX",
    },
    "HEY ARNOLD! AAEE": {
        'uttd': "AAEE",
        'title': "Hey Arnold! - The Movie",
    },
    "HEY!ARNOLD! AAEE": {
        'uttd': "AAEE",
        'title': "Hey Arnold! - The Movie",
    },
    "HH MLB 2002 ASSE": {
        'uttd': "ASSE",
        'title': "High Heat Major League Baseball 2002",
    },
    "HH MLB 2003 AHHE": {
        'uttd': "AHHE",
        'title': "High Heat Major League Baseball 2003",
    },
    "HH MLB 2003 AHXJ": {
        'uttd': "AHXJ",
        'title': "High Heat Major League Baseball 2003",
    },
    "HIGANBANA   AHZJ": {
        'uttd': "AHZJ",
        'title': "Higanbana",
    },
    "HIGEJINTORI AKUJ": {
        'uttd': "AKUJ",
        'title': "Kurohige no Kurutto Jintori",
    },
    "HI HI PUFFYABHHE": {
        'uttd': "BHHE",
        'title': "Hi Hi Puffy AmiYumi - Kaznapped!",
    },
    "HI HI PUFFYABHHJ": {
        'uttd': "BHHJ",
        'title': "Hi! Hi! Puffy AmiYumi",
    },
    "HI HI PUFFY BHHP": {
        'uttd': "BHHP",
        'title': "Hi Hi Puffy AmiYumi - Kaznapped!",
    },
    "HIKARUNOGO2 AKEJ": {
        'uttd': "AKEJ",
        'title': "Hikaru no Go 2",
    },
    "HIKARUNOGO  AHKJ": {
        'uttd': "AHKJ",
        'title': "Hikaru no Go",
    },
    "HIMAWARI    BNBJ": {
        'uttd': "BNBJ",
        'title': "Himawari Doubutsu Byouin - Pet no Oishasan Ikusei Game",
    },
    "HITOFUDEGBA BIIJ": {
        'uttd': "BIIJ",
        'title': "Tsuukin Hitofude",
    },
    "HM MFOM USA BFGE": {
        'uttd': "BFGE",
        'title': "Harvest Moon - More Friends of Mineral Town",
    },
    "HOBBIT EU   AH9P": {
        'uttd': "AH9P",
        'title': "Hobbit, The",
    },
    "HOBBIT NO BOAH9J": {
        'uttd': "AH9J",
        'title': "Hobbit no Bouken - Lord of the Rings - Hajimari no Monogatari",
    },
    "HOBBIT US   AH9E": {
        'uttd': "AH9E",
        'title': "Hobbit, The",
    },
    "HOBOSAN     AHVJ": {
        'uttd': "AHVJ",
        'title': "Nakayoshi Youchien - Sukoyaka Enji Ikusei Game",
    },
    "HOLDM&CASINOBWCP": {
        'uttd': "BWCP",
        'title': "2 Games in 1 - Golden Nugget Casino + Texas Hold'em Poker",
    },
    "HOODLUMS REVBRYE": {
        'uttd': "BRYE",
        'title': "Rayman - Hoodlum's Revenge",
    },
    "HOODLUMS REVBRYP": {
        'uttd': "BRYP",
        'title': "Rayman - Hoodlums' Revenge",
    },
    "HOT POTATO  AHPE": {
        'uttd': "AHPE",
        'title': "Hot Potato!",
    },
    "HOT POTATO  AHPP": {
        'uttd': "AHPP",
        'title': "Hot Potato!",
    },
    "HOT POTATO  AHPX": {
        'uttd': "AHPX",
        'title': "Hot Potato!",
    },
    "HOTSTCHOTWR BQJE": {
        'uttd': "BQJE",
        'title': "2 Games in 1 - Hot Wheels - Stunt Track Challenge + Hot Wheels - World Race",
    },
    "HOT WHEELS  BHXE": {
        'uttd': "BHXE",
        'title': "Hot Wheels - All Out",
    },
    "HOT WHEELS  BHXP": {
        'uttd': "BHXP",
        'title': "Hot Wheels - All Out",
    },
    "HOTWHEELS BRAHWE": {
        'uttd': "AHWE",
        'title': "Hot Wheels - Burnin' Rubber",
    },
    "HOTWHEELS BRAHWJ": {
        'uttd': "AHWJ",
        'title': "Hot Wheels Advance",
    },
    "HOTWHEELS PABHZP": {
        'uttd': "BHZP",
        'title': "2 Games in 1 - Hot Wheels - Velocity X + Hot Wheels - World Race",
    },
    "HOTWHEELSSTCBHEE": {
        'uttd': "BHEE",
        'title': "Hot Wheels - Stunt Track Challenge",
    },
    "HOT WHEELS VAH8E": {
        'uttd': "AH8E",
        'title': "Hot Wheels - Velocity X",
    },
    "HOT WHEELS VAH8P": {
        'uttd': "AH8P",
        'title': "Hot Wheels - Velocity X",
    },
    "HOTWHEELS WOBHWP": {
        'uttd': "BHWP",
        'title': "Hot Wheels - World Race",
    },
    "HOTWHEELS WRBHWE": {
        'uttd': "BHWE",
        'title': "Hot Wheels - World Race",
    },
    "HPOTTER COS A7HE": {
        'uttd': "A7HE",
        'title': "Harry Potter and the Chamber of Secrets",
    },
    "HPOTTER COS A7HJ": {
        'uttd': "A7HJ",
        'title': "Harry Potter to Himitsu no Heya",
    },
    "HUBEST_VOL01B7IJ": {
        'uttd': "B7IJ",
        'title': "Hudson Best Collection Vol. 1 - Bomberman Collection",
    },
    "HUBEST_VOL02B72J": {
        'uttd': "B72J",
        'title': "Hudson Best Collection Vol. 2 - Lode Runner Collection",
    },
    "HUBEST_VOL03B73J": {
        'uttd': "B73J",
        'title': "Hudson Best Collection Vol. 3 - Action Collection",
    },
    "HUBEST_VOL04B74J": {
        'uttd': "B74J",
        'title': "Hudson Best Collection Vol. 4 - Nazotoki Collection",
    },
    "HUBEST_VOL05B75J": {
        'uttd': "B75J",
        'title': "Hudson Best Collection Vol. 5 - Shooting Collection",
    },
    "HUBEST_VOL06B76J": {
        'uttd': "B76J",
        'title': "Hudson Best Collection Vol. 6 - Bouken Jima Collection",
    },
    "HUGO 2IN1   B2HP": {
        'uttd': "B2HP",
        'title': "2 Games in 1 - Hugo - Bukkazoom! + Hugo - The Evil Mirror Advance",
    },
    "HULKV1      AHLE": {
        'uttd': "AHLE",
        'title': "Incredible Hulk, The",
    },
    "HULKV1      AHLP": {
        'uttd': "AHLP",
        'title': "Incredible Hulk, The",
    },
    "HUNTER GBA00A8NJ": {
        'uttd': "A8NJ",
        'title': "Hunter X Hunter - Minna Tomodachi Daisakusen!!",
    },
    "HWVX HWWR   BHZE": {
        'uttd': "BHZE",
        'title': "2 Games in 1 - Hot Wheels - Velocity X + Hot Wheels - World Race",
    },
    "HYAKEI      BHAJ": {
        'uttd': "BHAJ",
        'title': "Hanabi Hyakkei Advance",
    },
    "HYDRA       AFHE": {
        'uttd': "AFHE",
        'title': "Strike Force Hydra",
    },
    "HYDRA       AFHP": {
        'uttd': "AFHP",
        'title': "Strike Force Hydra",
    },
    "HYOUTANJIMA BHYJ": {
        'uttd': "BHYJ",
        'title': "Hyokkori Hyoutanjima - Don Gabacho Daikatsuyaku no Maki",
    },
    "HYPER_SPORTSAWIJ": {
        'uttd': "AWIJ",
        'title': "Hyper Sports 2002 Winter",
    },
    "ICE AGE 2   BIAE": {
        'uttd': "BIAE",
        'title': "Ice Age 2 - The Meltdown",
    },
    "ICE AGE 2 THBIAP": {
        'uttd': "BIAP",
        'title': "Ice Age 2 - The Meltdown",
    },
    "ICEAGE      AIAE": {
        'uttd': "AIAE",
        'title': "Ice Age",
    },
    "ICEAGE      AIAJ": {
        'uttd': "AIAJ",
        'title': "Ice Age",
    },
    "ICE AGE     AIAP": {
        'uttd': "AIAP",
        'title': "Ice Age",
    },
    "ICE CLIMBER FICE": {
        'uttd': "FICE",
        'title': "Classic NES Series - Ice Climber",
    },
    "ICE CLIMBER FICJ": {
        'uttd': "FICJ",
        'title': "Famicom Mini Vol. 03 - Ice Climber",
    },
    "ICE NINE    AR3E": {
        'uttd': "AR3E",
        'title': "Ice Nine",
    },
    "IK ADVANCED AIKP": {
        'uttd': "AIKP",
        'title': "International Karate Advanced",
    },
    "IK PLUS     A3KE": {
        'uttd': "A3KE",
        'title': "International Karate Plus",
    },
    "IK PLUS     A3KP": {
        'uttd': "A3KP",
        'title': "International Karate Plus",
    },
    "INCREDBLEAGBBICD": {
        'uttd': "BICD",
        'title': "Unglaublichen, Die",
    },
    "INCREDBLEAGBBICE": {
        'uttd': "BICE",
        'title': "Incredibles, The",
    },
    "INCREDBLEAGBBICI": {
        'uttd': "BICI",
        'title': "Incredibili, Gli",
    },
    "INCREDBLEAGBBICS": {
        'uttd': "BICS",
        'title': "Increibles, Los",
    },
    "INCREDBLEAGBBICX": {
        'uttd': "BICX",
        'title': "Incredibles, The",
    },
    "INCREDBLROTUBIQE": {
        'uttd': "BIQE",
        'title': "Incredibles, The - Rise of the Underminer",
    },
    "INCREDBLROTUBIQX": {
        'uttd': "BIQX",
        'title': "Incredibles, The - Rise of the Underminer",
    },
    "INFILTRATOR BMHE": {
        'uttd': "BMHE",
        'title': "Medal of Honor - Infiltrator",
    },
    "INFILTRATOR BMHJ": {
        'uttd': "BMHJ",
        'title': "Medal of Honor - Infiltrator",
    },
    "INIDAS      AINJ": {
        'uttd': "AINJ",
        'title': "Initial D - Another Stage",
    },
    "INJUSTICEFORAJLE": {
        'uttd': "AJLE",
        'title': "Justice League - Injustice for All",
    },
    "INJUSTICEFORAJLP": {
        'uttd': "AJLP",
        'title': "Justice League - Injustice for All",
    },
    "INSPECTOR GAAIGE": {
        'uttd': "AIGE",
        'title': "Inspector Gadget - Advance Mission",
    },
    "INSPECTOR GAAIGP": {
        'uttd': "AIGP",
        'title': "Inspector Gadget - Advance Mission",
    },
    "INSPECTOR GAAIRP": {
        'uttd': "AIRP",
        'title': "Inspector Gadget Racing",
    },
    "INUKKO-CLUB AI9J": {
        'uttd': "AI9J",
        'title': "Inukko Club",
    },
    "INUYASYANARAAIYJ": {
        'uttd': "AIYJ",
        'title': "Inuyasha - Naraku no Wana! Mayoi no Mori no Shoutaijou",
    },
    "INVADER     AIVP": {
        'uttd': "AIVP",
        'title': "Invader",
    },
    "IRIDION3D   AI3E": {
        'uttd': "AI3E",
        'title': "Iridion 3D",
    },
    "IRIDIONII   AI2E": {
        'uttd': "AI2E",
        'title': "Iridion II",
    },
    "IRIDIONII   AI2P": {
        'uttd': "AI2P",
        'title': "Iridion II",
    },
    "ISLAND XTREMAXTE": {
        'uttd': "AXTE",
        'title': "LEGO Island Xtreme Stunts",
    },
    "ISPY CHALNGRA4CE": {
        'uttd': "A4CE",
        'title': "I Spy Challenger!",
    },
    "ISS ADVANCE AY2P": {
        'uttd': "AY2P",
        'title': "International Superstar Soccer Advance",
    },
    "I.S.S. AGB  AISP": {
        'uttd': "AISP",
        'title': "International Superstar Soccer",
    },
    "ISSEKIHATCHOAIEJ": {
        'uttd': "AIEJ",
        'title': "Isseki Hattyou - Kore 1ppon de 8syurui!",
    },
    "ITS MR PANTSBPIE": {
        'uttd': "BPIE",
        'title': "It's Mr. Pants",
    },
    "JACKIECHANDHAJCE": {
        'uttd': "AJCE",
        'title': "Jackie Chan Adventures - Legend of the Darkhand",
    },
    "JACKIECHANDHAJCF": {
        'uttd': "AJCF",
        'title': "Aventures de Jackie Chan, Les - La Legende de la Main Noire",
    },
    "JAGUAR      BPBJ": {
        'uttd': "BPBJ",
        'title': "Pyuu to Fuku! Jaguar - Byoo to Deru! Megane-kun",
    },
    "JAMES POND 2AJDE": {
        'uttd': "AJDE",
        'title': "James Pond - Codename Robocod",
    },
    "JAMES POND 2AJDP": {
        'uttd': "AJDP",
        'title': "James Pond - Codename Robocod",
    },
    "JAZZJACKRABBAJJE": {
        'uttd': "AJJE",
        'title': "Jazz Jackrabbit",
    },
    "JEDIPOWERBATASWE": {
        'uttd': "ASWE",
        'title': "Star Wars - Jedi Power Battles",
    },
    "JETFUSIONENGBJNE": {
        'uttd': "BJNE",
        'title': "Adventures of Jimmy Neutron, The - Boy Genius - Jet Fusion",
    },
    "JETGRNDRADIOAJRE": {
        'uttd': "AJRE",
        'title': "Jet Grind Radio",
    },
    "JET SET RADIAJRP": {
        'uttd': "AJRP",
        'title': "Jet Set Radio",
    },
    "JIMMY2002AGBAJXE": {
        'uttd': "AJXE",
        'title': "Adventures of Jimmy Neutron vs. Jimmy Negatron, The",
    },
    "JIMMY2GER   AJXD": {
        'uttd': "AJXD",
        'title': "Jimmy Neutron vs. Jimmy Negatron",
    },
    "JIMMYNEUAOTTBJYE": {
        'uttd': "BJYE",
        'title': "Adventures of Jimmy Neutron, The - Boy Genius - Attack of the Twonkies",
    },
    "JIMMYNEUAOTTBJYF": {
        'uttd': "BJYF",
        'title': "Jimmy Neutron - Un Garcon Genial - L'Attaque des Twonkies",
    },
    "JIMMYNEUTR01MJME": {
        'uttd': "MJME",
        'title': "Game Boy Advance Video - The Adventures of Jimmy Neutron - Boy Genius - Volume 1",
    },
    "JIMMY NEUTROAJNX": {
        'uttd': "AJNX",
        'title': "Jimmy Neutron - Boy Genius",
    },
    "JIMMYNEUTRONAJNE": {
        'uttd': "AJNE",
        'title': "Jimmy Neutron - Boy Genius",
    },
    "JINGUJISHIROBT3J": {
        'uttd': "BT3J",
        'title': "Tantei Jinguuji Saburou - Shiroi Kage no Syoujyo",
    },
    "JLH: FLASH  BJHE": {
        'uttd': "BJHE",
        'title': "Justice League Heroes - The Flash",
    },
    "JLH: FLASH  BJHP": {
        'uttd': "BJHP",
        'title': "Justice League Heroes - The Flash",
    },
    "JOERED      BAMJ": {
        'uttd': "BAMJ",
        'title': "Ashita no Joe - Makka ni Moeagare!",
    },
    "JONNYMOSELEYAJME": {
        'uttd': "AJME",
        'title': "Jonny Moseley Mad Trix",
    },
    "JP3ADVANCEDAAJQJ": {
        'uttd': "AJQJ",
        'title': "Jurassic Park III - Advanced Action",
    },
    "JP3DINOATTACAJQP": {
        'uttd': "AJQP",
        'title': "Jurassic Park III - Dino Attack",
    },
    "JP3ISLANDATTAJQE": {
        'uttd': "AJQE",
        'title': "Jurassic Park III - Island Attack",
    },
    "JP3KYORYUNIAAJ3J": {
        'uttd': "AJ3J",
        'title': "Jurassic Park III - Kyouryuu ni Ainiikou!",
    },
    "JP3PARKBUILDAJ3E": {
        'uttd': "AJ3E",
        'title': "Jurassic Park III - Park Builder",
    },
    "JP3PARKBUILDAJ3P": {
        'uttd': "AJ3P",
        'title': "Jurassic Park III - Park Builder",
    },
    "JP3 THE DNA ADNE": {
        'uttd': "ADNE",
        'title': "Jurassic Park III - The DNA Factor",
    },
    "JP3 THE DNA ADNJ": {
        'uttd': "ADNJ",
        'title': "Jurassic Park III - Ushinawareta Idenshi",
    },
    "JP3 THE DNA ADNP": {
        'uttd': "ADNP",
        'title': "Jurassic Park III - The DNA Factor",
    },
    "JPOCKET2    AJ2J": {
        'uttd': "AJ2J",
        'title': "J.League Pocket 2",
    },
    "JPOCKET     AJPJ": {
        'uttd': "AJPJ",
        'title': "J.League Pocket",
    },
    "JUKA        BJKE": {
        'uttd': "BJKE",
        'title': "Juka and the Monophonic Menace",
    },
    "JUKA        BJKP": {
        'uttd': "BJKP",
        'title': "Juka and the Monophonic Menace",
    },
    "JUNGLEBOOK2 AJFP": {
        'uttd': "AJFP",
        'title': "Jungle Book 2, The",
    },
    "JUNGLE BOOK AJFE": {
        'uttd': "AJFE",
        'title': "Jungle Book, The",
    },
    "JURASSICTOURAJ8J": {
        'uttd': "AJ8J",
        'title': "Jurassic Park Institute Tour - Dinosaur Rescue",
    },
    "JUSTICE LEAGBJLE": {
        'uttd': "BJLE",
        'title': "Justice League Chronicles",
    },
    "JUSTIRISER  BGJJ": {
        'uttd': "BGJJ",
        'title': "Genseishin Justirisers - Souchaku! Chikyuu no Senshitachi",
    },
    "JWEA2002    A2JJ": {
        'uttd': "A2JJ",
        'title': "J.League Winning Eleven Advance 2002",
    },
    "K-1POCKE_GP2A2OJ": {
        'uttd': "A2OJ",
        'title': "K-1 Pocket Grand Prix 2",
    },
    "K-1POCKET_GPAKVJ": {
        'uttd': "AKVJ",
        'title': "K-1 Pocket Grand Prix",
    },
    "KABUKUWA    BKKJ": {
        'uttd': "BKKJ",
        'title': "Minna no Shiiku Series - Boku no Kabuto-Kuwagata",
    },
    "KABUTO      AB7J": {
        'uttd': "AB7J",
        'title': "Minna no Shiiku Series 1 - Boku no Kabuto Mushi",
    },
    "KAERU B BACKAKDJ": {
        'uttd': "AKDJ",
        'title': "Kaeru B Back",
    },
    "KAIDAN      BGHJ": {
        'uttd': "BGHJ",
        'title': "Gakkou no Kaidan - Hyakuyobako no Fuuin",
    },
    "KAMAITACHI  AKZJ": {
        'uttd': "AKZJ",
        'title': "Kamaitachi no Yoru Advance",
    },
    "KAOTHEKANGARAKKE": {
        'uttd': "AKKE",
        'title': "Kao the Kangaroo",
    },
    "KAOTHEKANGARAKKP": {
        'uttd': "AKKP",
        'title': "Kao the Kangaroo",
    },
    "KAPPA       BK8J": {
        'uttd': "BK8J",
        'title': "Kappa no Kai-Kata - Katan Daibouken",
    },
    "KARNAAJ     AYKE": {
        'uttd': "AYKE",
        'title': "Karnaaj Rally",
    },
    "KAWAII DOG  AI7J": {
        'uttd': "AI7J",
        'title': "Nakayoshi Pet Advance Series 2 - Kawaii Koinu",
    },
    "KAWAIIKOGATABKIJ": {
        'uttd': "BKIJ",
        'title': "Nakayoshi Pet Advance Series 4 - Kawaii Koinu Mini - Wankoto Asobou!! Kogata Inu",
    },
    "KAWAIIKONEKOAN3J": {
        'uttd': "AN3J",
        'title': "Nakayoshi Pet Advance Series 3 - Kawaii Koneko",
    },
    "KAWANUSHI 34BN4J": {
        'uttd': "BN4J",
        'title': "Kawa no Nushitsuri 3 & 4",
    },
    "KAWANUSI5   AN5J": {
        'uttd': "AN5J",
        'title': "Kawa no Nushi Tsuri 5 - Fushigi no Mori Kara",
    },
    "KCEJDM5EX1  AY5J": {
        'uttd': "AY5J",
        'title': "Yu-Gi-Oh! Duel Monsters 5 Expert 1",
    },
    "KCEJDM6EX2  AY6J": {
        'uttd': "AY6J",
        'title': "Yu-Gi-Oh! Duel Monsters 6 Expert 2",
    },
    "KCEJ MINPRI BMOJ": {
        'uttd': "BMOJ",
        'title': "Minna no Ouji-sama",
    },
    "KCEJ TP2K3B A9LJ": {
        'uttd': "A9LJ",
        'title': "Tennis no Ouji-sama 2003 - Cool Blue",
    },
    "KCEJ TP2K3R A8RJ": {
        'uttd': "A8RJ",
        'title': "Tennis no Ouji-sama 2003 - Passion Red",
    },
    "KCEJ TP2K4G B4GJ": {
        'uttd': "B4GJ",
        'title': "Tennis no Ouji-sama 2004 - Glorious Gold",
    },
    "KCEJ TP2K4S B4SJ": {
        'uttd': "B4SJ",
        'title': "Tennis no Ouji-sama 2004 - Stylish Silver",
    },
    "KCEJ TPRI01 ATIJ": {
        'uttd': "ATIJ",
        'title': "Tennis no Ouji-sama - Genius Boys Academy",
    },
    "KCS ARCADE  AKCE": {
        'uttd': "AKCE",
        'title': "Konami Collector's Series - Arcade Advanced",
    },
    "KCS ARCADE  AKCJ": {
        'uttd': "AKCJ",
        'title': "Konami Arcade Game Collection",
    },
    "KCS ARCADE  AKCP": {
        'uttd': "AKCP",
        'title': "Konami Collector's Series - Arcade Classics",
    },
    "KELLY SLATERAS3E": {
        'uttd': "AS3E",
        'title': "Kelly Slater's Pro Surfer",
    },
    "KERPLUNKTATIBXCE": {
        'uttd': "BXCE",
        'title': "Ker Plunk! - Toss Across - Tip It",
    },
    "KID PADDLE  BYLP": {
        'uttd': "BYLP",
        'title': "Kid Paddle",
    },
    "KIDS CARDS  BCXE": {
        'uttd': "BCXE",
        'title': "Kid's Cards",
    },
    "KIDSNEXTDO01MKDE": {
        'uttd': "MKDE",
        'title': "Game Boy Advance Video - Codename Kids Next Door - Volume 1",
    },
    "KIDSNEXTDOORBNDE": {
        'uttd': "BNDE",
        'title': "Codename Kids Next Door - Operation S.O.D.A.",
    },
    "KIJUTSU     AG2J": {
        'uttd': "AG2J",
        'title': "Kami no Kijutsu - Illusion of the Evil Eyes",
    },
    "KIKIKAIKAIGAAKIJ": {
        'uttd': "AKIJ",
        'title': "Kiki Kaikai Advance",
    },
    "KILLER3DPOOLB3LE": {
        'uttd': "B3LE",
        'title': "Killer 3D Pool",
    },
    "KILLER3DPOOLB3LP": {
        'uttd': "B3LP",
        'title': "Killer 3D Pool",
    },
    "KILLSWITCH  BKHE": {
        'uttd': "BKHE",
        'title': "Kill Switch",
    },
    "KILLSWITCH  BKHP": {
        'uttd': "BKHP",
        'title': "Kill Switch",
    },
    "KIMPOSSIBLE2BKME": {
        'uttd': "BKME",
        'title': "Kim Possible 2 - Drakken's Demise",
    },
    "KIMPOSSIBLE2BKMP": {
        'uttd': "BKMP",
        'title': "Kim Possible 2 - Drakken's Demise",
    },
    "KIMPOSSIBLE3BQPE": {
        'uttd': "BQPE",
        'title': "Kim Possible III - Team Possible",
    },
    "KIM POSSIBLEAEYE": {
        'uttd': "AEYE",
        'title': "Kim Possible - Revenge of Monkey Fist",
    },
    "KIM POSSIBLEAEYP": {
        'uttd': "AEYP",
        'title': "Kim Possible",
    },
    "KIMPOSSIBLE BKMJ": {
        'uttd': "BKMJ",
        'title': "Kim Possible",
    },
    "KINBANGBA2  AK5J": {
        'uttd': "AK5J",
        'title': "Kinniku Banzuke - Kimero! Kiseki no Kanzen Seiha",
    },
    "KINGDOMHEARTB8CE": {
        'uttd': "B8CE",
        'title': "Kingdom Hearts - Chain of Memories",
    },
    "KINGDOMHEARTB8CJ": {
        'uttd': "B8CJ",
        'title': "Kingdom Hearts - Chain of Memories",
    },
    "KINGDOMHEARTB8CP": {
        'uttd': "B8CP",
        'title': "Kingdom Hearts - Chain of Memories",
    },
    "KINGKONG GBABKQE": {
        'uttd': "BKQE",
        'title': "Kong - The 8th Wonder of the World",
    },
    "KINGKONG GBABKQP": {
        'uttd': "BKQP",
        'title': "King Kong - The Official Game of the Movie",
    },
    "KINGOFEXNEOBAKOE": {
        'uttd': "AKOE",
        'title': "King of Fighters EX, The - NeoBlood",
    },
    "KINGOFEXNEOBAKOJ": {
        'uttd': "AKOJ",
        'title': "King of Fighters EX, The - NeoBlood",
    },
    "KINGOFEXNEOBAKOP": {
        'uttd': "AKOP",
        'title': "King of Fighters EX, The - NeoBlood",
    },
    "KING OF FIGHAEXE": {
        'uttd': "AEXE",
        'title': "King of Fighters EX2, The - Howling Blood",
    },
    "KINGOFSWINGEBBKP": {
        'uttd': "BBKP",
        'title': "Donkey Kong - King of Swing",
    },
    "KINNIKU AGB AK4J": {
        'uttd': "AK4J",
        'title': "Kinniku Banzuke - Kongou-kun no Daibouken!",
    },
    "KINNIKUMAN21AK2J": {
        'uttd': "AK2J",
        'title': "Kinnikuman IIsei - Seigi Choujin heno Michi",
    },
    "KISEKAE2    AAJJ": {
        'uttd': "AAJJ",
        'title': "Shin Kisekae Monogatari",
    },
    "KISEKAEANGELBE2J": {
        'uttd': "BE2J",
        'title': "Majokko Cream-chan no Gokko Series 2 - Kisekae Angel",
    },
    "KISSKISS    B2KJ": {
        'uttd': "B2KJ",
        'title': "Kiss x Kiss - Seirei Gakuen",
    },
    "KITARO      BGKJ": {
        'uttd': "BGKJ",
        'title': "Gegege no Kitarou - Kikiippatsu! Youkai Rettou",
    },
    "KITCHENBENTOA8OJ": {
        'uttd': "A8OJ",
        'title': "Dokidoki Cooking Series 2 - Gourmet Kitchen - Suteki na Obentou",
    },
    "KIWAME-MS21 AKMJ": {
        'uttd': "AKMJ",
        'title': "Kiwame Mahjong Deluxe - Mirai Senshi 21",
    },
    "KLAXCOMP    B68E": {
        'uttd': "B68E",
        'title': "Marble Madness - Klax",
    },
    "KLAXMARBLE  B68P": {
        'uttd': "B68P",
        'title': "Marble Madness - Klax",
    },
    "KLONOA2     AN6E": {
        'uttd': "AN6E",
        'title': "Klonoa 2 - Dream Champ Tournament",
    },
    "KLONOA      AKLE": {
        'uttd': "AKLE",
        'title': "Klonoa - Empire of Dreams",
    },
    "KLONOA      AKLJ": {
        'uttd': "AKLJ",
        'title': "Kaze no Klonoa - Yumemiru Teikoku",
    },
    "KLONOA EMPIRAKLP": {
        'uttd': "AKLP",
        'title': "Klonoa - Empire of Dreams",
    },
    "KLONOA G2   AN6J": {
        'uttd': "AN6J",
        'title': "Kaze no Klonoa G2 - Dream Champ Tournament",
    },
    "KLONOAHEROESAK7J": {
        'uttd': "AK7J",
        'title': "Klonoa Heroes - Densetsu no Star Medal",
    },
    "KOALA_BROS  BAKE": {
        'uttd': "BAKE",
        'title': "Koala Brothers - Outback Adventures",
    },
    "KOALA_BROS  BAKP": {
        'uttd': "BAKP",
        'title': "Koala Brothers - Outback Adventures",
    },
    "KOFEX2HOWLINAEXE": {
        'uttd': "AEXE",
        'title': "King of Fighters EX2, The - Howling Blood",
    },
    "KOFEX2HOWLINAEXJ": {
        'uttd': "AEXJ",
        'title': "King of Fighters EX2, The - Howling Blood",
    },
    "KOINUISSYO2 BI2J": {
        'uttd': "BI2J",
        'title': "Koinu to Issho 2",
    },
    "KOINU ISSYO BDIJ": {
        'uttd': "BDIJ",
        'title': "Koinu to Issho - Aijou Monogatari",
    },
    "KONCYUNOMORIBQKJ": {
        'uttd': "BQKJ",
        'title': "Konchuu no Mori no Daibouken",
    },
    "KONG        AKQE": {
        'uttd': "AKQE",
        'title': "Kong - The Animated Series",
    },
    "KONG        AKQP": {
        'uttd': "AKQP",
        'title': "Kong - The Animated Series",
    },
    "KONGATLANTISBK7P": {
        'uttd': "BK7P",
        'title': "Kong - King of Atlantis",
    },
    "KONG:KOA    BK7E": {
        'uttd': "BK7E",
        'title': "Kong - King of Atlantis",
    },
    "KOUMEIDEN   B3QJ": {
        'uttd': "B3QJ",
        'title': "Sangokushi - Koumeiden",
    },
    "KRAZY RACERSAKWE": {
        'uttd': "AKWE",
        'title': "Konami Krazy Racers",
    },
    "KRAZY RACERSAKWP": {
        'uttd': "AKWP",
        'title': "Konami Krazy Racers",
    },
    "KRRCART_AGB BKJJ": {
        'uttd': "BKJJ",
        'title': "Keroro Gunsou - Taiketsu! Keroro Cart de Arimasu!!",
    },
    "K/TMIRACLEFAAKTJ": {
        'uttd': "AKTJ",
        'title': "Hello Kitty Collection - Miracle Fashion Maker",
    },
    "KUNIKORE01  B9AJ": {
        'uttd': "B9AJ",
        'title': "Kunio Kun Nekketsu Collection 1",
    },
    "KUNIKORE02  B9BJ": {
        'uttd': "B9BJ",
        'title': "Kunio Kun Nekketsu Collection 2",
    },
    "KUNIKORE03  B9CJ": {
        'uttd': "B9CJ",
        'title': "Kunio Kun Nekketsu Collection 3",
    },
    "KURESHIN2004BKCJ": {
        'uttd': "BKCJ",
        'title': "Crayon Shin-chan - Arashi wo Yobu Cinema Land no Daibouken!",
    },
    "KURESHIN2004BKCS": {
        'uttd': "BKCS",
        'title': "Shin-chan - Aventuras en Cineland",
    },
    "KURESHIN2006BC2J": {
        'uttd': "BC2J",
        'title': "Crayon Shin-chan - Densetsu wo Yobu Omake no Miyako Shockgaan!",
    },
    "KURESHIN2006BC2S": {
        'uttd': "BC2S",
        'title': "Shin-chan - Contra los Munecos de Shock Gahn",
    },
    "KUROHIGEGOLFAGOJ": {
        'uttd': "AGOJ",
        'title': "Kurohige no Golf Shiyouyo",
    },
    "KURUPARA    A9QJ": {
        'uttd': "A9QJ",
        'title': "Kururin Paradise",
    },
    "KURURIN     AKRJ": {
        'uttd': "AKRJ",
        'title': "Kurukuru Kururin",
    },
    "KURURIN     AKRP": {
        'uttd': "AKRP",
        'title': "Kurukuru Kururin",
    },
    "KUWAGATA    AW7J": {
        'uttd': "AW7J",
        'title': "Minna no Shiiku Series 2 - Boku no Kuwagata",
    },
    "LADY SIA    ALDE": {
        'uttd': "ALDE",
        'title': "Lady Sia",
    },
    "LADY SIA    ALDP": {
        'uttd': "ALDP",
        'title': "Lady Sia",
    },
    "LA FAMILLE DAWLF": {
        'uttd': "AWLF",
        'title': "Famille Delajungle, La - Le Film",
    },
    "LANDBEFORETIALAE": {
        'uttd': "ALAE",
        'title': "Land Before Time, The",
    },
    "LANDBEFORETIALAP": {
        'uttd': "ALAP",
        'title': "Land Before Time, The",
    },
    "LBT_ITMB    BLOE": {
        'uttd': "BLOE",
        'title': "Land Before Time, The - Into the Mysterious Beyond",
    },
    "LBT_ITMB    BLOP": {
        'uttd': "BLOP",
        'title': "Land Before Time, The - Into the Mysterious Beyond",
    },
    "LEGENDS OF WA2LE": {
        'uttd': "A2LE",
        'title': "Legends of Wrestling II",
    },
    "LEGENDZSHIMABLJJ": {
        'uttd': "BLJJ",
        'title': "Rejienzu - Yomigaeru Shiren no Shima",
    },
    "LEGENDZSON__BLVJ": {
        'uttd': "BLVJ",
        'title': "Legendz - Sign of Nekuromu",
    },
    "LEGO BIONICLALBE": {
        'uttd': "ALBE",
        'title': "LEGO Bionicle",
    },
    "LEGO BIONICLALBP": {
        'uttd': "ALBP",
        'title': "LEGO Bionicle",
    },
    "LEGO DROME RAOEE": {
        'uttd': "AOEE",
        'title': "Drome Racers",
    },
    "LEGO ISLAND AL2E": {
        'uttd': "AL2E",
        'title': "LEGO Island 2 - The Brickster's Revenge",
    },
    "LEGO ISLAND AL2P": {
        'uttd': "AL2P",
        'title': "LEGO Island 2 - The Brickster's Revenge",
    },
    "LEGOKK&BB_EGBL5P": {
        'uttd': "BL5P",
        'title': "2 Games in 1 - LEGO Bionicle + LEGO Knights' Kingdom",
    },
    "LEGO_KNIGHTSBKNE": {
        'uttd': "BKNE",
        'title': "LEGO Knights' Kingdom",
    },
    "LEGO_KNIGHTSBKNP": {
        'uttd': "BKNP",
        'title': "LEGO Knights' Kingdom",
    },
    "LEGO RACERS ALRE": {
        'uttd': "ALRE",
        'title': "LEGO Racers 2",
    },
    "LEGO RACERS ALRP": {
        'uttd': "ALRP",
        'title': "LEGO Racers 2",
    },
    "LEGOSTARWARSBLWE": {
        'uttd': "BLWE",
        'title': "LEGO Star Wars - The Video Game",
    },
    "LEGOSTARWARSBLWJ": {
        'uttd': "BLWJ",
        'title': "LEGO Star Wars - The Video Game",
    },
    "LEINSTEINS  BEIE": {
        'uttd': "BEIE",
        'title': "Little Einsteins",
    },
    "LEMONY_ASOUEBLYD": {
        'uttd': "BLYD",
        'title': "Lemony Snicket - Ratselhafte Ereignisse",
    },
    "LEMONY_ASOUEBLYE": {
        'uttd': "BLYE",
        'title': "Lemony Snicket's - A Series of Unfortunate Events",
    },
    "LEMONY_ASOUEBLYI": {
        'uttd': "BLYI",
        'title': "Lemony Snicket - Una Serie di Sfortunati Eventi",
    },
    "LEMONY_ASOUEBLYX": {
        'uttd': "BLYX",
        'title': "Lemony Snicket's - A Series of Unfortunate Events",
    },
    "LETSBASSFISHAZBJ": {
        'uttd': "AZBJ",
        'title': "Bass Tsuri Shiyouze! - Tournament ha Senryaku da!",
    },
    "LET'S RIDEUSB34E": {
        'uttd': "B34E",
        'title': "Let's Ride! Sunshine Stables",
    },
    "LICCA OSHAREBRNJ": {
        'uttd': "BRNJ",
        'title': "Licca-chan no Oshare Nikki",
    },
    "LIFE_ADVANCEAZGJ": {
        'uttd': "AZGJ",
        'title': "Jinsei Game Advance",
    },
    "LILLIPUT    BRPJ": {
        'uttd': "BRPJ",
        'title': "Liliput Oukoku",
    },
    "LILO AND STIALTE": {
        'uttd': "ALTE",
        'title': "Lilo & Stitch",
    },
    "LILO AND STIALTP": {
        'uttd': "ALTP",
        'title': "Lilo & Stitch",
    },
    "LILO & STITCBLQP": {
        'uttd': "BLQP",
        'title': "2 Games in 1 - Peter Pan - Return to Neverland + Lilo & Stitch 2",
    },
    "LILO&STITCH2BLSE": {
        'uttd': "BLSE",
        'title': "Lilo & Stitch 2 - Hamsterviel Havoc",
    },
    "LILO&STITCH BLSJ": {
        'uttd': "BLSJ",
        'title': "Lilo & Stitch",
    },
    "LINK        FLBJ": {
        'uttd': "FLBJ",
        'title': "Famicom Mini Vol. 25 - The Legend of Zelda 2 - Link no Bouken",
    },
    "LIONKING 1.5BLKE": {
        'uttd': "BLKE",
        'title': "Lion King 1.5, The",
    },
    "LIONKING    BLKP": {
        'uttd': "BLKP",
        'title': "Lion King, The",
    },
    "LITLEMERMAIDBN9E": {
        'uttd': "BN9E",
        'title': "Little Mermaid, The - Magic in Two Kingdoms",
    },
    "LITTLEBUSTERALQJ": {
        'uttd': "ALQJ",
        'title': "Little Buster Q",
    },
    "LIZMCGUIRE3 BL3E": {
        'uttd': "BL3E",
        'title': "Lizzie McGuire 3 - Homecoming Havoc",
    },
    "LIZ_PRIN_ENGBLDP": {
        'uttd': "BLDP",
        'title': "2 Games in 1 - Disney Princess + Lizzie McGuire",
    },
    "LIZ_PRIN_SPABLDS": {
        'uttd': "BLDS",
        'title': "2 Games in 1 - Disney Princesas + Lizzie McGuire",
    },
    "LIZZIE 2    BL2E": {
        'uttd': "BL2E",
        'title': "Lizzie McGuire 2 - Lizzie Diaries",
    },
    "LIZZIE 2 SE BL4E": {
        'uttd': "BL4E",
        'title': "Lizzie McGuire 2 - Lizzie Diaries Special Edition",
    },
    "LIZZIEMCGUIRBLME": {
        'uttd': "BLME",
        'title': "Lizzie McGuire - On the Go!",
    },
    "LIZZIEMCGUIRBLMP": {
        'uttd': "BLMP",
        'title': "Lizzie McGuire",
    },
    "LK_AND_DP   BLPP": {
        'uttd': "BLPP",
        'title': "2 Games in 1 - Lion King, The + Disney Princess",
    },
    "LK_AND_DPFREBLPF": {
        'uttd': "BLPF",
        'title': "2 Games in 1 - Roi Lion, Le + Disney Princesse",
    },
    "LK_AND_DPGERBLPD": {
        'uttd': "BLPD",
        'title': "2 Games in 1 - Disneys Konig der Lowen + Disneys Prinzessinnen",
    },
    "LK_AND_DPIT BLPI": {
        'uttd': "BLPI",
        'title': "2 Games in 1 - Disney Principesse + Re Leone, Il",
    },
    "LK_AND_DP_SPBLPS": {
        'uttd': "BLPS",
        'title': "2 Games in 1 - Disney Princesas + Rey Leon, El",
    },
    "LK_&_BB_MULTBLBX": {
        'uttd': "BLBX",
        'title': "2 Games in 1 - Brother Bear + Lion King, The",
    },
    "LLB 2002    ALCE": {
        'uttd': "ALCE",
        'title': "Little League Baseball 2002",
    },
    "LODE RUNNER A39J": {
        'uttd': "A39J",
        'title': "Lode Runner",
    },
    "LOONEYTUNES2BLNE": {
        'uttd': "BLNE",
        'title': "2 Games in 1 - Looney Tunes - Acme Antics + Looney Tunes - Dizzy Driving",
    },
    "LOONEYTUNES2BLNP": {
        'uttd': "BLNP",
        'title': "2 Games in 1 - Looney Tunes - Acme Antics + Looney Tunes - Dizzy Driving",
    },
    "LOONEY TUNESBLTE": {
        'uttd': "BLTE",
        'title': "Looney Tunes - Back in Action",
    },
    "LOSTVIKINGS ALVE": {
        'uttd': "ALVE",
        'title': "Lost Vikings, The",
    },
    "LOVEHINAADVAALHJ": {
        'uttd': "ALHJ",
        'title': "Love Hina Advance - Shukufuku no Kane ha Naru Kana",
    },
    "LSW2GBA     BL7E": {
        'uttd': "BL7E",
        'title': "LEGO Star Wars II - The Original Trilogy",
    },
    "LSW2GBA     BL7P": {
        'uttd': "BL7P",
        'title': "LEGO Star Wars II - The Original Trilogy",
    },
    "LUCKY LUKE WALLP": {
        'uttd': "ALLP",
        'title': "Lucky Luke - Wanted!",
    },
    "LUFIA       AGDE": {
        'uttd': "AGDE",
        'title': "Lufia - The Ruins of Lore",
    },
    "LUNARLANDER B62P": {
        'uttd': "B62P",
        'title': "Millipede - Super Breakout - Lunar Lander",
    },
    "LUNAR LEGENDALNE": {
        'uttd': "ALNE",
        'title': "Lunar Legend",
    },
    "LUNAR LEGENDALNJ": {
        'uttd': "ALNJ",
        'title': "Lunar Legend",
    },
    "LUR2        BYPP": {
        'uttd': "BYPP",
        'title': "Horse & Pony Let's Ride 2",
    },
    "LUR2        BYPX": {
        'uttd': "BYPX",
        'title': "Pippa Funnell 2",
    },
    "LUR2        BYPY": {
        'uttd': "BYPY",
        'title': "Paard & Pony - Paard in Galop!",
    },
    "MADAGASCAR  BGZE": {
        'uttd': "BGZE",
        'title': "Madagascar",
    },
    "MADAGASCAR  BGZI": {
        'uttd': "BGZI",
        'title': "Madagascar",
    },
    "MADAGASCAR  BGZJ": {
        'uttd': "BGZJ",
        'title': "Madagascar",
    },
    "MADAGASCAR  BGZP": {
        'uttd': "BGZP",
        'title': "Madagascar",
    },
    "MADAGASCAR  BGZS": {
        'uttd': "BGZS",
        'title': "Madagascar",
    },
    "MADAGASCAR  BGZX": {
        'uttd': "BGZX",
        'title': "Madagascar",
    },
    "MADDEN 2005 BMFE": {
        'uttd': "BMFE",
        'title': "Madden NFL 2005",
    },
    "MADDEN 2006 B6ME": {
        'uttd': "B6ME",
        'title': "Madden NFL 06",
    },
    "MADDEN 2007 B7ME": {
        'uttd': "B7ME",
        'title': "Madden NFL 07",
    },
    "MADDEN NFL02A2ME": {
        'uttd': "A2ME",
        'title': "Madden NFL 2002",
    },
    "MADDEN NFL03ANJE": {
        'uttd': "ANJE",
        'title': "Madden NFL 2003",
    },
    "MADDEN NFL04BMDE": {
        'uttd': "BMDE",
        'title': "Madden NFL 2004",
    },
    "MADEINWARIO AZWJ": {
        'uttd': "AZWJ",
        'title': "Made in Wario",
    },
    "MAGICAL VACAAMVJ": {
        'uttd': "AMVJ",
        'title': "Magical Vacation",
    },
    "MAGINATION  A2IJ": {
        'uttd': "A2IJ",
        'title': "Magi Nation",
    },
    "MAHJONGKEIJIAMPJ": {
        'uttd': "AMPJ",
        'title': "Mahjong Keiji",
    },
    "MAHOUPUMPKINAWNJ": {
        'uttd': "AWNJ",
        'title': "Mahou no Pumpkin - Ann to Greg no Daibouken",
    },
    "Mail de CuteAMCJ": {
        'uttd': "AMCJ",
        'title': "Mail de Cute",
    },
    "MAJESCOS3IN1BRQE": {
        'uttd': "BRQE",
        'title': "Rec Room Challenge",
    },
    "MAKAIMURA   FMKJ": {
        'uttd': "FMKJ",
        'title': "Famicom Mini Vol. 18 - Makaimura",
    },
    "MANGAKA     ACOJ": {
        'uttd': "ACOJ",
        'title': "Manga-ka Debut Monogatari",
    },
    "MANIC MINER A4MP": {
        'uttd': "A4MP",
        'title': "Manic Miner",
    },
    "MAPPY       FMPJ": {
        'uttd': "FMPJ",
        'title': "Famicom Mini Vol. 08 - Mappy",
    },
    "MARCHP      BQLP": {
        'uttd': "BQLP",
        'title': "March of the Penguins",
    },
    "MARCHPENGUINBQLE": {
        'uttd': "BQLE",
        'title': "March of the Penguins",
    },
    "MARHEAVEN1  BM9J": {
        'uttd': "BM9J",
        'title': "Marheaven - Knockin on Heaven's Door",
    },
    "MARIO BALL  BMVE": {
        'uttd': "BMVE",
        'title': "Mario Pinball Land",
    },
    "MARIO BALL  BMVJ": {
        'uttd': "BMVJ",
        'title': "Super Mario Ball",
    },
    "MARIO BALL  BMVP": {
        'uttd': "BMVP",
        'title': "Super Mario Ball",
    },
    "MARIO BROS. FMBJ": {
        'uttd': "FMBJ",
        'title': "Famicom Mini Vol. 11 - Mario Bros.",
    },
    "MARIOGOLFGBABMGD": {
        'uttd': "BMGD",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGE": {
        'uttd': "BMGE",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGF": {
        'uttd': "BMGF",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGI": {
        'uttd': "BMGI",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGJ": {
        'uttd': "BMGJ",
        'title': "Mario Golf - GBA Tour",
    },
    "MARIOGOLFGBABMGP": {
        'uttd': "BMGP",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGS": {
        'uttd': "BMGS",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIOGOLFGBABMGU": {
        'uttd': "BMGU",
        'title': "Mario Golf - Advance Tour",
    },
    "MARIO KART  AMKE": {
        'uttd': "AMKE",
        'title': "Mario Kart - Super Circuit",
        'icon0': 'https://images.launchbox-app.com/faaa1b52-35d1-4881-85af-1440b0d05721.jpg',
        'pic0': 'https://images.launchbox-app.com/8ec6f272-8882-4fae-9958-7b008b99bb11.png',
        'pic1': 'https://images.launchbox-app.com/750b024b-d5d6-4d73-9b11-14035f70846a.jpg',
        'snd0': 'https://www.youtube.com/watch?v=k29shcWBc8E&list=PL27933B09777F55C7&index=1',
    },
    "MARIO KART  AMKJ": {
        'uttd': "AMKJ",
        'title': "Mario Kart Advance",
        'icon0': 'https://images.launchbox-app.com/0cba0b9e-5604-47dd-925b-a8ebcd29ee25.jpg',
        'pic0': 'https://images.launchbox-app.com/8ec6f272-8882-4fae-9958-7b008b99bb11.png',
        'pic1': 'https://images.launchbox-app.com/750b024b-d5d6-4d73-9b11-14035f70846a.jpg',
        'snd0': 'https://www.youtube.com/watch?v=k29shcWBc8E&list=PL27933B09777F55C7&index=1',
    },
    "MARIO KART  AMKP": {
        'uttd': "AMKP",
        'title': "Mario Kart - Super Circuit",
        'icon0': 'https://images.launchbox-app.com/faaa1b52-35d1-4881-85af-1440b0d05721.jpg',
        'pic0': 'https://images.launchbox-app.com/8ec6f272-8882-4fae-9958-7b008b99bb11.png',
        'pic1': 'https://images.launchbox-app.com/750b024b-d5d6-4d73-9b11-14035f70846a.jpg',
        'snd0': 'https://www.youtube.com/watch?v=k29shcWBc8E&list=PL27933B09777F55C7&index=1',
    },
    "MARIO&LUIGIJA88J": {
        'uttd': "A88J",
        'title': "Mario & Luigi RPG",
        'icon0': 'https://images.launchbox-app.com/a11e4deb-c68a-4b46-b225-d2aa3a846bc5.jpg',
        'pic0': 'https://images.launchbox-app.com/7976c4d6-30d5-4b18-b0b5-6209d844cecb.png',
        'pic1': 'https://images.launchbox-app.com/573d6a31-78f6-479a-96c8-8706364e66b9.jpg',
        'snd0': 'https://www.youtube.com/watch?v=8twTNeB6Hgo&list=PLXQMeRR5llU-_b1wHNCo5w2Lbszy9B6dO&index=1',
    },
    "MARIO&LUIGIPA88P": {
        'uttd': "A88P",
        'title': "Mario & Luigi - Superstar Saga",
        'icon0': 'https://images.launchbox-app.com/70592a60-f531-4473-ad4c-1a2d032a786c.jpg',
        'pic0': 'https://images.launchbox-app.com/7976c4d6-30d5-4b18-b0b5-6209d844cecb.png',
        'pic1': 'https://images.launchbox-app.com/573d6a31-78f6-479a-96c8-8706364e66b9.jpg',
        'snd0': 'https://www.youtube.com/watch?v=8twTNeB6Hgo&list=PLXQMeRR5llU-_b1wHNCo5w2Lbszy9B6dO&index=1',
    },
    "MARIO&LUIGIUA88E": {
        'uttd': "A88E",
        'title': "Mario & Luigi - Superstar Saga",
        'icon0': 'https://images.launchbox-app.com/70592a60-f531-4473-ad4c-1a2d032a786c.jpg',
        'pic0': 'https://images.launchbox-app.com/7976c4d6-30d5-4b18-b0b5-6209d844cecb.png',
        'pic1': 'https://images.launchbox-app.com/573d6a31-78f6-479a-96c8-8706364e66b9.jpg',
        'snd0': 'https://www.youtube.com/watch?v=8twTNeB6Hgo&list=PLXQMeRR5llU-_b1wHNCo5w2Lbszy9B6dO&index=1',
    },
    "MARIOPARTYEUB8MP": {
        'uttd': "B8MP",
        'title': "Mario Party Advance",
    },
    "MARIOPARTYJAB8MJ": {
        'uttd': "B8MJ",
        'title': "Mario Party Advance",
    },
    "MARIOPARTYUSB8ME": {
        'uttd': "B8ME",
        'title': "Mario Party Advance",
    },
    "MARIOTENNISABTME": {
        'uttd': "BTME",
        'title': "Mario Tennis Power Tour",
    },
    "MARIOTENNISABTMJ": {
        'uttd': "BTMJ",
        'title': "Mario Tennis Advance",
    },
    "MARIOTENNISABTMP": {
        'uttd': "BTMP",
        'title': "Mario Power Tennis",
    },
    "MARIOVSDK   BM5E": {
        'uttd': "BM5E",
        'title': "Mario vs. Donkey Kong",
    },
    "MARIOVSDK   BM5J": {
        'uttd': "BM5J",
        'title': "Mario vs. Donkey Kong",
    },
    "MARIOVSDK   BM5P": {
        'uttd': "BM5P",
        'title': "Mario vs. Donkey Kong",
    },
    "MARY KATE ANAKSE": {
        'uttd': "AKSE",
        'title': "Mary-Kate and Ashley - Girls Night Out",
    },
    "MATANTEILOKIBMRJ": {
        'uttd': "BMRJ",
        'title': "Matantei Loki Ragnarok - Gensou no Labyrinth",
    },
    "MATCHBOXMISSBB4E": {
        'uttd': "BB4E",
        'title': "2 Games in 1 - Matchbox Emergency Response + Matchbox Air, Land & Sea Rescue",
    },
    "MATCHBOXMISSBB4P": {
        'uttd': "BB4P",
        'title': "2 Games in 1 - Matchbox Emergency Response + Matchbox Air, Land & Sea Rescue",
    },
    "MAWARUWARIO RZWJ": {
        'uttd': "RZWJ",
        'title': "Mawaru - Made in Wario",
    },
    "MAX2BLUEADV AMHE": {
        'uttd': "AMHE",
        'title': "Bomberman Max 2 - Blue Advance",
    },
    "MAX2-REDADV AMYE": {
        'uttd': "AMYE",
        'title': "Bomberman Max 2 - Red Advance",
    },
    "MAX ADVANCE BMEP": {
        'uttd': "BMEP",
        'title': "Max Payne Advance",
    },
    "MAX PAYNE   BMEE": {
        'uttd': "BMEE",
        'title': "Max Payne",
    },
    "MAYA THE BEEABVP": {
        'uttd': "ABVP",
        'title': "Maya the Bee - The Great Adventure",
    },
    "MAYA THE BEEBEEP": {
        'uttd': "BEEP",
        'title': "Maya the Bee - Sweet Gold",
    },
    "MAZESOFFATE BFQE": {
        'uttd': "BFQE",
        'title': "Mazes of Fate",
    },
    "MB BASEBALL AMBJ": {
        'uttd': "AMBJ",
        'title': "Mobile Pro Yakyuu - Kantoku no Saihai",
    },
    "MBEANZPP    BMBE": {
        'uttd': "BMBE",
        'title': "Mighty Beanz - Pocket Puzzles",
    },
    "MBXCTH      ARQE": {
        'uttd': "ARQE",
        'title': "Matchbox Cross Town Heroes",
    },
    "MBXCTH      ARQP": {
        'uttd': "ARQP",
        'title': "Matchbox Cross Town Heroes",
    },
    "MCRAE RALLY2ACME": {
        'uttd': "ACME",
        'title': "Colin McRae Rally 2.0",
    },
    "MCRAE RALLY2ACMP": {
        'uttd': "ACMP",
        'title': "Colin McRae Rally 2.0",
    },
    "M&D MAGICAL3BM3J": {
        'uttd': "BM3J",
        'title': "Mickey to Donald no Magical Quest 3",
    },
    "M&D MAGICAL3BMQE": {
        'uttd': "BMQE",
        'title': "Magical Quest 3 Starring Mickey & Donald",
    },
    "M&D MAGICAL3BMQP": {
        'uttd': "BMQP",
        'title': "Magical Quest 3 Starring Mickey & Donald",
    },
    "MECH PLATOONAKGE": {
        'uttd': "AKGE",
        'title': "Mech Platoon",
    },
    "MECH PLATOONAKGJ": {
        'uttd': "AKGJ",
        'title': "Kikaika Guntai - Mech Platoon",
    },
    "MECH PLATOONAKGP": {
        'uttd': "AKGP",
        'title': "Mech Platoon",
    },
    "MEDABOTS MTBAK8E": {
        'uttd': "AK8E",
        'title': "Medabots AX - Metabee Version",
    },
    "MEDABOTS_MTBAK8P": {
        'uttd': "AK8P",
        'title': "Medabots AX - Metabee Version",
    },
    "MEDABOTSMTBVA8BE": {
        'uttd': "A8BE",
        'title': "Medabots - Metabee Version",
    },
    "MEDABOTSMTBVA8BP": {
        'uttd': "A8BP",
        'title': "Medabots - Metabee Version",
    },
    "MEDABOTS RKSAK9E": {
        'uttd': "AK9E",
        'title': "Medabots AX - Rokusho Version",
    },
    "MEDABOTS_RKSAK9P": {
        'uttd': "AK9P",
        'title': "Medabots AX - Rokusho Version",
    },
    "MEDABOTSRKSVA9BE": {
        'uttd': "A9BE",
        'title': "Medabots - Rokusho Version",
    },
    "MEDABOTSRKSVA9BP": {
        'uttd': "A9BP",
        'title': "Medabots - Rokusho Version",
    },
    "MEDACOREKBT A5KJ": {
        'uttd': "A5KJ",
        'title': "Medarot Ni Core - Kabuto Version",
    },
    "MEDACOREKWG A5QJ": {
        'uttd': "A5QJ",
        'title': "Medarot Ni Core - Kuwagata Version",
    },
    "MEDALOFHONORAUGE": {
        'uttd': "AUGE",
        'title': "Medal of Honor - Underground",
    },
    "MEDALOFHONORAUGP": {
        'uttd': "AUGP",
        'title': "Medal of Honor - Underground",
    },
    "MEDALOFHONORAUGX": {
        'uttd': "AUGX",
        'title': "Medal of Honor - Underground",
    },
    "MEDAROTGKBT AGHJ": {
        'uttd': "AGHJ",
        'title': "Medarot G - Kabuto Version",
    },
    "MEDAROTGKWG AGIJ": {
        'uttd': "AGIJ",
        'title': "Medarot G - Kuwagata Version",
    },
    "MEDAROTNVKBTANAJ": {
        'uttd': "ANAJ",
        'title': "Medarot Navi - Kabuto",
    },
    "MEDAROTNVKWGAVIJ": {
        'uttd': "AVIJ",
        'title': "Medarot Navi - Kuwagata",
    },
    "MEGA_EXE3_BLA3XE": {
        'uttd': "A3XE",
        'title': "Megaman Battle Network 3 Blue",
    },
    "MEGA_EXE3_BLA3XP": {
        'uttd': "A3XP",
        'title': "Megaman Battle Network 3 Blue",
    },
    "MEGA_EXE3_WHA6BE": {
        'uttd': "A6BE",
        'title': "Megaman Battle Network 3 White",
    },
    "MEGA_EXE3_WHA6BP": {
        'uttd': "A6BP",
        'title': "Megaman Battle Network 3 White",
    },
    "MEGAMAN5_TC_BRKE": {
        'uttd': "BRKE",
        'title': "Megaman Battle Network 5 - Team Colonel",
    },
    "MEGAMAN5_TC_BRKP": {
        'uttd': "BRKP",
        'title': "Megaman Battle Network 5 - Team Colonel",
    },
    "MEGAMAN5_TP_BRBE": {
        'uttd': "BRBE",
        'title': "Megaman Battle Network 5 - Team Protoman",
    },
    "MEGAMAN5_TP_BRBP": {
        'uttd': "BRBP",
        'title': "Megaman Battle Network 5 - Team Protoman",
    },
    "MEGAMAN6_FXXBR6E": {
        'uttd': "BR6E",
        'title': "Megaman Battle Network 6 - Cybeast Falzar",
    },
    "MEGAMAN6_FXXBR6P": {
        'uttd': "BR6P",
        'title': "Megaman Battle Network 6 - Cybeast Falzar",
    },
    "MEGAMAN6_GXXBR5E": {
        'uttd': "BR5E",
        'title': "Megaman Battle Network 6 - Cybeast Gregar",
    },
    "MEGAMAN6_GXXBR5P": {
        'uttd': "BR5P",
        'title': "Megaman Battle Network 6 - Cybeast Gregar",
    },
    "MEGAMAN&BASSA6ME": {
        'uttd': "A6ME",
        'title': "Megaman & Bass",
    },
    "MEGAMAN&BASSA6MP": {
        'uttd': "A6MP",
        'title': "Megaman & Bass",
    },
    "MEGAMANBN2  AM2P": {
        'uttd': "AM2P",
        'title': "Megaman Battle Network 2",
    },
    "MEGAMANBN4BMB4BE": {
        'uttd': "B4BE",
        'title': "Megaman Battle Network 4 - Blue Moon",
    },
    "MEGAMANBN4RSB4WE": {
        'uttd': "B4WE",
        'title': "Megaman Battle Network 4 - Red Sun",
    },
    "MEGAMAN_BN  AREE": {
        'uttd': "AREE",
        'title': "Megaman Battle Network",
    },
    "MEGAMAN_EXE2AE2E": {
        'uttd': "AE2E",
        'title': "Megaman Battle Network 2",
    },
    "MEGAMANEXEBNAREP": {
        'uttd': "AREP",
        'title': "Megaman Battle Network",
    },
    "MEGAMANZERO2A62E": {
        'uttd': "A62E",
        'title': "Megaman Zero 2",
    },
    "MEGAMANZERO2A62P": {
        'uttd': "A62P",
        'title': "Megaman Zero 2",
    },
    "MEGAMANZERO3BZ3E": {
        'uttd': "BZ3E",
        'title': "Megaman Zero 3",
    },
    "MEGAMANZERO3BZ3P": {
        'uttd': "BZ3P",
        'title': "Megaman Zero 3",
    },
    "MEGAMANZERO4B4ZE": {
        'uttd': "B4ZE",
        'title': "Megaman Zero 4",
    },
    "MEGAMANZERO4B4ZP": {
        'uttd': "B4ZP",
        'title': "Megaman Zero 4",
    },
    "MEGAMAN ZEROAZCE": {
        'uttd': "AZCE",
        'title': "Megaman Zero",
    },
    "MEINELIEBE  AYMJ": {
        'uttd': "AYMJ",
        'title': "Tanbi Musou - Meine Liebe",
    },
    "MEIN GESTUETBHUP": {
        'uttd': "BHUP",
        'title': "Horse And Pony - My Stud Farm",
    },
    "MEIN PFERD  BEFP": {
        'uttd': "BEFP",
        'title': "Best Friends - My Horse",
    },
    "MEN IN BLACKAMIP": {
        'uttd': "AMIP",
        'title': "Men in Black - The Series",
    },
    "MESIA       BDLJ": {
        'uttd': "BDLJ",
        'title': "Shin Megami Tensei Devil Children - Messiah Riser",
    },
    "METALGUN    AAPJ": {
        'uttd': "AAPJ",
        'title': "Metalgun Slinger",
    },
    "METALMAX2KAIA9TJ": {
        'uttd': "A9TJ",
        'title': "Metal Max 2 Kai",
    },
    "METAL SLUG  BSME": {
        'uttd': "BSME",
        'title': "Metal Slug Advance",
        'icon0': 'https://images.launchbox-app.com/5211fca7-d0dc-4c53-9dda-f2fd7a5309f6.jpg',
        'pic0': 'https://images.launchbox-app.com/e9a2f52c-25b4-4184-8ef0-0e3785d4d1ce.png',
        'pic1': 'https://images.launchbox-app.com/158d45de-507b-4124-9917-a4c90d6cca91.jpg',
    },
    "METFUSIONCHNAMTC": {
        'uttd': "AMTC",
        'title': "Miteluode Ronghe",
    },
    "METROID4EUR AMTP": {
        'uttd': "AMTP",
        'title': "Metroid Fusion",
        'icon0': 'https://images.launchbox-app.com/0f4e70dc-3a84-4ac5-86a9-f47f5399c04e.jpg',
        'pic0': 'https://images.launchbox-app.com/86d2ae66-c545-425d-9145-d72e3bba4d6f.png',
        'pic1': 'https://images.launchbox-app.com/6e710e66-3704-409d-ba78-6e78b4b0bcb5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=L-TE2h_XB4w&list=PL71442F24C8795CD7&index=1',
    },
    "METROID4JPN AMTJ": {
        'uttd': "AMTJ",
        'title': "Metroid Fusion",
        'icon0': 'https://images.launchbox-app.com/0f4e70dc-3a84-4ac5-86a9-f47f5399c04e.jpg',
        'pic0': 'https://images.launchbox-app.com/86d2ae66-c545-425d-9145-d72e3bba4d6f.png',
        'pic1': 'https://images.launchbox-app.com/6e710e66-3704-409d-ba78-6e78b4b0bcb5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=L-TE2h_XB4w&list=PL71442F24C8795CD7&index=1',
    },
    "METROID4USA AMTE": {
        'uttd': "AMTE",
        'title': "Metroid Fusion",
        'icon0': 'https://images.launchbox-app.com/0f4e70dc-3a84-4ac5-86a9-f47f5399c04e.jpg',
        'pic0': 'https://images.launchbox-app.com/86d2ae66-c545-425d-9145-d72e3bba4d6f.png',
        'pic1': 'https://images.launchbox-app.com/6e710e66-3704-409d-ba78-6e78b4b0bcb5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=L-TE2h_XB4w&list=PL71442F24C8795CD7&index=1',
    },
    "MEZA_KOUSIENBMKJ": {
        'uttd': "BMKJ",
        'title': "Mezase Koushien",
    },
    "MGAH        AM3E": {
        'uttd': "AM3E",
        'title': "Midway's Greatest Arcade Hits",
    },
    "M HOUSHIN   AJOJ": {
        'uttd': "AJOJ",
        'title': "Magical Houshin",
    },
    "MH PRO2 AGB AH2E": {
        'uttd': "AH2E",
        'title': "Mat Hoffman's Pro BMX 2",
    },
    "MH PRO BMX  AHOE": {
        'uttd': "AHOE",
        'title': "Mat Hoffman's Pro BMX",
    },
    "MH PRO BMX  AHOX": {
        'uttd': "AHOX",
        'title': "Mat Hoffman's Pro BMX",
    },
    "MIBTHESERIESAMIE": {
        'uttd': "AMIE",
        'title': "Men in Black - The Series",
    },
    "MIC&MIN MA  A3ME": {
        'uttd': "A3ME",
        'title': "Magical Quest Starring Mickey & Minnie",
    },
    "MIC&MIN MA  A3MJ": {
        'uttd': "A3MJ",
        'title': "Mickey to Minnie no Magical Quest",
    },
    "MIC&MIN MA  A3MP": {
        'uttd': "A3MP",
        'title': "Magical Quest Starring Mickey & Minnie",
    },
    "MICRO MACHINAXZP": {
        'uttd': "AXZP",
        'title': "Micro Machines",
    },
    "MIDNIGHTCLUBAMQE": {
        'uttd': "AMQE",
        'title': "Midnight Club - Street Racing",
    },
    "MIDNIGHTCLUBAMQP": {
        'uttd': "AMQP",
        'title': "Midnight Club - Street Racing",
    },
    "MIJNMANEGEDUBPVY": {
        'uttd': "BPVY",
        'title': "Paard & Pony - Mijn Manege",
    },
    "MILLIPEDECOMB62E": {
        'uttd': "B62E",
        'title': "Millipede - Super Breakout - Lunar Lander",
    },
    "MIMPOSSIBLE AIHE": {
        'uttd': "AIHE",
        'title': "Mission Impossible - Operation Surma",
    },
    "MINIMONIAGB AOHJ": {
        'uttd': "AOHJ",
        'title': "Minimoni - Onegai Ohoshi-sama!",
    },
    "MINIMONI    AHCJ": {
        'uttd': "AHCJ",
        'title': "Minimoni - Mika no Happy Morning Chatty",
    },
    "MIN_MAHJONGGBMJJ": {
        'uttd': "BMJJ",
        'title': "Minna no Soft Series - Minna no Mahjong",
    },
    "MINNADE PUYOAPYJ": {
        'uttd': "APYJ",
        'title': "Minna de Puyo Puyo",
    },
    "MINORITY REPARME": {
        'uttd': "ARME",
        'title': "Minority Report - Everybody Runs",
    },
    "MIRUMODEPON2BMPJ": {
        'uttd': "BMPJ",
        'title': "Wagamama Fairy Mirumo de Pon! - Taisen Mahoudama",
    },
    "MIRUMODEPON3BMYJ": {
        'uttd': "BMYJ",
        'title': "Wagamama Fairy Mirumo de Pon! - 8 Nin no Toki no Yousei",
    },
    "MIRUMODEPON4BWFJ": {
        'uttd': "BWFJ",
        'title': "Wagamama Fairy Mirumo de Pon! - Yume no Kakera",
    },
    "MIRUMODEPON5BWPJ": {
        'uttd': "BWPJ",
        'title': "Wagamama Fairy Mirumo de Pon! - Nazo no Kagi to Shinjitsu no Tobir",
    },
    "MIRUMODEPON6BMIJ": {
        'uttd': "BMIJ",
        'title': "Wagamama Fairy Mirumo de Pon! - Dokidoki Memorial Panic",
    },
    "MIRUMODEPON!AWKJ": {
        'uttd': "AWKJ",
        'title': "Wagamama Fairy Mirumo de Pon! - Ougon Maracas no Densetsu",
    },
    "MISSION IMPOAIHP": {
        'uttd': "AIHP",
        'title': "Mission Impossible - Operation Surma",
    },
    "MISTER NUTZ AZRP": {
        'uttd': "AZRP",
        'title': "Mr. Nutz",
    },
    "MK_ADVANCE  AM5E": {
        'uttd': "AM5E",
        'title': "Mortal Kombat Advance",
    },
    "MKALLIANCE  AXDE": {
        'uttd': "AXDE",
        'title': "Mortal Kombat - Deadly Alliance",
    },
    "MKALLIANCE  AXDP": {
        'uttd': "AXDP",
        'title': "Mortal Kombat - Deadly Alliance",
    },
    "MKASWEET16  AAYE": {
        'uttd': "AAYE",
        'title': "Mary-Kate and Ashley Sweet 16 - Licensed to Drive",
    },
    "MKTOURNAMENTAW4E": {
        'uttd': "AW4E",
        'title': "Mortal Kombat - Tournament Edition",
    },
    "MLB 2K7     B2YE": {
        'uttd': "B2YE",
        'title': "2K Sports - Major League Baseball 2K7",
    },
    "M.M.4 F.CARDAA4J": {
        'uttd': "AA4J",
        'title': "Monster Maker 4 - Flash Card",
    },
    "M.M.4 K.DICEAA5J": {
        'uttd': "AA5J",
        'title': "Monster Maker 4 - Killer Dice",
    },
    "MM ADVANCE  AMRE": {
        'uttd': "AMRE",
        'title': "Motocross Maniacs Advance",
    },
    "MM ADVANCE  AMRJ": {
        'uttd': "AMRJ",
        'title': "Motocross Maniacs Advance",
    },
    "MM ADVANCE  AMRP": {
        'uttd': "AMRP",
        'title': "Maniac Racers Advance",
    },
    "MMBLAST     AMLE": {
        'uttd': "AMLE",
        'title': "M&M's Blast!",
    },
    "M&M MAGICAL2A29J": {
        'uttd': "A29J",
        'title': "Mickey to Minnie no Magical Quest 2",
    },
    "M&M MAGICAL2AQME": {
        'uttd': "AQME",
        'title': "Magical Quest 2 Starring Mickey & Minnie",
    },
    "M&M MAGICAL2AQMP": {
        'uttd': "AQMP",
        'title': "Magical Quest 2 Starring Mickey & Minnie",
    },
    "MMSBREAKEM  BEME": {
        'uttd': "BEME",
        'title': "M&M's Break' Em",
    },
    "MOERO JALECOBJCJ": {
        'uttd': "BJCJ",
        'title': "Moero!! Jaleco Collection",
    },
    "MOJIPITTAN  A8MJ": {
        'uttd': "A8MJ",
        'title': "Kotoba no Puzzle - Mojipittan Advance",
    },
    "MOMO MATSURIAMMJ": {
        'uttd': "AMMJ",
        'title': "Momotarou Matsuri",
    },
    "MOMOTETSU-G BM2J": {
        'uttd': "BM2J",
        'title': "Momotarou Densetsu G - Gold Deck wo Tsukure!",
    },
    "MONKEYBALLJRALUE": {
        'uttd': "ALUE",
        'title': "Super Monkey Ball Jr.",
    },
    "MONOPOLY    BUME": {
        'uttd': "BUME",
        'title': "Monopoly",
    },
    "MONOPOLY    BUMP": {
        'uttd': "BUMP",
        'title': "Monopoly",
    },
    "MONSNEMO_DUTBDZH": {
        'uttd': "BDZH",
        'title': "2 Games in 1 - Monsters en Co. + Finding Nemo",
    },
    "MONSRANCHERAAMFE": {
        'uttd': "AMFE",
        'title': "Monster Rancher Advance",
    },
    "MONSTER BASSA4BE": {
        'uttd': "A4BE",
        'title': "Monster! Bass Fishing",
    },
    "MONSTER BASSA4BP": {
        'uttd': "A4BP",
        'title': "Monster! Bass Fishing",
    },
    "MONSTERFARM2A2QJ": {
        'uttd': "A2QJ",
        'title': "Monster Farm Advance 2",
    },
    "MONSTERFARMAAMFJ": {
        'uttd': "AMFJ",
        'title': "Monster Farm Advance",
    },
    "MONSTERFORCEAM8E": {
        'uttd': "AM8E",
        'title': "Monster Force",
    },
    "MONSTERFORCEAM8P": {
        'uttd': "AM8P",
        'title': "Monster Force",
    },
    "MONSTERGATE1ANFJ": {
        'uttd': "ANFJ",
        'title': "Monster Gate",
    },
    "MONSTERGATE2A6GJ": {
        'uttd': "A6GJ",
        'title': "Monster Gate - Ooinaru Dungeon - Fuuin no Orb",
    },
    "MONSTERGUARDAMNJ": {
        'uttd': "AMNJ",
        'title': "Monster Guardians",
    },
    "MONSTERHOUSEBQ7E": {
        'uttd': "BQ7E",
        'title': "Monster House",
    },
    "MONSTERHOUSEBQ7P": {
        'uttd': "BQ7P",
        'title': "Monster House",
    },
    "MONSTERHOUSEBQ7X": {
        'uttd': "BQ7X",
        'title': "Monster House",
    },
    "MONSTER JAM AJAE": {
        'uttd': "AJAE",
        'title': "Monster Jam - Maximum Destruction",
    },
    "MONSTER JAM AJAP": {
        'uttd': "AJAP",
        'title': "Monster Jam - Maximum Destruction",
    },
    "MONSTERRANC2A2QE": {
        'uttd': "A2QE",
        'title': "Monster Rancher Advance 2",
    },
    "MONSTERS,INCAMXE": {
        'uttd': "AMXE",
        'title': "Monsters, Inc.",
    },
    "MONSTERS,INCAMXJ": {
        'uttd': "AMXJ",
        'title': "Monsters, Inc.",
    },
    "MONSTERS INCAMXX": {
        'uttd': "AMXX",
        'title': "Monsters, Inc.",
    },
    "MONSTERS INCAMXY": {
        'uttd': "AMXY",
        'title': "Monsters, Inc.",
    },
    "MONSTERTRUCKBMCE": {
        'uttd': "BMCE",
        'title': "Monster Trucks",
    },
    "MONSTERTRUCKBYME": {
        'uttd': "BYME",
        'title': "Monster Trucks Mayhem",
    },
    "MONSTERTRUCKBYMP": {
        'uttd': "BYMP",
        'title': "Monster Trucks Mayhem",
    },
    "MONT_NEMO   BDZE": {
        'uttd': "BDZE",
        'title': "2 Games in 1 - Monsters, Inc. + Finding Nemo",
    },
    "MONT_NEMO   BDZP": {
        'uttd': "BDZP",
        'title': "2 Games in 1 - Monsters, Inc. + Finding Nemo",
    },
    "MOORHEN 3   AU3P": {
        'uttd': "AU3P",
        'title': "Moorhen 3 - The Chicken Chase!",
    },
    "MORITASHOGI AMSJ": {
        'uttd': "AMSJ",
        'title': "Morita Shougi Advance",
    },
    "MORTAL KOMBAAM5P": {
        'uttd': "AM5P",
        'title': "Mortal Kombat Advance",
    },
    "MOTHER12    A2UJ": {
        'uttd': "A2UJ",
        'title': "Mother 1+2",
    },
    "MOTHER3     A3UJ": {
        'uttd': "A3UJ",
        'title': "Mother 3",
    },
    "MOTOGP      AM4E": {
        'uttd': "AM4E",
        'title': "Moto GP",
    },
    "MOTOGP      AM4J": {
        'uttd': "AM4J",
        'title': "Moto GP",
    },
    "MOTOGP      AM4P": {
        'uttd': "AM4P",
        'title': "Moto GP",
    },
    "MOTORACERADVA9MP": {
        'uttd': "A9MP",
        'title': "Motoracer Advance",
    },
    "MOUSE TRAP  B3OE": {
        'uttd': "B3OE",
        'title': "Mouse Trap - Simon - Operation",
    },
    "MP3PLAYER   ZMDE": {
        'uttd': "ZMDE",
        'title': "Nintendo MP3 Player",
    },
    "MR ADVANCE  A9ME": {
        'uttd': "A9ME",
        'title': "Motoracer Advance",
    },
    "MR. DRILLER2AD2J": {
        'uttd': "AD2J",
        'title': "Mr. Driller 2",
    },
    "MR. DRILLER2AD2P": {
        'uttd': "AD2P",
        'title': "Mr. Driller 2",
    },
    "MR. DRILLER2BR2E": {
        'uttd': "BR2E",
        'title': "Mr. Driller 2",
    },
    "MR.DRILLER AAD5J": {
        'uttd': "AD5J",
        'title': "Mr. Driller A - Fushigi na Pacteria",
    },
    "MR INCREDIBLBICJ": {
        'uttd': "BICJ",
        'title': "Mr. Incredible",
    },
    "MR.I UM     BIQJ": {
        'uttd': "BIQJ",
        'title': "Mr. Incredible - Kyouteki Under Minor Toujyou",
    },
    "MSPAC-MANMM BPCE": {
        'uttd': "BPCE",
        'title': "Ms. Pac-Man - Maze Madness",
    },
    "MSPAC-MANMM BPCP": {
        'uttd': "BPCP",
        'title': "Ms. Pac-Man - Maze Madness",
    },
    "MSS SHANGHAIBSHJ": {
        'uttd': "BSHJ",
        'title': "Minna no Soft Series - Shanghai",
    },
    "MSSTETRISADVBTTJ": {
        'uttd': "BTTJ",
        'title': "Tetris Advance",
    },
    "M.SUMMONER  A3NJ": {
        'uttd': "A3NJ",
        'title': "Monster Summoner",
    },
    "MTM         BMTE": {
        'uttd': "BMTE",
        'title': "Monster Truck Madness",
    },
    "MTR         BRHE": {
        'uttd': "BRHE",
        'title': "Meet the Robinsons",
    },
    "MTR         BRHP": {
        'uttd': "BRHP",
        'title': "Meet the Robinsons",
    },
    "MUCHA_LUCHA_BMLE": {
        'uttd': "BMLE",
        'title': "Mucha Lucha! - Mascaritas of the Lost Code",
    },
    "MUGENBORG   AG6J": {
        'uttd': "AG6J",
        'title': "Mugenborg",
    },
    "MUNCH       BODD": {
        'uttd': "BODD",
        'title': "Oddworld - Munch's Oddysee",
    },
    "MUNCH       BODE": {
        'uttd': "BODE",
        'title': "Oddworld - Munch's Oddysee",
    },
    "MUPPET PINBAAMWE": {
        'uttd': "AMWE",
        'title': "Muppet Pinball Mayhem",
    },
    "MUPPET PINBAAMWP": {
        'uttd': "AMWP",
        'title': "Muppet Pinball Mayhem",
    },
    "MUPPETS SHOWAZME": {
        'uttd': "AZME",
        'title': "Muppets, The - On With the Show!",
    },
    "MURASAME    FNMJ": {
        'uttd': "FNMJ",
        'title': "Famicom Mini Vol. 22 - Nazo no Murasame Jou",
    },
    "MUSHIKING GCBK6J": {
        'uttd': "BK6J",
        'title': "Konchu Ouja - Mushiking",
    },
    "MUTSU       AMUJ": {
        'uttd': "AMUJ",
        'title': "Mutsu - Water Looper Mutsu",
    },
    "MV1 ALLIANCEB4ME": {
        'uttd': "B4ME",
        'title': "Marvel - Ultimate Alliance",
    },
    "MV1 ALLIANCEB4MP": {
        'uttd': "B4MP",
        'title': "Marvel - Ultimate Alliance",
    },
    "MX 2002     A2XE": {
        'uttd': "A2XE",
        'title': "MX 2002 featuring Ricky Carmichael",
    },
    "MYLITTLEPONYBL6E": {
        'uttd': "BL6E",
        'title': "My Little Pony - Crystal Princess - The Runaway Rainbow",
    },
    "NAKAYOSHI-KRAKPJ": {
        'uttd': "AKPJ",
        'title': "Nakayoshi Mahjong - Kaburiichi",
    },
    "NAMCO 50    B5NE": {
        'uttd': "B5NE",
        'title': "Namco Museum 50th Anniversary",
    },
    "NAMCO 50    B5NP": {
        'uttd': "B5NP",
        'title': "Namco Museum 50th Anniversary",
    },
    "NAMCOMUSEUM ANME": {
        'uttd': "ANME",
        'title': "Namco Museum",
    },
    "NAMCOMUSEUM ANMJ": {
        'uttd': "ANMJ",
        'title': "Namco Museum",
    },
    "NAMCOMUSEUM ANMP": {
        'uttd': "ANMP",
        'title': "Namco Museum",
    },
    "NANCYDREWMHMANDE": {
        'uttd': "ANDE",
        'title': "Nancy Drew - Message in a Haunted Mansion",
    },
    "NANPURE     BUOJ": {
        'uttd': "BUOJ",
        'title': "Minna no Soft Series - Numpla Advance",
    },
    "NAPOLEON    ANPJ": {
        'uttd': "ANPJ",
        'title': "Napoleon",
    },
    "NAPOLEON F  ANPF": {
        'uttd': "ANPF",
        'title': "Aigle de Guerre, L'",
    },
    "NARIKIRI2   AN9J": {
        'uttd': "AN9J",
        'title': "Tales of the World - Narikiri Dungeon 2",
    },
    "NARNIA LWW  B2WE": {
        'uttd': "B2WE",
        'title': "Chronicles of Narnia, The - The Lion, the Witch and the Wardrobe",
    },
    "NARUTO ACT1 A7AJ": {
        'uttd': "A7AJ",
        'title': "Naruto - Ninjutsu Zenkai! Saikyou Ninja Daikesshuu",
    },
    "NARUTO ACT2 BN2J": {
        'uttd': "BN2J",
        'title': "Naruto - Saikyou Ninja Daikesshuu 2",
    },
    "NARUTOKONOHAAUEJ": {
        'uttd': "AUEJ",
        'title': "Naruto - Konoha Senki",
    },
    "NARUTORPG   BNRJ": {
        'uttd': "BNRJ",
        'title': "Naruto RPG - Uketsugareshi Hi no Ishi",
    },
    "NARUTO US1  A7AE": {
        'uttd': "A7AE",
        'title': "Naruto - Ninja Council",
    },
    "NARUTO US2  BN2E": {
        'uttd': "BN2E",
        'title': "Naruto - Ninja Council 2",
    },
    "NASCAR HEAT ANHE": {
        'uttd': "ANHE",
        'title': "NASCAR Heat 2002",
    },
    "NA-SU       BPNJ": {
        'uttd': "BPNJ",
        'title': "Pikapika Nurse Monogatari - Nurse Ikusei Game",
    },
    "NATURAL2 DUOAN2J": {
        'uttd': "AN2J",
        'title': "Natural 2 - Duo",
    },
    "NBA JAM 2002ABNE": {
        'uttd': "ABNE",
        'title': "NBA Jam 2002",
    },
    "NEEDFORSPEEDAZFE": {
        'uttd': "AZFE",
        'title': "Need for Speed - Porsche Unleashed",
    },
    "NEEDFORSPEEDAZFP": {
        'uttd': "AZFP",
        'title': "Need for Speed - Porsche Unleashed",
    },
    "NEGIMAGI2   BNMJ": {
        'uttd': "BNMJ",
        'title': "Mahou Sensei Negima! - Private Lesson 2 Ojamashimasuu Parasite de Chu",
    },
    "NEGIMAGI    BNGJ": {
        'uttd': "BNGJ",
        'title': "Mahou Sensei Negima! - Private Lesson Damedesuu Toshokanjima",
    },
    "NEMO2INCPACKBNEE": {
        'uttd': "BNEE",
        'title': "2 Games in 1 - Finding Nemo - The Continuing Adventures + Incredibles, The",
    },
    "NEMOINCREDIBBIND": {
        'uttd': "BIND",
        'title': "2 Games in 1 - Findet Nemo + Unglaublichen, Die",
    },
    "NEMOINCREDIBBINP": {
        'uttd': "BINP",
        'title': "2 Games in 1 - Finding Nemo + Incredibles, The",
    },
    "NEMOINCREDIBBINX": {
        'uttd': "BINX",
        'title': "2 Games in 1 - Finding Nemo + Incredibles, The",
    },
    "NEMOINCREDIBBINY": {
        'uttd': "BINY",
        'title': "2 Games in 1 - Finding Nemo + Incredibles, The",
    },
    "NEMOINCREDIBBINZ": {
        'uttd': "BINZ",
        'title': "2 Games in 1 - Buscando a Nemo + Increibles, Los",
    },
    "NEMO_MON_FREBDZF": {
        'uttd': "BDZF",
        'title': "2 Games in 1 - Monstres & Cie + Le Monde de Nemo",
    },
    "NEMO_MON_ITABDZI": {
        'uttd': "BDZI",
        'title': "2 Games in 1 - Monsters & Co. + Alla Ricerca di Nemo",
    },
    "NEMO&MONSGERBDZD": {
        'uttd': "BDZD",
        'title': "2 Games in 1 - Monster AG, Die + Findet Nemo",
    },
    "NEMO_MON_SPABDZS": {
        'uttd': "BDZS",
        'title': "2 Games in 1 - Monstruos, S.A. + Buscando a Nemo",
    },
    "NEMO NEMO2  BFWP": {
        'uttd': "BFWP",
        'title': "2 Games in 1 - Finding Nemo + Finding Nemo - The Continuing Adventures",
    },
    "NEMO NEMO2  BFWX": {
        'uttd': "BFWX",
        'title': "2 Games in 1 - Finding Nemo + Finding Nemo - The Continuing Adventures",
    },
    "NEMO NEMO2  BFWY": {
        'uttd': "BFWY",
        'title': "2 Games in 1 - Findet Nemo + Findet Nemo - Das Abenteuer Geht Weiter",
    },
    "NEMO NEMO2  BFWZ": {
        'uttd': "BFWZ",
        'title': "2 Games in 1 - Finding Nemo + Finding Nemo - The Continuing Adventures",
    },
    "NES METROID FMRE": {
        'uttd': "FMRE",
        'title': "Classic NES Series - Metroid",
    },
    "NES ZELDA 2 FLBE": {
        'uttd': "FLBE",
        'title': "Classic NES Series - Zelda II - The Adventure of Link",
    },
    "NETSAL      ANVJ": {
        'uttd': "ANVJ",
        'title': "Shiren Monsters Netsal",
    },
    "NFLBLITZ2002ABZE": {
        'uttd': "ABZE",
        'title': "NFL Blitz 20-02",
    },
    "NFL BLITZ2K3ANKE": {
        'uttd': "ANKE",
        'title': "NFL Blitz 20-03",
    },
    "NFS CARBON  BN7E": {
        'uttd': "BN7E",
        'title': "Need for Speed Carbon - Own the City",
    },
    "NFSMW       BNWE": {
        'uttd': "BNWE",
        'title': "Need for Speed - Most Wanted",
    },
    "NFSUG2      BNFE": {
        'uttd': "BNFE",
        'title': "Need for Speed - Underground 2",
    },
    "NFSUG       BNSE": {
        'uttd': "BNSE",
        'title': "Need for Speed - Underground",
    },
    "NGT / ROLANDATXP": {
        'uttd': "ATXP",
        'title': "Next Generation Tennis",
    },
    "NHL 2002    ANLE": {
        'uttd': "ANLE",
        'title': "NHL 2002",
    },
    "NHL HITZ 20 AN4E": {
        'uttd': "AN4E",
        'title': "NHL Hitz 20-03",
    },
    "NICKELODEON BI7E": {
        'uttd': "BI7E",
        'title': "Nickelodeon Vol. 1 GBA 4-Pack",
    },
    "NICKTOONS003MN3E": {
        'uttd': "MN3E",
        'title': "Game Boy Advance Video - Nicktoons - Volume 3",
    },
    "NICKTOONS 01MNCE": {
        'uttd': "MNCE",
        'title': "Game Boy Advance Video - Nicktoon's Collection - Volume 1",
    },
    "NICKTOONS 02MN2E": {
        'uttd': "MN2E",
        'title': "Game Boy Advance Video - Nicktoon's Collection - Volume 2",
    },
    "NICKTOONS   BCCE": {
        'uttd': "BCCE",
        'title': "Nicktoons - Freeze Frame Frenzy",
    },
    "NICKTOONS   BCCX": {
        'uttd': "BCCX",
        'title': "SpongeBob SquarePants and Friends - Freeze Frame Frenzy",
    },
    "NICKTOONSBVIBNVE": {
        'uttd': "BNVE",
        'title': "Nicktoons - Battle for Volcano Island",
    },
    "NICKTOONS RAANQP": {
        'uttd': "ANQP",
        'title': "Nicktoons Racing",
    },
    "NICKTOONSRACANQE": {
        'uttd': "ANQE",
        'title': "Nicktoons Racing",
    },
    "NICKTOONSUNIBNUE": {
        'uttd': "BNUE",
        'title': "Nicktoons Unite!",
    },
    "NIGHTFIRE   A7OE": {
        'uttd': "A7OE",
        'title': "007 - NightFire",
    },
    "NIGHTMARE   BNCE": {
        'uttd': "BNCE",
        'title': "Tim Burton's Nightmare Before Christmas, The - The Pumpkin King",
    },
    "NIGHTMARE   BNCJ": {
        'uttd': "BNCJ",
        'title': "Tim Burton's Nightmare Before Christmas, The - The Pumpkin King",
    },
    "NINJA COP   ANXP": {
        'uttd': "ANXP",
        'title': "Ninja Cop",
    },
    "NINJA FIVE 0ANXE": {
        'uttd': "ANXE",
        'title': "Ninja Five-0",
    },
    "NITRO KART  BCNE": {
        'uttd': "BCNE",
        'title': "Crash Nitro Kart",
    },
    "NITRO KART  BCNJ": {
        'uttd': "BCNJ",
        'title': "Crash Bandicoot - Bakusou! Nitro Cart",
    },
    "NITRO KART  BCNP": {
        'uttd': "BCNP",
        'title': "Crash Nitro Kart",
    },
    "NOBUNAGA    ANBJ": {
        'uttd': "ANBJ",
        'title': "Nobunaga no Yabou",
    },
    "NOBUNAGAIBUNANOJ": {
        'uttd': "ANOJ",
        'title': "Nobunaga Ibun",
    },
    "NODDYTOYLANDBNKE": {
        'uttd': "BNKE",
        'title': "Noddy - A Day in Toyland",
    },
    "NODDYTOYLANDBNKP": {
        'uttd': "BNKP",
        'title': "Noddy - A Day in Toyland",
    },
    "NYANNYANKO01BNYJ": {
        'uttd': "BNYJ",
        'title': "Nyan Nyan Nyanko no Nyan Collection",
    },
    "OCHAKEN     BDRJ": {
        'uttd': "BDRJ",
        'title': "Ochaken no Heya",
    },
    "OCHAKENDREAMBCUJ": {
        'uttd': "BCUJ",
        'title': "Ochaken no Yumebouken",
    },
    "OCHAKENISLANBO2J": {
        'uttd': "BO2J",
        'title': "Ochainu no Bouken Jima - Honwaka Yume no Island",
    },
    "OCHAKURU    BIKJ": {
        'uttd': "BIKJ",
        'title': "Ochaken Kururin - Honwaka Puzzle de Hotto Shiyo",
    },
    "ODDPARENTS  BFOE": {
        'uttd': "BFOE",
        'title': "Fairly Odd Parents!, The - Clash with the Anti-World",
    },
    "ODDPARENTS  BFOP": {
        'uttd': "BFOP",
        'title': "Fairly Odd Parents!, The - Clash with the Anti-World",
    },
    "O_INKOCLUB  AICJ": {
        'uttd': "AICJ",
        'title': "Oshaberi Inko Club",
    },
    "OJARUGEKKO  BOJJ": {
        'uttd': "BOJJ",
        'title': "Ojarumaru - Gekkouchou Sanpo de Ojaru",
    },
    "OKUMAN 01   AOKJ": {
        'uttd': "AOKJ",
        'title': "Okumanchouja Game - Nottori Daisakusen!",
    },
    "ONEPIEBASEBAB08J": {
        'uttd': "B08J",
        'title': "One Piece - Going Baseball",
    },
    "ONEPIEBASEBABO8K": {
        'uttd': "BO8K",
        'title': "One Piece - Going Baseball - Haejeok Yaku",
    },
    "ONEPIECE    BONE": {
        'uttd': "BONE",
        'title': "One Piece",
    },
    "ONEPIECEKINGAUSJ": {
        'uttd': "AUSJ",
        'title': "From TV Animation One Piece - Mezase! King of Berry",
    },
    "ONIGASHIMA  FFMJ": {
        'uttd': "FFMJ",
        'title': "Famicom Mini Vol. 26 - Famicom Mukashi Banashi - Shin Onigashima - Zen Kou Hen",
    },
    "ONITAC1     A6OJ": {
        'uttd': "A6OJ",
        'title': "Onimusha Tactics",
    },
    "ONITAC1EU   A6OP": {
        'uttd': "A6OP",
        'title': "Onimusha Tactics",
    },
    "ONITAC1US   A6OE": {
        'uttd': "A6OE",
        'title': "Onimusha Tactics",
    },
    "ONMYOU ZERO BITJ": {
        'uttd': "BITJ",
        'title': "Onmyou Taisenki Zeroshiki",
    },
    "ONPI7TSUJIMAAO7J": {
        'uttd': "AO7J",
        'title': "From TV Animation One Piece - Nanatsu Shima no Daihihou",
    },
    "ONPI7TSUJIMAAO7K": {
        'uttd': "AO7K",
        'title': "One Piece - Ilgop Seomui Daebomul",
    },
    "OPEN SEASON BOAE": {
        'uttd': "BOAE",
        'title': "Open Season",
    },
    "OPEN SEASON BOAP": {
        'uttd': "BOAP",
        'title': "Open Season",
    },
    "OPEN SEASON BOAX": {
        'uttd': "BOAX",
        'title': "Open Season",
    },
    "OPERATION ALBAAE": {
        'uttd': "BAAE",
        'title': "Operation Armored Liberty",
    },
    "ORBITAL     BVEJ": {
        'uttd': "BVEJ",
        'title': "bit Generations - Orbital",
    },
    "ORIENTALBLUEAORJ": {
        'uttd': "AORJ",
        'title': "Oriental Blue - Ao no Tengai",
    },
    "OSANPO      BISJ": {
        'uttd': "BISJ",
        'title': "Koinu-Chan no Hajimete no Osanpo - Koinu no Kokoro Ikusei Game",
    },
    "OSHAREWANKO A5SJ": {
        'uttd': "A5SJ",
        'title': "Oshare Wanko",
    },
    "OSYARE PRI2 AO2J": {
        'uttd': "AO2J",
        'title': "Oshare Princess 2",
    },
    "OSYARE PRI3 BO3J": {
        'uttd': "BO3J",
        'title': "Oshare Princess 3",
    },
    "OSYARE PRI4 BOPJ": {
        'uttd': "BOPJ",
        'title': "Twin Series 2 - Oshare Princess 4 + Sweet Life",
    },
    "OSYARE PRI5 BO5J": {
        'uttd': "BO5J",
        'title': "Oshare Princess 5",
    },
    "OSYARE PRI  AOPJ": {
        'uttd': "AOPJ",
        'title': "Oshare Princess",
    },
    "OTTIFANTEN PBOFD": {
        'uttd': "BOFD",
        'title': "Ottifanten Pinball",
    },
    "OugonTaiyo_AAGSJ": {
        'uttd': "AGSJ",
        'title': "Ougon no Taiyou - Hirakareshi Fuuin",
    },
    "OUGONTAIYO_BAGFJ": {
        'uttd': "AGFJ",
        'title': "Ougon no Taiyou - Ushinawareshi Toki",
    },
    "OUKOKUGAISUTAECJ": {
        'uttd': "AECJ",
        'title': "Samurai Evolution - Oukoku Geist",
    },
    "OVER THE HEDBH5E": {
        'uttd': "BH5E",
        'title': "Over the Hedge",
    },
    "OVERTHEHEDGEBH5D": {
        'uttd': "BH5D",
        'title': "Ab Durch Die Hecke",
    },
    "OVERTHEHEDGEBH5F": {
        'uttd': "BH5F",
        'title': "Nos Voisins - Les Hommes",
    },
    "OVERTHEHEDGEBH5H": {
        'uttd': "BH5H",
        'title': "Over the Hedge - Beesten bij de Buren",
    },
    "OVERTHEHEDGEBH5I": {
        'uttd': "BH5I",
        'title': "Gang del Bosco, La",
    },
    "OVERTHEHEDGEBH5P": {
        'uttd': "BH5P",
        'title': "Over the Hedge",
    },
    "OVERTHEHEDGEBH5S": {
        'uttd': "BH5S",
        'title': "Vecinos Invasores",
    },
    "OZZY&DRIX   BOZE": {
        'uttd': "BOZE",
        'title': "Ozzy & Drix",
    },
    "PACMANCOLLE APCE": {
        'uttd': "APCE",
        'title': "Pac-Man Collection",
    },
    "PACMANCOLLE APCJ": {
        'uttd': "APCJ",
        'title': "Pac-Man Collection",
    },
    "PACMANCOLLE APCP": {
        'uttd': "APCP",
        'title': "Pac-Man Collection",
    },
    "PAC-MAN     FP7E": {
        'uttd': "FP7E",
        'title': "Classic NES Series - Pac-Man",
    },
    "PAC-MAN     FPMJ": {
        'uttd': "FPMJ",
        'title': "Famicom Mini Vol. 06 - Pac-Man",
    },
    "PAC-MANWORLDBPAE": {
        'uttd': "BPAE",
        'title': "Pac-Man World",
    },
    "PAC-MANWORLDBPAP": {
        'uttd': "BPAP",
        'title': "Pac-Man World",
    },
    "PAC PINBALL BP8E": {
        'uttd': "BP8E",
        'title': "Pac-Man Pinball Advance",
    },
    "PAC PINBALL BP8P": {
        'uttd': "BP8P",
        'title': "Pac-Man Pinball Advance",
    },
    "PAC WORLD 2 B2CE": {
        'uttd': "B2CE",
        'title': "Pac-Man World 2",
    },
    "PAC WORLD 2 B2CP": {
        'uttd': "B2CP",
        'title': "Pac-Man World 2",
    },
    "PANDORATOMORBSLP": {
        'uttd': "BSLP",
        'title': "Tom Clancy's Splinter Cell - Pandora Tomorrow",
    },
    "PANZOU      B3IJ": {
        'uttd': "B3IJ",
        'title': "Miracle! Banzou - 7 Tsuno Hosh no Kaizokuno",
    },
    "PAPERBOYCOMPB6BE": {
        'uttd': "B6BE",
        'title': "Paperboy - Rampage",
    },
    "PAPERBOYRAMPB6BP": {
        'uttd': "B6BP",
        'title': "Paperboy - Rampage",
    },
    "PARTHENA    FPTJ": {
        'uttd': "FPTJ",
        'title': "Famicom Mini Vol. 24 - Hikari Shinwa - Palthena no Kagami",
    },
    "PAWAPOKE1&2 B8PJ": {
        'uttd': "B8PJ",
        'title': "Power Pro Kun Pocket 1+2",
    },
    "PAWAPOKE3   AP3J": {
        'uttd': "AP3J",
        'title': "Power Pro Kun Pocket 3",
    },
    "PAWAPOKE4   AP4J": {
        'uttd': "AP4J",
        'title': "Power Pro Kun Pocket 4",
    },
    "PAWAPOKE5   A5PJ": {
        'uttd': "A5PJ",
        'title': "Power Pro Kun Pocket 5",
    },
    "PAWAPOKE6   BP6J": {
        'uttd': "BP6J",
        'title': "Power Pro Kun Pocket 6",
    },
    "PAWAPOKE7   BP7J": {
        'uttd': "BP7J",
        'title': "Power Pro Kun Pocket 7",
    },
    "PAWAPOKED1  BBQJ": {
        'uttd': "BBQJ",
        'title': "Pawa Poke Dash",
    },
    "PAWSANDCLAWSBURE": {
        'uttd': "BURE",
        'title': "Paws & Claws - Pet Resort",
    },
    "PAYBACK     BPKP": {
        'uttd': "BPKP",
        'title': "Payback",
    },
    "PAZ TANTEI  AEHJ": {
        'uttd': "AEHJ",
        'title': "Puzzle & Tantei Collection",
    },
    "PAZUNINN    BPZJ": {
        'uttd': "BPZJ",
        'title': "Pazunin - Uminin no Puzzle de Nimu",
    },
    "PBDRBYSTLON A8PJ": {
        'uttd': "A8PJ",
        'title': "Derby Stallion Advance",
    },
    "PDA4AGB     PDA1": {
        'uttd': "PDA1",
        'title': "Personal Data Assistant for Game Boy Advance",
    },
    "PENGUINS    BM7E": {
        'uttd': "BM7E",
        'title': "Madagascar - Operation Penguin",
    },
    "PENGUINS    BM7P": {
        'uttd': "BM7P",
        'title': "Madagascar - Operation Penguin",
    },
    "PENGUINS    BM7S": {
        'uttd': "BM7S",
        'title': "Madagascar - Operacion Pinguino",
    },
    "PENGUINS    BM7X": {
        'uttd': "BM7X",
        'title': "Madagascar - Operation Penguin",
    },
    "PENGUINS    BM7Y": {
        'uttd': "BM7Y",
        'title': "Madagascar - Operation Penguin",
    },
    "PENNY RACERSAQAP": {
        'uttd': "AQAP",
        'title': "Penny Racers",
    },
    "PETER PAN   BPTE": {
        'uttd': "BPTE",
        'title': "Peter Pan - The Motion Picture Event",
    },
    "PETER PAN   BPTP": {
        'uttd': "BPTP",
        'title': "Peter Pan - The Motion Picture Event",
    },
    "PETERPAN RTNAPPE": {
        'uttd': "APPE",
        'title': "Peter Pan - Return to Neverland",
    },
    "PETERPAN RTNAPPP": {
        'uttd': "APPP",
        'title': "Peter Pan - Return to Neverland",
    },
    "PET GALLERY2BKPJ": {
        'uttd': "BKPJ",
        'title': "Kawaii Pet Game Gallery 2",
    },
    "PET GALLERY BKGJ": {
        'uttd': "BKGJ",
        'title': "Kawaii Pet Game Gallery",
    },
    "PETSHOP3    A63J": {
        'uttd': "A63J",
        'title': "Kawaii Pet Shop Monogatari 3",
    },
    "PETZVET     BNBE": {
        'uttd': "BNBE",
        'title': "Petz Vet",
    },
    "PFERDEHOFEURBPVP": {
        'uttd': "BPVP",
        'title': "Pferd & Pony - Mein Pferdehof",
    },
    "PHALANX     APXE": {
        'uttd': "APXE",
        'title': "Phalanx - The Enforce Fighter A-144",
    },
    "PHALANX     APXJ": {
        'uttd': "APXJ",
        'title': "Phalanx - The Enforce Fighter A-144",
    },
    "PHALANX     APXP": {
        'uttd': "APXP",
        'title': "Phalanx - The Enforce Fighter A-144",
    },
    "PHANTASIA   AN8E": {
        'uttd': "AN8E",
        'title': "Tales of Phantasia",
    },
    "PHANTASIA   AN8J": {
        'uttd': "AN8J",
        'title': "Tales of Phantasia",
    },
    "PHANTASIA   AN8P": {
        'uttd': "AN8P",
        'title': "Tales of Phantasia",
    },
    "PHANTASY STAAYCP": {
        'uttd': "AYCP",
        'title': "Phantasy Star Collection",
    },
    "PHANTASYSTARAYCE": {
        'uttd': "AYCE",
        'title': "Phantasy Star Collection",
    },
    "PHILOFUTURE BFXE": {
        'uttd': "BFXE",
        'title': "Phil of the Future",
    },
    "PIA33       BP3J": {
        'uttd': "BP3J",
        'title': "Pia Carrot he Youkoso!! 3.3",
    },
    "PICHIPICHI00BMAJ": {
        'uttd': "BMAJ",
        'title': "Mermaid Melody - Pichi Pichi Pitch",
    },
    "PICHIPICHI02B3MJ": {
        'uttd': "B3MJ",
        'title': "Mermaid Melody - Pichi Pichi Picchi Pichi Pichitto Live Start",
    },
    "PICHIPICHI2 BM8J": {
        'uttd': "BM8J",
        'title': "Mermaid Melody - Pichipichi Pitch Pichipichi Party",
    },
    "PIGLET'SGAMEA9NE": {
        'uttd': "A9NE",
        'title': "Piglet's Big Game",
    },
    "PIGLET'SGAMEA9NX": {
        'uttd': "A9NX",
        'title': "Piglet's Big Game",
    },
    "PINBALL ADV APZP": {
        'uttd': "APZP",
        'title': "Pinball Advance",
    },
    "PINBALL CHALAPLP": {
        'uttd': "APLP",
        'title': "Pinball Challenge Deluxe",
    },
    "PINBALL DEADAPDE": {
        'uttd': "APDE",
        'title': "Pinball of the Dead, The",
    },
    "PINBALL DEADAZOJ": {
        'uttd': "AZOJ",
        'title': "Pinball of the Dead, The",
    },
    "PINBALL OF TAPDP": {
        'uttd': "APDP",
        'title': "Pinball of the Dead, The",
    },
    "PINBALL TYCNA2TE": {
        'uttd': "A2TE",
        'title': "Pinball Tycoon",
    },
    "PINBALL TYCNA2TP": {
        'uttd': "A2TP",
        'title': "Pinball Tycoon",
    },
    "PINKEY TOWN APNJ": {
        'uttd': "APNJ",
        'title': "Pinky Monkey Town",
    },
    "PINK PANTHERAP7P": {
        'uttd': "AP7P",
        'title': "Pink Panther - Pinkadelic Pursuit",
    },
    "PINK PANTHERAPEE": {
        'uttd': "APEE",
        'title': "Pink Panther - Pinkadelic Pursuit",
    },
    "PINKY&BRAIN APIP": {
        'uttd': "APIP",
        'title': "Pinky and the Brain - The Masterplan",
    },
    "PINOBEE     APBE": {
        'uttd': "APBE",
        'title': "Pinobee - Wings of Adventure",
    },
    "PINOBEE     APBJ": {
        'uttd': "APBJ",
        'title': "Pinobee no Daibouken",
    },
    "PINO & PHOE AP6J": {
        'uttd': "AP6J",
        'title': "Pinobee & Phoebee",
    },
    "PIRATESCARIBA8QE": {
        'uttd': "A8QE",
        'title': "Pirates of the Caribbean - The Curse of the Black Pearl",
    },
    "PIRATESCARIBA8QP": {
        'uttd': "A8QP",
        'title': "Pirates of the Caribbean - The Curse of the Black Pearl",
    },
    "PIRATESDMC  B8QE": {
        'uttd': "B8QE",
        'title': "Pirates of the Caribbean - Dead Man's Chest",
    },
    "PITFALL     APFE": {
        'uttd': "APFE",
        'title': "Pitfall - The Mayan Adventure",
    },
    "PITFALL     BPHE": {
        'uttd': "BPHE",
        'title': "Pitfall - The Lost Expedition",
    },
    "PITFALL     BPHF": {
        'uttd': "BPHF",
        'title': "Pitfall - L'Expedition Perdue",
    },
    "PITFALL     BPHP": {
        'uttd': "BPHP",
        'title': "Pitfall - The Lost Expedition",
    },
    "PLANET MNSTRAPME": {
        'uttd': "APME",
        'title': "Planet Monsters",
    },
    "PLANET MNSTRAPMP": {
        'uttd': "APMP",
        'title': "Planet Monsters",
    },
    "PLANETOFAPESAYNE": {
        'uttd': "AYNE",
        'title': "Planet of the Apes",
    },
    "PLANETOFAPESAYNP": {
        'uttd': "AYNP",
        'title': "Planet of the Apes",
    },
    "PLAYAN      ZMAJ": {
        'uttd': "ZMAJ",
        'title': "Playan AV Player",
    },
    "PLAYYANMICROZMBJ": {
        'uttd': "ZMBJ",
        'title': "Playan Micro",
    },
    "PLUSTER RACEA2PJ": {
        'uttd': "A2PJ",
        'title': "Bouken Yuuki Pluster World - Pluston GP",
    },
    "PLUSTER RPG2BPDJ": {
        'uttd': "BPDJ",
        'title': "Bouken Yuuki Pluster World - Densetsu no Plust Gate EX",
    },
    "PLUSTER RPG APJJ": {
        'uttd': "APJJ",
        'title': "Bouken Yuuki Pluster World - Densetsu no Plust Gate",
    },
    "PMWANDMPMMM B6PE": {
        'uttd': "B6PE",
        'title': "2 Games in 1 - Pac-Man World + Ms. Pac-Man - Maze Madness",
    },
    "PMWANDMPMMM B6PP": {
        'uttd': "B6PP",
        'title': "2 Games in 1 - Pac-Man World + Ms. Pac-Man - Maze Madness",
    },
    "PNATASHASSAPBNPE": {
        'uttd': "BNPE",
        'title': "Princess Natasha",
    },
    "POCKETDOGS  BTDE": {
        'uttd': "BTDE",
        'title': "Pocket Dogs",
    },
    "POCKET MUSICAP9P": {
        'uttd': "AP9P",
        'title': "Pocket Music",
    },
    "POCKETRESORTBM4J": {
        'uttd': "BM4J",
        'title': "Mickey no Pocket Resort",
    },
    "POCKY-ROCKY APKE": {
        'uttd': "APKE",
        'title': "Pocky & Rocky with Becky",
    },
    "POKE DUNGEONB24E": {
        'uttd': "B24E",
        'title': "Pokemon Mystery Dungeon - Red Rescue Team",
    },
    "POKE DUNGEONB24J": {
        'uttd': "B24J",
        'title': "Pokemon Fushigi no Dungeon - Aka no Kyuujotai",
    },
    "POKE DUNGEONB24P": {
        'uttd': "B24P",
        'title': "Pokemon Mystery Dungeon - Red Rescue Team",
    },
    "POKEGBAVID01MPAE": {
        'uttd': "MPAE",
        'title': "Game Boy Advance Video - Pokemon - Volume 1",
    },
    "POKEGBAVID02MPBE": {
        'uttd': "MPBE",
        'title': "Game Boy Advance Video - Pokemon - Volume 2",
    },
    "POKEGBAVID03MPCE": {
        'uttd': "MPCE",
        'title': "Game Boy Advance Video - Pokemon - Volume 3",
    },
    "POKEGBAVID04MPDE": {
        'uttd': "MPDE",
        'title': "Game Boy Advance Video - Pokemon - Volume 4",
    },
    "POKEINU     BTDJ": {
        'uttd': "BTDJ",
        'title': "Poke Inu - Poket Dogs",
    },
    "POKEMON EMERBPED": {
        'uttd': "BPED",
        'title': "Pokemon - Smaragd-Edition",
        'icon0': 'https://images.launchbox-app.com/76544f7b-a881-4a4a-83ec-721b9bdef3c1.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON EMERBPEE": {
        'uttd': "BPEE",
        'title': "Pokemon - Emerald Version",
        'icon0': 'https://images.launchbox-app.com/76544f7b-a881-4a4a-83ec-721b9bdef3c1.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON EMERBPEF": {
        'uttd': "BPEF",
        'title': "Pokemon - Version Emeraude",
        'icon0': 'https://images.launchbox-app.com/76544f7b-a881-4a4a-83ec-721b9bdef3c1.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON EMERBPEI": {
        'uttd': "BPEI",
        'title': "Pokemon - Versione Smeraldo",
        'icon0': 'https://images.launchbox-app.com/76544f7b-a881-4a4a-83ec-721b9bdef3c1.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON EMERBPEJ": {
        'uttd': "BPEJ",
        'title': "Pocket Monsters - Emerald",
        'icon0': 'https://images.launchbox-app.com/12d8ee3e-3c80-4548-8d2e-ed3161fe3ed5.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON EMERBPES": {
        'uttd': "BPES",
        'title': "Pokemon - Edicion Esmeralda",
        'icon0': 'https://images.launchbox-app.com/76544f7b-a881-4a4a-83ec-721b9bdef3c1.jpg',
        'pic0': 'https://images.launchbox-app.com/d7ede79c-0ad1-4ffc-bc0f-20008d86d16f.png',
        'pic1': 'https://images.launchbox-app.com/ea68934a-f38d-49be-b8d3-b4f10304a927.jpg',
        'snd0': 'https://www.youtube.com/watch?v=yNJ66qzmDks&list=PL22604C8CC8FCB417&index=1',
    },
    "POKEMON FIREBPRD": {
        'uttd': "BPRD",
        'title': "Pokemon - Feuerrote Edition",
    },
    "POKEMON FIREBPRE": {
        'uttd': "BPRE",
        'title': "Pokemon - Fire Red Version",
    },
    "POKEMON FIREBPRF": {
        'uttd': "BPRF",
        'title': "Pokemon - Version Rouge Feu",
    },
    "POKEMON FIREBPRI": {
        'uttd': "BPRI",
        'title': "Pokemon - Versione Rosso Fuoco",
    },
    "POKEMON FIREBPRJ": {
        'uttd': "BPRJ",
        'title': "Pocket Monsters - FireRed",
    },
    "POKEMON FIREBPRS": {
        'uttd': "BPRS",
        'title': "Pokemon - Edicion Rojo Fuego",
    },
    "POKEMON LEAFBPGD": {
        'uttd': "BPGD",
        'title': "Pokemon - Blattgrune Edition",
    },
    "POKEMON LEAFBPGE": {
        'uttd': "BPGE",
        'title': "Pokemon - Leaf Green Version",
    },
    "POKEMON LEAFBPGF": {
        'uttd': "BPGF",
        'title': "Pokemon - Version Vert Feuille",
    },
    "POKEMON LEAFBPGI": {
        'uttd': "BPGI",
        'title': "Pokemon - Versione Verde Foglia",
    },
    "POKEMON LEAFBPGJ": {
        'uttd': "BPGJ",
        'title': "Pocket Monsters - LeafGreen",
    },
    "POKEMON LEAFBPGS": {
        'uttd': "BPGS",
        'title': "Pokemon - Edicion Verde Hoja",
    },
    "POKEMON RUBYAXVD": {
        'uttd': "AXVD",
        'title': "Pokemon - Rubin-Edition",
        'icon0': 'https://images.launchbox-app.com/c10d1bcb-3446-448b-8cf5-4b1df49eb394.png',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON RUBYAXVE": {
        'uttd': "AXVE",
        'title': "Pokemon - Ruby Version",
        'icon0': 'https://images.launchbox-app.com/c10d1bcb-3446-448b-8cf5-4b1df49eb394.png',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON RUBYAXVF": {
        'uttd': "AXVF",
        'title': "Pokemon - Version Rubis",
        'icon0': 'https://images.launchbox-app.com/c10d1bcb-3446-448b-8cf5-4b1df49eb394.png',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON RUBYAXVI": {
        'uttd': "AXVI",
        'title': "Pokemon - Versione Rubino",
        'icon0': 'https://images.launchbox-app.com/c10d1bcb-3446-448b-8cf5-4b1df49eb394.png',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON RUBYAXVJ": {
        'uttd': "AXVJ",
        'title': "Pocket Monsters - Ruby",
        'icon0': 'https://images.launchbox-app.com/adeb5ca1-a43e-41a1-8f5f-3be54b56c012.jpg',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON RUBYAXVS": {
        'uttd': "AXVS",
        'title': "Pokemon - Edicion Rubi",
        'icon0': 'https://images.launchbox-app.com/c10d1bcb-3446-448b-8cf5-4b1df49eb394.png',
        'pic0': 'https://images.launchbox-app.com/06551353-2456-4601-a9ad-23e927abe628.png',
        'pic1': 'https://images.launchbox-app.com/1d82df1e-481a-4163-ba5f-41356d4895b5.jpg',
        'snd0': 'https://www.youtube.com/watch?v=C9rEeGWK0pQ&list=PLEiOTsktKIotvaMzRhqvCsT7PHbm67nsq&index=1',
    },
    "POKEMON SAPPAXPD": {
        'uttd': "AXPD",
        'title': "Pokemon - Saphir-Edition",
    },
    "POKEMON SAPPAXPE": {
        'uttd': "AXPE",
        'title': "Pokemon - Sapphire Version",
    },
    "POKEMON SAPPAXPF": {
        'uttd': "AXPF",
        'title': "Pokemon - Version Saphir",
    },
    "POKEMON SAPPAXPI": {
        'uttd': "AXPI",
        'title': "Pokemon - Versione Zaffiro",
    },
    "POKEMON SAPPAXPJ": {
        'uttd': "AXPJ",
        'title': "Pocket Monsters - Sapphire",
    },
    "POKEMON SAPPAXPS": {
        'uttd': "AXPS",
        'title': "Pokemon - Edicion Zafiro",
    },
    "POKEPIN R/S BPPE": {
        'uttd': "BPPE",
        'title': "Pokemon Pinball - Ruby & Sapphire",
        'icon0': 'https://images.launchbox-app.com/ac9df2f2-7820-4769-bd5f-0338a5193da5.jpg',
        'pic0': 'https://images.launchbox-app.com/8d6075de-0871-43e9-9c8c-2ec26f12db32.png',
        'pic1': 'https://images.launchbox-app.com/19c9e387-4e85-40f1-b0b2-7869cba3f3eb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=S3pOGfFVits&list=PLUXEBUs17WcRIF9kz-yAq-T2TenT0ei8U&index=1',
    },
    "POKEPIN R/S BPPJ": {
        'uttd': "BPPJ",
        'title': "Pokemon Pinball - Ruby & Sapphire",
        'icon0': 'https://images.launchbox-app.com/8f306af2-99e4-413b-9f68-ac3e489e34e0.jpg',
        'pic0': 'https://images.launchbox-app.com/8d6075de-0871-43e9-9c8c-2ec26f12db32.png',
        'pic1': 'https://images.launchbox-app.com/19c9e387-4e85-40f1-b0b2-7869cba3f3eb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=S3pOGfFVits&list=PLUXEBUs17WcRIF9kz-yAq-T2TenT0ei8U&index=1',
    },
    "POKEPIN R/S BPPP": {
        'uttd': "BPPP",
        'title': "Pokemon Pinball - Ruby & Sapphire",
        'icon0': 'https://images.launchbox-app.com/ac9df2f2-7820-4769-bd5f-0338a5193da5.jpg',
        'pic0': 'https://images.launchbox-app.com/8d6075de-0871-43e9-9c8c-2ec26f12db32.png',
        'pic1': 'https://images.launchbox-app.com/19c9e387-4e85-40f1-b0b2-7869cba3f3eb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=S3pOGfFVits&list=PLUXEBUs17WcRIF9kz-yAq-T2TenT0ei8U&index=1',
    },
    "POLAREXPRESSBPXE": {
        'uttd': "BPXE",
        'title': "Polar Express, The",
    },
    "POLARIUMGBA BIIE": {
        'uttd': "BIIE",
        'title': "Polarium Advance",
    },
    "POLARIUMGBA BIIP": {
        'uttd': "BIIP",
        'title': "Polarium Advance",
    },
    "POLLY POCKETAOTE": {
        'uttd': "AOTE",
        'title': "Polly Pocket! - Super Splash Island",
    },
    "POLLY POCKETAOTP": {
        'uttd': "AOTP",
        'title': "Polly Pocket! - Super Splash Island",
    },
    "POLLY POCKETB3FE": {
        'uttd': "B3FE",
        'title': "Polly Pocket! - Super Splash Island",
    },
    "POLLY POCKETB3FP": {
        'uttd': "B3FP",
        'title': "Polly Pocket! - Super Splash Island",
    },
    "PONGCOMP    B64E": {
        'uttd': "B64E",
        'title': "Pong - Asteroids - Yars' Revenge",
    },
    "POPEYE RFS  APOE": {
        'uttd': "APOE",
        'title': "Popeye - Rush for Spinach",
    },
    "POPIDOL     BIDD": {
        'uttd': "BIDD",
        'title': "Deutschland sucht den Superstar",
    },
    "POPIDOL     BIDE": {
        'uttd': "BIDE",
        'title': "American Idol",
    },
    "POPIDOL     BIDP": {
        'uttd': "BIDP",
        'title': "Pop Idol",
    },
    "POP&LARA    B2QP": {
        'uttd': "B2QP",
        'title': "2 Games in 1 - Prince of Persia - The Sands of Time + Tomb Raider - The Prophecy",
    },
    "POSTMAN PAT BROP": {
        'uttd': "BROP",
        'title': "Postman Pat and the Greendale Rocket",
    },
    "POTTER G.O.FBH8E": {
        'uttd': "BH8E",
        'title': "Harry Potter and the Goblet of Fire",
    },
    "POWER RANGERBPOX": {
        'uttd': "BPOX",
        'title': "Power Rangers - Dino Thunder",
    },
    "PPG HIM N SEAP5E": {
        'uttd': "AP5E",
        'title': "Powerpuff Girls, The - Him and Seek",
    },
    "PPG HIMNSEEKAP5P": {
        'uttd': "AP5P",
        'title': "Powerpuff Girls, The - Him and Seek",
    },
    "PPG MOJOGOGOAPTE": {
        'uttd': "APTE",
        'title': "Powerpuff Girls, The - Mojo Jojo A-Go-Go",
    },
    "PPG MOJOGOGOAPTP": {
        'uttd': "APTP",
        'title': "Powerpuff Girls, The - Mojo Jojo A-Go-Go",
    },
    "P PROF 1    BPJE": {
        'uttd': "BPJE",
        'title': "Pocket Professor",
    },
    "PRANGERS_SPDBRDE": {
        'uttd': "BRDE",
        'title': "Power Rangers - S.P.D.",
    },
    "PRANGERS_SPDBRDX": {
        'uttd': "BRDX",
        'title': "Power Rangers - S.P.D.",
    },
    "PRANGERS_SPDBRDY": {
        'uttd': "BRDY",
        'title': "Power Rangers - S.P.D.",
    },
    "PRDINOTHUNDEBPOE": {
        'uttd': "BPOE",
        'title': "Power Rangers - Dino Thunder",
    },
    "PREHISTO MANAPHE": {
        'uttd': "APHE",
        'title': "Prehistorik Man",
    },
    "PREMIER MANABP4P": {
        'uttd': "BP4P",
        'title': "Premier Manager 2004-2005",
    },
    "PREMIER MANABP5P": {
        'uttd': "BP5P",
        'title': "Premier Manager 2005-2006",
    },
    "PREMIER MAN BPMP": {
        'uttd': "BPMP",
        'title': "Premier Manager 2003-04",
    },
    "PRINCEPERSIABPYE": {
        'uttd': "BPYE",
        'title': "Prince of Persia - The Sands of Time",
    },
    "PRINCEPERSIABPYP": {
        'uttd': "BPYP",
        'title': "Prince of Persia - The Sands of Time",
    },
    "PRINCESSBLUEA3HJ": {
        'uttd': "A3HJ",
        'title': "Hime Kishi Monogatari - Princess Blue",
    },
    "PRINCESS NATBNPP": {
        'uttd': "BNPP",
        'title': "Princess Natasha",
    },
    "PRINCESSTOWNBQNE": {
        'uttd': "BQNE",
        'title': "Disney Princess - Royal Adventure",
    },
    "PRINCESSTOWNBQNP": {
        'uttd': "BQNP",
        'title': "Disney Princess - Royal Adventure",
    },
    "PRNINJASTORMBPWE": {
        'uttd': "BPWE",
        'title': "Power Rangers - Ninja Storm",
    },
    "PRNINJASTORMBPWP": {
        'uttd': "BPWP",
        'title': "Power Rangers - Ninja Storm",
    },
    "PRNINJA&TF  BRZE": {
        'uttd': "BRZE",
        'title': "2 Games in 1 - Power Rangers - Ninja Storm + Power Rangers - Time Force",
    },
    "PRNS&TFFRE  BRZF": {
        'uttd': "BRZF",
        'title': "2 Games in 1 - Power Rangers - Ninja Storm + Power Rangers - Time Force",
    },
    "PRO BEACH SOAVEP": {
        'uttd': "AVEP",
        'title': "Pro Beach Soccer",
    },
    "PROUDFAMIL01MFPE": {
        'uttd': "MFPE",
        'title': "Game Boy Advance Video - The Proud Family - Volume 1",
    },
    "PROUDFAMILYGBD7E": {
        'uttd': "BD7E",
        'title': "Proud Family, The",
    },
    "PRPACKNJS&TFBRZP": {
        'uttd': "BRZP",
        'title': "2 Games in 1 - Power Rangers - Ninja Storm + Power Rangers - Time Force",
    },
    "PRTF        APRD": {
        'uttd': "APRD",
        'title': "Power Rangers - Time Force",
    },
    "PRTF        APRE": {
        'uttd': "APRE",
        'title': "Power Rangers - Time Force",
    },
    "PRTF        APRF": {
        'uttd': "APRF",
        'title': "Power Rangers - La Force du Temps",
    },
    "PR_TF&NS_GERBRZD": {
        'uttd': "BRZD",
        'title': "2 Games in 1 - Power Rangers - Ninja Storm + Power Rangers - Time Force",
    },
    "PR_WILDFORCEAPWE": {
        'uttd': "APWE",
        'title': "Power Rangers - Wild Force",
    },
    "PSJUOGBA    AJUJ": {
        'uttd': "AJUJ",
        'title': "Jissen Pachi-Slot Hisshouhou! - Juuou Advance",
    },
    "PUKU22 CUPIDBPQJ": {
        'uttd': "BPQJ",
        'title': "PukuPuku Tennen Kairanban - Koi no Cupid Daisakusen",
    },
    "PUKU23 BOARDB3PJ": {
        'uttd': "B3PJ",
        'title': "PukuPuku Tennen Kairanban - Youkoso Illusion Land he",
    },
    "PUKUPUKU-1  APUJ": {
        'uttd': "APUJ",
        'title': "PukuPuku Tennen Kairanban",
    },
    "PUNCH KING  APGE": {
        'uttd': "APGE",
        'title': "Punch King - Arcade Boxing",
    },
    "PUNCH KING  APGP": {
        'uttd': "APGP",
        'title': "Punch King - Arcade Boxing",
    },
    "PURIMAJIMAJIBFMJ": {
        'uttd': "BFMJ",
        'title': "Futari ha Pretty Cure Max Heart - Maji Maji! Fight de IN Janai",
    },
    "PURIYUMESONOBFPJ": {
        'uttd': "BFPJ",
        'title': "Futari ha Pretty Cure - Arienaai! Yume no Sono ha Daimeikyuu",
    },
    "PUYO FEVER  BPFJ": {
        'uttd': "BPFJ",
        'title': "Puyo Puyo Fever",
    },
    "PUYO POP    APYE": {
        'uttd': "APYE",
        'title': "Puyo Pop",
    },
    "PUYO POP    APYP": {
        'uttd': "APYP",
        'title': "Puyo Pop",
    },
    "PUYO POP FEVBPFP": {
        'uttd': "BPFP",
        'title': "Puyo Pop Fever",
    },
    "PUZZBOB-ADV ABMJ": {
        'uttd': "ABMJ",
        'title': "Super Puzzle Bobble Advance",
    },
    "PUZZLEFIGHT2AZ8E": {
        'uttd': "AZ8E",
        'title': "Super Puzzle Fighter II Turbo",
    },
    "PUZZLEFIGHT2AZ8P": {
        'uttd': "AZ8P",
        'title': "Super Puzzle Fighter II Turbo",
    },
    "QUAD DESFURYBQDE": {
        'uttd': "BQDE",
        'title': "Quad Desert Fury",
    },
    "QUIDDITCH WCBHPE": {
        'uttd': "BHPE",
        'title': "Harry Potter - Quidditch World Cup",
    },
    "QUIDDITCH WCBHPJ": {
        'uttd': "BHPJ",
        'title': "Harry Potter - Quidditch World Cup",
    },
    "R2RBOXING R2AR2E": {
        'uttd': "AR2E",
        'title': "Ready 2 Rumble Boxing - Round 2",
    },
    "R2RBOXING R2AR2P": {
        'uttd': "AR2P",
        'title': "Ready 2 Rumble Boxing - Round 2",
    },
    "RACING FEVERBRWP": {
        'uttd': "BRWP",
        'title': "Racing Fever",
    },
    "RACING GEARSBRAE": {
        'uttd': "BRAE",
        'title': "Racing Gears Advance",
    },
    "RACING GEARSBRAP": {
        'uttd': "BRAP",
        'title': "Racing Gears Advance",
    },
    "RAINBOWSIX-RAR6E": {
        'uttd': "AR6E",
        'title': "Tom Clancy's Rainbow Six - Rogue Spear",
    },
    "RAINBOWSIX-RAR6P": {
        'uttd': "AR6P",
        'title': "Tom Clancy's Rainbow Six - Rogue Spear",
    },
    "RAMPPUZZLEATARXE": {
        'uttd': "ARXE",
        'title': "Rampage - Puzzle Attack",
    },
    "RAPALA PRO FBRFE": {
        'uttd': "BRFE",
        'title': "Rapala Pro Fishing",
    },
    "RAREDKC1    A5NE": {
        'uttd': "A5NE",
        'title': "Donkey Kong Country",
    },
    "RAREDKC1    A5NJ": {
        'uttd': "A5NJ",
        'title': "Super Donkey Kong",
    },
    "RAREDKC1    A5NP": {
        'uttd': "A5NP",
        'title': "Donkey Kong Country",
    },
    "RAREDKC2    B2DE": {
        'uttd': "B2DE",
        'title': "Donkey Kong Country 2",
    },
    "RAREDKC2    B2DJ": {
        'uttd': "B2DJ",
        'title': "Super Donkey Kong 2",
    },
    "RAREDKC3    BDQE": {
        'uttd': "BDQE",
        'title': "Donkey Kong Country 3",
    },
    "RAREDKC3    BDQJ": {
        'uttd': "BDQJ",
        'title': "Super Donkey Kong Country 3",
    },
    "RAREDKC3    BDQP": {
        'uttd': "BDQP",
        'title': "Donkey Kong Country 3",
    },
    "RAVE2       ARIJ": {
        'uttd': "ARIJ",
        'title': "Groove Adventure Rave - Hikari to Yami no Daikessen 2",
    },
    "RAVE        ARVJ": {
        'uttd': "ARVJ",
        'title': "Groove Adventure Rave - Hikari to Yami no Daikessen",
    },
    "RAVE MASTER BRME": {
        'uttd': "BRME",
        'title': "Rave Master - Special Attack Force!",
    },
    "RAVEN2      BZSE": {
        'uttd': "BZSE",
        'title': "That's So Raven 2 - Supernatural Style",
    },
    "RAYMAN 10TH BX5E": {
        'uttd': "BX5E",
        'title': "Rayman 10th Anniversary - Rayman Advance + Rayman 3",
    },
    "RAYMAN 10TH BX5P": {
        'uttd': "BX5P",
        'title': "Rayman 10th Anniversary - Rayman Advance + Rayman 3",
    },
    "RAYMAN 3    AYZE": {
        'uttd': "AYZE",
        'title': "Rayman 3",
    },
    "RAYMAN 3    AYZP": {
        'uttd': "AYZP",
        'title': "Rayman 3",
    },
    "RAYMAN4     BQ3E": {
        'uttd': "BQ3E",
        'title': "Rayman - Raving Rabbids",
    },
    "RAYMAN4     BQ3P": {
        'uttd': "BQ3P",
        'title': "Rayman - Raving Rabbids",
    },
    "RAYMAN      ARYE": {
        'uttd': "ARYE",
        'title': "Rayman Advance",
    },
    "RAYMAN      ARYP": {
        'uttd': "ARYP",
        'title': "Rayman Advance",
    },
    "RAZOR FREESTARFE": {
        'uttd': "ARFE",
        'title': "Razor Freestyle Scooter",
    },
    "RCKTPWRBCHBNAR4E": {
        'uttd': "AR4E",
        'title': "Rocket Power - Beach Bandits",
    },
    "REBELSTAR   BRLE": {
        'uttd': "BRLE",
        'title': "Rebelstar - Tactical Command",
    },
    "REBELSTAR   BRLP": {
        'uttd': "BRLP",
        'title': "Rebelstar - Tactical Command",
    },
    "RECCATHEGAMEARHJ": {
        'uttd': "ARHJ",
        'title': "Recca no Honoo - The Game",
    },
    "REIGN OF FIRAR9E": {
        'uttd': "AR9E",
        'title': "Reign of Fire",
    },
    "REIGN OF FIRAR9P": {
        'uttd': "AR9P",
        'title': "Reign of Fire",
    },
    "RETSUDENGBA ARAJ": {
        'uttd': "ARAJ",
        'title': "Shin Nippon Pro Wrestling - Toukon Retsuden Advance",
    },
    "RETURN KING BLRE": {
        'uttd': "BLRE",
        'title': "Lord of the Rings, The - The Return of the King",
    },
    "RETURN KING BLRJ": {
        'uttd': "BLRJ",
        'title': "Lord of the Rings, The - Ou no Kikan",
    },
    "REVENGEOFSHIA3RE": {
        'uttd': "A3RE",
        'title': "Revenge of Shinobi, The",
    },
    "RHYTHMTENGOKBRIJ": {
        'uttd': "BRIJ",
        'title': "Rhythm Tengoku",
    },
    "RIDE DREAMERBL9E": {
        'uttd': "BL9E",
        'title': "Let's Ride! Dreamer - Inspired by a True Story",
    },
    "RILAKKUMADAYBR9J": {
        'uttd': "BR9J",
        'title': "Relaxuma na Mainichi",
    },
    "RIPPING GAMEARDE": {
        'uttd': "ARDE",
        'title': "Ripping Friends, The",
    },
    "RISKCOMP    B66E": {
        'uttd': "B66E",
        'title': "Risk - Battleship - Clue",
    },
    "RIVERCRANSOMBDTE": {
        'uttd': "BDTE",
        'title': "River City Ransom EX",
    },
    "RIVIERA     BREE": {
        'uttd': "BREE",
        'title': "Riviera - The Promised Land",
    },
    "RIVIERA     BREJ": {
        'uttd': "BREJ",
        'title': "Yakusoku no Chi Riviera",
    },
    "ROADRASHJAILA9RE": {
        'uttd': "A9RE",
        'title': "Road Rash - Jailbreak",
    },
    "ROADRASHJAILA9RP": {
        'uttd': "A9RP",
        'title': "Road Rash - Jailbreak",
    },
    "ROADTRIPSHIFA6RE": {
        'uttd': "A6RE",
        'title': "Shifting Gears Road Trip",
    },
    "ROBO GX     ARJJ": {
        'uttd': "ARJJ",
        'title': "Custom Robo GX",
    },
    "ROBO MACROSSARBE": {
        'uttd': "ARBE",
        'title': "Robotech - The Macross Saga",
    },
    "ROBOPON2CROSACVE": {
        'uttd': "ACVE",
        'title': "Robopon 2 - Cross Version",
    },
    "ROBOPON2CROSACVJ": {
        'uttd': "ACVJ",
        'title': "Robot Ponkottsu 2 - Cross Version",
    },
    "ROBOPON2RINGARPE": {
        'uttd': "ARPE",
        'title': "Robopon 2 - Ring Version",
    },
    "ROBOPON2RINGARPJ": {
        'uttd': "ARPJ",
        'title': "Robot Ponkottsu 2 - Ring Version",
    },
    "ROBORUMBLE  BHQP": {
        'uttd': "BHQP",
        'title': "Agent Hugo - Roborumble",
    },
    "ROBOTS      BRTE": {
        'uttd': "BRTE",
        'title': "Robots",
    },
    "ROBOTS      BRTJ": {
        'uttd': "BRTJ",
        'title': "Robots",
    },
    "ROBOTS      BRTP": {
        'uttd': "BRTP",
        'title': "Robots",
    },
    "ROBOT WARS AARUE": {
        'uttd': "ARUE",
        'title': "Robot Wars - Advanced Destruction",
    },
    "ROBOT WARS AARWP": {
        'uttd': "ARWP",
        'title': "Robot Wars - Advanced Destruction",
    },
    "ROBOT WARS EARSP": {
        'uttd': "ARSP",
        'title': "Robot Wars - Extreme Destruction",
    },
    "ROCKEMSOCKEMBR7E": {
        'uttd': "BR7E",
        'title': "Rock'em Sock'em Robots",
    },
    "ROCKEMSOCKEMBR7P": {
        'uttd': "BR7P",
        'title': "Rock'em Sock'em Robots",
    },
    "ROCKET_POWERAZZE": {
        'uttd': "AZZE",
        'title': "Rocket Power - Zero Gravity Zone",
    },
    "ROCKETPOWERFARKF": {
        'uttd': "ARKF",
        'title': "Rocket Power - Le Cauchemar d'Otto",
    },
    "ROCK_EXE3_BKA3XJ": {
        'uttd': "A3XJ",
        'title': "Battle Network Rockman EXE 3 Black",
    },
    "ROCKEXE4.5ROBR4J": {
        'uttd': "BR4J",
        'title': "Rockman EXE 4.5 - Real Operation",
    },
    "ROCK_EXE4_BMB4BJ": {
        'uttd': "B4BJ",
        'title': "Rockman EXE 4 - Tournament Blue Moon",
    },
    "ROCK_EXE4_BMB4BP": {
        'uttd': "B4BP",
        'title': "Megaman Battle Network 4 - Blue Moon",
    },
    "ROCK_EXE4_RSB4WJ": {
        'uttd': "B4WJ",
        'title': "Rockman EXE 4 - Tournament Red Sun",
    },
    "ROCK_EXE4_RSB4WP": {
        'uttd': "B4WP",
        'title': "Megaman Battle Network 4 - Red Sun",
    },
    "ROCKEXE5_TOBBRBJ": {
        'uttd': "BRBJ",
        'title': "Rockman EXE 5 - Team of Blues",
    },
    "ROCKEXE5_TOCBRKJ": {
        'uttd': "BRKJ",
        'title': "Rockman EXE 5 - Team of Colonel",
    },
    "ROCKEXE6_GXXBR5J": {
        'uttd': "BR5J",
        'title': "Rockman EXE 6 - Dennoujuu Grega",
    },
    "ROCKEXE6_RXXBR6J": {
        'uttd': "BR6J",
        'title': "Rockman EXE 6 - Dennoujuu Faltzer",
    },
    "ROCK&FORTE  AFCJ": {
        'uttd': "AFCJ",
        'title': "Rockman & Forte",
    },
    "ROCKMAN_EXE2AE2J": {
        'uttd': "AE2J",
        'title': "Battle Network Rockman EXE 2",
    },
    "ROCKMAN_EXE3A6BJ": {
        'uttd': "A6BJ",
        'title': "Battle Network Rockman EXE 3",
    },
    "ROCKMAN_EXE AREJ": {
        'uttd': "AREJ",
        'title': "Battle Network Rockman EXE",
    },
    "ROCKMANZERO2A62J": {
        'uttd': "A62J",
        'title': "Rockman Zero 2",
    },
    "ROCKMANZERO3BZ3J": {
        'uttd': "BZ3J",
        'title': "Rockman Zero 3",
    },
    "ROCKMANZERO4B4ZJ": {
        'uttd': "B4ZJ",
        'title': "Rockman Zero 4",
    },
    "ROCKMAN ZEROARZJ": {
        'uttd': "ARZJ",
        'title': "Rockman Zero",
    },
    "ROCKY       AROP": {
        'uttd': "AROP",
        'title': "Rocky",
    },
    "ROCKY BOXINGAR8E": {
        'uttd': "AR8E",
        'title': "Rocky",
    },
    "RPGTCOOLGBA A8TJ": {
        'uttd': "A8TJ",
        'title': "RPG Tsukuru Advance",
    },
    "RR GO PARTY AR5E": {
        'uttd': "AR5E",
        'title': "Rugrats - I Gotta Go Party",
    },
    "RR GO PARTY AR5F": {
        'uttd': "AR5F",
        'title': "Razmoket, Les - A moi la Fiesta",
    },
    "RRRACING    A4RE": {
        'uttd': "A4RE",
        'title': "Rock n' Roll Racing",
    },
    "RRRACING    A4RP": {
        'uttd': "A4RP",
        'title': "Rock n' Roll Racing",
    },
    "RTYPE III   BR3E": {
        'uttd': "BR3E",
        'title': "R-Type III - The Third Lightning",
    },
    "RTYPE III   BR3P": {
        'uttd': "BR3P",
        'title': "R-Type III - The Third Lightning",
    },
    "RUGRATSGWILDA5WE": {
        'uttd': "A5WE",
        'title': "Rugrats - Go Wild",
    },
    "RUGRATSGWILDA5WF": {
        'uttd': "A5WF",
        'title': "Razmoket, Les - Rencontrent les Delajungle",
    },
    "SABREWULFTHQAWUE": {
        'uttd': "AWUE",
        'title': "Sabre Wulf",
    },
    "SABREWULFTHQAWUP": {
        'uttd': "AWUP",
        'title': "Sabre Wulf",
    },
    "SABRINA-THE A3BE": {
        'uttd': "A3BE",
        'title': "Sabrina - The Teenage Witch - Potion Commotion",
    },
    "SABRINA-THE A3BP": {
        'uttd': "A3BP",
        'title': "Sabrina - The Teenage Witch - Potion Commotion",
    },
    "SAIYUUKI    BGMJ": {
        'uttd': "BGMJ",
        'title': "Gensou Maden Saiyuuki - Hangyaku no Toushin-taishi",
    },
    "SAKATUKUADV AC2J": {
        'uttd': "AC2J",
        'title': "J.League Pro Soccer Club wo Tsukurou! Advance",
    },
    "SAKURA001MTOBKSJ": {
        'uttd': "BKSJ",
        'title': "Cardcaptor Sakura - Card Friends",
    },
    "SAKURA      BK3J": {
        'uttd': "BK3J",
        'title': "Cardcaptor Sakura - Sakura Card de Mini Game",
    },
    "SALT LAKE 20AS5E": {
        'uttd': "AS5E",
        'title': "Salt Lake 2002",
    },
    "SALT LAKE 20AWGP": {
        'uttd': "AWGP",
        'title': "Salt Lake 2002",
    },
    "SAMURAIJACK AJTE": {
        'uttd': "AJTE",
        'title': "Samurai Jack - The Amulet of Time",
    },
    "SAMURAI-MMV1AOSJ": {
        'uttd': "AOSJ",
        'title': "Samurai Deeper Kyo",
    },
    "SANGOKUMUSOUB36J": {
        'uttd': "B36J",
        'title': "Shin Sangoku Musou Advance",
    },
    "SANGOKUSHI  ASXJ": {
        'uttd': "ASXJ",
        'title': "Sangokushi",
    },
    "SANRIO PURO A85J": {
        'uttd': "A85J",
        'title': "Sanrio Puroland - All Characters",
    },
    "SANSARA 1X2 ASNJ": {
        'uttd': "ASNJ",
        'title': "Sansara Naga 1x2",
    },
    "SANTA       AUZE": {
        'uttd': "AUZE",
        'title': "Santa Claus Saves the Earth",
    },
    "SANTA CLAUS AXXP": {
        'uttd': "AXXP",
        'title': "Santa Claus Jr. Advance",
    },
    "SANTACLAUSE3B33E": {
        'uttd': "B33E",
        'title': "Santa Clause 3, The - The Escape Clause",
    },
    "SBBFBBNTFFF BU2E": {
        'uttd': "BU2E",
        'title': "2 Games in 1 - SpongeBob SquarePants - Battle for Bikini Bottom + Nicktoons - Freeze Frame Frenzy",
    },
    "SBFOP       BX6E": {
        'uttd': "BX6E",
        'title': "2 Games in 1 - SpongeBob SquarePants - Battle for Bikini Bottom + Fairly Odd Parents!, The - Breakin' da Rules",
    },
    "SBREVENGEGBAAQ3E": {
        'uttd': "AQ3E",
        'title': "SpongeBob SquarePants - Revenge of the Flying Dutchman",
    },
    "SBREVENGEGBABDFE": {
        'uttd': "BDFE",
        'title': "2 Games in 1 - SpongeBob SquarePants - SuperSponge + Revenge of the Flying Dutchman",
    },
    "SBSPBATTLEBBBSQE": {
        'uttd': "BSQE",
        'title': "SpongeBob SquarePants - Battle for Bikini Bottom",
    },
    "SBSPBATTLEBBBSQP": {
        'uttd': "BSQP",
        'title': "SpongeBob SquarePants - Battle for Bikini Bottom",
    },
    "SBSP BFVI   BNVP": {
        'uttd': "BNVP",
        'title': "SpongeBob SquarePants and Friends - Battle for Volcano Island",
    },
    "SBSP_&_JNBG_BBJP": {
        'uttd': "BBJP",
        'title': "2 Games in 1 - SpongeBob SquarePants - Battle for Bikini Bottom + Jimmy Neutron - Boy Genius",
    },
    "SBSPLIGHTS  BQQE": {
        'uttd': "BQQE",
        'title': "SpongeBob SquarePants - Lights, Camera, Pants!",
    },
    "SBSPLIGHTS  BQQX": {
        'uttd': "BQQX",
        'title': "SpongeBob SquarePants - Lights, Camera, Pants!",
    },
    "SBSPMOVIE   BSNE": {
        'uttd': "BSNE",
        'title': "SpongeBob SquarePants - The Movie",
    },
    "SBSPMOVIE   BSNX": {
        'uttd': "BSNX",
        'title': "SpongeBob SquarePants - The Movie",
    },
    "SBSPMOVIEFFFB2BP": {
        'uttd': "B2BP",
        'title': "2 Games in 1 - SpongeBob SquarePants - The Movie + SpongeBob SquarePants and Friends - Freeze Frame Frenzy",
    },
    "SBSP SS     ASPE": {
        'uttd': "ASPE",
        'title': "SpongeBob SquarePants - SuperSponge",
    },
    "SBSPUNITE   BNUP": {
        'uttd': "BNUP",
        'title': "SpongeBob SquarePants and Friends Unite!",
    },
    "SB_SS_&_FTRFBDFP": {
        'uttd': "BDFP",
        'title': "2 Games in 1 - SpongeBob SquarePants - SuperSponge + Revenge of the Flying Dutchman",
    },
    "SBSS_&RGW_ENBRSP": {
        'uttd': "BRSP",
        'title': "2 Games in 1 - Rugrats - Go Wild + SpongeBob SquarePants - SuperSponge",
    },
    "S BUBBLE POPAVZE": {
        'uttd': "AVZE",
        'title': "Super Bubble Pop",
    },
    "S BUBBLE POPAVZP": {
        'uttd': "AVZP",
        'title': "Super Bubble Pop",
    },
    "SCAN HUNTER A57J": {
        'uttd': "A57J",
        'title': "Scan Hunter - Sennen Kaigyo wo Oe!",
    },
    "SCOOBY CYBERASDE": {
        'uttd': "ASDE",
        'title': "Scooby-Doo and the Cyber Chase",
    },
    "SCOOBY CYBERASDX": {
        'uttd': "ASDX",
        'title': "Scooby-Doo and the Cyber Chase",
    },
    "SCOOBY-DOO_2BMUE": {
        'uttd': "BMUE",
        'title': "Scooby-Doo 2 - Monsters Unleashed",
    },
    "SCOOBY DOO 2BMUX": {
        'uttd': "BMUX",
        'title': "Scooby-Doo 2 - Monsters Unleashed",
    },
    "SCOOBYMAYHEMBMME": {
        'uttd': "BMME",
        'title': "Scooby-Doo! - Mystery Mayhem",
    },
    "SCOOBYMAYHEMBMMP": {
        'uttd': "BMMP",
        'title': "Scooby-Doo! - Mystery Mayhem",
    },
    "SCOOBYMOVIEEAP8D": {
        'uttd': "AP8D",
        'title': "Scooby-Doo",
    },
    "SCOOBYMOVIEEAP8E": {
        'uttd': "AP8E",
        'title': "Scooby-Doo",
    },
    "SCOOBYMOVIEEAP8F": {
        'uttd': "AP8F",
        'title': "Scooby-Doo",
    },
    "SCOOBYMOVIEEAP8P": {
        'uttd': "AP8P",
        'title': "Scooby-Doo",
    },
    "SCOOBYMOVIEEAP8S": {
        'uttd': "AP8S",
        'title': "Scooby-Doo",
    },
    "SCOOBYMOVMONBPUE": {
        'uttd': "BPUE",
        'title': "2 Games in 1 - Scooby-Doo + Scooby-Doo 2 - Monsters Unleashed",
    },
    "SCOOBYUN    B25E": {
        'uttd': "B25E",
        'title': "Scooby-Doo! - Unmasked",
    },
    "SCOOBYUN    B25X": {
        'uttd': "B25X",
        'title': "Scooby-Doo! - Unmasked",
    },
    "SCOOBYUN    B25Y": {
        'uttd': "B25Y",
        'title': "Scooby-Doo! - Unmasked",
    },
    "SCORPIONKINGASZE": {
        'uttd': "ASZE",
        'title': "Scorpion King, The - Sword of Osiris",
    },
    "SCORPIONKINGASZP": {
        'uttd': "ASZP",
        'title': "Scorpion King, The - Sword of Osiris",
    },
    "SCRABBLE    AQBP": {
        'uttd': "AQBP",
        'title': "Scrabble",
    },
    "SCRABBLECOMPB67E": {
        'uttd': "B67E",
        'title': "Sorry! - Aggravation - Scrabble Junior",
    },
    "SCRABBLESCRABLAP": {
        'uttd': "BLAP",
        'title': "Scrabble Scramble",
    },
    "SCRABBLE SCRBLAX": {
        'uttd': "BLAX",
        'title': "Scrabble Scramble",
    },
    "SCRABLEBLASTBLAE": {
        'uttd': "BLAE",
        'title': "Scrabble Blast!",
    },
    "SCREWBREAKERV49J": {
        'uttd': "V49J",
        'title': "Screw Breaker - Goushin Dorirurero",
    },
    "SCURGEHIVE  BHVE": {
        'uttd': "BHVE",
        'title': "Scurge - Hive",
    },
    "SCURGEHIVE  BHVP": {
        'uttd': "BHVP",
        'title': "Scurge - Hive",
    },
    "SD_CC&MH_EFGBCVE": {
        'uttd': "BCVE",
        'title': "2 Games in 1 - Scooby-Doo! - Mystery Mayhem + Scooby-Doo and the Cyber Chase",
    },
    "SD_CC&MH_EFGBCVP": {
        'uttd': "BCVP",
        'title': "2 Games in 1 - Scooby-Doo! - Mystery Mayhem + Scooby-Doo and the Cyber Chase",
    },
    "SD GACHAPON1FSDJ": {
        'uttd': "FSDJ",
        'title': "Famicom Mini Vol. 30 - SD Gundam World - Gachapon Senshi Scramble Wars",
    },
    "SDGFORCE    BG4J": {
        'uttd': "BG4J",
        'title': "SD Gundam Force",
    },
    "SDGFORCE    BGEE": {
        'uttd': "BGEE",
        'title': "SD Gundam Force",
    },
    "SD_MP&MU_ENGBPUP": {
        'uttd': "BPUP",
        'title': "2 Games in 1 - Scooby-Doo + Scooby-Doo 2 - Monsters Unleashed",
    },
    "SD_MP&MU_FREBPUF": {
        'uttd': "BPUF",
        'title': "2 Games in 1 - Scooby-Doo + Scooby-Doo 2 - Les Monstres Se Dechainent",
    },
    "SD_MP_&MU_SPBPUS": {
        'uttd': "BPUS",
        'title': "2 Games in 1 - Scooby-Doo + Scooby-Doo 2 - Desatado",
    },
    "SD_SUMOS_AGBBDPE": {
        'uttd': "BDPE",
        'title': "Super Duper Sumos",
    },
    "SEA MONKEYS A7ME": {
        'uttd': "A7ME",
        'title': "Amazing Virtual Sea Monkeys, The",
    },
    "SEA TRADER  ALJE": {
        'uttd': "ALJE",
        'title': "Sea Trader - Rise of Taipan",
    },
    "SECRETAGENTBAAHE": {
        'uttd': "AAHE",
        'title': "Secret Agent Barbie - Royal Jewels Mission",
    },
    "SECRETAGENTBAAHP": {
        'uttd': "AAHP",
        'title': "Secret Agent Barbie - Royal Jewels Mission",
    },
    "SEEDDESTINY B42J": {
        'uttd': "B42J",
        'title': "Kidou Senshi Gundam Seed Destiny",
    },
    "SEGA ARCADE AYPE": {
        'uttd': "AYPE",
        'title': "Sega Arcade Gallery",
    },
    "SEGA ARCADE AYPP": {
        'uttd': "AYPP",
        'title': "Sega Arcade Gallery",
    },
    "SEGA RALLY  AYLE": {
        'uttd': "AYLE",
        'title': "Sega Rally Championship",
    },
    "SEGA RALLY  AYLJ": {
        'uttd': "AYLJ",
        'title': "Sega Rally Championship",
    },
    "SEGA RALLY CAYLP": {
        'uttd': "AYLP",
        'title': "Sega Rally Championship",
    },
    "SEGA SMASH PA3PE": {
        'uttd': "A3PE",
        'title': "Sega Smash Pack",
    },
    "SEGA SMASH PA3PP": {
        'uttd': "A3PP",
        'title': "Sega Smash Pack",
    },
    "SEIKEN SHIN1AVSJ": {
        'uttd': "AVSJ",
        'title': "Shinyaku Seiken Densetsu",
    },
    "SENNENKAZOKUBKAJ": {
        'uttd': "BKAJ",
        'title': "Sennen Kazoku",
    },
    "SERIOUS SAM AENE": {
        'uttd': "AENE",
        'title': "Serious Sam Advance",
    },
    "SERIOUS SAM AENP": {
        'uttd': "AENP",
        'title': "Serious Sam Advance",
    },
    "SHAMAN KING2AKAJ": {
        'uttd': "AKAJ",
        'title': "Shaman King Card Game - Chou Senjiryakketsu 2",
    },
    "SHAMAN KING2B2ME": {
        'uttd': "B2ME",
        'title': "Shaman King - Master of Spirits 2",
    },
    "SHAMAN KING2B2MP": {
        'uttd': "B2MP",
        'title': "Shaman King - Master of Spirits 2",
    },
    "SHAMAN KING3AL3J": {
        'uttd': "AL3J",
        'title': "Shaman King Card Game - Chou Senjiryakketsu 3",
    },
    "SHAMAN KING BSOE": {
        'uttd': "BSOE",
        'title': "Shaman King - Master of Spirits",
    },
    "SHAMAN KING BSOP": {
        'uttd': "BSOP",
        'title': "Shaman King - Master of Spirits",
    },
    "SHAMUSADV   BBAE": {
        'uttd': "BBAE",
        'title': "Shamu's Deep Sea Adventures",
    },
    "SHAMUSADV   BBAP": {
        'uttd': "BBAP",
        'title': "Shamu's Deep Sea Adventures",
    },
    "SHANGHAI ADVASVJ": {
        'uttd': "ASVJ",
        'title': "Shanghai Advance",
    },
    "SHARK STORY BSUI": {
        'uttd': "BSUI",
        'title': "Shark Story",
    },
    "SHARK TALE  B9TJ": {
        'uttd': "B9TJ",
        'title': "Shark Tale",
    },
    "SHARK TALE  BSUE": {
        'uttd': "BSUE",
        'title': "Shark Tale",
    },
    "SHARK TALE  BSUX": {
        'uttd': "BSUX",
        'title': "Shark Tale",
    },
    "SHAUNPALMER1ASCD": {
        'uttd': "ASCD",
        'title': "Shaun Palmer's Pro Snowboarder",
    },
    "SHAUNPALMER1ASCE": {
        'uttd': "ASCE",
        'title': "Shaun Palmer's Pro Snowboarder",
    },
    "SHEEP       AEPP": {
        'uttd': "AEPP",
        'title': "Sheep",
    },
    "SHEEP       AHIJ": {
        'uttd': "AHIJ",
        'title': "Hitsuji no Kimochi",
    },
    "SHIMURA_KEN A64J": {
        'uttd': "A64J",
        'title': "Shimura Ken no Baka Tonosama - Bakushou Tenka Touitsu Game",
    },
    "SHININGFORCEAF5E": {
        'uttd': "AF5E",
        'title': "Shining Force - Resurrection of the Dark Dragon",
    },
    "SHININGFORCEAF5J": {
        'uttd': "AF5J",
        'title': "Shining Force - Kuroki Ryuu no Fukkatsu",
    },
    "SHININGFORCEAF5P": {
        'uttd': "AF5P",
        'title': "Shining Force - Resurrection of the Dark Dragon",
    },
    "SHININGSOUL2AU2E": {
        'uttd': "AU2E",
        'title': "Shining Soul II",
    },
    "SHININGSOUL2AU2J": {
        'uttd': "AU2J",
        'title': "Shining Soul II",
    },
    "SHINING SOULAHUE": {
        'uttd': "AHUE",
        'title': "Shining Soul",
    },
    "SHINING SOULAHUJ": {
        'uttd': "AHUJ",
        'title': "Shining Soul",
    },
    "SHINING SOULAHUP": {
        'uttd': "AHUP",
        'title': "Shining Soul",
    },
    "SHINING SOULAU2P": {
        'uttd': "AU2P",
        'title': "Shining Soul II",
    },
    "SHINJAJA    BNJJ": {
        'uttd': "BNJJ",
        'title': "Jajamaru Jr. Denshouki - Jalecolle mo Arisourou",
    },
    "SHINMEDA-KBTBKVJ": {
        'uttd': "BKVJ",
        'title': "Shingata Medarot - Kabuto Version",
    },
    "SHINMEDA-KWGBKUJ": {
        'uttd': "BKUJ",
        'title': "Shingata Medarot - Kuwagata Version",
    },
    "SHORTCAKEIRCB35P": {
        'uttd': "B35P",
        'title': "Strawberry Shortcake - Ice Cream Island Riding Camp",
    },
    "SHREK 2.1   BSIE": {
        'uttd': "BSIE",
        'title': "Shrek 2 - Beg for Mercy",
    },
    "SHREK 2.1   BSIX": {
        'uttd': "BSIX",
        'title': "Shrek 2 - Beg for Mercy",
    },
    "SHREK 2     BSEE": {
        'uttd': "BSEE",
        'title': "Shrek 2",
    },
    "SHREK 2     BSEX": {
        'uttd': "BSEX",
        'title': "Shrek 2",
    },
    "SHREK 2/MADABXGE": {
        'uttd': "BXGE",
        'title': "2 Games in 1 - Shrek 2 + Madagascar",
    },
    "SHREK 2/MADABXGP": {
        'uttd': "BXGP",
        'title': "2 Games in 1 - Shrek 2 + Madagascar",
    },
    "SHREK 2-PENGBXHE": {
        'uttd': "BXHE",
        'title': "2 Games in 1 - Shrek 2 + Madagascar - Operation Penguin",
    },
    "SHREK 2-PENGBXHP": {
        'uttd': "BXHP",
        'title': "2 Games in 1 - Shrek 2 + Madagascar - Operation Penguin",
    },
    "SHREK 3     AOIE": {
        'uttd': "AOIE",
        'title': "Shrek - Reekin' Havoc",
    },
    "SHREK 3     B3HE": {
        'uttd': "B3HE",
        'title': "Shrek the Third",
    },
    "SHREK HATC  AH4E": {
        'uttd': "AH4E",
        'title': "Shrek - Hassle at the Castle",
    },
    "SHREK HATC  AH4P": {
        'uttd': "AH4P",
        'title': "Shrek - Hassle at the Castle",
    },
    "SHREK KART  AS4E": {
        'uttd': "AS4E",
        'title': "Shrek - Swamp Kart Speedway",
    },
    "SHREK REEKINAOIP": {
        'uttd': "AOIP",
        'title': "Shrek - Reekin' Havoc",
    },
    "SHREK SHARK BS7E": {
        'uttd': "BS7E",
        'title': "2 Games in 1 - Shrek 2 + Shark Tale",
    },
    "SHREK SHARK BS7P": {
        'uttd': "BS7P",
        'title': "2 Games in 1 - Shrek 2 + Shark Tale",
    },
    "SHREK SMASHNB4IE": {
        'uttd': "B4IE",
        'title': "Shrek - Smash n' Crash Racing",
    },
    "SHREK SMASHNB4IP": {
        'uttd': "B4IP",
        'title': "Shrek - Smash n' Crash Racing",
    },
    "SIFKBASEBALLAKBE": {
        'uttd': "AKBE",
        'title': "Sports Illustrated for Kids - Baseball",
    },
    "SIFKFOOTBALLAKFE": {
        'uttd': "AKFE",
        'title': "Sports Illustrated for Kids - Football",
    },
    "SIGMA STAR  B3GE": {
        'uttd': "B3GE",
        'title': "Sigma Star Saga",
    },
    "SIKAMARUKAKEB4KJ": {
        'uttd': "B4KJ",
        'title': "Shikakui Atama wo Marukusuru Advance - Kanji Keisan",
    },
    "SIKAMARUKOSAB4RJ": {
        'uttd': "B4RJ",
        'title': "Shikakui Atama wo Marukusuru Advance - Kokugo Sansu Rika Shakai",
    },
    "SILENT HILL ASHJ": {
        'uttd': "ASHJ",
        'title': "Silent Hill - Play Novel",
    },
    "SILENT SCOPEAIPE": {
        'uttd': "AIPE",
        'title': "Silent Scope",
    },
    "SILENT SCOPEAIPJ": {
        'uttd': "AIPJ",
        'title': "Silent Scope",
    },
    "SILENT SCOPEAIPP": {
        'uttd': "AIPP",
        'title': "Silent Scope",
    },
    "SILK&COTTON A7IJ": {
        'uttd': "A7IJ",
        'title': "Silk to Cotton",
    },
    "SIMCITY 2000A5CE": {
        'uttd': "A5CE",
        'title': "Sim City 2000",
    },
    "SIMCITY 2000A5CP": {
        'uttd': "A5CP",
        'title': "Sim City 2000",
    },
    "SIMPSONSRAGEA4AE": {
        'uttd': "A4AE",
        'title': "Simpsons, The - Road Rage",
    },
    "SIMPSONSRAGEA4AX": {
        'uttd': "A4AX",
        'title': "Simpsons, The - Road Rage",
    },
    "SIMS2 PETS  B4OE": {
        'uttd': "B4OE",
        'title': "Sims 2, The - Pets",
    },
    "SIMS2 PETS  B4OX": {
        'uttd': "B4OX",
        'title': "Sims 2, The - Pets",
    },
    "SISTERP-MMV1A4PJ": {
        'uttd': "A4PJ",
        'title': "Sister Princess - RePure",
    },
    "SITTING DUCKBSDE": {
        'uttd': "BSDE",
        'title': "Sitting Ducks",
    },
    "SITTING DUCKBSDP": {
        'uttd': "BSDP",
        'title': "Sitting Ducks",
    },
    "SK8 THPS2   ATHJ": {
        'uttd': "ATHJ",
        'title': "SK8 - Tony Hawk's Pro Skater 2",
    },
    "SK LOS HAWK BHLE": {
        'uttd': "BHLE",
        'title': "Shaman King - Legacy of the Spirits - Soaring Hawk",
    },
    "SK LOS WOLF BWSE": {
        'uttd': "BWSE",
        'title': "Shaman King - Legacy of the Spirits - Sprinting Wolf",
    },
    "SKYDANCERS  B4DE": {
        'uttd': "B4DE",
        'title': "Sky Dancers - They Magically Fly!",
    },
    "SKYDANCERS  B4DP": {
        'uttd': "B4DP",
        'title': "Sky Dancers - They Magically Fly!",
    },
    "SLOT!PRO2   ATBJ": {
        'uttd': "ATBJ",
        'title': "Slot! Pro 2 Advance - GoGo Juggler & New Tairyou",
    },
    "SLOT!PRO    ASFJ": {
        'uttd': "ASFJ",
        'title': "Slot! Pro Advance - Takarabune & Ooedo Sakurafubuki 2",
    },
    "SLUGFEST2K4 A5ME": {
        'uttd': "A5ME",
        'title': "MLB SlugFest 20-04",
    },
    "SMASHDRIVE  BSVE": {
        'uttd': "BSVE",
        'title': "Smashing Drive",
    },
    "SMASHDRIVE  BSVP": {
        'uttd': "BSVP",
        'title': "Smashing Drive",
    },
    "SMPWAKEBOARDAWDE": {
        'uttd': "AWDE",
        'title': "Wakeboarding Unleashed featuring Shaun Murray",
    },
    "SMPW!!!!!!!!AWDE": {
        'uttd': "AWDE",
        'title': "Wakeboarding Unleashed featuring Shaun Murray",
    },
    "SMUGGLERSRUNASGE": {
        'uttd': "ASGE",
        'title': "Smuggler's Run",
    },
    "SMUGGLERSRUNASGP": {
        'uttd': "ASGP",
        'title': "Smuggler's Run",
    },
    "SNAPKIDS    AEAJ": {
        'uttd': "AEAJ",
        'title': "Snap Kid's",
    },
    "SNOOD2ONVAC B2VE": {
        'uttd': "B2VE",
        'title': "Snood 2 - Snoods on Vacation",
    },
    "SNOOD2ONVAC B2VP": {
        'uttd': "B2VP",
        'title': "Snood 2 - Snoods on Vacation",
    },
    "SNOOD       ASQE": {
        'uttd': "ASQE",
        'title': "Snood",
    },
    "SNOOD       ASQP": {
        'uttd': "ASQP",
        'title': "Snood",
    },
    "SOCCER KID  AK6E": {
        'uttd': "AK6E",
        'title': "Soccer Kid",
    },
    "SOCCER MANIAALSE": {
        'uttd': "ALSE",
        'title': "LEGO Soccer Mania",
    },
    "SONICADVANC2A2NE": {
        'uttd': "A2NE",
        'title': "Sonic Advance 2",
    },
    "SONICADVANC2A2NJ": {
        'uttd': "A2NJ",
        'title': "Sonic Advance 2",
    },
    "SONICADVANC3B3SE": {
        'uttd': "B3SE",
        'title': "Sonic Advance 3",
    },
    "SONICADVANC3B3SJ": {
        'uttd': "B3SJ",
        'title': "Sonic Advance 3",
    },
    "SONIC ADVANCA2NP": {
        'uttd': "A2NP",
        'title': "Sonic Advance 2",
    },
    "SONIC ADVANCASOP": {
        'uttd': "ASOP",
        'title': "Sonic Advance",
    },
    "SONIC ADVANCB3SP": {
        'uttd': "B3SP",
        'title': "Sonic Advance 3",
    },
    "SONICADVANCEASOE": {
        'uttd': "ASOE",
        'title': "Sonic Advance",
    },
    "SONICADVANCEASOJ": {
        'uttd': "ASOJ",
        'title': "Sonic Advance",
    },
    "SONICBATTLE BSBE": {
        'uttd': "BSBE",
        'title': "Sonic Battle",
    },
    "SONICBATTLE BSBJ": {
        'uttd': "BSBJ",
        'title': "Sonic Battle",
    },
    "SONIC BATTLEBSBP": {
        'uttd': "BSBP",
        'title': "Sonic Battle",
    },
    "SONICGENESISBIJE": {
        'uttd': "BIJE",
        'title': "Sonic the Hedgehog - Genesis",
    },
    "SONICPINBALLA3VE": {
        'uttd': "A3VE",
        'title': "Sonic Pinball Party",
    },
    "SONICPINBALLA3VP": {
        'uttd': "A3VP",
        'title': "Sonic Pinball Party",
    },
    "SONICPINBALLA86J": {
        'uttd': "A86J",
        'title': "Sonic Pinball Party",
    },
    "SONIC X   01MSHE": {
        'uttd': "MSHE",
        'title': "Game Boy Advance Video - Sonic X - Volume 1",
    },
    "SOUND OF THUA3QP": {
        'uttd': "A3QP",
        'title': "Sound of Thunder, A",
    },
    "SOUNDVOYAGERBVGJ": {
        'uttd': "BVGJ",
        'title': "bit Generations - Soundvoyager",
    },
    "SPACE CHANNEA5UE": {
        'uttd': "A5UE",
        'title': "Space Channel 5 - Ulala's Cosmic Attack",
    },
    "SPACE CHANNEA5UP": {
        'uttd': "A5UP",
        'title': "Space Channel 5 - Ulala's Cosmic Attack",
    },
    "SPACE INVADEAIDE": {
        'uttd': "AIDE",
        'title': "Space Invaders",
    },
    "SPACE INVADEAIDF": {
        'uttd': "AIDF",
        'title': "Space Invaders",
    },
    "SPACE INV EXAIDJ": {
        'uttd': "AIDJ",
        'title': "Space Invaders EX",
    },
    "SPEEDBALL 2 AS6P": {
        'uttd': "AS6P",
        'title': "Speedball 2 - Brutal Deluxe",
    },
    "SPIDER-MAN2 BSPE": {
        'uttd': "BSPE",
        'title': "Spider-Man 2",
    },
    "SPIDER-MAN 2BSPI": {
        'uttd': "BSPI",
        'title': "Spider-Man 2",
    },
    "SPIDER-MAN2 BSPX": {
        'uttd': "BSPX",
        'title': "Spider-Man 2",
    },
    "SPIDERMAN3  BI3D": {
        'uttd': "BI3D",
        'title': "Spider-Man 3",
    },
    "SPIDERMAN3  BI3E": {
        'uttd': "BI3E",
        'title': "Spider-Man 3",
    },
    "SPIDERMAN3  BI3I": {
        'uttd': "BI3I",
        'title': "Spider-Man 3",
    },
    "SPIDERMAN3  BI3P": {
        'uttd': "BI3P",
        'title': "Spider-Man 3",
    },
    "SPIDERMAN3  BI3S": {
        'uttd': "BI3S",
        'title': "Spider-Man 3",
    },
    "SPIDER-MAN  AKXD": {
        'uttd': "AKXD",
        'title': "Spider-Man",
    },
    "SPIDERMAN   AKXE": {
        'uttd': "AKXE",
        'title': "Spider-Man",
    },
    "SPIDER-MAN  AKXF": {
        'uttd': "AKXF",
        'title': "Spider-Man",
    },
    "SPIDER-MAN  BX3E": {
        'uttd': "BX3E",
        'title': "2 Games in 1 - Spider-Man + Spider-Man 2",
    },
    "SPIDER-MAN MBX3P": {
        'uttd': "BX3P",
        'title': "2 Games in 1 - Spider-Man + Spider-Man 2",
    },
    "SPIDERMAN MMASEE": {
        'uttd': "ASEE",
        'title': "Spider-Man - Mysterio's Menace",
    },
    "SPIDERMAN MMASEJ": {
        'uttd': "ASEJ",
        'title': "Spider-Man - Mysterio no Kyoui",
    },
    "SPIDEY      BC9E": {
        'uttd': "BC9E",
        'title': "Spider-Man - Battle for New York",
    },
    "SPIDEY      BC9P": {
        'uttd': "BC9P",
        'title': "Spider-Man - Battle for New York",
    },
    "SPIDEYMM X2 BX2E": {
        'uttd': "BX2E",
        'title': "2 Games in 1 - Spider-Man - Mysterio's Menace + X2 - Wolverine's Revenge",
    },
    "SPIRIT: DER AC6D": {
        'uttd': "AC6D",
        'title': "Spirit - Der wilde Mustang - Auf der Suche nach Homeland",
    },
    "SPIRIT: L'ETAC6F": {
        'uttd': "AC6F",
        'title': "Spirit - L'Etalon des Plaines - A la Recherche de la Terre Natale",
    },
    "SPIRITSPELLSAWNE": {
        'uttd': "AWNE",
        'title': "Spirits & Spells",
    },
    "SPIRIT: STALAC6E": {
        'uttd': "AC6E",
        'title': "Spirit - Stallion of the Cimarron - Search for Homeland",
    },
    "SPIRIT: STALAC6P": {
        'uttd': "AC6P",
        'title': "Spirit - Stallion of the Cimarron - Search for Homeland",
    },
    "SPLINTERCELLAO4E": {
        'uttd': "AO4E",
        'title': "Tom Clancy's Splinter Cell",
    },
    "SPONGEBOB003MS3E": {
        'uttd': "MS3E",
        'title': "Game Boy Advance Video - SpongeBob SquarePants - Volume 3",
    },
    "SPONGEBOB 01MSSE": {
        'uttd': "MSSE",
        'title': "Game Boy Advance Video - SpongeBob SquarePants - Volume 1",
    },
    "SPONGEBOB 02MS2E": {
        'uttd': "MS2E",
        'title': "Game Boy Advance Video - SpongeBob SquarePants - Volume 2",
    },
    "SPONGEBOBCKKBQ4E": {
        'uttd': "BQ4E",
        'title': "SpongeBob SquarePants - Creature from the Krusty Krab",
    },
    "SPONGEBOBCKKBQ4P": {
        'uttd': "BQ4P",
        'title': "SpongeBob SquarePants - Creature from the Krusty Krab",
    },
    "SPONGECOMP1EBSZP": {
        'uttd': "BSZP",
        'title': "2 Games in 1 - SpongeBob SquarePants - SuperSponge + SpongeBob SquarePants - Battle for Bikini Bottom",
    },
    "SPONGECOMP1MBSZX": {
        'uttd': "BSZX",
        'title': "2 Games in 1 - SpongeBob SquarePants - SuperSponge + SpongeBob SquarePants - Battle for Bikini Bottom",
    },
    "SPOOKY TREE BBOE": {
        'uttd': "BBOE",
        'title': "Berenstain Bears, The - Spooky Old Tree",
    },
    "SPORTSMAN'S B23E": {
        'uttd': "B23E",
        'title': "2 Games in 1 - Cabela's Big Game Hunter - 2005 Adventures + Rapala Pro Fishing",
    },
    "SPR DROPZONEAZNE": {
        'uttd': "AZNE",
        'title': "Archer Maclean's - Super Dropzone",
    },
    "SPR DROPZONEAZNP": {
        'uttd': "AZNP",
        'title': "Archer Maclean's - Super Dropzone",
    },
    "SPUER DODGE ADFP": {
        'uttd': "ADFP",
        'title': "Super Dodge Ball Advance",
    },
    "SPYHUNTCOMP B6AE": {
        'uttd': "B6AE",
        'title': "Spy Hunter - Super Sprint",
    },
    "SPY HUNTER  AHNE": {
        'uttd': "AHNE",
        'title': "Spy Hunter",
    },
    "SPY HUNTER  AHNP": {
        'uttd': "AHNP",
        'title': "Spy Hunter",
    },
    "SPYHUNTSUPERB6AP": {
        'uttd': "B6AP",
        'title': "Spy Hunter - Super Sprint",
    },
    "SPYKIDSCHALLA2KE": {
        'uttd': "A2KE",
        'title': "Spy Kids Challenger",
    },
    "SPY KIDS IIIAV3E": {
        'uttd': "AV3E",
        'title': "Spy Kids 3-D - Game Over",
    },
    "SPY KIDS IIIAV3P": {
        'uttd': "AV3P",
        'title': "Spy Kids 3-D - Game Over",
    },
    "SPY MUPPETS BSSE": {
        'uttd': "BSSE",
        'title': "Spy Muppets - License to Croak",
    },
    "SPYRO 2     A2SE": {
        'uttd': "A2SE",
        'title': "Spyro 2 - Season of Flame",
    },
    "SPYRO 2     A2SP": {
        'uttd': "A2SP",
        'title': "Spyro 2 - Season of Flame",
    },
    "SPYRO 3     AOWE": {
        'uttd': "AOWE",
        'title': "Spyro - Attack of the Rhynocs",
    },
    "SPYRO 3     AOWP": {
        'uttd': "AOWP",
        'title': "Spyro Adventure",
    },
    "SPYRO       A4SJ": {
        'uttd': "A4SJ",
        'title': "Spyro Advance",
    },
    "SPYRO       ASYE": {
        'uttd': "ASYE",
        'title': "Spyro - Season of Ice",
    },
    "SPYRO       ASYP": {
        'uttd': "ASYP",
        'title': "Spyro - Season of Ice",
    },
    "SPYRO ORANGEBS8J": {
        'uttd': "BS8J",
        'title': "Spyro Advance - Wakuwaku Tomodachi Daisakusen!",
    },
    "SPYRO ORANGEBSTE": {
        'uttd': "BSTE",
        'title': "Spyro Orange - The Cortex Conspiracy",
    },
    "SPYRO ORANGEBSTP": {
        'uttd': "BSTP",
        'title': "Spyro Fusion",
    },
    "SPYRO S PACKB8SE": {
        'uttd': "B8SE",
        'title': "2 Games in 1 - Spyro - Season of Ice + Spyro 2 - Season of Flame",
    },
    "SR MAHJONG DBDMJ": {
        'uttd': "BDMJ",
        'title': "Super Real Mahjong Dousoukai",
    },
    "SRS - STREETBCZP": {
        'uttd': "BCZP",
        'title': "Street Racing Syndicate",
    },
    "SRTOG2      B2RE": {
        'uttd': "B2RE",
        'title': "Super Robot Taisen - Original Generation 2",
    },
    "SRTOG       AOGE": {
        'uttd': "AOGE",
        'title': "Super Robot Taisen - Original Generation",
    },
    "SRWA        ASRJ": {
        'uttd': "ASRJ",
        'title': "Super Robot Taisen A",
    },
    "SRWD        A6SJ": {
        'uttd': "A6SJ",
        'title': "Super Robot Taisen D",
    },
    "SRWJ        B6JJ": {
        'uttd': "B6JJ",
        'title': "Super Robot Taisen",
    },
    "SRWOG2      B2RJ": {
        'uttd': "B2RJ",
        'title': "Super Robot Taisen - Original Generation 2",
    },
    "SRWOG       AOGJ": {
        'uttd': "AOGJ",
        'title': "Super Robot Taisen - Original Generation",
    },
    "SRWR        AJ9J": {
        'uttd': "AJ9J",
        'title': "Super Robot Taisen R",
    },
    "SS DBL PACK BQWE": {
        'uttd': "BQWE",
        'title': "Strawberry Shortcake - Summertime Adventure - Special Edition",
    },
    "SSF2TREVIVALAXRE": {
        'uttd': "AXRE",
        'title': "Super Street Fighter II Turbo - Revival",
    },
    "SSF2TREVIVALAXRP": {
        'uttd': "AXRP",
        'title': "Super Street Fighter II Turbo - Revival",
    },
    "SSF2XREVIVALAXRJ": {
        'uttd': "AXRJ",
        'title': "Super Street Fighter II X - Revival",
    },
    "SS_&_RGW_FREBRSF": {
        'uttd': "BRSF",
        'title': "2 Games in 1 - Les Razmoket Rencontrent les Delajungle + SpongeBob SquarePants - SuperSponge",
    },
    "SSX3        BSXE": {
        'uttd': "BSXE",
        'title': "SSX 3",
    },
    "SSXTRICKY   AXYE": {
        'uttd': "AXYE",
        'title': "SSX Tricky",
    },
    "STADIUMGAMESA9GE": {
        'uttd': "A9GE",
        'title': "Stadium Games",
    },
    "STADIUMGAMESA9GP": {
        'uttd': "A9GP",
        'title': "Stadium Games",
    },
    "STAFY 2     AVFJ": {
        'uttd': "AVFJ",
        'title': "Densetsu no Stafy 2",
    },
    "STAFY 3     B3DJ": {
        'uttd': "B3DJ",
        'title': "Densetsu no Stafy 3",
    },
    "STAFY       ASTJ": {
        'uttd': "ASTJ",
        'title': "Densetsu no Stafy",
    },
    "STARCOM     ASKJ": {
        'uttd': "ASKJ",
        'title': "Sutakomi - Star Communicator",
    },
    "STARSKYHUTCHAYHE": {
        'uttd': "AYHE",
        'title': "Starsky & Hutch",
    },
    "STARSKYHUTCHAYHP": {
        'uttd': "AYHP",
        'title': "Starsky & Hutch",
    },
    "STAR SOLDIERFSOJ": {
        'uttd': "FSOJ",
        'title': "Famicom Mini Vol. 10 - Star Soldier",
    },
    "STAR WARS   BE3P": {
        'uttd': "BE3P",
        'title': "Star Wars Episode III - Revenge of the Sith",
    },
    "STAR WARS EPAS2E": {
        'uttd': "AS2E",
        'title': "Star Wars Episode II - Attack of the Clones",
    },
    "STAR WARS EPAS2X": {
        'uttd': "AS2X",
        'title': "Star Wars Episode II - Attack of the Clones",
    },
    "STARWARSFOTFBSWE": {
        'uttd': "BSWE",
        'title': "Star Wars - Flight of the Falcon",
    },
    "STARWARSFOTFBSWP": {
        'uttd': "BSWP",
        'title': "Star Wars - Flight of the Falcon",
    },
    "STARWARSJEDIASWX": {
        'uttd': "ASWX",
        'title': "Star Wars - Jedi Power Battles",
    },
    "STARWARSROTSBE3E": {
        'uttd': "BE3E",
        'title': "Star Wars Episode III - Revenge of the Sith",
    },
    "STAR WARS: TA2WE": {
        'uttd': "A2WE",
        'title': "Star Wars - The New Droid Army",
    },
    "STAR WARS: TA2WP": {
        'uttd': "A2WP",
        'title': "Star Wars - The New Droid Army",
    },
    "STAR WARS TRBCKE": {
        'uttd': "BCKE",
        'title': "Star Wars Trilogy - Apprentice of the Force",
    },
    "STAR WARS TRBCKP": {
        'uttd': "BCKP",
        'title': "Star Wars Trilogy - Apprentice of the Force",
    },
    "STAR X      AS8E": {
        'uttd': "AS8E",
        'title': "Star X",
    },
    "STAR X      AS8P": {
        'uttd': "AS8P",
        'title': "Star X",
    },
    "STEELEMPIRE BKTJ": {
        'uttd': "BKTJ",
        'title': "Koutetsu Teikoku from HOT-B",
    },
    "STEEL EMPIREBKTP": {
        'uttd': "BKTP",
        'title': "Steel Empire",
    },
    "STELLVIA_GBABUVJ": {
        'uttd': "BUVJ",
        'title': "Uchuu no Stellvia",
    },
    "STRAWBERRY01MSBE": {
        'uttd': "MSBE",
        'title': "Game Boy Advance Video - Strawberry Shortcake - Volume 1",
    },
    "STRAWBERRYSCB35E": {
        'uttd': "B35E",
        'title': "Strawberry Shortcake - Summertime Adventure",
    },
    "STREET FIGHTAZUE": {
        'uttd': "AZUE",
        'title': "Street Fighter Alpha 3 Upper",
    },
    "STREET FIGHTAZUJ": {
        'uttd': "AZUJ",
        'title': "Street Fighter Zero 3 Upper",
    },
    "STREET FIGHTAZUP": {
        'uttd': "AZUP",
        'title': "Street Fighter Alpha 3 Upper",
    },
    "STREETJAM   A3ZE": {
        'uttd': "A3ZE",
        'title': "Street Jam Basketball",
    },
    "STREETRACINGBCZE": {
        'uttd': "BCZE",
        'title': "Street Racing Syndicate",
    },
    "STUART LITTLASLF": {
        'uttd': "ASLF",
        'title': "Stuart Little 2",
    },
    "STUARTLITTLEASLE": {
        'uttd': "ASLE",
        'title': "Stuart Little 2",
    },
    "STUNTMAN    AUXE": {
        'uttd': "AUXE",
        'title': "Stuntman",
    },
    "STUNTMAN    AUXP": {
        'uttd': "AUXP",
        'title': "Stuntman",
    },
    "SUDOKU FEVERB3ZE": {
        'uttd': "B3ZE",
        'title': "Global Star Sudoku Fever",
    },
    "SUDOKU FEVERB3ZP": {
        'uttd': "B3ZP",
        'title': "Global Star Sudoku Fever",
    },
    "SUM ALL FEARAA6E": {
        'uttd': "AA6E",
        'title': "Sum of All Fears, The",
    },
    "SUM ALL FEARAA6P": {
        'uttd': "AA6P",
        'title': "Sum of All Fears, The",
    },
    "SUMMONIGHCSSAB4J": {
        'uttd': "AB4J",
        'title': "Summon Night - Craft Sword Monogatari",
    },
    "SUMMONIGHSCSAB4E": {
        'uttd': "AB4E",
        'title': "Summon Night - Swordcraft Story",
    },
    "SUPER CLPSE2BCLE": {
        'uttd': "BCLE",
        'title': "Super Collapse! II",
    },
    "SUPERDODGE  ADFE": {
        'uttd': "ADFE",
        'title': "Super Dodge Ball Advance",
    },
    "SUPER GHOULSAG5E": {
        'uttd': "AG5E",
        'title': "Super Ghouls'n Ghosts",
    },
    "SUPERMAN: COASUP": {
        'uttd': "ASUP",
        'title': "Superman - Countdown to Apokolips",
    },
    "SUPERMAN CTAASUE": {
        'uttd': "ASUE",
        'title': "Superman - Countdown to Apokolips",
    },
    "SUPERMAN R  BQXE": {
        'uttd': "BQXE",
        'title': "Superman Returns - Fortress of Solitude",
    },
    "SUPER MARIO2FM2J": {
        'uttd': "FM2J",
        'title': "Famicom Mini Vol. 21 - Super Mario Bros. 2",
    },
    "SUPER MARIOAAMAC": {
        'uttd': "AMAC",
        'title': "Chaoji Maliou 2",
    },
    "SUPER MARIOAAMAE": {
        'uttd': "AMAE",
        'title': "Super Mario Advance",
    },
    "SUPER MARIOAAMAJ": {
        'uttd': "AMAJ",
        'title': "Super Mario Advance",
    },
    "SUPER MARIOAAMZE": {
        'uttd': "AMZE",
        'title': "Super Mario Advance",
    },
    "SUPER MARIOBAA2C": {
        'uttd': "AA2C",
        'title': "Chaoji Maliou Shijie",
    },
    "SUPER MARIOBAA2E": {
        'uttd': "AA2E",
        'title': "Super Mario Advance 2 - Super Mario World",
    },
    "SUPER MARIOBAA2J": {
        'uttd': "AA2J",
        'title': "Super Mario Advance 2",
    },
    "SUPER MARIOBAA2P": {
        'uttd': "AA2P",
        'title': "Super Mario Advance 2 - Super Mario World",
    },
    "SUPER MARIOCA3AC": {
        'uttd': "A3AC",
        'title': "Yaoxi Dao",
    },
    "SUPER MARIOCA3AE": {
        'uttd': "A3AE",
        'title': "Super Mario Advance 3 - Yoshi's Island",
    },
    "SUPER MARIOCA3AJ": {
        'uttd': "A3AJ",
        'title': "Super Mario Advance 3",
    },
    "SUPER MARIOCA3AP": {
        'uttd': "A3AP",
        'title': "Super Mario Advance 3 - Yoshi's Island",
    },
    "SUPER MARIODAX4E": {
        'uttd': "AX4E",
        'title': "Super Mario Advance 4 - Super Mario Bros. 3",
    },
    "SUPER MARIODAX4J": {
        'uttd': "AX4J",
        'title': "Super Mario Advance 4",
    },
    "SUPER MARIODAX4P": {
        'uttd': "AX4P",
        'title': "Super Mario Advance 4 - Super Mario Bros. 3",
    },
    "SUPER MARIO FSME": {
        'uttd': "FSME",
        'title': "Classic NES Series - Super Mario Bros.",
    },
    "SUPER MARIO FSMJ": {
        'uttd': "FSMJ",
        'title': "Famicom Mini Vol. 01 - Super Mario Bros.",
    },
    "SUPER MONKEYALUP": {
        'uttd': "ALUP",
        'title': "Super Monkey Ball Jr.",
    },
    "SUPERPAKVOL1B5AP": {
        'uttd': "B5AP",
        'title': "2 Games in 1 - Spyro - Season of Ice + Crash Bandicoot 2 - N-Tranced",
    },
    "SUPERPAKVOL2B52P": {
        'uttd': "B52P",
        'title': "2 Games in 1 - Spyro 2 - Season of Flame + Crash Nitro Kart",
    },
    "SUPERPAKVOL4BBEE": {
        'uttd': "BBEE",
        'title': "2 Games in 1 - Barbie Groovy Games + Secret Agent Barbie - Royal Jewels Mission",
    },
    "SUPERPAKVOL4BBEP": {
        'uttd': "BBEP",
        'title': "2 Games in 1 - Barbie Groovy Games + Secret Agent Barbie - Royal Jewels Mission",
    },
    "SUPERROBOT01MSRE": {
        'uttd': "MSRE",
        'title': "Game Boy Advance Video - Super Robot Monkey Team Hyper Force Go! - Volume 1",
    },
    "SUPER SLAM  B4UE": {
        'uttd': "B4UE",
        'title': "Shrek Super Slam",
    },
    "SUPER SLAM  B4UP": {
        'uttd': "B4UP",
        'title': "Shrek Super Slam",
    },
    "SURAIMUMORIMA9KJ": {
        'uttd': "A9KJ",
        'title': "Slime Morimori Dragon Quest - Shougeki no Shippo Dan",
    },
    "SURFS UP    BXUE": {
        'uttd': "BXUE",
        'title': "Surf's Up",
    },
    "SWEET DREAMSB4TE": {
        'uttd': "B4TE",
        'title': "Strawberry Shortcake - Sweet Dreams",
    },
    "SWORDCRAFT2 BSKE": {
        'uttd': "BSKE",
        'title': "Summon Night - Swordcraft Story 2",
    },
    "SWORD OF MANAVSE": {
        'uttd': "AVSE",
        'title': "Sword of Mana",
    },
    "SWORD OF MANAVSP": {
        'uttd': "AVSP",
        'title': "Sword of Mana",
    },
    "SWORD OF MANAVSX": {
        'uttd': "AVSX",
        'title': "Sword of Mana",
    },
    "SWORD OF MANAVSY": {
        'uttd': "AVSY",
        'title': "Sword of Mana",
    },
    "SYLVANIA4   A4LJ": {
        'uttd': "A4LJ",
        'title': "Sylvanian Families 4 - Meguru Kisetsu no Tapestry",
    },
    "SYLVANIA5   BS5J": {
        'uttd': "BS5J",
        'title': "Silvanian Family - Yousei no Stick to Fushigi no Ki - Marron-inu no Onna-no-ko",
    },
    "SYLVANIA6   BSFJ": {
        'uttd': "BSFJ",
        'title': "Sylvania Family - Fashion Designer Ninaritai!",
    },
    "SYOGI       BSGJ": {
        'uttd': "BSGJ",
        'title': "Minna no Soft Series - Minna no Shogi",
    },
    "SYUGA2 HEARTB4LJ": {
        'uttd': "B4LJ",
        'title': "Sugar Sugar Rune - Heart Gaippai! Moegi Gakuen",
    },
    "TACTICSOGRE ATOE": {
        'uttd': "ATOE",
        'title': "Tactics Ogre - The Knight of Lodis",
    },
    "TAK GJC     BJWE": {
        'uttd': "BJWE",
        'title': "Tak - Great Juju Challenge",
    },
    "TAK GJC     BJWX": {
        'uttd': "BJWX",
        'title': "Tak - Great Juju Challenge",
    },
    "TAK&JUJUENG BJUE": {
        'uttd': "BJUE",
        'title': "Tak and the Power of Juju",
    },
    "TAK&JUJUENG BT9E": {
        'uttd': "BT9E",
        'title': "Tak 2 - The Staff of Dreams",
    },
    "TAK&JUJUMULTBJUP": {
        'uttd': "BJUP",
        'title': "Tak and the Power of Juju",
    },
    "TAK&JUJUMULTBJUX": {
        'uttd': "BJUX",
        'title': "Tak and the Power of Juju",
    },
    "TAK&JUJUMULTBT9X": {
        'uttd': "BT9X",
        'title': "Tak 2 - The Staff of Dreams",
    },
    "TAK_RUG_SSPOB44P": {
        'uttd': "B44P",
        'title': "3 Games in 1 - Rugrats - I Gotta Go Party + SpongeBob SquarePants - SuperSponge + Tak and the Power of Juju",
    },
    "TANG TANG   ATAE": {
        'uttd': "ATAE",
        'title': "Tang Tang",
    },
    "TANG TANG   ATAP": {
        'uttd': "ATAP",
        'title': "Tang Tang",
    },
    "TANTEI CLUB1FTKJ": {
        'uttd': "FTKJ",
        'title': "Famicom Mini Vol. 27 - Famicom Tantei Club - Kieta Koukeisha - Zen Kou Hen",
    },
    "TANTEI CLUB2FTUJ": {
        'uttd': "FTUJ",
        'title': "Famicom Mini Vol. 28 - Famicom Tantei Club Part II - Ushiro ni Tatsu Shoujo - Zen Kou Hen",
    },
    "TANTEI-Q2   BTIJ": {
        'uttd': "BTIJ",
        'title': "Tantei Gakuen Q - Kyukyoku Trick ni Idome",
    },
    "TANTEI-Q    BTQJ": {
        'uttd': "BTQJ",
        'title': "Tantei Gakuen Q - Meitantei ha Kimi da!",
    },
    "TARZANRTJ   AJGE": {
        'uttd': "AJGE",
        'title': "Tarzan - Return to the Jungle",
    },
    "TAXI 3      AXQF": {
        'uttd': "AXQF",
        'title': "Taxi 3",
    },
    "TEDDY       ATDJ": {
        'uttd': "ATDJ",
        'title': "Daisuki Teddy",
    },
    "TEEN TITAN 2BZUE": {
        'uttd': "BZUE",
        'title': "Teen Titans 2 - The Brotherhood's Revenge",
    },
    "TEENTITANS  BBLE": {
        'uttd': "BBLE",
        'title': "Teen Titans",
    },
    "TEKKEN ADVANATKP": {
        'uttd': "ATKP",
        'title': "Tekken Advance",
    },
    "TEKKEN      ATKE": {
        'uttd': "ATKE",
        'title': "Tekken Advance",
    },
    "TEKKEN      ATKJ": {
        'uttd': "ATKJ",
        'title': "Tekken Advance",
    },
    "TELEFANG2POWATPJ": {
        'uttd': "ATPJ",
        'title': "Keitai Denjuu Telefang 2 - Power",
    },
    "TELEFANG2SPEATSJ": {
        'uttd': "ATSJ",
        'title': "Keitai Denjuu Telefang 2 - Speed",
    },
    "TENIPURI2   AVAJ": {
        'uttd': "AVAJ",
        'title': "Tennis no Ouji-sama - Aim at the Victory!",
    },
    "TENNISMASTERAT8P": {
        'uttd': "AT8P",
        'title': "Tennis Masters Series 2003",
    },
    "TENPINALLEY2BTPE": {
        'uttd': "BTPE",
        'title': "Ten Pin Alley 2",
    },
    "TERMINATOR 3AO3E": {
        'uttd': "AO3E",
        'title': "Terminator 3 - Rise of the Machines",
    },
    "TERMINATOR 3AO3P": {
        'uttd': "AO3P",
        'title': "Terminator 3 - Rise of the Machines",
    },
    "TETRISWORLDSATWE": {
        'uttd': "ATWE",
        'title': "Tetris Worlds",
    },
    "TETRISWORLDSATWJ": {
        'uttd': "ATWJ",
        'title': "Tetris Worlds",
    },
    "TETRISWORLDSATWX": {
        'uttd': "ATWX",
        'title': "Tetris Worlds",
    },
    "TETRISWORLDSATWY": {
        'uttd': "ATWY",
        'title': "Tetris Worlds",
    },
    "TETSUMAN AGBANTJ": {
        'uttd': "ANTJ",
        'title': "Nippon Pro Mahjong Renmei Kounin Tetsuman Advance - Menkyo Kaiden Series",
    },
    "TETSUYA     ATYJ": {
        'uttd': "ATYJ",
        'title': "Gambler Densetsu Tetsuya - Yomigaeru Densetsu",
    },
    "TEXAS HOLDEMBXAE": {
        'uttd': "BXAE",
        'title': "Texas Hold'em Poker",
    },
    "TGGT-CHAMP  ATCE": {
        'uttd': "ATCE",
        'title': "Top Gear GT Championship",
    },
    "TGGT-CHAMP  ATCP": {
        'uttd': "ATCP",
        'title': "Top Gear GT Championship",
    },
    "TGRALLY     AYEJ": {
        'uttd': "AYEJ",
        'title': "Top Gear Rally",
    },
    "TGRALLY     BTGE": {
        'uttd': "BTGE",
        'title': "Top Gear Rally",
    },
    "TGRALLY     BTGP": {
        'uttd': "BTGP",
        'title': "TG Rally",
    },
    "TGRALLY     BTGX": {
        'uttd': "BTGX",
        'title': "Top Gear Rally",
    },
    "THATSSORAVENBRVE": {
        'uttd': "BRVE",
        'title': "That's So Raven",
    },
    "THEANTBULLY BUYE": {
        'uttd': "BUYE",
        'title': "Ant Bully, The",
    },
    "THEANTBULLY BUYP": {
        'uttd': "BUYP",
        'title': "Ant Bully, The",
    },
    "THE CAT IN TAQTP": {
        'uttd': "AQTP",
        'title': "Dr. Seuss' The Cat in the Hat",
    },
    "THE GAME OF B3UE": {
        'uttd': "B3UE",
        'title': "Life - Yahtzee - Payday",
    },
    "THE GRIM ADVBIEE": {
        'uttd': "BIEE",
        'title': "Grim Adventures of Billy & Mandy, The",
    },
    "THE INVINCIBAIOE": {
        'uttd': "AIOE",
        'title': "Invincible Iron Man, The",
    },
    "THE LOST VIKALVP": {
        'uttd': "ALVP",
        'title': "Lost Vikings, The",
    },
    "THEMUMMY    AUME": {
        'uttd': "AUME",
        'title': "Mummy, The",
    },
    "THE MUMMY   AUMP": {
        'uttd': "AUMP",
        'title': "Mummy, The",
    },
    "THE REVENGE A3RP": {
        'uttd': "A3RP",
        'title': "Revenge of Shinobi, The",
    },
    "THE REVENGE A7SP": {
        'uttd': "A7SP",
        'title': "Smurfs, The - The Revenge of the Smurfs",
    },
    "THE SIMS 2  B46E": {
        'uttd': "B46E",
        'title': "Sims 2, The",
    },
    "THE SIMS ADVASIE": {
        'uttd': "ASIE",
        'title': "Sims, The - Bustin' Out",
    },
    "THE SIMS ADVB4PJ": {
        'uttd': "B4PJ",
        'title': "Sims, The",
    },
    "THE TOWER   BTRJ": {
        'uttd': "BTRJ",
        'title': "Welcome to the Tower SP",
    },
    "THE TOWER SPBTRE": {
        'uttd': "BTRE",
        'title': "Welcome to the Tower SP",
    },
    "THE URBZ AGBBOCE": {
        'uttd': "BOCE",
        'title': "Urbz, The - Sims in the City",
    },
    "THE URBZ AGBBOCJ": {
        'uttd': "BOCJ",
        'title': "Urbz, The - Sims in the City",
    },
    "THE WILD    BWLE": {
        'uttd': "BWLE",
        'title': "Wild, The",
    },
    "THIRD AGE   B3AE": {
        'uttd': "B3AE",
        'title': "Lord of the Rings, The - The Third Age",
    },
    "THIRD AGE   B3AJ": {
        'uttd': "B3AJ",
        'title': "Lord of the Rings, The - Uchitsu Kuni Daisanki",
    },
    "THORNBERRYS AWLE": {
        'uttd': "AWLE",
        'title': "Wild Thornberrys Movie, The",
    },
    "TH SK8LAND  BH9E": {
        'uttd': "BH9E",
        'title': "Tony Hawk's American Sk8land",
    },
    "TH SK8LAND  BH9P": {
        'uttd': "BH9P",
        'title': "Tony Hawk's American Sk8land",
    },
    "TH SK8LAND  BH9X": {
        'uttd': "BH9X",
        'title': "Tony Hawk's American Sk8land",
    },
    "THUG2       B2TE": {
        'uttd': "B2TE",
        'title': "Tony Hawk's Underground 2",
    },
    "THUG SLATER BX4E": {
        'uttd': "BX4E",
        'title': "2 Games in 1 - Tony Hawk's Underground + Kelly Slater's Pro Surfer",
    },
    "THUGTHUGTHUGBTOE": {
        'uttd': "BTOE",
        'title': "Tony Hawk's Underground",
    },
    "THUNDERALLEYBTHE": {
        'uttd': "BTHE",
        'title': "Thunder Alley",
    },
    "THUNDERBIRDSATNP": {
        'uttd': "ATNP",
        'title': "Thunderbirds - International Rescue",
    },
    "THUNDERBIRDSBTBE": {
        'uttd': "BTBE",
        'title': "Thunderbirds",
    },
    "TIERPENSION BQTP": {
        'uttd': "BQTP",
        'title': "My Pet Hotel",
    },
    "TIERPENSION BQTX": {
        'uttd': "BQTX",
        'title': "Mijn Dierenpension",
    },
    "TIERPRAXIS  BQVP": {
        'uttd': "BQVP",
        'title': "Meine Tierarztpraxis",
    },
    "TIERPRAXIS  BQVX": {
        'uttd': "BQVX",
        'title': "Mijn Dierenpraktijk",
    },
    "TIGERWOODS04BTWE": {
        'uttd': "BTWE",
        'title': "Tiger Woods PGA Tour 2004",
    },
    "TIGER WOODS AT5E": {
        'uttd': "AT5E",
        'title': "Tiger Woods PGA Tour Golf",
    },
    "TIGER WOODS AT5X": {
        'uttd': "AT5X",
        'title': "Tiger Woods PGA Tour Golf",
    },
    "TIRETBUT    ATVP": {
        'uttd': "ATVP",
        'title': "Tir et But - Edition Champions du Monde",
    },
    "TITEUF DUO  BT5F": {
        'uttd': "BT5F",
        'title': "2 Games in 1 - Titeuf - Ze Gagmachine + Titeuf - Mega Compet'",
    },
    "TITEUF THE CBTCF": {
        'uttd': "BTCF",
        'title': "Titeuf - Mega Compet'",
    },
    "TITEUF ZE GAAT7F": {
        'uttd': "AT7F",
        'title': "Titeuf - Ze Gagmachine",
    },
    "TITEUF, ZE GAT7P": {
        'uttd': "AT7P",
        'title': "Tootuff - The Gagmachine",
    },
    "TLOS:ANB    B3YE": {
        'uttd': "B3YE",
        'title': "Legend of Spyro, The - A New Beginning",
    },
    "TLOS:ANB    B3YP": {
        'uttd': "B3YP",
        'title': "Legend of Spyro, The - A New Beginning",
    },
    "TMNT      01MTME": {
        'uttd': "MTME",
        'title': "Game Boy Advance Video - Teenage Mutant Ninja Turtles - Volume 1",
    },
    "TMNT        BEXE": {
        'uttd': "BEXE",
        'title': "TMNT",
    },
    "TMNT        BEXP": {
        'uttd': "BEXP",
        'title': "TMNT",
    },
    "TMNT GBA 1+2BT8E": {
        'uttd': "BT8E",
        'title': "2 Games in 1 - Teenage Mutant Ninja Turtles + Teenage Mutant Ninja Turtles 2 - Battle Nexus",
    },
    "TMNT GBA 1+2BT8P": {
        'uttd': "BT8P",
        'title': "2 Games in 1 - Teenage Mutant Ninja Turtles + Teenage Mutant Ninja Turtles 2 - Battle Nexus",
    },
    "TMNT GBA 2  BT2E": {
        'uttd': "BT2E",
        'title': "Teenage Mutant Ninja Turtles 2 - Battle Nexus",
    },
    "TMNT GBA 2  BT2P": {
        'uttd': "BT2P",
        'title': "Teenage Mutant Ninja Turtles 2 - Battle Nexus",
    },
    "TMNT GBA    BNTE": {
        'uttd': "BNTE",
        'title': "Teenage Mutant Ninja Turtles",
    },
    "TMNT GBA    BNTP": {
        'uttd': "BNTP",
        'title': "Teenage Mutant Ninja Turtles",
    },
    "TMNTV01FR000MTMF": {
        'uttd': "MTMF",
        'title': "Game Boy Advance Video - Teenage Mutant Ninja Turtles - Le Demenagement",
    },
    "TOCA        ATQP": {
        'uttd': "ATQP",
        'title': "TOCA World Touring Cars",
    },
    "TOGRE GAIDENATOJ": {
        'uttd': "ATOJ",
        'title': "Tactics Ogre Gaiden - The Knight of Lodis",
    },
    "TOKON HEAT  A59J": {
        'uttd': "A59J",
        'title': "Toukon Heat",
    },
    "TOKYO MYUMYUAM7J": {
        'uttd': "AM7J",
        'title': "Hamepane - Tokyo Mew Mew",
    },
    "TOMAJERRYGBABJTE": {
        'uttd': "BJTE",
        'title': "Tom and Jerry Tales",
    },
    "TOMAJERRYGBABJTP": {
        'uttd': "BJTP",
        'title': "Tom and Jerry Tales",
    },
    "TOM AND JERRAIFE": {
        'uttd': "AIFE",
        'title': "Tom and Jerry in Infurnal Escape",
    },
    "TOM AND JERRAIFP": {
        'uttd': "AIFP",
        'title': "Tom and Jerry in Infurnal Escape",
    },
    "TOMATO_ADV  AGLJ": {
        'uttd': "AGLJ",
        'title': "Tomato Adventure",
    },
    "TOMB RAIDER AL9E": {
        'uttd': "AL9E",
        'title': "Tomb Raider - The Prophecy",
    },
    "TOMB-RAIDER AL9P": {
        'uttd': "AL9P",
        'title': "Tomb Raider - The Prophecy",
    },
    "TOMB-RAIDER AUTJ": {
        'uttd': "AUTJ",
        'title': "Tomb Raider - The Prophecy",
    },
    "TOMB RAIDER BL8E": {
        'uttd': "BL8E",
        'title': "Tomb Raider - Legend",
    },
    "TOMB RAIDER BL8P": {
        'uttd': "BL8P",
        'title': "Tomb Raider - Legend",
    },
    "TOM CLANCY'SAO4P": {
        'uttd': "AO4P",
        'title': "Tom Clancy's Splinter Cell",
    },
    "TOM CLANCY'SBSLE": {
        'uttd': "BSLE",
        'title': "Tom Clancy's Splinter Cell - Pandora Tomorrow",
    },
    "TOMJERRYRINGATJE": {
        'uttd': "ATJE",
        'title': "Tom and Jerry - The Magic Ring",
    },
    "TOMJERRYRINTATJP": {
        'uttd': "ATJP",
        'title': "Tom and Jerry - The Magic Ring",
    },
    "TONKA ON JOBBT7E": {
        'uttd': "BT7E",
        'title': "Tonka - On the Job",
    },
    "TONY HAWK 2!ATHD": {
        'uttd': "ATHD",
        'title': "Tony Hawk's Pro Skater 2",
    },
    "TONY HAWK 2!ATHE": {
        'uttd': "ATHE",
        'title': "Tony Hawk's Pro Skater 2",
    },
    "TONY HAWK 2!ATHF": {
        'uttd': "ATHF",
        'title': "Tony Hawk's Pro Skater 2",
    },
    "TONY HAWK 3!AT3D": {
        'uttd': "AT3D",
        'title': "Tony Hawk's Pro Skater 3",
    },
    "TONY HAWK 3!AT3E": {
        'uttd': "AT3E",
        'title': "Tony Hawk's Pro Skater 3",
    },
    "TONY HAWK 3!AT3F": {
        'uttd': "AT3F",
        'title': "Tony Hawk's Pro Skater 3",
    },
    "TONY HAWK 4!AT6E": {
        'uttd': "AT6E",
        'title': "Tony Hawk's Pro Skater 4",
    },
    "TONYHAWKDJ  BXSP": {
        'uttd': "BXSP",
        'title': "Tony Hawk's Downhill Jam",
    },
    "TONY HAWK'S BXSE": {
        'uttd': "BXSE",
        'title': "Tony Hawk's Downhill Jam",
    },
    "TOPGUN CZ   A2YE": {
        'uttd': "A2YE",
        'title': "Top Gun - Combat Zones",
    },
    "TOPGUN FSTA ATGE": {
        'uttd': "ATGE",
        'title': "Top Gun - Firestorm Advance",
    },
    "TOP SPIN 2  B27E": {
        'uttd': "B27E",
        'title': "Top Spin 2",
    },
    "TOP SPIN 2  B27P": {
        'uttd': "B27P",
        'title': "Top Spin 2",
    },
    "TORUNEKO2   AT2J": {
        'uttd': "AT2J",
        'title': "Dragon Quest Characters - Torneco no Daibouken 2 Advance - Fushigi no Dungeon",
    },
    "TOTALLYSPIESBTUE": {
        'uttd': "BTUE",
        'title': "Totally Spies!",
    },
    "TOTALLYSPIESBTUP": {
        'uttd': "BTUP",
        'title': "Totally Spies!",
    },
    "TOTALSOCCER ATUJ": {
        'uttd': "ATUJ",
        'title': "Total Soccer Advance",
    },
    "TOTAL SOCCERATUP": {
        'uttd': "ATUP",
        'title': "Total Soccer",
    },
    "TOWERSHAFT  BABJ": {
        'uttd': "BABJ",
        'title': "Aleck Bordon Adventure - Tower & Shaft Advance",
    },
    "TOWNARIKIRI3B3TJ": {
        'uttd': "B3TJ",
        'title': "Tales of the World - Narikiri Dungeon 3",
    },
    "TOW SUMMLINEA9PJ": {
        'uttd': "A9PJ",
        'title': "Tales of the World - Summoner's Lineage",
    },
    "TOYROBOFORCEATRJ": {
        'uttd': "ATRJ",
        'title': "Toyrobo Force",
    },
    "TRAP2 MINAMIAODJ": {
        'uttd': "AODJ",
        'title': "Minami no Umi no Odyssey",
    },
    "TRINGO      BTJE": {
        'uttd': "BTJE",
        'title': "Tringo",
    },
    "TRINGO      BTJP": {
        'uttd': "BTJP",
        'title': "Tringo",
    },
    "TROLLZHAIRAFBT6E": {
        'uttd': "BT6E",
        'title': "Trollz - Hair Affair!",
    },
    "TROLLZHAIRAFBT6P": {
        'uttd': "BT6P",
        'title': "Trollz - Hair Affair!",
    },
    "TROLLZHAIRAFBT6X": {
        'uttd': "BT6X",
        'title': "Trollz - Hair Affair!",
    },
    "TROLLZHAIRAFBT6Y": {
        'uttd': "BT6Y",
        'title': "Trollz - Hair Affair!",
    },
    "TRON 2.0 KILBTNE": {
        'uttd': "BTNE",
        'title': "Tron 2.0 - Killer App",
    },
    "TRON 2.0 KILBTNP": {
        'uttd': "BTNP",
        'title': "Tron 2.0 - Killer App",
    },
    "TRUCKS/FURY BWQE": {
        'uttd': "BWQE",
        'title': "2 Games in 1 - Quad Desert Fury + Monster Trucks",
    },
    "TRUCKS&QUAD BWQP": {
        'uttd': "BWQP",
        'title': "2 Games in 1 - Quad Desert Fury + Monster Trucks",
    },
    "TS MANAGER  ATFP": {
        'uttd': "ATFP",
        'title': "Total Soccer Manager",
    },
    "TSPIES 2    B2LE": {
        'uttd': "B2LE",
        'title': "Totally Spies! 2 - Undercover",
    },
    "TSPIES 2    B2LP": {
        'uttd': "B2LP",
        'title': "Totally Spies! 2 - Undercover",
    },
    "TSTAR       B9SP": {
        'uttd': "B9SP",
        'title': "Trick Star",
    },
    "TSUBASA 2001AKYJ": {
        'uttd': "AKYJ",
        'title': "Captain Tsubasa - Eikou no Kiseki",
    },
    "TTABBD      ATTE": {
        'uttd': "ATTE",
        'title': "Tiny Toon Adventures - Scary Dreams",
    },
    "TTABBD      ATTP": {
        'uttd': "ATTP",
        'title': "Tiny Toon Adventures - Buster's Bad Dream",
    },
    "TTA-WACKY   AWSE": {
        'uttd': "AWSE",
        'title': "Tiny Toon Adventures - Wacky Stackers",
    },
    "TTA-WACKY   AWSP": {
        'uttd': "AWSP",
        'title': "Tiny Toon Adventures - Wacky Stackers",
    },
    "TURBO TURTLEAK3E": {
        'uttd': "AK3E",
        'title': "Turbo Turtle Adventure",
    },
    "TUROK EVOL  AT4E": {
        'uttd': "AT4E",
        'title': "Turok Evolution",
    },
    "TUROK EVOL  AT4P": {
        'uttd': "AT4P",
        'title': "Turok Evolution",
    },
    "TUWAMONOGBA B2OJ": {
        'uttd': "B2OJ",
        'title': "Pro Mahjong Tsuwamono Advance",
    },
    "TWEETY MAGICATMD": {
        'uttd': "ATMD",
        'title': "Tweety and the Magic Gems",
    },
    "TWEETY MAGICATME": {
        'uttd': "ATME",
        'title': "Tweety and the Magic Gems",
    },
    "TWEETY MAGICATMF": {
        'uttd': "ATMF",
        'title': "Titi et les Bijoux Magiques",
    },
    "TWEETY MAGICATMP": {
        'uttd': "ATMP",
        'title': "Tweety and the Magic Gems",
    },
    "TWEETY PARTYAMJJ": {
        'uttd': "AMJJ",
        'title': "Tweety no Hearty Party",
    },
    "TWINBEE     FTWJ": {
        'uttd': "FTWJ",
        'title': "Famicom Mini Vol. 19 - Twin Bee",
    },
    "TWIN SERIES1BFVJ": {
        'uttd': "BFVJ",
        'title': "Twin Series 1 - Mezase Debut! Fashion Designer Monogatari + Kawaii Pet Game Gallery 2",
    },
    "TWIN SERIES3BQMJ": {
        'uttd': "BQMJ",
        'title': "Twin Series 3 - Insect Monster + Suchai Labyrinth",
    },
    "TWIN SERIES4BHFJ": {
        'uttd': "BHFJ",
        'title': "Twin Series 4 - Hamu Hamu Monster EX + F Puzzle Hamusuta",
    },
    "TWIN SERIES5BMWJ": {
        'uttd': "BMWJ",
        'title': "Twin Series 5 - Wanwan Meitantei EX + Manou no Kuni no Cake House",
    },
    "TWIN SERIES6BWNJ": {
        'uttd': "BWNJ",
        'title': "Twin Series 6 - Wannyan Idol Gakuen + Koinu to Issho",
    },
    "TWIN SERIES7B2PJ": {
        'uttd': "B2PJ",
        'title': "Twin Series 7 - Twin Puzzle - Kisekae Wanko Ex + Puzzle Rainbow Magic 2",
    },
    "TWO TOWERS  ALPE": {
        'uttd': "ALPE",
        'title': "Lord of the Rings, The - The Two Towers",
    },
    "TWO TOWERS  ALPJ": {
        'uttd': "ALPJ",
        'title': "Lord of the Rings, The - Futatsu no Tou",
    },
    "TXRA        BTZE": {
        'uttd': "BTZE",
        'title': "Tokyo Xtreme Racer Advance",
    },
    "TXRA        BTZP": {
        'uttd': "BTZP",
        'title': "Tokyo Xtreme Racer Advance",
    },
    "TY3         BTVE": {
        'uttd': "BTVE",
        'title': "Ty the Tasmanian Tiger - Night of the Quinkan",
    },
    "TYBUSHRESCUEBTYE": {
        'uttd': "BTYE",
        'title': "Ty the Tasmanian Tiger 2 - Bush Rescue",
    },
    "TYSON BOXINGAM6E": {
        'uttd': "AM6E",
        'title': "Mike Tyson Boxing",
    },
    "TYSON BOXINGAM9P": {
        'uttd': "AM9P",
        'title': "Mike Tyson Boxing",
    },
    "UBG         ABUE": {
        'uttd': "ABUE",
        'title': "Ultimate Brain Games",
    },
    "UCG         BUCE": {
        'uttd': "BUCE",
        'title': "Ultimate Card Games",
    },
    "UEKIJINGIBTLBUHJ": {
        'uttd': "BUHJ",
        'title': "Ueki no Housoku",
    },
    "UI IRE      AEWJ": {
        'uttd': "AEWJ",
        'title': "Ui-Ire - World Soccer Winning Eleven",
    },
    "UKICANI     ACLJ": {
        'uttd': "ACLJ",
        'title': "Sakura Momoko no UkiUki Carnival",
    },
    "ULT ARCADE  BUZE": {
        'uttd': "BUZE",
        'title': "Ultimate Arcade Games",
    },
    "ULTIMATE BEAAVEE": {
        'uttd': "AVEE",
        'title': "Ultimate Beach Soccer",
    },
    "ULTIMATE PUZBUAE": {
        'uttd': "BUAE",
        'title': "Ultimate Puzzle Games",
    },
    "ULTRAGUARDMABUTJ": {
        'uttd': "BUTJ",
        'title': "Ultra Keibitai - Monster Attack",
    },
    "ULTRAMAN    BU6J": {
        'uttd': "BU6J",
        'title': "Taiketsu! Ultra Hero",
    },
    "ULTSPIDERMANBULE": {
        'uttd': "BULE",
        'title': "Ultimate Spider-Man",
    },
    "ULTSPIDERMANBULP": {
        'uttd': "BULP",
        'title': "Ultimate Spider-Man",
    },
    "ULTSPIDERMANBULX": {
        'uttd': "BULX",
        'title': "Ultimate Spider-Man",
    },
    "UMUSCLE     AK2E": {
        'uttd': "AK2E",
        'title': "Ultimate Muscle - The Kinnikuman Legacy - The Path of the Superhero",
    },
    "UNFABULOUS  BU4E": {
        'uttd': "BU4E",
        'title': "Unfabulous!",
    },
    "UNIEUROLOTR ALOP": {
        'uttd': "ALOP",
        'title': "Lord of the Rings, The - The Fellowship of the Ring",
    },
    "UNIVERSLOTR ALOE": {
        'uttd': "ALOE",
        'title': "Lord of the Rings, The - The Fellowship of the Ring",
    },
    "UNO 52      BU5E": {
        'uttd': "BU5E",
        'title': "Uno 52",
    },
    "UNO 52      BU5P": {
        'uttd': "BU5P",
        'title': "Uno 52",
    },
    "UNO FREEFALLBUIE": {
        'uttd': "BUIE",
        'title': "Uno Free Fall",
    },
    "UNO FREEFALLBUIP": {
        'uttd': "BUIP",
        'title': "Uno Free Fall",
    },
    "UNOSKIPBO   BUQP": {
        'uttd': "BUQP",
        'title': "2 Games in 1 - Uno + Skip-Bo",
    },
    "UNOUNOSKIPBOBUQE": {
        'uttd': "BUQE",
        'title': "2 Games in 1 - Uno + Skip-Bo",
    },
    "URBANYETI   AYIE": {
        'uttd': "AYIE",
        'title': "Urban Yeti!",
    },
    "UWINTERGAMESBUWE": {
        'uttd': "BUWE",
        'title': "Ultimate Winter Games",
    },
    "VANDELBUSTERBOVJ": {
        'uttd': "BOVJ",
        'title': "Bouken-Ou Beet - Busters Road",
    },
    "VAN HELSING BANE": {
        'uttd': "BANE",
        'title': "Van Helsing",
    },
    "VAN HELSING BANP": {
        'uttd': "BANP",
        'title': "Van Helsing",
    },
    "VATTROLLERX1BRXJ": {
        'uttd': "BRXJ",
        'title': "Vattroller X",
    },
    "VIOLENCE-K  BZGJ": {
        'uttd': "BZGJ",
        'title': "Zettaizetsumei Dangerous Jiisan - Naki no Ikkai Zettai Fukujuu Violence Kouchou",
    },
    "VIP         AVPP": {
        'uttd': "AVPP",
        'title': "V.I.P.",
    },
    "VIRTKASPAROVAVKE": {
        'uttd': "AVKE",
        'title': "Virtual Kasparov",
    },
    "VIRTKASPAROVAVKP": {
        'uttd': "AVKP",
        'title': "Virtual Kasparov",
    },
    "VIRTUA TENNIAVTP": {
        'uttd': "AVTP",
        'title': "Virtua Tennis",
    },
    "VIRTUATENNISAVTE": {
        'uttd': "AVTE",
        'title': "Virtua Tennis",
    },
    "VMASTERCROSSAVMJ": {
        'uttd': "AVMJ",
        'title': "V-Master Cross",
    },
    "VRALLY 3    AVRE": {
        'uttd': "AVRE",
        'title': "V-Rally 3",
    },
    "VRALLY 3    AVRJ": {
        'uttd': "AVRJ",
        'title': "V-Rally 3",
    },
    "V-RALLY 3   AVRP": {
        'uttd': "AVRP",
        'title': "V-Rally 3",
    },
    "WADE HIXTONSBSRE": {
        'uttd': "BSRE",
        'title': "Wade Hixton's Counter Punch",
    },
    "WAIWAI      AKWJ": {
        'uttd': "AKWJ",
        'title': "Konami Wai Wai Racing Advance",
    },
    "WANKOMIKKUSUBWXJ": {
        'uttd': "BWXJ",
        'title': "Wanko Mix - Chiwanko World",
    },
    "WANKURU     BWKJ": {
        'uttd': "BWKJ",
        'title': "Wanko de Kururin! Wancle",
    },
    "WANNYANIDOL BWAJ": {
        'uttd': "BWAJ",
        'title': "Majokko Cream-chan no Gokko Series 1 - Wannyan Idol Gakuen",
    },
    "WAN TANTEI  BWMJ": {
        'uttd': "BWMJ",
        'title': "WanWan Meitantei",
    },
    "WARIOLAND   AWAJ": {
        'uttd': "AWAJ",
        'title': "Wario Land Advance",
    },
    "WARIOLANDE  AWAC": {
        'uttd': "AWAC",
        'title': "Waliou Xunbao Ji",
    },
    "WARIOLANDE  AWAE": {
        'uttd': "AWAE",
        'title': "Wario Land 4",
    },
    "WARIOTWISTEDRZWE": {
        'uttd': "RZWE",
        'title': "WarioWare - Twisted!",
    },
    "WARIOWAREINCAZWC": {
        'uttd': "AZWC",
        'title': "Waliou Zhizao",
        'icon0': 'https://images.launchbox-app.com/3a73f46b-8f2d-48eb-a0e7-dce3021e4075.png',
        'pic0': 'https://images.launchbox-app.com/aaa2b723-93e1-413e-9889-e87f751c9242.png',
        'pic1': 'https://images.launchbox-app.com/85dc2462-9b5b-481f-894c-2ddc4266f2ac.jpg',
        'snd0': 'https://www.youtube.com/watch?v=G4EQLdH4UVc&list=PLjyLjyXJQJUPePFzsfvc-AtVPLUJ1qsrv&index=1',
    },
    "WARIOWAREINCAZWE": {
        'uttd': "AZWE",
        'title': "WarioWare, Inc. - Mega Microgame$!",
        'icon0': 'https://images.launchbox-app.com/9fb1b982-cb23-44d3-8066-1ebe3eeee661.jpg',
        'pic0': 'https://images.launchbox-app.com/34d3c1ca-b813-4273-b746-ab0a223a533f.png',
        'pic1': 'https://images.launchbox-app.com/85dc2462-9b5b-481f-894c-2ddc4266f2ac.jpg',
        'snd0': 'https://www.youtube.com/watch?v=G4EQLdH4UVc&list=PLjyLjyXJQJUPePFzsfvc-AtVPLUJ1qsrv&index=1',
    },
    "WARIOWAREINCAZWP": {
        'uttd': "AZWP",
        'title': "WarioWare, Inc. - Minigame Mania",
        'icon0': 'https://images.launchbox-app.com/36209cf7-49d9-4f10-82d8-e33c72137269.jpg',
        'pic0': 'https://images.launchbox-app.com/d3ce4feb-8648-47a8-959f-fab8dc16ff4a.png',
        'pic1': 'https://images.launchbox-app.com/85dc2462-9b5b-481f-894c-2ddc4266f2ac.jpg',
        'snd0': 'https://www.youtube.com/watch?v=G4EQLdH4UVc&list=PLjyLjyXJQJUPePFzsfvc-AtVPLUJ1qsrv&index=1',
    },
    "W.A.SOCCER_WAASJ": {
        'uttd': "AASJ",
        'title': "World Advance Soccer - Shouri heno Michi",
    },
    "WATASHI-MK  AW3J": {
        'uttd': "AW3J",
        'title': "Watashi no Makesalon",
    },
    "WCPOKER     BP9E": {
        'uttd': "BP9E",
        'title': "World Championship Poker",
    },
    "WCPOKER     BP9P": {
        'uttd': "BP9P",
        'title': "World Championship Poker",
    },
    "Whac-A-Mole BWEE": {
        'uttd': "BWEE",
        'title': "Whac-A-Mole",
    },
    "WHISTLE!    A73J": {
        'uttd': "A73J",
        'title': "Whistle! - Dai 37 Kai Tokyo-to Chuugakkou Sougou Taiiku Soccer Taikai",
    },
    "WHO WANTS TOBWJP": {
        'uttd': "BWJP",
        'title': "Who Wants to Be a Millionaire Junior",
    },
    "WILDEKERLE01BWUD": {
        'uttd': "BWUD",
        'title': "Die Wilden Fussball Kerle - Entscheidung im Teufelstopf",
    },
    "WILDEKERLE02BXWD": {
        'uttd': "BXWD",
        'title': "Wilden Fussball-Kerle, Die - Gefahr im Wilde Kerle Land",
    },
    "WING COMMANDAW9E": {
        'uttd': "AW9E",
        'title': "Wing Commander - Prophecy",
    },
    "WING COMMANDAW9P": {
        'uttd': "AW9P",
        'title': "Wing Commander - Prophecy",
    },
    "WINGS       AWQE": {
        'uttd': "AWQE",
        'title': "Wings",
    },
    "WINGS       AWQP": {
        'uttd': "AWQP",
        'title': "Wings",
    },
    "WINNIE-RM3  BWZP": {
        'uttd': "BWZP",
        'title': "2 Games in 1 - Winnie the Pooh's - Rumbly Tumbly Adventure + Rayman 3",
    },
    "WINNIE THE PBWHE": {
        'uttd': "BWHE",
        'title': "Winnie the Pooh's - Rumbly Tumbly Adventure",
    },
    "WINNIE THE PBWHP": {
        'uttd': "BWHP",
        'title': "Winnie the Pooh's - Rumbly Tumbly Adventure",
    },
    "WINNINGPOST AWPJ": {
        'uttd': "AWPJ",
        'title': "Winning Post",
    },
    "WINTERSPIELEBWYP": {
        'uttd': "BWYP",
        'title': "Winter Sports",
    },
    "WINTERSPORTSAWIE": {
        'uttd': "AWIE",
        'title': "ESPN International Winter Sports 2002",
    },
    "WINTERSPORTSAWIP": {
        'uttd': "AWIP",
        'title': "ESPN International Winter Sports 2002",
    },
    "WINXCLUB    BWIE": {
        'uttd': "BWIE",
        'title': "Winx Club",
    },
    "WINXCLUB    BWIP": {
        'uttd': "BWIP",
        'title': "Winx Club",
    },
    "WINXQFTCDX  BWVE": {
        'uttd': "BWVE",
        'title': "Winx Club - Quest for the Codex",
    },
    "WINXQFTCDX  BWVP": {
        'uttd': "BWVP",
        'title': "Winx Club - Quest for the Codex",
    },
    "W.I.T.C.H.  BWTP": {
        'uttd': "BWTP",
        'title': "W.i.t.c.h.",
    },
    "WIZ SUMMONERAWZJ": {
        'uttd': "AWZJ",
        'title': "Wizardry Summoner",
    },
    "WLDTHRNBRRYSAWTD": {
        'uttd': "AWTD",
        'title': "Expedition der Stachelbeeren - Zoff im Zoo",
    },
    "WOLF3D      AWOE": {
        'uttd': "AWOE",
        'title': "Wolfenstein 3-D",
    },
    "WOLF3D      AWOP": {
        'uttd': "AWOP",
        'title': "Wolfenstein 3-D",
    },
    "WORLD TENNISAWCE": {
        'uttd': "AWCE",
        'title': "World Tennis Stars",
    },
    "WORLD TENNISAWCP": {
        'uttd': "AWCP",
        'title': "World Tennis Stars",
    },
    "WORMS BLAST AWBP": {
        'uttd': "AWBP",
        'title': "Worms Blast",
    },
    "WORMSWORLDPTAWYE": {
        'uttd': "AWYE",
        'title': "Worms World Party",
    },
    "WORMSWORLDPTAWYP": {
        'uttd': "AWYP",
        'title': "Worms World Party",
    },
    "WPT2K6      B26E": {
        'uttd': "B26E",
        'title': "World Poker Tour",
    },
    "WPT2K6      BWOP": {
        'uttd': "BWOP",
        'title': "World Poker Tour",
    },
    "WRECKINGCREWFWCJ": {
        'uttd': "FWCJ",
        'title': "Famicom Mini Vol. 14 - Wrecking Crew",
    },
    "WS POCKET 2 AJKJ": {
        'uttd': "AJKJ",
        'title': "Jikkyou World Soccer Pocket 2",
    },
    "W.S.POCKET  AJWJ": {
        'uttd': "AJWJ",
        'title': "Jikkyou World Soccer Pocket",
    },
    "WTATOUR     ACIJ": {
        'uttd': "ACIJ",
        'title': "WTA Tour Tennis Pocket",
    },
    "WTATOUR     ATEE": {
        'uttd': "ATEE",
        'title': "WTA Tour Tennis",
    },
    "WTATOUR     ATEP": {
        'uttd': "ATEP",
        'title': "Pro Tennis WTA Tour",
    },
    "WWCC5       AWWE": {
        'uttd': "AWWE",
        'title': "Woody Woodpecker in Crazy Castle 5",
    },
    "WWCC5       AWWJ": {
        'uttd': "AWWJ",
        'title': "Woody Woodpecker - Crazy Castle 5",
    },
    "WWCC5       AWWP": {
        'uttd': "AWWP",
        'title': "Woody Woodpecker in Crazy Castle 5",
    },
    "WWE_RTWM_X8 AW8E": {
        'uttd': "AW8E",
        'title': "WWE - Road to WrestleMania X8",
    },
    "WWE_SURVIVORBWWE": {
        'uttd': "BWWE",
        'title': "WWE - Survivor Series",
    },
    "WWF_ROAD_WM AWFE": {
        'uttd': "AWFE",
        'title': "WWF - Road to WrestleMania",
    },
    "WWTBAM      A55D": {
        'uttd': "A55D",
        'title': "Wer wird Millionar",
    },
    "WWTBAM      A55F": {
        'uttd': "A55F",
        'title': "Qui Veut Gagner des millions",
    },
    "WWTBAM      A55H": {
        'uttd': "A55H",
        'title': "Weekend Miljonairs",
    },
    "WWTBAM      A55I": {
        'uttd': "A55I",
        'title': "Chi Vuol Essere Milionario",
    },
    "WWTBAM      A55P": {
        'uttd': "A55P",
        'title': "Who Wants to Be a Millionaire",
    },
    "WWTBAM      A55S": {
        'uttd': "A55S",
        'title': "Quiere ser Millonario",
    },
    "WWTBAM      A55U": {
        'uttd': "A55U",
        'title': "Who Wants to Be a Millionaire",
    },
    "WWTBAM      B55P": {
        'uttd': "B55P",
        'title': "Who Wants to Be a Millionaire - 2nd Edition",
    },
    "X2 WOLVERINEAWVE": {
        'uttd': "AWVE",
        'title': "X2 - Wolverine's Revenge",
    },
    "X2 WOLVERINEAWVF": {
        'uttd': "AWVF",
        'title': "X-Men 2 - La Vengeance de Wolverine",
    },
    "X-BLADEZ    AXIE": {
        'uttd': "AXIE",
        'title': "X-Bladez - Inline Skater",
    },
    "XBLADEZ: INLAXIP": {
        'uttd': "AXIP",
        'title': "X-Bladez - Inline Skater",
    },
    "XEVIOUS     FXVE": {
        'uttd': "FXVE",
        'title': "Classic NES Series - Xevious",
    },
    "XEVIOUS     FXVJ": {
        'uttd': "FXVJ",
        'title': "Famicom Mini Vol. 07 - Xevious",
    },
    "XMENROA     AXME": {
        'uttd': "AXME",
        'title': "X-Men - Reign of Apocalypse",
    },
    "X-MEN: THE OB3XE": {
        'uttd': "B3XE",
        'title': "X-Men III - The Official Game",
    },
    "X-MEN: THE OB3XP": {
        'uttd': "B3XP",
        'title': "X-Men III - The Official Game",
    },
    "XS MOTO     BXME": {
        'uttd': "BXME",
        'title': "XS Moto",
    },
    "XXX         AX3E": {
        'uttd': "AX3E",
        'title': "xXx",
    },
    "XXX         AX3F": {
        'uttd': "AX3F",
        'title': "xXx",
    },
    "YAKUMAN     AYAJ": {
        'uttd': "AYAJ",
        'title': "Dokodemo Taikyoku - Yakuman Advance",
    },
    "YAKUTUKUADV ALMJ": {
        'uttd': "ALMJ",
        'title': "Pro Yakyuu Team wo Tsukurou! Advance",
    },
    "YAMADAHAJIMEBSYJ": {
        'uttd': "BSYJ",
        'title': "Sentouin Yamada Hajime",
    },
    "YGGDRA UNIONBYUE": {
        'uttd': "BYUE",
        'title': "Yggdra Union - We'll Never Fight Alone",
    },
    "YGGDRA UNIONBYUJ": {
        'uttd': "BYUJ",
        'title': "Yggdra Union",
    },
    "YOSHI'S U/G KYGJ": {
        'uttd': "KYGJ",
        'title': "Yoshi no Banyu Inryoku",
    },
    "YOSHI'S U/G KYGP": {
        'uttd': "KYGP",
        'title': "Yoshi's Universal Gravitation",
    },
    "YOSHI TOPSY KYGE": {
        'uttd': "KYGE",
        'title': "Yoshi Topsy-Turvy",
    },
    "YOUKAIDOU   AFUJ": {
        'uttd': "AFUJ",
        'title': "Youkaidou",
    },
    "Y-RHAPSODY  AYRJ": {
        'uttd': "AYRJ",
        'title': "Narikiri Jockey Game - Yuushun Rhapsody",
    },
    "YUGIOH01FR00MYGF": {
        'uttd': "MYGF",
        'title': "Game Boy Advance Video - Yu-Gi-Oh! Yugi vs. Joey",
    },
    "YUGIOH    01MYGE": {
        'uttd': "MYGE",
        'title': "Game Boy Advance Video - Yu-Gi-Oh! Yugi vs. Joey - Volume 1",
    },
    "YUGIOH 2IN1 BY2E": {
        'uttd': "BY2E",
        'title': "2 Games in 1 - Yu-Gi-Oh! The Sacred Cards + Yu-Gi-Oh! Reshef of Destruction",
    },
    "YUGIOH 2IN1 BY2P": {
        'uttd': "BY2P",
        'title': "2 Games in 1 - Yu-Gi-Oh! The Sacred Cards + Yu-Gi-Oh! Reshef of Destruction",
    },
    "YU-GI-OH DDMAYDE": {
        'uttd': "AYDE",
        'title': "Yu-Gi-Oh! Dungeon Dice Monsters",
    },
    "YU-GI-OH DDMAYDJ": {
        'uttd': "AYDJ",
        'title': "Yu-Gi-Oh! Dungeon Dice Monsters",
    },
    "YU-GI-OH DDMAYDP": {
        'uttd': "AYDP",
        'title': "Yu-Gi-Oh! Dungeon Dice Monsters",
    },
    "YUGIOH DM7  AY7E": {
        'uttd': "AY7E",
        'title': "Yu-Gi-Oh! The Sacred Cards",
    },
    "YUGIOH DM7  AY7P": {
        'uttd': "AY7P",
        'title': "Yu-Gi-Oh! The Sacred Cards",
    },
    "YUGIOH DM8  AY8E": {
        'uttd': "AY8E",
        'title': "Yu-Gi-Oh! Reshef of Destruction",
    },
    "YUGIOH DM8  AY8P": {
        'uttd': "AY8P",
        'title': "Yu-Gi-Oh! Reshef of Destruction",
    },
    "YUGIOHDMEX06BY6J": {
        'uttd': "BY6J",
        'title': "Yu-Gi-Oh! Duel Monsters Expert 2006",
    },
    "YUGIOHDMEX3 BY3J": {
        'uttd': "BY3J",
        'title': "Yu-Gi-Oh! Duel Monsters Expert 3",
    },
    "YUGIOHDMGX  BYGJ": {
        'uttd': "BYGJ",
        'title': "Yu-Gi-Oh! Duel Monsters GX - Mezase Duel King!",
    },
    "YUGIOHDMI2  BYIJ": {
        'uttd': "BYIJ",
        'title': "Yu-Gi-Oh! Duel Monsters - International Worldwide Edition 2",
    },
    "YUGIOHDPACK2BYVE": {
        'uttd': "BYVE",
        'title': "2 Games in 1 - Yu-Gi-Oh! Destiny Board Traveler + Yu-Gi-Oh! Dungeon Dice Monsters",
    },
    "YU-GI-OH!EDSAY5E": {
        'uttd': "AY5E",
        'title': "Yu-Gi-Oh! The Eternal Duelist Soul",
    },
    "YUGIOHGXDA  BYGE": {
        'uttd': "BYGE",
        'title': "Yu-Gi-Oh! GX Duel Academy",
    },
    "YUGIOHGXDA  BYGP": {
        'uttd': "BYGP",
        'title': "Yu-Gi-Oh! GX Duel Academy",
    },
    "YUGIOHWCT06 BY6E": {
        'uttd': "BY6E",
        'title': "Yu-Gi-Oh! Ultimate Masters - World Championship Tournament 2006",
    },
    "YUGIOHWCT06 BY6P": {
        'uttd': "BY6P",
        'title': "Yu-Gi-Oh! Ultimate Masters Edition - World Championship Tournament 2006",
    },
    "YUGIOHWWE   AYWE": {
        'uttd': "AYWE",
        'title': "Yu-Gi-Oh! Worldwide Edition - Stairway to the Destined Duel",
    },
    "YUGIOHWWE   AYWJ": {
        'uttd': "AYWJ",
        'title': "Yu-Gi-Oh! Duel Monsters - International Worldwide Edition",
    },
    "YUGIOHWWE   AYWP": {
        'uttd': "AYWP",
        'title': "Yu-Gi-Oh! Worldwide Edition - Stairway to the Destined Duel",
    },
    "YUGIOU DBT  BYDE": {
        'uttd': "BYDE",
        'title': "Yu-Gi-Oh! Destiny Board Traveler",
    },
    "YUGIOU DBT-EBYDP": {
        'uttd': "BYDP",
        'title': "Yu-Gi-Oh! Destiny Board Traveler",
    },
    "YUGIOU DM7  AY7J": {
        'uttd': "AY7J",
        'title': "Yu-Gi-Oh! Duel Monsters 7 - Kettou Toshi Densetsu",
    },
    "YUGIOU DM8  AY8J": {
        'uttd': "AY8J",
        'title': "Yu-Gi-Oh! Duel Monsters 8 - Hametsu no Daijashin",
    },
    "YUGIOU SUGO BYSJ": {
        'uttd': "BYSJ",
        'title': "Yu-Gi-Oh! Sugoroku no Sugoroku",
    },
    "YUYUHAKUSHO1BYYE": {
        'uttd': "BYYE",
        'title': "Yu Yu Hakusho - Spirit Detective",
    },
    "YUYUHAKUSHO1BYYP": {
        'uttd': "BYYP",
        'title': "Yu Yu Hakusho - Spirit Detective",
    },
    "YUYUHAKUSHO2BRGE": {
        'uttd': "BRGE",
        'title': "Yu Yu Hakusho - Tournament Tactics",
    },
    "YWCT2004EUR BYWP": {
        'uttd': "BYWP",
        'title': "Yu-Gi-Oh! World Championship Tournament 2004",
    },
    "YWCT2004USA BYWE": {
        'uttd': "BYWE",
        'title': "Yu-Gi-Oh! World Championship Tournament 2004",
    },
    "YWCT2005EUR BYOP": {
        'uttd': "BYOP",
        'title': "Yu-Gi-Oh! Day of the Duelist - World Championship Tournament 2005",
    },
    "YWCT2005USA BY7E": {
        'uttd': "BY7E",
        'title': "Yu-Gi-Oh! 7 Trials to Glory - World Championship Tournament 2005",
    },
    "ZACKANDCODY BZCE": {
        'uttd': "BZCE",
        'title': "Suite Life of Zack & Cody, The - Tipton Caper",
    },
    "ZAPPER      AZPE": {
        'uttd': "AZPE",
        'title': "Zapper",
    },
    "ZAPPER      AZPP": {
        'uttd': "AZPP",
        'title': "Zapper",
    },
    "ZATCH EA1   A4GE": {
        'uttd': "A4GE",
        'title': "ZatchBell! - Electric Arena",
    },
    "ZELDA 1     FZLE": {
        'uttd': "FZLE",
        'title': "Classic NES Series - The Legend of Zelda",
    },
    "ZELDA 1     FZLJ": {
        'uttd': "FZLJ",
        'title': "Famicom Mini Vol. 05 - The Hyrule Fantasy - Zelda no Densetsu 1",
    },
    "ZEROMISSIONCBMXC": {
        'uttd': "BMXC",
        'title': "Miteluote Lingdian Renwu",
    },
    "ZEROMISSIONEBMXE": {
        'uttd': "BMXE",
        'title': "Metroid - Zero Mission",
        'icon0': 'https://images.launchbox-app.com/a2331b18-0475-4f67-bb6a-9f928fe62474.jpg',
        'pic0': 'https://images.launchbox-app.com/9fd48d9e-d7f4-41e9-9019-1a78d014020a.png',
        'pic1': 'https://images.launchbox-app.com/d64b324c-7512-4a6a-b84c-3c577f5015fb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=9sC4wlz4zrY&list=PLA4B22C847C11C106&index=1',
    },
    "ZEROMISSIONJBMXJ": {
        'uttd': "BMXJ",
        'title': "Metroid - Zero Mission",
        'icon0': 'https://images.launchbox-app.com/a2331b18-0475-4f67-bb6a-9f928fe62474.jpg',
        'pic0': 'https://images.launchbox-app.com/9fd48d9e-d7f4-41e9-9019-1a78d014020a.png',
        'pic1': 'https://images.launchbox-app.com/d64b324c-7512-4a6a-b84c-3c577f5015fb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=9sC4wlz4zrY&list=PLA4B22C847C11C106&index=1',
    },
    "ZEROMISSIONPBMXP": {
        'uttd': "BMXP",
        'title': "Metroid - Zero Mission",
        'icon0': 'https://images.launchbox-app.com/a2331b18-0475-4f67-bb6a-9f928fe62474.jpg',
        'pic0': 'https://images.launchbox-app.com/9fd48d9e-d7f4-41e9-9019-1a78d014020a.png',
        'pic1': 'https://images.launchbox-app.com/d64b324c-7512-4a6a-b84c-3c577f5015fb.jpg',
        'snd0': 'https://www.youtube.com/watch?v=9sC4wlz4zrY&list=PLA4B22C847C11C106&index=1',
    },
    "ZERO ONE    AF3J": {
        'uttd': "AF3J",
        'title': "Zero One",
    },
    "ZERO ONE SP BZOJ": {
        'uttd': "BZOJ",
        'title': "Zero One SP",
    },
    "ZEROTOURS   AZTJ": {
        'uttd': "AZTJ",
        'title': "Zero-Tours",
    },
    "ZIDANE FOOTBAZDP": {
        'uttd': "AZDP",
        'title': "Zidane Football Generation",
    },
    "Z.O.E 2173  AZEJ": {
        'uttd': "AZEJ",
        'title': "Z.O.E. 2173 - Testament",
    },
    "Z.O.E EU    AZEP": {
        'uttd': "AZEP",
        'title': "Zone of the Enders - The Fist of Mars",
    },
    "Z.O.E USA   AZEE": {
        'uttd': "AZEE",
        'title': "Zone of the Enders - The Fist of Mars",
    },
    "ZOEY 101    BZYE": {
        'uttd': "BZYE",
        'title': "Zoey 101",
    },
    "ZOIDSFUZORS BZFJ": {
        'uttd': "BZFJ",
        'title': "Zoids Saga - Fuzors",
    },
    "ZOIDS LEGACYAZ2E": {
        'uttd': "AZ2E",
        'title': "Zoids Legacy",
    },
    "ZOIDSSAGA2  AZ2J": {
        'uttd': "AZ2J",
        'title': "Zoids Saga II",
    },
    "ZOIDSSAGA   ATZJ": {
        'uttd': "ATZJ",
        'title': "Zoids Saga",
    },
    "ZOKTAI      U32J": {
        'uttd': "U32J",
        'title': "Zoku Bokura no Taiyou - Taiyou Shounen Django",
    },
    "ZOO CUBE    ANCE": {
        'uttd': "ANCE",
        'title': "ZooCube",
    },
    "ZOO CUBE    ANCJ": {
        'uttd': "ANCJ",
        'title': "ZooCube",
    },
    "ZOO CUBE    ANCP": {
        'uttd': "ANCP",
        'title': "ZooCube",
    },
    "ZOOO        BMZJ": {
        'uttd': "BMZJ",
        'title': "Minna no Soft Series - Zooo",
    },
    "ZOOO        BMZP": {
        'uttd': "BMZP",
        'title': "Zooo",
    },
    "ZORORIOHIME BKOJ": {
        'uttd': "BKOJ",
        'title': "Kaiketsu Zorori to Mahou no Yuuenchi - Ohimesama wo Sukue!",
    },
}
