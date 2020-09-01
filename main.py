c#! /usr/bin/env python3

from guitarists_package import guitarists_band_check as gbc

a = gbc.check_band("AD/DC")
if a!= False:
  print(a)
else:
  print("no")


