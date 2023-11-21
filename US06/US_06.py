from datetime import datetime
import pandas as pd

def convert_gedcom_date_to_datetime(gedcom_date, each_row):
    return datetime.strptime(gedcom_date.strip(), '%d %b %Y')

def greaterDate(first_date, second_date):
    return datetime.strptime(first_date, " %d %b %Y") > datetime.strptime(second_date, " %d %b %Y")

def test_divorce_before_death(families, individuals):
    # errors = []
    for index, row in families.iterrows():
        divorceDate = row['DIVORCE']

        husband_death = individuals.loc[individuals['ID'] == row['HUSBAND ID'], 'DEATH'].iloc[0]
        wife_death = individuals.loc[individuals['ID'] == row['WIFE ID'], 'DEATH'].iloc[0]

        if str(husband_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(husband_death), str(divorceDate)) == False:
              print("ERROR: US06: Input Line #: " + ": HUSBAND " + row['HUSBAND ID'] + " DEATH date before divorce.")

        if str(wife_death) != 'nan' and str(divorceDate) != 'nan':
          if greaterDate(str(wife_death), str(divorceDate)) == False:
              print("ERROR: US06: Input Line #: " + ": WIFE " + row['WIFE ID'] + " DEATH date before divorce.")
