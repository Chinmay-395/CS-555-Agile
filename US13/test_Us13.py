import unittest
from unittest.mock import patch
from pandas import DataFrame
from Initialparser import parse
from US_13 import check_sibling_birth_dates


class TestCheckSiblingBirthDates(unittest.TestCase):
    
    def setUp(self):
        list_indi, list_fam = parse("test_US.ged")
        self.df_indi = DataFrame(list_indi)
        self.df_fam = DataFrame(list_fam)

    def check_siblings_birth_dates(self):
       result = check_sibling_birth_dates(self.df_indi,self.df_fam)
       print(result)
       expected_result = [('F1', 'I1', 'I5'), ('F1', 'I2', 'I5'), ('F1', 'I3', 'I4'), ('F1', 'I5', 'I6')]
       self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()