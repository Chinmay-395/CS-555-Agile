from datetime import datetime
import pandas as pd

def convert_gedcom_date_to_datetime(gedcom_date, each_row):
    try:
        return datetime.strptime(gedcom_date.strip(), '%d %b %Y')
    # remove the below exception
    except ValueError:
        print(f"US05: ERROR: FAMILY: Incorrect data for marriage {each_row[6]} in family ID {each_row[0]}")
        return None

def test_marriage_before_death(families, individuals):
    errors = []
    for index, row in families.iterrows():
        if "MARRIED" in families and row["MARRIED"] is not None:
            husband = row["HUSBAND ID"]
            wife = row["WIFE ID"]
            # print("type: ",type(row))
            # print("row \n", row)
            marriage_date = convert_gedcom_date_to_datetime(row["MARRIED"], row)
            husband_death_date = individuals[individuals['ID']==husband].squeeze()['DEATH']
            wife_death_date = individuals[individuals['ID']==wife].squeeze()['DEATH']
            if not pd.isna(husband_death_date):
                husband_death_date = convert_gedcom_date_to_datetime(husband_death_date,row)
                if husband_death_date<marriage_date:
                    errors.append([husband,wife])
            if not pd.isna(wife_death_date):
                wife_death_date = convert_gedcom_date_to_datetime(wife_death_date, row)
                if wife_death_date<marriage_date:
                    errors.append([husband,wife])
    # return errors
    if len(errors) > 0:
        for each_err in errors:
            print(f"US05: \n ERROR: FAMILY: Husband ID {each_err[0]} Wife ID {each_err[1]} married after death")
    elif len(errors) == 0:
        print("US05: No Marriage before death")
