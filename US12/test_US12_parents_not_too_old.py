import unittest
from unittest.mock import patch
import sys
from US12_parents_not_too_old import parents_not_too_old
# this is done to import the code from module InitialParser.py
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse
from pandas import DataFrame

class TestUS12(unittest.TestCase):
    # both parents are dead
    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS-555-Agile/US12/export-BloodTree12.ged")
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        parents_not_too_old(df_indi,df_fam)
        mock_print.assert_called_with("ERROR: FAMILY: US12:  FAMILY ID: F1: F1 Age of child: 10 Age of mother: 93 Age of Father: 93")

if __name__ == '__main__':
    unittest.main()