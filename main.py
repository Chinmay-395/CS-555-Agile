from prettytable import PrettyTable
from datetime import datetime
import time

def checkIfValidTag(tagVal:str) -> str:
    listOfValidTags = ["INDI","NAME", "SEX", "BIRT", "DEAT", 
                       "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE",
                        "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
    valid = "N"
    if tagVal in listOfValidTags:
        valid = "Y"
    return valid

def dematrializing(input_string_list:list[str]) -> tuple[str,str,str,str]:
    l_lvl = input_string_list[0]
    # check whether the tag exists on the 2nd position
    if len(input_string_list) > 2 and checkIfValidTag(input_string_list[1]) == "Y":
        l_Tag = input_string_list[1]
        l_valid = "Y"
        if len(input_string_list) > 2:
            l_args = input_string_list[2]
        else:
            l_args = ""
    # tags such as TRLR and HEAD only have 2 values which is level and tag
    elif len(input_string_list) == 2 :
        # print("The String is invalid", input_string_list)
        l_lvl = input_string_list[0]
        l_Tag = input_string_list[1]
        l_valid = checkIfValidTag(input_string_list[1])
        l_args=""    
    # if the tag is present at 3rd position
    elif len(input_string_list) > 2 and checkIfValidTag(input_string_list[2]) == "Y":
        l_Tag = input_string_list[2]
        l_valid = "Y"
        if len(input_string_list) > 1:
            l_args = input_string_list[1]
        else:
            l_args = ""
    # finally at the very end if those tags are not present any of these.
    else:
        l_Tag = input_string_list[1]
        l_valid = "N"
        if len(input_string_list) > 2:
            l_args = input_string_list[2]
        else:
            l_args = ""
    return l_lvl, l_Tag, l_valid, l_args



# Read the GEDCOM file line by line Chinmay_Dali_GEDCOM
with open("Sachin_Devangan_CS_555_WS4.ged", "r") as file:
    file_content = ""
    for line in file:
        # read each line
        print(f"--> {line}")
        file_content = file_content + f"--> {line} \n"
        # Remove leading and trailing whitespace
        the_input_string = line.strip().split(" ", 2)
        # check if there are empty spaces or empty lines in the GED file
        if(len(line) == 1 and line.isspace()):
            print("")
        else:
            
            level, tag, valid, argument = dematrializing(the_input_string)
            # Print the formatted output
            if(
            len(level) != 0 and 
            len(tag) != 0 and 
            len(valid) != 0):
                output_str = f"<-- {level}|{tag}|{valid}|{argument} \n"
                print(output_str)
                file_content += output_str


# Open the file in "w" mode, which will create or overwrite the file
with open("output.txt", "w") as file:
    file.write(file_content)

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
    op_list = [0 for i in range(6)]
    op_list[5] = []
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
    list_indi = []
    list_fam = []
    indi = indi_list()
    print("THE SIZE OF INDI ", len(indi))
    fam = fam_list()
    print("THE SIZE OF INDI ", len(fam))
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
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[1] = str[2]
                if(str[1] == 'WIFE'):
                    fam[2] = str[2]
                if(str[1] == 'CHIL'):
                    fam[5].append(str[2])
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = date
                        indi[7] = "Y"
                        date_format_as = str[2] + " " + str[3] + " " + str[4]
                        print("date ",date_format_as)
                        indi[8] = calculate_age(date_format_as)
                    if(date_id == 'DEAT'):
                        indi[4] = date
                        indi[7] = "N"
                    if(date_id == 'MARR'):
                        fam[3] = date
                    if(date_id == 'DIV'):
                        fam[4] = date
    return list_indi, list_fam

def main(file_name):
    list_indi, list_fam = parse(file_name)
    # list_indi.sort()
    # list_fam.sort()
    print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    print_list(list_indi)
    print_list(list_fam)

main('Sachin_Devangan_CS_555_WS4.ged')