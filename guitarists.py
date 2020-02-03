list_of_guitarists = {'Eric Clapton':'Cream',
'Jimmy Page': 'Led Zeppelin',
'Keith Richards': 'Rolling Stones',
'Eddie Van Halen': 'Van Halen',
'David Gilmour': 'Pink Floyd',
'Angus Young': 'AD/DC',
'Brian May': 'Queen',
'Johnny Ramone': 'Ramones',
'Tom Morello': 'Rage Against the Machine',
'Slash': "Guns'n Roses",
'Jim Root': 'Slipknot',
'Kirk Hammet': 'Metallica'
}

def check_guitarist(guitar_player):
    if guitar_player in list_of_guitarists:
        print("{} plays for {}".format(guitar_player, list_of_guitarists[guitar_player]))
    else:
        print("Sorry, {} does not seem to be a known guitarist".format(guitar_player))

def check_band(band_name):
    for guitarist, band in list_of_guitarists.items():
        if band == band_name:
            print("The guitar hero of {} is {}".format(band, guitarist))
            return
    print("Sorry, we don't know who is the guitar hero of {}".format(band_name))
