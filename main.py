


import sys
import argparse
import sqlite3
import hashlib
from guitarists_package import guitarists_band_check as gbc
from scripts import dbmanager



def parse_argument():
    """guitarists or bands name"""
    parser = argparse.ArgumentParser(
             prog="This program checks for a band or a famuse guitarists in a band")
             
    parser.add_argument('n', help="insert the name of the guitarist or the band you would like to check")
    parser.add_argument('-b', action='store_true', default=False,
                        help="check for bands")
    parser.add_argument('-v', action='store_true', default=False,
                        help='Decide the level of verbosity')
    # Check for username and password
    parser.add_argument('-p', help="password",
                        required=True)
    parser.add_argument('-u', help="usernamename"
                        "(requires -p)", required=True)
    args = parser.parse_args()
    return args

def high_verbosity(name,b):
  #answer with high verbosity
  if b:
    guitarist = gbc.check_band(name)
    if guitarist == False :
      print("Sorry, we don't know who is the guitar hero of {}".format(name))
    else:
      print("The guitar hero of {} is {}".format(name, guitarist))
  else:
    band = gbc.check_guitarist(name)
    if band == False :
      print("Sorry, {} does not seem to be a known guitarist".format(name))
    else:
      print("{} plays for {}".format(name, band))

def low_verbosity(name,b):
  #answer with low verbosity
  if b:
    guitarist = gbc.check_band(name)
    if guitarist == False :
      print("we don't know {}".format(name))
    else:
      print("{}:{}".format(name, guitarist))
  else:
    band = gbc.check_guitarist(name)
    if band == False :
      print("we don't know {} ".format(name))
    else:
      print("{}:{}".format(name, band))


db_corr = 'scripts/user_database.db'

if __name__ == "__main__":
    parse_argument()
    args = parse_argument()
    if dbmanager.check_for_username(args.u, args.p, db_corr):
        if args.v:
          high_verbosity(args.n,args.b)
        else:
          low_verbosity(args.n,args.b)


