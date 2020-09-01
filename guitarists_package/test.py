"""Test the creation of csv."""

import csv
import os.path


def type_f(path):
    """Find the extention of the file."""
    extension = os.path.splitext(path)[1]
    return extension


def csv_reader(path):
    """Read csv file as dictionary."""
    reader = csv.reader(open(path, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v


csv_reader('guitarists_package/list_of_guitarists.csv')
