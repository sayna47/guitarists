"""Test code to check for errors."""

import unittest
from guitarists_package import test
import sys
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        """Check if there is a csv file."""
        self.assertFalse(os.path.exists("guitarists_package/whateve.csv"))

    def test_empty_datafile(self):
        """Check the presence of data inside the csv file."""
        datafile = test.csv_reader(path=self.temporary_file)
        self.assertFalse(datafile)

    def test_valid_extension(self):
        """Check the extension of the file."""
        extension =test.type_f(path=self.temporary_file)
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)

if __name__ == '__main__':
    unittest.main()
