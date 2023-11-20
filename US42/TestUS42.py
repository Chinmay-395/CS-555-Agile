import unittest
import pandas as pd

from US42_reject_illegitimate_dates import rejectIllegitimateDates


class TestUS42(unittest.TestCase):
    def testRejectIllegitimateDates(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["1990 MAY 14", "1990 MAY 14"],
            "CHILD": ["NA", "NA"],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [True, True],
            "AGE": [33, 31],
        }

        indi_df = pd.DataFrame(individuals_data)
        family_data = {
            "ID": ["F1"],
            "HUSBAND ID": ["I1"],
            "HUSBAND NAME": ["John /Doe/"],
            "WIFE ID": ["I2"],
            "WIFE NAME": ["Jane /Doe/"],
            "CHILDREN": ["NA"],
            "MARRIED": ["10 NOV 2012"],
            "DIVORCE STATUS": [False],
        }
        fam_df = pd.DataFrame(family_data)

        self.assertEqual(
            rejectIllegitimateDates(indi_df, fam_df),
            "US42: No illegitimate dates",
            "rejectIllegitimateDates() did not produce excepted output",
        )

    def testRejectIllegitimateDates2(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["1990 MAY 14", "1990 MAY 14"],
            "CHILD": ["NA", "NA"],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [True, True],
            "AGE": [33, 31],
        }

        indi_df = pd.DataFrame(individuals_data)
        family_data = {
            "ID": ["F1"],
            "HUSBAND ID": ["I1"],
            "HUSBAND NAME": ["John /Doe/"],
            "WIFE ID": ["I2"],
            "WIFE NAME": ["Jane /Doe/"],
            "CHILDREN": ["NA"],
            "MARRIED": ["29 FEB 2011"],
            "DIVORCE STATUS": [False],
        }
        fam_df = pd.DataFrame(family_data)

        self.assertEqual(
            rejectIllegitimateDates(indi_df, fam_df),
            ["29 FEB 2011"],
            "rejectIllegitimateDates() did not produce excepted output",
        )


if __name__ == "__main__":
    unittest.main()
