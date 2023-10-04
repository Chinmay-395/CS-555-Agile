from datetime import datetime
import pandas as pd

def convert_gedcom_date_to_datetime(gedcom_date):
    try:
        return datetime.strptime(gedcom_date.strip(), '%d %b %Y')
    except ValueError:
        return None

def test_marriage_after_divorce(families, individuals):
    errors = []
    for index, row in families.iterrows():
        if row["DIVORCE STATUS"] is True:
            print("yes")
            print(row["DIVORCE"])
            marriage_date = convert_gedcom_date_to_datetime(row["MARRIED"])
            divorce_date = convert_gedcom_date_to_datetime(row["DIVORCE"])
            print(marriage_date)
            print(divorce_date)
            if divorce_date<marriage_date:
                errors.append([row["HUSBAND ID"],row["WIFE ID"]])
    return errors
