from US22_unique_ids import check_unique_ids
import unittest
import pandas as pd

class TestUS22(unittest.TestCase):
    def testDuplicateIds(self):
        # Test data with duplicate individual and family IDs
        individual_data = [
            ["@I1@", "Sachin Devangan", "M", " 28 OCT 1981", "NA", ['@F4@'], "@F2@", True, 41],
            ["@I1@", "Laxmi Devangan", "F", " 30 DEC 1982", "NA", ['@F4@'], 0, True, 40]
        ]

        family_data = [
            ["@F1@", "1990 MAY 1", "NA", "@I1@", "Sachin Devangan", "@I2@", "Laxmi Devangan", []],
            ["@F1@", "1985 MAR 8", "NA", "@I3@", "John Doe", "@I4@", "Jane Smith", []]
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

        errors = check_unique_ids(individuals_df, families_df)

        print(errors)

        expected_errors = [
            "US22: Error: Duplicate individual IDs found: ['@I1@']",
            "US22: Error: Duplicate family IDs found: ['@F1@']"
        ]

        self.assertEqual(errors, expected_errors, f"Expected {expected_errors}, but got {errors}")

if __name__ == "__main__":
    unittest.main()
