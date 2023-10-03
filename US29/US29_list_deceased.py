import pandas as pd


def listDeceased(individuals):
    # Data Validation
    if not isinstance(individuals, pd.DataFrame):
        return "ERROR: US29: Input parameter of wrong type."
    if len(individuals) == 0:
        return "ANOMALY: US29: No family members available."

    deceased_people = []

    # Iterate through dataframe
    for index, person in individuals.iterrows():
        if person["ALIVE"] == False:
            deceased_people.append((person["ID"], person["NAME"]))

    if len(deceased_people) > 0:
        return deceased_people
    else:
        return "US29: There are no deceased_people in the GEDCOM file."
