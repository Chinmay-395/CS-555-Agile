import unittest
import pandas as pd
from datetime import datetime
from US31_list_living_single import listLivingSinglesOver30, calculate_age

class TestUS31(unittest.TestCase):
   def testLivingSinglesOver30(self):
    data = [
        ["@I1@", "Sachin Devangan", "M", "1999 JAN 1", "NA", [], "@F1@", True, 33],
        ["@I2@", "Chinmay Dali", "M", "1999 MAY 14", "NA", ["@F1@"], 0, True, 44],
        ["@I3@", "Person Single, Not Over 30", "M", "1992 JUN 20", "NA", [], [], True, 29],
        ["@I4@", "Person Dead", "M", "1985 DEC 5", "2020 JAN 1", [], [], False, 34],
        ["@I5@", "Person Married", "M", "1982 FEB 10", "NA", ["@F2@"], ["@I6@"], True, 39],
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
    
    # Calculate ages for testing
    df['AGE'] = df['BIRTHDAY'].apply(calculate_age)
    
    # Filter out rows with None ages for comparison
    filtered_df = df.dropna(subset=['AGE'])

    self.assertEqual(
        listLivingSinglesOver30(filtered_df),
        "US31: There are no one over 30 who has never been married",
        "listLivingSinglesOver30() did not produce expected output."
    )


    # def testNoLivingSinglesOver30(self):
    #    data = [
    #     ["@I1@", "Person Single, Not Over 30", "M", "1992 JUN 20", "NA", [], [], True, 29],
    #     ["@I2@", "Another Single, Not Over 30", "F", "1995 AUG 12", "NA", [], [], True, 26],
    # ]
    # columns = [
    #     "ID",
    #     "NAME",
    #     "GENDER",
    #     "BIRTHDAY",
    #     "DEATH",
    #     "CHILD",
    #     "SPOUSE",
    #     "ALIVE",
    #     "AGE",
    # ]
    # df = pd.DataFrame(data, columns=columns)
    
    # # Calculate ages for testing
    # df['AGE'] = df['BIRTHDAY'].apply(calculate_age)
    
    # # Filter out rows with None ages for comparison
    # filtered_df = df.dropna(subset=['AGE'])

    # self.assertEqual(
    #     listLivingSinglesOver30(filtered_df),
    #     "Living singles over 30: []",
    #     "US31: There are no living singles over 30."
    # )


    # def testLivingSinglesOver30(self):
    #   data = [
    #     ["@I1@", "Sachin Devangan", "M", "1985 JAN 1", "NA", [], "@F1@", True, 37],
    #     ["@I2@", "Chinmay Dali", "M", "1980 MAY 14", "NA", [], [], True, 42],
    #     ["@I3@", "Person Single, Not Over 30", "M", "1992 JUN 20", "NA", [], [], True, 29],
    #     ["@I4@", "Person Dead", "M", "1978 DEC 5", "2020 JAN 1", [], [], False, 43],
    #     ["@I5@", "Person Married", "M", "1982 FEB 10", "NA", ["@F2@"], ["@I6@"], True, 39],
    # ]
    # columns = [
    #     "ID",
    #     "NAME",
    #     "GENDER",
    #     "BIRTHDAY",
    #     "DEATH",
    #     "CHILD",
    #     "SPOUSE",
    #     "ALIVE",
    #     "AGE",
    # ]
    # df = pd.DataFrame(data, columns=columns)
    
    # # Calculate ages for testing
    # df['AGE'] = df['BIRTHDAY'].apply(calculate_age)
    
    # # Filter out rows with None ages for comparison
    # filtered_df = df.dropna(subset=['AGE'])

    # self.assertEqual(
    #     listLivingSinglesOver30(filtered_df),
    #     "Living singles over 30: [('I1', 37, ' Sachin /Devangan/'), ('I2', 42, 'Chinmay /Dali/')]",
    #     "US31: Found living singles over 30."
    # )



    # def testInvalidDateFormat(self):
    #  data = [
    #     ["@I1@", "Person Invalid Date", "M", "01 JAN 1990", "NA", [], "@F1@", True, 33],
    # ]
    # columns = [
    #     "ID",
    #     "NAME",
    #     "GENDER",
    #     "BIRTHDAY",
    #     "DEATH",
    #     "CHILD",
    #     "SPOUSE",
    #     "ALIVE",
    #     "AGE",
    # ]
    # df = pd.DataFrame(data, columns=columns)
    
    # # Calculate ages for testing
    # df['AGE'] = df['BIRTHDAY'].apply(calculate_age)

    # self.assertEqual(
    #     listLivingSinglesOver30(df),
    #     "Living singles over 30: [('I1', 33, 'Person Invalid Date')]",
    #     "US31: Handle invalid date format correctly."
    # )


    # def testAllDeadOrMarried(self):
    #     data = [
    #     ["@I1@", "Person Dead", "M", "1980 JAN 1", "2020 JAN 1", [], [], False, 40],
    #     ["@I2@", "Person Dead", "F", "1975 MAY 14", "2019 DEC 31", [], [], False, 44],
    #     ["@I3@", "Person Married", "M", "1982 JUN 20", "NA", ["@F1@"], ["@I4@"], True, 39],
    #     ["@I4@", "Person Married", "F", "1980 DEC 5", "NA", ["@F1@"], ["@I3@"], True, 42],
    # ]
    # columns = [
    #     "ID",
    #     "NAME",
    #     "GENDER",
    #     "BIRTHDAY",
    #     "DEATH",
    #     "CHILD",
    #     "SPOUSE",
    #     "ALIVE",
    #     "AGE",
    # ]
    # df = pd.DataFrame(data, columns=columns)
    
    # # Calculate ages for testing
    # df['AGE'] = df['BIRTHDAY'].apply(calculate_age)
    
    # # Filter out rows with None ages for comparison
    # filtered_df = df.dropna(subset=['AGE'])

    # self.assertEqual(
    #     listLivingSinglesOver30(filtered_df),
    #     "Living singles over 30: []",
    #     "US31: There are no living singles over 30."
    # )



if __name__ == "__main__":
    unittest.main()
