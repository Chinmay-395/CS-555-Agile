def test_male_last_names(families, individuals):
    errors = []

    for family in families:
        # Assuming that the 'HUSBAND NAME' key holds the full name, split it to get the last name.
        if 'HUSBAND NAME' in family:
            husband_name = family['HUSBAND NAME']
            # The last name will be the last part of the 'HUSBAND NAME' after split.
            husband_last_name = husband_name.strip().split(' ')[-1]
            children_ids = family.get('CHILDREN', [])
            for child_id in children_ids:
                # Find the child in individuals
                child = next((item for item in individuals if item["ID"] == child_id), None)
                if child and child['gender'] == 'M':
                    child_name = child['NAME']
                    child_last_name = child_name.strip().split(' ')[-1]
                    # Check if the last names match
                    if child_last_name != husband_last_name:
                        errors.append(f"USXX:ERROR: FAMILY: {family['ID']} Male member {child['ID']} named {child_name} does not have the same last name as the father {husband_last_name}")

    return errors
