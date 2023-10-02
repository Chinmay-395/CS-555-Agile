from datetime import datetime

def calculate_age(birthday):
    try:
        # Attempt to parse the birthdate from GEDCOM format ('1990 JAN 1') to datetime object
        birthdate = datetime.strptime(birthday, '%Y %b %d')
    except ValueError:
        # Handle other date formats or return an error code as needed
        return None
    
    # Get the current date
    current_date = datetime.now()
    # Calculate age
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age

def listLivingSinglesOver30(individuals):
    living_singles_over_30 = []
    for index, person in individuals.iterrows():
        print(f"Checking person: {person['NAME']}, Age: {calculate_age(person['BIRTHDAY'])}, Married: {len(person['SPOUSE']) > 0}")
        if calculate_age(person["BIRTHDAY"]) > 30 and person["ALIVE"] and len(person["SPOUSE"]) == 0:
            living_singles_over_30.append((person["ID"], person["AGE"], person["NAME"]))
    
    if len(living_singles_over_30) > 0:
        print('List of Living Singles Over 30 who have never been married:')
        for person in living_singles_over_30:
            print(f'ID: {person[0]}, Age: {person[1]}, Name: {person[2]}')
    else:
        print('US31: No one over 30 who has never been married.')


