import math
from datetime import datetime
from datetime import date
import pandas as pd
def date_check(the_date):
  return date.today() > the_date.date()

def dates_before_current_date(indi_df, fam_df):
    for id in indi_df['ID']:
        birthday_date = indi_df.loc[indi_df['ID'] == id, 'BIRTHDAY'].iloc[0]
        if not date_check(datetime.strptime(birthday_date," %d %b %Y")):
            print("ERROR: INDIVIDUAL: US01: " + " Birthday" + birthday_date + " occurs in the future")

    is_alive = indi_df.loc[indi_df['ID'] == id, 'ALIVE'].iloc[0]
    if not is_alive:
        death_date = indi_df.loc[indi_df['ID'] == id, 'DEATH'].iloc[0]
        if not date_check(datetime.strptime(death_date," %d %b %Y")):
            print("ERROR: INDIVIDUAL: US01: " + " Death" + death_date + " occurs in the future")


    for id in fam_df['ID']:
        marriage_date = fam_df.loc[fam_df['ID'] == id, 'MARRIED'].iloc[0]
        if not date_check(datetime.strptime(marriage_date," %d %b %Y")):
            print("ERROR: FAMILY: US01: " + " Married" + marriage_date + " occurs in the future")
    
    are_divorced = fam_df.loc[fam_df['ID'] == id, 'DIVORCE STATUS'].iloc[0]
    if are_divorced:
        divorce_date = fam_df.loc[fam_df['ID'] == id, 'DIVORCED'].iloc[0]
        if not date_check(datetime.strptime(divorce_date," %d %b %Y")):
            print("ERROR: FAMILY: US01: " + " Divorce" + divorce_date + " occurs in the future")


