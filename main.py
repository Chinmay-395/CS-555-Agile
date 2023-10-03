from pandas import read_csv,DataFrame
from Initialparser import parse
from US33.US33_list_orphans import listOrphans
from US31.US31_list_living_single import listLivingSinglesOver30
from US35.US35_list_recent_births import listRecentBirths
from US29.US29_list_deceased import listDeceased


def main(file_name):
    list_indi, list_fam = parse(file_name)
<<<<<<< HEAD
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    
    
    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    # print("DF \n ", df_indi, "\n")
    # print("DF \n ", df_fam, "\n")
    # run sa3.ged
    listOrphans(df_indi,df_fam)

    # run Sachin_Devangan_CS_555_WS4.ged
=======
    print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    print_Indi(list_indi)
    print_Fam(list_fam)
    df_indi = read_csv("individual_tb.csv")
    df_fam = read_csv("family_tb.csv")
    listOrphans(df_indi, df_fam)

>>>>>>> nouman
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)

    print("List of Deceased People:", listDeceased(df_indi))


main("Sachin_Devangan_CS_555_WS4.ged")
