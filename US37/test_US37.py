import unittest
from unittest.mock import patch
import sys,os
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from US37_list_recent_Survivors import list_recent_survivors
from Initialparser import parse
from pandas import DataFrame

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/recent_survivor_test.ged'
        individuals, families = parse(filename)
        df_indi = DataFrame(individuals)
        df_fam = DataFrame(families)
        list_recent_survivors(df_indi, df_fam)
        mock_print.assert_called_with("US37: The list of all living spouses and descendants of people who died in the last 30 days: [{'name': ('I2', 42), 'living spouses': [('I1', 43)], 'living descendants': [('I3', 33)]}]")

if __name__ == '__main__':
    unittest.main()