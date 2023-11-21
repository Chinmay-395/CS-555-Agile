import unittest

import pandas as pd

from US32_list_multiple_births import listMultipleBirths

# Assume you have your function listMultipleBirths defined in a module called family_functions


class TestListMultipleBirths(unittest.TestCase):
    def test_multiple_births_exist(self):
        individuals_data = {
            "ID": ["I1", "I2", "I3", "I4", "I5"],
            "NAME": ["John", "Alice", "Bob", "Eve", "Charlie"],
            "BIRTHDAY": [
                "1 JAN 1990",
                "1 JAN 1990",
                "1 JAN 1990",
                "1 JAN 1990",
                "1 JAN 1990",
            ],
        }

        families_data = {"ID": ["F1"], "CHILDREN": [["I1", "I2", "I3", "I4", "I5"]]}

        individuals = pd.DataFrame(individuals_data)
        families = pd.DataFrame(families_data)

        result = listMultipleBirths(individuals, families)

        self.assertIn(
            "F1",
            result,
            "Expected family F1 to be in the list of families with multiple births",
        )

    def test_no_multiple_births(self):
        individuals_data = {
            "ID": ["I1", "I2", "I3", "I4", "I5"],
            "NAME": ["John", "Alice", "Bob", "Eve", "Charlie"],
            "BIRTHDAY": [
                "1 JAN 1990",
                "2 FEB 1990",
                "3 MAR 1990",
                "4 APR 1990",
                "5 MAY 1990",
            ],
        }

        families_data = {"ID": ["F1"], "CHILDREN": [["I1", "I2", "I3", "I4", "I5"]]}

        individuals = pd.DataFrame(individuals_data)
        families = pd.DataFrame(families_data)

        result = listMultipleBirths(individuals, families)

        self.assertNotIn(
            "F1",
            result,
            "Expected family F1 not to be in the list of families with multiple births",
        )


if __name__ == "__main__":
    unittest.main()
