from pandas import read_csv,DataFrame
from Initialparser import parse
from US33.US33_list_orphans import listOrphans
from US31.US31_list_living_single import listLivingSinglesOver30
from US35.US35_list_recent_births import listRecentBirths
from US29.US29_list_deceased import listDeceased
from US_04.UseCase_04 import test_marriage_after_divorce
from US37.US37_list_recent_Survivors import list_recent_survivors
from US27.US27_include_age import include_individual_ages
def main(file_name):
    list_indi, list_fam = parse(file_name)
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    
    
    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    print("DF indi\n ", df_indi, "\n")
    print("DF fam \n ", df_fam, "\n")
    # run sa3.ged
    listOrphans(df_indi,df_fam)

    # run Sachin_Devangan_CS_555_WS4.ged
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)

    print("List of Deceased People:", listDeceased(df_indi))
    
    test_marriage_after_divorce(df_fam,df_indi)
    list_recent_survivors(df_indi, df_fam)

    include_individual_ages(df_indi, df_fam)


main("Sachin_Devangan_CS_555_WS4.ged")
# print("--------------------------------------------- \n")
# main("sa2.ged")
# print("--------------------------------------------- \n")
# main("sa3.ged")
# print("--------------------------------------------- \n")
# main("test_ged_file.ged")