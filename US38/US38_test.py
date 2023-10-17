from US38_list_upcoming_birthdays import listUpcomingBirthdays
import unittest
import pandas as pd


class TestUS35(unittest.TestCase):
    def testUpcomingBirthdayList2(self):
        data = [
            ["@I1@", "Sachin Devangan", "M", " 28 OCT 1981", "NA", ['@F4@'], "@F2@", True, 41],
            ["@I4@", "Laxmi Devangan", "F", " 30 DEC 1982", "NA", ['@F4@'], 0, True, 40]
        ]
        columns = [
            "ID",
            "NAME",
            "GENDER",
            "BIRTHDAY",
            "DEATH",
            "CHILD",
            "SPOUSE",
            "ALIVE",
            "AGE",
        ]
        df = pd.DataFrame(data, columns=columns)

        self.assertEqual(
            listUpcomingBirthdays(df),
            [('@I1@', ' 28 OCT 1981', 'Sachin Devangan')],
            "listUpcomingBirthdays() did not produce expected output.",
        )

    def testUpcomingBirthdayList1(self):
        data = [
            ["@I8@", "Bhaskar Devangan", "M", " 18 OCT 1981", "NA", ['@F4@'], "@F2@", True, 41],
            ["@I9@", "Laxmi Devangan", "F", " 30 OCT 1982", "NA", ['@F4@'], 0, True, 40]
        ]
        columns = [
            "ID",
            "NAME",
            "GENDER",
            "BIRTHDAY",
            "DEATH",
            "CHILD",
            "SPOUSE",
            "ALIVE",
            "AGE",
        ]
        df = pd.DataFrame(data, columns=columns)

        self.assertEqual(
            listUpcomingBirthdays(df),
            [('@I8@', ' 18 OCT 1981', 'Bhaskar Devangan'),('@I9@', ' 30 OCT 1982', 'Laxmi Devangan')],
            "listUpcomingBirthdays() did not produce expected output.",
        )

    def testUpcomingBirthdayList3(self):
        data = []
        columns = [
            "ID",
            "NAME",
            "GENDER",
            "BIRTHDAY",
            "DEATH",
            "CHILD",
            "SPOUSE",
            "ALIVE",
            "AGE",
        ]
        df = pd.DataFrame(data, columns=columns)

        self.assertEqual(
            listUpcomingBirthdays(df),
            "ANOMALY: US38: No family members available.",
            "listUpcomingBirthdays() did not produce expected output.",
        )
    
    def testUpcomingBirthdayList4(self):
        data = ["@I1@", "Person Invalid", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33]
    

        self.assertEqual(
            listUpcomingBirthdays(data),
            "ERROR: US38: Input parameter of wrong type.",
            "listUpcomingBirthdays() did not produce expected output.",
        )

    def testUpcomingBirthdayList5(self):
        data = [
            ["@I1@", "Sachin Devangan", "M", " 01 JAN 1999", "NA", ['@F4@'], "@F2@", True, 24],
            ["@I4@", "Ranjana Devangan", "F", " 02 FEB 1982", "NA", ['@F1@'], 0, True, 40]
        ]
        columns = [
            "ID",
            "NAME",
            "GENDER",
            "BIRTHDAY",
            "DEATH",
            "CHILD",
            "SPOUSE",
            "ALIVE",
            "AGE",
        ]
        df = pd.DataFrame(data, columns=columns)

        self.assertEqual(
            listUpcomingBirthdays(df),
            "US38: There are no Upcoming Birthdays in the GEDCOM file.",
            "listUpcomingBirthdays() did not produce expected output.",
        )

    

if __name__ == "__main__":
    unittest.main()
