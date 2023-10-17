import unittest
import pandas as pd
from Us38_smelly_code import listUpcomingBirthdays

class TestSmellyCode(unittest.TestCase):
    def testEmptyDataFrame(self):
        data = []
        columns = ["ID", "NAME", "GENDER", "BIRTHDAY", "DEATH", "CHILD", "SPOUSE", "ALIVE", "AGE"]
        df = pd.DataFrame(data, columns=columns)
        self.assertEqual(
            listUpcomingBirthdays(df),
           "ANOMALY: US38: No data.",
            "listUpcomingBirthdays() did not produce expected output for empty DataFrame.",
        )

    def testInvalidInputType(self):
        data = ["@I1@", "Person Invalid", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33]
        self.assertEqual(
            listUpcomingBirthdays(data),
            "ERR: US38: Bad input.",
            "listUpcomingBirthdays() did not produce expected output for invalid input type.",
        )

    def testNoUpcomingBirthdays(self):
        data = [
            ["@I1@", "Sachin Devangan", "M", " 01 JAN 1999", "NA", ['@F4@'], "@F2@", True, 24],
            ["@I4@", "Ranjana Devangan", "F", " 02 FEB 1982", "NA", ['@F1@'], 0, True, 40]
        ]
        columns = ["ID", "NAME", "GENDER", "BIRTHDAY", "DEATH", "CHILD", "SPOUSE", "ALIVE", "AGE"]
        df = pd.DataFrame(data, columns=columns)
        self.assertEqual(
            listUpcomingBirthdays(df),
            "US38: No Upcoming Birthdays in GEDCOM file.",
            "listUpcomingBirthdays() did not produce expected output when there are no upcoming birthdays.",
        )

    def testUpcomingBirthdaysFound(self):
        data = [
            ["@I8@", "Bhaskar Devangan", "M", " 18 OCT 1981", "NA", ['@F4@'], "@F2@", True, 41],
            ["@I9@", "Laxmi Devangan", "F", " 30 OCT 1982", "NA", ['@F4@'], 0, True, 40]
        ]
        columns = ["ID", "NAME", "GENDER", "BIRTHDAY", "DEATH", "CHILD", "SPOUSE", "ALIVE", "AGE"]
        df = pd.DataFrame(data, columns=columns)
        self.assertEqual(
            listUpcomingBirthdays(df),
            [('@I8@', ' 18 OCT 1981', 'Bhaskar Devangan'), ('@I9@', ' 30 OCT 1982', 'Laxmi Devangan')],
            "listUpcomingBirthdays() did not produce expected output for upcoming birthdays.",
        )

    def testUpcomingBirthdaysWithNoData(self):
        data = ["@I1@", "Person Invalid", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33]
        self.assertEqual(
            listUpcomingBirthdays(data),
            "ERR: US38: Bad input.",
            "listUpcomingBirthdays() did not produce expected output for upcoming birthdays with no data.",
        )

if __name__ == "__main__":
    unittest.main()
