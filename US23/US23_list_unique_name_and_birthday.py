import pandas as pd


def listUniqueNameAndBirthdays(individuals):
    errors = []
    name_birthday_map = {}

    for index, row in individuals.iterrows():
        if row["BIRTHDAY"] in name_birthday_map:
            if row["NAME"] in name_birthday_map[row["BIRTHDAY"]]:
                errors.append(f'{row["NAME"]} / {row["BIRTHDAY"]}')
            else:
                name_birthday_map[row["BIRTHDAY"]].append(row["NAME"])
        else:
            name_birthday_map[row["BIRTHDAY"]] = [row["NAME"]]

    if len(errors) > 0:
        return f"US23: List of people with the same name and birthday: {errors}"
    else:
        return f"US23: No people with the same name and birthday"
