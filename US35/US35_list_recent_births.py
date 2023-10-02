from datetime import datetime

def listRecentBirths(individuals, days=30):
    recent_births = []  
    current_date = datetime.now() 

    for index, row in individuals.iterrows():
        if row['BIRTHDAY'] != 'NA':  # Check if the birthdate is available in the data
            # Parse the birthdate from GEDCOM format ('1999 JAN 1') to datetime object
            birthdate = datetime.strptime(row['BIRTHDAY'], '%Y %b %d')
            # Calculate the number of days between birthdate and current date
            days_since_birth = (current_date - birthdate).days
            
            
            if days_since_birth <= days:
                # If the condition is met, add the individual's ID, birthdate, and name to the recent_births list
                recent_births.append((row['ID'], row['BIRTHDAY'], row['NAME']))
                
   
    if len(recent_births) > 0:

        print('US35: List of Recent Births (last', days, 'days):')
        print(recent_births)
    else:

        print('US35: No recent births found in the last', days, 'days.')
