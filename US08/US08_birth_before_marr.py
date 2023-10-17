from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import sys
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/")
from US40.US40_include_ip_lines import get_line
MONTHS_AFTER_DIVORCE = 9

def birth_before_marriage_of_parents(indi_df, fam_df):
    """
    Function to identify individuals born before the marriage of their parents.

    Parameters:
    - indi_df: DataFrame of individuals.
    - fam_df: DataFrame of families.

    Returns:
    - anomalies_df: DataFrame of identified anomalies.
    """
    # print("US40: BIRTH BEFORE MARRIAGE OF PARENTS ")
    list_ans = []
    list_of_anomalies = []
    list_of_errors = []
    
    for _, each_indi in indi_df.iterrows():
        family_id = each_indi['CHILD']
        if pd.isna(family_id):
            list_ans.append(each_indi)
        else:
            try:
                family = fam_df[fam_df['ID'] == family_id].iloc[0]
                indi_birthday = convert_gedcom_date_to_datetime(each_indi['BIRTHDAY'],each_indi)
                family_married_date = convert_gedcom_date_to_datetime(family['MARRIED'],each_indi)
                if indi_birthday < family_married_date:
                    list_of_anomalies.append((each_indi['ID'], each_indi['AGE'], each_indi['NAME']))
                elif family['DIVORCE STATUS'] == True and indi_birthday > family_married_date + relativedelta(months=+9):  # 9 months in days
                    list_of_anomalies.append((each_indi['ID'], each_indi['AGE'], each_indi['NAME']))
                else:
                    list_ans.append(each_indi)
            
            except IndexError:
                list_of_errors.append(f"No family found with ID: {family_id} for individual {each_indi['ID']}")
            except Exception as e:
                line_no = get_line(each_indi['ID'])
                list_of_errors.append(f"Error processing record {each_indi['ID']}: {str(e)} at line number {line_no}")

    
    print("US08: BIRTH BEFORE MARRIAGE OF PARENTS ")
    if len(list_of_anomalies) > 0:
        print(list_of_anomalies)
    elif len(list_of_anomalies) == 0:
        print("US08: No births before marriage of parents")
    if list_of_errors:
        for error in list_of_errors:
            print(error)
    

def convert_gedcom_date_to_datetime(gedcom_date, each_row):
    """Convert GEDCOM date format to Python datetime object."""
    try:
        return datetime.strptime(gedcom_date.strip(), '%d %b %Y')
    # remove the below exception
    except ValueError:
        if 'I' in each_row[0]:
            print(f"US08: ERROR: INDIVIDUAL: Incorrect data for birthday {each_row[6]} in individual ID {each_row[0]}")
        else:
            print(f"US08: ERROR: FAMILY: Incorrect data for marriage {each_row[6]} in Family ID {each_row[0]}")
        return None
    
    
