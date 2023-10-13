import pandas as pd
from datetime import datetime

def listUpcomingBirthdays(individuals, days=30):
    # Data Validation
    if not isinstance(individuals, pd.DataFrame):
        return "ERROR: US38: Input parameter of wrong type."
    if len(individuals) == 0:
        return "ANOMALY: US38: No family members available."

    upcoming_birthdays = []  
    current_date = datetime.now() 

    for index, row in individuals.iterrows():
        if row['BIRTHDAY'] != '':  # Check if the birthdate is available in the data
            # Parse the birthdate from GEDCOM format (' 1999 JAN 1') to datetime object
            # there is extra space that needs to be considered as dates are in string and they have an initial single character space
            birthdate = datetime.strptime(row['BIRTHDAY'], " %d %b %Y")
            
            # Calculate the next occurrence of the birthdate in the current year
            next_birthday = birthdate.replace(year=current_date.year)
            if next_birthday < current_date:
                next_birthday = next_birthday.replace(year=current_date.year + 1)

            # Calculate the number of days between current date and next birthday
            days_until_birthday = (next_birthday - current_date).days
            
            if 0 <= days_until_birthday <= days:
                # If the condition is met, add the individual's ID, birthdate, and name to the upcoming_birthdays list
                upcoming_birthdays.append((row['ID'], row['BIRTHDAY'], row['NAME']))
                
    if len(upcoming_birthdays) > 0:
        # print('US35: List of Upcoming birthday (next', days, 'days):')
        # print(upcoming_birthdays)
        return upcoming_birthdays
    else:
        # print('US35: No Upcoming birthday found in the next', days, 'days.')
         return 'US38: There are no Upcoming Birthdays in the GEDCOM file.'

