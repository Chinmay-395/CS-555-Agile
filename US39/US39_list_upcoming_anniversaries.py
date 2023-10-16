import pandas as pd
from datetime import datetime, timedelta

"""
This is the second attempt. Refactored some of the code and reduced complexity. Also made it much more readable
"""


# Check if the spouse with the given ID is alive.
def is_spouse_alive(individuals, spouse_id):
    spouse_info = individuals[individuals['ID'] == spouse_id]
    return spouse_info['ALIVE'].any() if not spouse_info.empty else False


# Check if the anniversary is within the next 'days' days.
def is_anniversary_within_range(marriage_date, days=30):
    current_date = datetime.now()
    anniversary_in_range = (
        current_date + timedelta(days=days)) >= marriage_date >= current_date
    return anniversary_in_range


# List upcoming anniversaries for spouses who are alive.
def listUpcomingAnniversaries(individuals, family, days=30):
    upcoming_anniversaries = set()

    for index, row in family.iterrows():
        husband_id, wife_id = row['HUSBAND ID'], row['WIFE ID']

        # Check if either the husband or wife is alive
        if is_spouse_alive(individuals, husband_id) or is_spouse_alive(individuals, wife_id):
            marriage_date = datetime.strptime(
                row['MARRIED'].strip(), '%d %b %Y')
            # Adjust the year of marriage date to the current year
            marriage_date = marriage_date.replace(year=datetime.now().year)

            if is_anniversary_within_range(marriage_date, days):
                anniversary_tuple = (
                    row['HUSBAND NAME'], row['WIFE NAME'], marriage_date.strftime('%d %b'))
                upcoming_anniversaries.add(anniversary_tuple)

    if len(upcoming_anniversaries) == 0:
        return "US39: There are no upcoming anniversaries."
    else:
        return upcoming_anniversaries


"""
This is the first attempt to write this function. No refactoring has been done.
"""
# def listUpcomingAnniversaries(individuals, family, days=30):
#     # Data Validation
#     if not isinstance(family, pd.DataFrame) or not isinstance(individuals, pd.DataFrame):
#         return "ERROR: Input parameters of the wrong type."

#     if len(family) == 0 or len(individuals) == 0:
#         return "ANOMALY: No family members or individuals available."

#     upcoming_anniversaries = set()
#     current_date = datetime.now()

#     for index, row in family.iterrows():
#         husband_id = row['HUSBAND ID']
#         wife_id = row['WIFE ID']

#         # Check if either the husband or wife is alive
#         is_husband_alive = individuals.loc[individuals['ID']
#                                            == husband_id, 'ALIVE'].values
#         is_wife_alive = individuals.loc[individuals['ID']
#                                         == wife_id, 'ALIVE'].values

#         if (is_husband_alive and is_husband_alive[0]) or (is_wife_alive and is_wife_alive[0]):
#             marriage_date = datetime.strptime(
#                 row['MARRIED'].strip(), '%d %b %Y')
#             # Adjust the year of marriage date to the current year
#             marriage_date = marriage_date.replace(year=current_date.year)

#             # Check if the anniversary is within the next 30 days
#             anniversary_in_range = (
#                 current_date + timedelta(days=days)) >= marriage_date >= current_date
#             if anniversary_in_range:
#                 anniversary_tuple = (
#                     row['HUSBAND NAME'], row['WIFE NAME'], marriage_date.strftime('%d %b'))
#                 upcoming_anniversaries.add(anniversary_tuple)

#     if len(upcoming_anniversaries) == 0:
#         return "US39: There are no upcoming anniversaries."
#     else:
#         return upcoming_anniversaries
