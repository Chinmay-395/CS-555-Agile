import unittest

import pandas as pd
import numpy as np
import datetime

from US36_list_recent_deaths import listRecentDeaths

today = datetime.date.today()
delta = datetime.timedelta(days=20)
twenty_days_ago = (today - delta).strftime("%d %b %Y")


class TestUS29(unittest.TestCase):
    def testListRecentDeaths1(self):
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
            listRecentDeaths(indi_df),
            "US35: No recent deaths found in the last 30 days.",
            "listRecentDeaths(indi_df) did not produce expected output.",
        )

    def testListRecentDeaths2(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": [twenty_days_ago, np.nan],
            "CHILD": ["", ""],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [False, True],
            "AGE": [33, 31],
        }
        indi_df = pd.DataFrame(individuals_data)

        self.assertEqual(
            listRecentDeaths(indi_df),
            "US35: List of Recent Deaths in the (last', 30, 'days): [('I1', '04 Oct 2023', 'John Doe')]",
            "listRecentDeaths(indi_df) did not produce expected output.",
        )

    def testListRecentDeaths3(self):
        individuals_data = {
            "ID": ["I1", "I2"],
            "NAME": ["John Doe", "Jane Doe"],
            "GENDER": ["M", "F"],
            "BIRTHDAY": ["1990 MAY 14", "1992 DEC 21"],
            "DEATH": ["21 MAY 2022", np.nan],
            "CHILD": ["NA", "NA"],
            "SPOUSE": ["I2", "I1"],
            "ALIVE": [True, False],
            "AGE": [33, 31],
        }
        indi_df = pd.DataFrame(individuals_data)

        self.assertEqual(
            listRecentDeaths(indi_df),
            "US35: No recent deaths found in the last 30 days.",
            "listRecentDeaths(indi_df) did not produce expected output.",
        )


if __name__ == "__main__":
    unittest.main()
