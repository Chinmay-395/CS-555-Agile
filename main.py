from pandas import DataFrame
from Initialparser import parse
from US03.US03_birth_before_death import birthBeforeDeath
from US29.US29_list_deceased import listDeceased
from US31.US31_list_living_single import listLivingSinglesOver30
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths
from US04.UseCase_04 import test_marriage_after_divorce
from US37.US37_list_recent_Survivors import list_recent_survivors
from US27.US27_include_age import include_individual_ages
from US05.UseCase_05 import test_marriage_before_death
from US08.US08_birth_before_marr import birth_before_marriage_of_parents
from US06.US_06 import test_divorce_before_death
from US13.US_13 import check_sibling_birth_dates
# US40 won't be included its a generic function for printing errors

def main(file_name):
    list_indi, list_fam = parse(file_name)
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))

    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    print("DF indi\n ", df_indi, "\n")
    df_indi.to_csv("individual_tb.csv", encoding='utf-8', index=False)
    print("DF fam \n ", df_fam, "\n")
    df_fam.to_csv("family_tb.csv", encoding='utf-8', index=False)
    # run sa3.ged
    listOrphans(df_indi, df_fam)

    # # run Sachin_Devangan_CS_555_WS4.ged
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)

    print("US29: List of Deceased People:", listDeceased(df_indi)) #
    # # US04	Marriage before divorce
    test_marriage_after_divorce(df_fam,df_indi)
    # # US37	List recent survivors
    list_recent_survivors(df_indi, df_fam)

    # include_individual_ages(df_indi, df_fam) # this is from sprint-2 
    print("US03: Birth before death \n", birthBeforeDeath(df_indi))
    
    birth_before_marriage_of_parents(df_indi,df_fam) # US08

    print("US06: DIVORCE BEFORE DEATH",test_divorce_before_death(df_fam,df_indi))

    print("US13: Siblings spacing", check_sibling_birth_dates(df_indi,df_fam))

    include_individual_ages(df_indi,df_fam)





main("sa4.ged")
# print("--------------------------------------------- \n")
# main("sa2.ged")
# print("--------------------------------------------- \n")
# main("sa3.ged")
# print("--------------------------------------------- \n")
# main("test_ged_file.ged")