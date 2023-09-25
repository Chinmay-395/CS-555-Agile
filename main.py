from prettytable import PrettyTable
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
with open("Chinmay_Dali_GEDCOM.ged", "r") as file:
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

def individualTable(path:str) -> None:
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("File not found : ",path )
    else:
        print("path found")
        content_list = []
        file_content = fp.readlines()
        for line in file_content:
            line = list(line.rstrip("\n").split(" ", 2))
            content_list.append(line)
        counter =0
        for i in content_list:
            if int(i[0]) == 0 and len(i) == 3 and i[2] == 'INDI':
                data = create_data(counter, content_list, i[1])
                
            elif int(i[0]) == 0 and len(i) == 3 and i[2] == 'FAM':
                data = create_data(counter, content_list, i[1])
                
            counter = counter + 1
            fp.close()

# get the today's date
today = time.strftime("%Y %m %d").split(' ')
# months of the year
month=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
# date format as YYYY-MM-DD
def date_format(date_list):
    yyyy=date_list[2]
    mm=('%02d' % (month.index(date_list[1])+1))
    dd= '%02d' % int(date_list[0])
    return (yyyy, mm, dd)

# meta function to calculate age
def age_carry(new,old):
    if(new[1]<old[1]):
        return 1
    elif(new[1]==old[1] and new[2]<old[2]):
        return 1
    else:
        return 0

def print_indi(indi_dict):
    x = PrettyTable(["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"])
    for _u,_v in indi_dict.items():
        uid=_u
        name=_v.get('NAME')
        sex=_v.get('SEX', 'NA')
        DOB=_v.get('BIRT', 'NA')
        born = (DOB!='NA')
        if born:
            DOB=date_format(DOB.split(' '))
        DOD=_v.get('DEAT','NA')
        alive=(DOD=='NA')
        if not alive:
            DOD = date_format(DOD.split(' '))
        if not born:
            age = 'NA'
        elif alive:
            age = int(today[0]) - int(DOB[0]) - age_carry(today,DOB)
        else:
            age = int(DOD[0]) - int(DOB[0]) - age_carry(DOD,DOB)
        child=_v.get('FAMC','NA')
        spouse=_v.get('FAMS', 'NA')
        x.add_row([uid,name,sex,born and '-'.join(DOB) or 'NA', age, born and alive, alive and 'NA' or '-'.join(DOD), child, spouse])
    print(x)