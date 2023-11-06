def less_than_150_years(individuals):
    for index, row in individuals.iterrows():
        if row["AGE"] < 150:
            print("ERROR: INDIVIDUAL: US02: " + " Age " + str(row["AGE"]) + " ID: " + str(row['ID']) + " is less than 150")

    