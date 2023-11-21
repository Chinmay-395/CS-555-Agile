import unittest
from unittest.mock import patch
import sys
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/")
from US08_birth_before_marr import birth_before_marriage_of_parents
from Initialparser import parse
from pandas import DataFrame

class TestUS08_birth_before_marriage_of_parents(unittest.TestCase):


    # no parent is dead
    @patch('builtins.print')
    def test_input_data2(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US08/no_birth_before_marraige.ged")
        # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        birth_before_marriage_of_parents(df_indi,df_fam)
        mock_print.assert_called_with('US08: No births before marriage of parents')

    # no parents are dead but the rest of the family is dead
    @patch('builtins.print')
    def test_input_data3(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US08/birth_before_marriage.ged")
        # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        birth_before_marriage_of_parents(df_indi,df_fam)
        mock_print.assert_called_with([('I22', 28, ' Prabhu /Devangan/')])

    

if __name__ == '__main__':
    unittest.main()