import unittest
from unittest.mock import patch
import pytest
import pandas as pd
import sys
from US27_include_age import include_individual_ages
sys.path.insert(1,"/home/chinmay/Coding/Courses/CS-555-Agile/")
from Initialparser import parse

class TestUS33_list_orphans(unittest.TestCase):
    # both parents are dead
    @patch('builtins.print')
    def test_input_data1(self,mock_print):
        list_indi, list_fam = parse("/home/chinmay/Coding/Courses/CS-555-Agile/US27/include_age.ged")
        df_indi = pd.DataFrame(list_indi)
        df_fam = pd.DataFrame(list_fam)
        include_individual_ages(df_indi,df_fam)
        # str1= str(include_individual_ages(df_indi,df_fam)) 
        mock_print.assert_called_with("ages of the individuals are already included")


if __name__ == '__main__':
    unittest.main()