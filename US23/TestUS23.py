import datetime
import unittest

import numpy as np
import pandas as pd

from US23_list_unique_name_and_birthday import listUniqueNameAndBirthdays


class TestUS23(unittest.TestCase):
    def testListUniqueNameAndBirthdays1(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["14 MAY 1990", "21 DEC 1992"],
            "DEATH": [np.nan, np.nan],
            "CHILD": ["NA", "NA"],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [True, True],
            "AGE": [33, 31],
        }

        indi_df = pd.DataFrame(individuals_data)

        self.assertEqual(
            listUniqueNameAndBirthdays(indi_df),
            "US35: No people with the same name and birthday",
            "listUniqueNameAndBirthdays(indi_df) did not produce expected output.",
        )

    def testListUniqueNameAndBirthdays2(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "John Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1990 MAY 14"],
            "DEATH": ["1999 JAN 1", np.nan],
            "CHILD": ["", ""],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [False, True],
            "AGE": [33, 31],
        }
        indi_df = pd.DataFrame(individuals_data)

        self.assertEqual(
            listUniqueNameAndBirthdays(indi_df),
            "US35: List of people with the same name and birthday: ['John Doe / 1990 MAY 14']",
            "listUniqueNameAndBirthdays(indi_df) did not produce expected output.",
        )


if __name__ == "__main__":
    unittest.main()
