# User Story 37

from datetime import date, datetime
import pandas as pd
from printOutput import printingAllTheStuff
def is_within_last_30_days(event_date):
    return (date.today() - datetime.strptime(event_date," %d %b %Y").date()).days <= 30 if pd.notna(event_date) else False
    
# List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
# Assuming spouses mean they were married at one point and don't have to be together
def list_recent_survivors(individuals, families):
    # print("HELLOOO")
    recent_survivors = []
    for index, row in individuals.iterrows():
        if not row['ALIVE']:
            if is_within_last_30_days(row['DEATH']):
                print("THE NAME: ",row['NAME'])
                living_spouses, living_descendants = [], []
                for family in row['SPOUSE']:
                    family_row = families.loc[families['ID'] == family]
                    print("the family row", family_row)
                    # living_spouses and living_descendents lists are unsorted
                    gender_column_string = 'HUSBAND ID' if row['GENDER'] != 'M' else 'WIFE ID'
                    spouse_id = family_row.at[family_row.index[0], gender_column_string]

                    spouse_row = individuals.loc[individuals['ID'] == spouse_id]
                    spouse_age = spouse_row.at[spouse_row.index[0], 'AGE']
                    spouse_alive = spouse_row.at[spouse_row.index[0], 'ALIVE']
                    living_spouses.append((spouse_id, spouse_age)) if spouse_alive else None

                    children_list = family_row.at[family_row.index[0], 'CHILDREN']
                    descendants_rows = individuals.loc[individuals['ID'].isin(children_list) & individuals['ALIVE'] == True]

                    for index, descendant in descendants_rows.iterrows():
                        living_descendants.append((descendant['ID'], descendant['AGE']))

                # print("THE ENTIRE ROW", row)
                new_recent_survivors = {
                    'name': (row['ID'], row['AGE']),
                    'living spouses': living_spouses, 
                    'living descendants': living_descendants
                }
                recent_survivors.append(new_recent_survivors)

    if len(recent_survivors)>0:
        print("US37: The list of all living spouses and descendants of people who died in the last 30 days: " + str(recent_survivors))
    elif len(recent_survivors) == 0:
        print("US37: No recent survivors found ")
    # printingAllTheStuff(pd.DataFrame())