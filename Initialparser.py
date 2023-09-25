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