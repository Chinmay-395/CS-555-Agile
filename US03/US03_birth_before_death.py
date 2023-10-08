import pandas as pd

gedcom_file_line_number = -1


def birthBeforeDeath(individuals):
    # Data Validation
    if not isinstance(individuals, pd.DataFrame):
        return "ERROR: Input parameter of wrong type."
    if len(individuals) == 0:
        return "ERROR: No family members available."

    birth_before_death_errors = []

    # Iterate through dataframe
    for index, person in individuals.iterrows():
        if person["ALIVE"] == False:
            person_id = person["ID"]
            if person["DEATH"] == "NA":
                return f"ERROR: {person_id} is dead, but no Death date given"
            death_date = pd.to_datetime(person["DEATH"]).strftime("%Y-%m-%d")
            birth_date = pd.to_datetime(person["BIRTHDAY"]).strftime("%Y-%m-%d")
            if birth_date >= death_date:
                birth_before_death_errors.append(
                    f"ERROR: INDIVIDUAL: US03: {gedcom_file_line_number}: {person_id}: Died {death_date} before born {birth_date}"
                )

    return birth_before_death_errors
