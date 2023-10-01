# def listLivingSingles(individuals):
#     print(individuals)
#     living_singles = []
#     for index, row in individuals.iterrows():
#         if row['AGE'] >= 18 and row['ALIVE'] == True and len(row['SPOUSE']) == 0 :
#             living_singles.append((row['ID'], row['AGE'], row['NAME']))
#     if len(living_singles) > 0:
#         print('US31: List of Living Singles:')
#         print(living_singles)

# from datetime import datetime

# # Function to parse date and calculate age
# def calculate_age(birthday_str):
#     try:
#         # Parse the date with the format "YYYY MMM D"
#         birthdate = datetime.strptime(birthday_str, "%Y %b %d")
#         return birthdate
#     except ValueError:
#         # Handle different date formats if needed
#         print("Invalid date format:", birthday_str)
#         return None

# # Function to list living singles
# def listLivingSingles(individuals):
#     living_singles = []
#     for _, person in individuals.iterrows():
#         birthdate = calculate_age(person["BIRTHDAY"])
#         if birthdate and birthdate.year <= 2005 and person["ALIVE"] == "True" and person["SPOUSE"] == "NA":
#             living_singles.append((person["ID"], birthdate.strftime("%Y-%m-%d"), person["NAME"]))
#     if len(living_singles) > 0:
#         print("US31: List of Living Singles:")
#         for single in living_singles:
#             print(single)


# from datetime import datetime

# def calculate_age(birthday):
#     # Parse the birthday string into a datetime object
#     birthdate = datetime.strptime(birthday, '%Y %b %d')
    
#     # Get the current date
#     current_date = datetime.now()
    
#     # Calculate the age
#     age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    
#     return age


# def listLivingSinglesOver30(individuals_data):
#     living_singles_over_30 = []
#     for person in individuals_data:
#         if calculate_age(person["BIRTHDAY"]) > 30 and person["ALIVE"] and len(person["SPOUSE"]) == 0:
#             living_singles_over_30.append((person["ID"], person["NAME"], calculate_age(person["BIRTHDAY"])))
#     if living_singles_over_30:
#         print("List of Living Singles Over 30 Who Have Never Been Married:")
#         for person_id, person_name, person_age in living_singles_over_30:
#             print(f"ID: {person_id}, Name: {person_name}, Age: {person_age}")

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


