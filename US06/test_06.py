import unittest
from unittest.mock import patch
from pandas import DataFrame
import sys
from Initialparser import parse
from US_06 import test_divorce_before_death 


class TestUSMarriageBeforeDeath(unittest.TestCase):
    
    def setUp(self):
        list_indi, list_fam = parse("test_US06.ged")
        self.df_indi = DataFrame(list_indi)
        self.df_fam = DataFrame(list_fam)

    def test_marriage_before_death(self):
       result = test_divorce_before_death(self.df_fam, self.df_indi)
       print(result)
       expected_result = ["US06:ERROR: FAMILY: Husband ID I1 Wife ID I2 divorced after death"]
       self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()