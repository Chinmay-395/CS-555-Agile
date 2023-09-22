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