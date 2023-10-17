import unittest

import pandas as pd

from US39_list_upcoming_anniversaries import listUpcomingAnniversaries


class TestUS29(unittest.TestCase):
    def testUpcomingAnniverseries1(self):

        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["NA", "NA"],
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
            listUpcomingAnniversaries(indi_df, fam_df),
            {('John /Doe/', 'Jane /Doe/', '10 Nov')},
            "listUpcomingAnniversaries(indi_df, fam_df) did not produce expected output.",
        )

    def testUpcomingAnniverseries2(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["NA", "NA"],
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
            "MARRIED": ["7 MAY 1995"],
            "DIVORCE STATUS": [True],
        }
        fam_df = pd.DataFrame(family_data)

        self.assertEqual(
            listUpcomingAnniversaries(indi_df, fam_df),
            "US39: There are no upcoming anniversaries.",
            "listUpcomingAnniversaries(indi_df, fam_df) did not produce expected output.",
        )

    def testUpcomingAnniverseries3(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["NA", "NA"],
            "CHILD": ["NA", "NA"],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [False, False],
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
            "MARRIED": ["7 MAY 1995"],
            "DIVORCE STATUS": [False],
        }
        fam_df = pd.DataFrame(family_data)

        self.assertEqual(
            listUpcomingAnniversaries(indi_df, fam_df),
            "US39: There are no upcoming anniversaries.",
            "listUpcomingAnniversaries(indi_df, fam_df) did not produce expected output.",
        )


if __name__ == "__main__":
    unittest.main()
