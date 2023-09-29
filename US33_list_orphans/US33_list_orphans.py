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

def hasDeadParents(child_id, individuals, families):
    deadparents = False
    for index, row in families.iterrows():
        # print("THE TYPE OF CHILDREN ", type(row['CHILDREN']))
        res = ast.literal_eval(row['CHILDREN'])
        # row['children'] != 'nan' does not work because it can be a list, so to check if entry is not empty check if it's a list
        if type(row['CHILDREN']) is str and (child_id in res):
            husband_id = row['HUSBAND ID']
            wife_id = row['WIFE ID']
            deadparents = not individuals[individuals['ID']==husband_id].squeeze()['ALIVE'] and not individuals[individuals['ID']==wife_id].squeeze()['ALIVE']
    return deadparents