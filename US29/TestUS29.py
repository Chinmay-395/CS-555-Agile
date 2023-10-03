from US29_list_deceased import listDeceased
import unittest
import pandas as pd


class TestUS29(unittest.TestCase):
    def testDeceasedList1(self):
        data = [
            ["@I1@", "Person Alive", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33],
            [
                "@I2@",
                "Person Deceased",
                "M",
                "1979 MAY 14",
                "NA",
                ["@F1@"],
                0,
                False,
                44,
            ],
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
            listDeceased(df),
            [("@I2@", "Person Deceased")],
            "listDeceased() did not produce expected output.",
        )

    def testDeceasedList2(self):
        data = [
            ["@I1@", "Person Alive", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33],
            [
                "@I2@",
                "Person Deceased 1",
                "M",
                "1979 MAY 14",
                "NA",
                ["@F1@"],
                0,
                False,
                44,
            ],
            [
                "@I3@",
                "Person Deceased 2",
                "M",
                "1979 MAY 14",
                "NA",
                ["@F2@"],
                0,
                False,
                44,
            ],
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
            listDeceased(df),
            [("@I2@", "Person Deceased 1"), ("@I3@", "Person Deceased 2")],
            "listDeceased() did not produce expected output.",
        )

    def testDeceasedList3(self):
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
            listDeceased(df),
            "ANOMALY: US29: No family members available.",
            "listDeceased() did not produce expected output.",
        )

    def testDeceasedList4(self):
        data = [
            ["@I1@", "Person Invalid", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33]
        ]

        self.assertEqual(
            listDeceased(data),
            "ERROR: US29: Input parameter of wrong type.",
            "listDeceased() did not produce expected output.",
        )

    def testDeceasedList5(self):
        data = [
            ["@I1@", "Person Alive 1", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33],
            [
                "@I2@",
                "Person Alive 2",
                "M",
                "1979 MAY 14",
                "NA",
                ["@F1@"],
                0,
                True,
                44,
            ],
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
            listDeceased(df),
            "US29: There are no deceased_people in the GEDCOM file.",
            "listDeceased() did not produce expected output.",
        )


if __name__ == "__main__":
    unittest.main()
