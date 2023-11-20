from datetime import datetime
import unittest
import pandas as pd
from US10_Marriage_after_14 import listValidMarriages

class TestUS10(unittest.TestCase):
    def test_valid_marriages(self):
        # Test data with duplicate individual and family IDs
        individual_data = [
            ["@I6@","Abhishek Devangan","M","1985 MAR 16","NA",['@F3@'],"@F2@",True,38],
            ["@I7@","Meenakshi Devangan","F","1985 MAR 13","NA",['@F3@'],0,True,38]
        ]

        family_data = [
            ["@F3@","2015 DEC 16","NA","@I6@","Abhishek Devangan","@I7@","Meenakshi Devangan","['@I12@', '@I13@']"]
        ]

        individual_columns = [
            "ID",
            "NAME",
            "GENDER",
            "BIRTHDAY",
            "DEATH",
            "CHILD",
            "SPOUSE",
            "ALIVE",
            "AGE"
        ]

        family_columns = [
            "ID",
            "MARRIED",
            "DIVORCE",
            "HUSBAND ID",
            "HUSBAND NAME",
            "WIFE ID",
            "WIFE NAME",
            "CHILDREN"
        ]

        individuals_df = pd.DataFrame(individual_data, columns=individual_columns)
        families_df = pd.DataFrame(family_data, columns=family_columns)



        # Call the function to get the valid marriages list
        valid_marriages = listValidMarriages(individuals_df, families_df)

        # Expected valid marriages list based on the test data
        expected_valid_marriages = [
            {'Husband ID': 'I6', 'Husband Name': 'Abhishek Devangan', 'Wife ID': 'I7', 'Wife Name': 'Meenakshi Devangan'}
        ]

        # Assert that the function's output matches the expected valid marriages list
        self.assertEqual(valid_marriages, expected_valid_marriages, f"Expected {expected_valid_marriages}, but got {valid_marriages}")
if __name__ == "__main__":
    unittest.main()
