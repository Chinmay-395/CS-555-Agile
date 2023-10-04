from datetime import datetime
import pandas as pd

def convert_gedcom_date_to_datetime(gedcom_date):
    try:
        return datetime.strptime(gedcom_date.strip(), '%d %b %Y')
    except ValueError:
        return None

def test_marriage_before_death(families, individuals):
    errors = []
    for index, row in families.iterrows():
        if row["MARRIED"] is not None:
            husband = row["HUSBAND ID"]
            wife = row["WIFE ID"]
            marriage_date = convert_gedcom_date_to_datetime(row["MARRIED"])
            husband_death_date = individuals[individuals['ID']==husband].squeeze()['DEATH']
            wife_death_date = individuals[individuals['ID']==wife].squeeze()['DEATH']
            if not pd.isna(husband_death_date):
                husband_death_date = convert_gedcom_date_to_datetime(husband_death_date)
                if husband_death_date<marriage_date:
                    errors.append([husband,wife])
            if not pd.isna(wife_death_date):
                wife_death_date = convert_gedcom_date_to_datetime(wife_death_date)
                if wife_death_date<marriage_date:
                    errors.append([husband,wife])
    return errors
