import pandas as pd

def noMarriageToDescendants(individuals, families):
    def getDescendants(person_id, descendants):
        children = families[(families['HUSBAND ID'] == person_id) | (families['WIFE ID'] == person_id)]['CHILDREN']
        for child_list in children:
            for child in child_list:
                if child not in descendants:
                    descendants.append(child)
                    getDescendants(child, descendants)
        return descendants

    violations = []
    for index, family in families.iterrows():
        husband_descendants = getDescendants(family['HUSBAND ID'], [])
        wife_descendants = getDescendants(family['WIFE ID'], [])

        if family['WIFE ID'] in husband_descendants:
            violations.append((family['HUSBAND ID'], family['WIFE ID']))
        elif family['HUSBAND ID'] in wife_descendants:
            violations.append((family['WIFE ID'], family['HUSBAND ID']))

    if len(violations) == 0:
        return "US18: No marriages to descendants found"
    else:
        return violations


