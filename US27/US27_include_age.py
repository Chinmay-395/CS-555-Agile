import math
def include_individual_ages(indi_df,fam_df):
    print("US27: Include age of individuals:")
    list_of_errors=[]
    for _,row in indi_df.iterrows():
        if math.isnan(row['AGE']) or row['AGE'] < 0:
            s ="ERROR: INDIVIDUAL: US27: name " + row['NAME'] +" age " + row['AGE'] + " INDIVIDUAL ID " + row['ID']
            list_of_errors.append(s)

    if len(list_of_errors) == 0:
        print("ages of the individuals are already included")
    elif len(list_of_errors) > 0:
        for x in list_of_errors:
            print(x)
