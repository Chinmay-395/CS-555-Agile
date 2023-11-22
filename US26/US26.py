import pandas as pd

def checkCorrespondingEntries(individuals, families):
    inconsistencies = []

    # Check for each individual
    for index, person in individuals.iterrows():
        # Check as a child
        if 'CHILD' in person and not pd.isnull(person['CHILD']):
            if not any(person['CHILD'] in family['CHILDREN'] for index, family in families.iterrows() if not pd.isnull(family['CHILDREN'])):
                inconsistencies.append(f"Individual {person['ID']} as child not found in family records")

        # Check as a spouse
        if 'SPOUSE' in person and not pd.isnull(person['SPOUSE']):
            for spouse_family in person['SPOUSE']:
                if not any(spouse_family == family['ID'] for index, family in families.iterrows()):
                    inconsistencies.append(f"Individual {person['ID']} as spouse not found in family {spouse_family}")

    # Check for each family
    for index, family in families.iterrows():
        # Check husband
        if 'HUSBAND ID' in family and not pd.isnull(family['HUSBAND ID']):
            if not any(family['HUSBAND ID'] in individual['SPOUSE'] for index, individual in individuals.iterrows() if not pd.isnull(individual['SPOUSE'])):
                inconsistencies.append(f"Family {family['ID']} husband {family['HUSBAND ID']} not found in individual records")

        # Check wife
        if 'WIFE ID' in family and not pd.isnull(family['WIFE ID']):
            if not any(family['WIFE ID'] in individual['SPOUSE'] for index, individual in individuals.iterrows() if not pd.isnull(individual['SPOUSE'])):
                inconsistencies.append(f"Family {family['ID']} wife {family['WIFE ID']} not found in individual records")

        # Check children
        if 'CHILDREN' in family and not pd.isnull(family['CHILDREN']):
            for child in family['CHILDREN']:
                if not any(child == individual['CHILD'] for index, individual in individuals.iterrows() if not pd.isnull(individual['CHILD'])):
                    inconsistencies.append(f"Family {family['ID']} child {child} not found in individual records")

    if len(inconsistencies) == 0:
        return "US26: All entries are corresponding"
    else:
        return inconsistencies

