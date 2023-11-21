import unittest
from unittest.mock import patch
import sys
from US07_less_than_150 import less_than_150_years
# this is done to import the code from module InitialParser.py
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse
from pandas import DataFrame

class TestUS01(unittest.TestCase):

    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS-555-Agile/US07/test.ged")
        
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        less_than_150_years(df_indi)
        mock_print.assert_called_with("ERROR: INDIVIDUAL: US02:  Age 41 ID: I4 is less than 150")




if __name__ == '__main__':
    unittest.main()