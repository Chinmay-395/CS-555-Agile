import ast
def listOrphans(individuals, families):
    orphans = []
    for index, row in individuals.iterrows():
        if row['AGE'] < 18:
            if hasDeadParents(row['ID'],individuals,families):
                orphans.append((row['ID'], row['AGE'], row['NAME']))
    if len(orphans) > 0:
        print('US33: List of Orphans:')
        print(orphans) 
    elif len(orphans) == 0:
        print('US33: No orphans in this family tree')

def hasDeadParents(child_id, individuals, families):
    deadparents = False
    for index, row in families.iterrows():
        if type(row['CHILDREN']) is list and (child_id in row['CHILDREN']):
            husband_id = row['HUSBAND ID']
            wife_id = row['WIFE ID']
            deadparents = not individuals[individuals['ID']==husband_id].squeeze()['ALIVE'] and not individuals[individuals['ID']==wife_id].squeeze()['ALIVE']
    return deadparents