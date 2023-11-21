import unittest
from unittest.mock import patch
import sys
from US01_dates_before_curr_date import dates_before_current_date
# this is done to import the code from module InitialParser.py
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse
from pandas import DataFrame

class TestUS01(unittest.TestCase):

    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS-555-Agile/US01/test.ged")
        
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        dates_before_current_date(df_indi,df_fam)
        mock_print.assert_called_with("ERROR: INDIVIDUAL: US01:  Birthday 1 JAN 2050 occurs in the future")




if __name__ == '__main__':
    unittest.main()