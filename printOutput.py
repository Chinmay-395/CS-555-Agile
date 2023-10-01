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