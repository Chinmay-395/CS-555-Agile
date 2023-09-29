from prettytable import PrettyTable
from datetime import datetime
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import time
import ast


# list of headers in individual tables
'''
Individual Table:
ID, NAME, Gender, Birthday, Age, Alive, Death, Child, Spouse

Families
ID, Married, Divorced, Husband ID, Husband Name, Wife ID, Wife Name, Children
'''

"""This function creates a new list for an individual"""
def indi_list():
    op_list = [0 for i in range(9)]
    op_list[5] = []
    return op_list

"""This function creates a new list for a family"""
def fam_list():
    op_list = [0 for i in range(8)]
    op_list[7] = []
    return op_list

"""This function takes input '/Last_Name/' and returns 'Last_Name' as output (removes the slashes in .ged file)"""
def getLastName(str):
    temp=''
    for i in str:
        if(i != '/'):
            temp += i
    return temp

"""This function prints the contents of the input list"""
def print_list(ip_list):
    print("\n")
    for i in ip_list:
        print(i)

def print_Indi(ip_list):
    table = PrettyTable()
    table.field_names = ["ID", "NAME", "GENDER","BIRTHDAY","DEATH","CHILD","SPOUSE","ALIVE", "AGE"]
    for i in ip_list:
        table.add_row(i)
    
    tbl_as_csv = table.get_csv_string().replace('\r','')
    # saving it as individual table in a excel file
    text_file = open("individual_tb.csv", "w")
    n = text_file.write(tbl_as_csv)
    text_file.close()

def print_Fam(ip_list):
    table = PrettyTable()
    table.field_names = ["ID", "MARRIED", "DIVORCE","HUSBAND ID","HUSBAND NAME","WIFE ID","WIFE NAME","CHILDREN"]
    for i in ip_list:
        table.add_row(i)
    
    tbl_as_csv = table.get_csv_string().replace('\r','')
    # saving it as family table in a excel file
    text_file = open("family_tb.csv", "w")
    n = text_file.write(tbl_as_csv)
    text_file.close()


def calculate_age(date_of_birth):
    # Define a dictionary to map month names to their numeric values
    month_mapping = {
        'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
        'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
    }

    # Split the date_of_birth string into day, month, and year
    parts = date_of_birth.split()
    day = int(parts[0])
    month = month_mapping[parts[1].upper()]
    year = int(parts[2])

    # Get the current date
    current_date = datetime.now()

    # Create a datetime object for the date of birth
    dob = datetime(year, month, day)

    # Calculate the age
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

    return age

"""This function parses the GEDCOM File and returns 2 lists: one for individuals and another for families"""
def parse(file_name):
    f = open(file_name,'r')
    indi_on = 0
    fam_on = 0
    giant_dict = {}
    list_indi = []
    list_fam = []
    indi = indi_list()
    
    fam = fam_list()
    
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indi_on == 1):
                    list_indi.append(indi)
                    indi = indi_list()
                    indi_on = 0
                if(fam_on == 1):
                    list_fam.append(fam)
                    fam = fam_list()
                    fam_on = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indi_on = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        fam_on = 1
                        fam[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + getLastName(str[3])
                    giant_dict[indi[0]] = indi[1]
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[3] = str[2]
                    fam[4] = giant_dict[str[2]]
                if(str[1] == 'WIFE'):
                    fam[5] = str[2]
                    fam[6] = giant_dict[str[2]]
                if(str[1] == 'CHIL'):
                    fam[7].append(str[2])
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = date
                        indi[7] = "TRUE"
                        date_format_as = str[2] + " " + str[3] + " " + str[4]
                        # print("date ",date_format_as)
                        indi[8] = calculate_age(date_format_as)
                        indi[4] = "NA" #death will be NA until it is explicitly mentioned
                    if(date_id == 'DEAT'):
                        indi[4] = date
                        indi[7] = "FALSE"
                    # checking for married status    
                    if(date_id == 'MARR'):
                        fam[1] = date
                        fam[2] = "NA" # divorce will be NA until it is explicitly mentioned
                    # elif(date_id != 'MARR'):
                    #     fam[1] = "NA"
                    #     fam[5] = "NA"
                    #     fam[6] = "NA"
                    # checking if dead
                    if(date_id == 'DIV'):
                        fam[2] = date
    return list_indi, list_fam

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