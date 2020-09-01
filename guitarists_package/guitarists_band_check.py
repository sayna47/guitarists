"""This is our birthday module."""

import csv

"""Open list_of_guitarists.csv file and turn it to dictionary."""

reader = csv.reader(open('guitarists_package/list_of_guitarists.csv', 'r'))
guitarists_list = {}
for row in reader:
    k, v = row
    guitarists_list[k] = v


"""These are the functions."""


def check_guitarist(guitar_player):
    if guitar_player in guitarists_list:
        return guitarists_list[guitar_player]
    else:
        return False

def check_band(band_name):
    for guitarist, band in guitarists_list.items():
        if band == band_name:
            return guitarist
            
    return False