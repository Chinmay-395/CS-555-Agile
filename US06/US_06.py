from datetime import datetime
import pandas as pd

def convert_gedcom_date_to_datetime(gedcom_date, each_row):
    return datetime.strptime(gedcom_date.strip(), '%d %b %Y')

def test_divorce_before_death(families, individuals):
    errors = []
    for index, row in families.iterrows():
        if row["MARRIED"] is not None and row["DIVORCE"] is not None:
            husband = row["HUSBAND ID"]
            wife = row["WIFE ID"]
            divorce_date = convert_gedcom_date_to_datetime(row["DIVORCE"], row)
            husband_death_date = individuals[individuals['ID']==husband].squeeze()['DEATH']
            wife_death_date = individuals[individuals['ID']==wife].squeeze()['DEATH']
            if not pd.isna(husband_death_date):
                husband_death_date = convert_gedcom_date_to_datetime(husband_death_date, row)
                if husband_death_date < divorce_date:
                    errors.append(f"US06:ERROR: FAMILY: Husband ID {husband} Wife ID {wife} divorced after death")
            if not pd.isna(wife_death_date):
                wife_death_date = convert_gedcom_date_to_datetime(wife_death_date, row)
                if wife_death_date < divorce_date:
                    errors.append(f"US06:ERROR: FAMILY: Husband ID {husband} Wife ID {wife} divorced after death")
    return errors
