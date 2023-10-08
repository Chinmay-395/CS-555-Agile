import unittest

import pandas as pd

from US03_birth_before_death import birthBeforeDeath


class TestUS03(unittest.TestCase):
    def testBirthBeforeDeath1(self):
        data = [
            [
                "@I1@",
                "Person Deceased 1",
                "M",
                "2022 JAN 1",
                "2022 JAN 1",
                [],
                "@F1@",
                False,
                33,
            ],
            [
                "@I2@",
                "Person Deceased 2",
                "M",
                "1979 MAY 14",
                "1979 JAN 12",
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
            birthBeforeDeath(df),
            [
                "ERROR: INDIVIDUAL: US03: -1: @I1@: Died 2022-01-01 before born 2022-01-01",
                "ERROR: INDIVIDUAL: US03: -1: @I2@: Died 1979-01-12 before born 1979-05-14",
            ],
            "birthBeforeDeath() did not produce expected output.",
        )

    def testBirthBeforeDeath2(self):
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
            birthBeforeDeath(df),
            "ERROR: @I2@ is dead, but no Death date given",
            "birthBeforeDeath() did not produce expected output.",
        )

    def testBirthBeforeDeath3(self):
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
            birthBeforeDeath(df),
            "ERROR: No family members available.",
            "birthBeforeDeath() did not produce expected output.",
        )

    def testBirthBeforeDeath4(self):
        data = [
            ["@I1@", "Person Invalid", "M", "1990 JAN 1", "NA", [], "@F1@", True, 33]
        ]

        self.assertEqual(
            birthBeforeDeath(data),
            "ERROR: Input parameter of wrong type.",
            "birthBeforeDeath() did not produce expected output.",
        )

    def testBirthBeforeDeath5(self):
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
            birthBeforeDeath(df),
            [],
            "birthBeforeDeath() did not produce expected output.",
        )

    def testBirthBeforeDeath6(self):
        data = [
            ["@I1@", "Person Dead", "M", "1990 JAN 1", "NA", [], "@F1@", False, 33],
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
            birthBeforeDeath(df),
            'ERROR: @I1@ is dead, but no Death date given',
            "birthBeforeDeath() did not produce expected output.",
        )


if __name__ == "__main__":
    unittest.main()
