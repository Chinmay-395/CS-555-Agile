from datetime import datetime

def calculate_age(birthday):
    try:
        # Attempt to parse the birthdate from GEDCOM format ('1990 JAN 1') to datetime object
        print("THE TYPE ", type(birthday))
        birthdate = datetime.strptime(birthday, '%d %b %Y')
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
        # print("each person ",person)
        print("THE AGE OF PERSON ",person["AGE"], " ",person["NAME"])
        # cannot testify if the "nan" with length of the list
        if person["AGE"] > 30 and person["ALIVE"] and type(person["SPOUSE"]) is not list:
            living_singles_over_30.append((person["ID"], person["AGE"], person["NAME"]))
    
    if len(living_singles_over_30) > 0:
        print('List of Living Singles Over 30 who have never been married:')
        for person in living_singles_over_30:
            print(f'ID: {person[0]}, Age: {person[1]}, Name: {person[2]}')
    else:
        print('US31: No one over 30 who has never been married.')


