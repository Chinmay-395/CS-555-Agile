
from datetime import datetime
import pandas as pd
from Initialparser import print_Indi, print_Fam, parse
from datetime import date
import time
import ast


def listOrphans(individuals, families):
    orphans = []
    for index, row in individuals.iterrows():
        if row['AGE'] < 18:
        # print("THE ROW ", row['NAME'], " id ", row['ID'])
            if hasDeadParents(row['ID'],individuals,families):
                orphans.append((row['ID'], row['AGE']))
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

def main(file_name):
    list_indi, list_fam = parse(file_name)
    print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    print_Indi(list_indi)
    print_Fam(list_fam)
    df_indi = pd.read_csv('individual_tb.csv')
    df_fam = pd.read_csv('family_tb.csv')
    listOrphans(df_indi,df_fam)

main('sa3.ged')