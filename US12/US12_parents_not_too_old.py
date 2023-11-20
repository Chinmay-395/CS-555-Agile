import math
    
def parents_not_too_old(individuals,families):
    for index, row in families.iterrows():
        if not math.isnan(row.children):
            mother_age=individuals.loc[individuals['ID']==row['WIFE ID'],'age'].iloc[0]
            father_age=individuals.loc[individuals['ID']==row['HUSBAND ID'],'age'].iloc[0]
            for child in row.children:
                child_age=individuals.loc[individuals['id']==child,'age'].iloc[0]
                if (mother_age-child_age)>=60 or (father_age-child_age)>=80:                     
                        print("ERROR: FAMILY: US12: " + " FAMILY ID: " + row['ID'] + ": " + row['id'] + " Age of child: " + str(child_age) + " Age of mother: " + str(mother_age)+ " Age of Father: "+ str(father_age))     
    