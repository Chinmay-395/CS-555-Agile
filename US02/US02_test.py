from US02.US02_birth_before_marriage import validateBirthBeforeMarriage
import unittest
import pandas as pd


class TestValidateBirthBeforeMarriage(unittest.TestCase):
    def test_birth_before_marriage_errors(self):
        # Sample individual data with birthdate after marriage date
        data = {
            'ID': ['@I1@', '@I2@'],
            'BIRTHDAY': ['1 JAN 1990', '1 JAN 1980'],
            'SPOUSE': ['@F1@', '@F2@']
        }
        individuals = pd.DataFrame(data)

        # Sample family data with marriage dates
        family_data = {
            'ID': ['@F1@', '@F2@'],
            'MARRIED': ['1 JAN 1995', '1 JAN 1985']
        }
        families = pd.DataFrame(family_data)

        # Call the function to get errors
        errors = validateBirthBeforeMarriage(individuals, families)

        # Check if the errors are as expected
        self.assertEqual(errors, ["Error: Individual @I1@ has birthdate 1 JAN 1990 after marriage date 1 JAN 1995."])

if __name__ == '__main__':
    unittest.main()
