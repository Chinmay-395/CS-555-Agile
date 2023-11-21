import pandas as pd


def listMultipleBirths(individuals, families):
    multiple_birth_families = []
    for index, family_row in families.iterrows():
        children_list = family_row["CHILDREN"]
        if len(children_list) >= 5:
            same_birthday_count = 0
            common_birthday = None

            for child_id in children_list:
                # Find the individual's entry for the child
                for ind_index, ind_row in individuals.iterrows():
                    if ind_row["ID"] == child_id:
                        child_birthday = ind_row["BIRTHDAY"]

                        # If common_birthday is not set, set it to the current child's birthday
                        if common_birthday is None:
                            common_birthday = child_birthday

                        # Check if the current child's birthday matches the common_birthday
                        if child_birthday == common_birthday:
                            same_birthday_count += 1

            # If more than 5 children have the same birthday, print the family ID
            if same_birthday_count == 5:
                multiple_birth_families.append(family_row["ID"])

    if len(multiple_birth_families) > 0:
        return f"US32: List of families with multiple births: {multiple_birth_families}"
    else:
        return f"US32: There are no families with multiple births."
