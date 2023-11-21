import unittest
from unittest.mock import patch
import sys
from US33_list_orphans import listOrphans
# this is done to import the code from module InitialParser.py
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse
from pandas import DataFrame

class TestUS33_list_orphans(unittest.TestCase):
    # both parents are dead
    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS-555-Agile/US33/recent_orphans.ged")
        print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
        df_indi = DataFrame(list_indi)
        df_fam = DataFrame(list_fam)
        listOrphans(df_indi,df_fam)
        mock_print.assert_called_with([('I3', 10, ' Mehul /Das/')])


    # # no parent is dead
    # @patch('builtins.print')
    # def test_input_data2(self,mock_print):
    #     list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US33/recent_orphans_no_orphans.ged")
    #     print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    #     df_indi = DataFrame(list_indi)
    #     df_fam = DataFrame(list_fam)
    #     listOrphans(df_indi,df_fam)
    #     mock_print.assert_called_with('US33: No orphans in this family tree')

    # # no parents are dead but the rest of the family is dead
    # @patch('builtins.print')
    # def test_input_data3(self,mock_print):
    #     list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US33/recent_orphans2.ged")
    #     print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    #     df_indi = DataFrame(list_indi)
    #     df_fam = DataFrame(list_fam)
    #     listOrphans(df_indi,df_fam)
    #     mock_print.assert_called_with([('I4', 4, ' Roshan /Mehra/')])

    # # everyone in this family is dead
    # @patch('builtins.print')
    # def test_input_data4(self,mock_print):
    #     list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US33/recent_orphans3.ged")
    #     print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    #     df_indi = DataFrame(list_indi)
    #     df_fam = DataFrame(list_fam)
    #     listOrphans(df_indi,df_fam)
    #     mock_print.assert_called_with([('I4', 1, ' Roshan /Mehra/')])

    # # only one parent is dead
    # @patch('builtins.print')
    # def test_input_data5(self,mock_print):
    #     list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/US33/recent_orphans4.ged")
    #     print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    #     df_indi = DataFrame(list_indi)
    #     df_fam = DataFrame(list_fam)
    #     listOrphans(df_indi,df_fam)
    #     mock_print.assert_called_with('US33: No orphans in this family tree')




if __name__ == '__main__':
    unittest.main()