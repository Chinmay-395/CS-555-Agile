import unittest
from unittest.mock import patch
from pandas import DataFrame
from Initialparser import parse
from UseCase_05 import test_marriage_before_death 

class TestUSMarriageAfterDivorce(unittest.TestCase):
    
    def setUp(self):
        list_indi, list_fam = parse("test_us_04.ged")
        self.df_indi = DataFrame(list_indi)
        self.df_fam = DataFrame(list_fam)

    def test_marriage_after_divorce(self):
       result = test_marriage_before_death(self.df_fam, self.df_indi)
       expected_result = [['I3', 'I4']]
       self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
