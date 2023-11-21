import unittest
from unittest.mock import patch
import sys
from US30_list_living_married import list_living_married
# this is done to import the code from module InitialParser.py
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse
from pandas import DataFrame

class TestUS30(unittest.TestCase):
    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("export-BloodTree12.ged")
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        list_living_married(df_indi,df_fam)
        mock_print.assert_called_with("US30: The list of living people that are married: [('I5', 79), ('I6', 78), ('I7', 33)]")

if __name__ == '__main__':

    unittest.main()