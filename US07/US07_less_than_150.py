def less_than_150_years(indi_fam):
    bool_val = False
    for index, row in indi_fam.iterrows():
        if row["AGE"] > 150:
            bool_val = True
            print("ERROR: INDIVIDUAL: US02: " + " Age " + str(row["AGE"]) + " ID: " + str(row['ID']) + " is less than 150")
    if not bool_val:
        print("US07: No Errors found")
    
    