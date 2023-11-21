import math
    
def parents_not_too_old(individuals,families):
    for index, row in families.iterrows():
        if isinstance(row['CHILDREN'],list) and len(row['CHILDREN'])>0:
            mother_age=individuals.loc[individuals['ID']==row['WIFE ID'],'AGE'].iloc[0]
            father_age=individuals.loc[individuals['ID']==row['HUSBAND ID'],'AGE'].iloc[0]
            for child in row['CHILDREN']:
                child_age=individuals.loc[individuals['ID']==child,'AGE'].iloc[0]
                if (mother_age-child_age)>=60 or (father_age-child_age)>=80:                     
                        print("ERROR: FAMILY: US12: " + " FAMILY ID: " + row['ID'] + ": " + row['ID'] + " Age of child: " + str(child_age) + " Age of mother: " + str(mother_age)+ " Age of Father: "+ str(father_age))     
    