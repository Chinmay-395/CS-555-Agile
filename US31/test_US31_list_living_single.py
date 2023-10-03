import unittest
from unittest.mock import patch
from pandas import DataFrame
import sys
from US31_list_living_single import listLivingSinglesOver30
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/")
from Initialparser import parse


class TestUS33_list_orphans(unittest.TestCase):
    
    @patch('builtins.print')
    def test_input_data(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US31/living_single_test.ged")
        print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        listLivingSinglesOver30(df_indi)
        mock_print.assert_called_with([('I3')])

if __name__ == '__main__':
    unittest.main()