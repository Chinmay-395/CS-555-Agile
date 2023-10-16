import math
def include_individual_ages(indi_df,fam_df):
    for index,row in indi_df.iterrows():
        if math.isnan(row['AGE']) or row['AGE'] < 0:
            print("ERROR: INDIVIDUAL: US27: name " + row['NAME'] +" age " + row['AGE'] + " INDIVIDUAL ID " + row['ID'])