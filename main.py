from pandas import read_csv,DataFrame
from Initialparser import parse
from US33.US33_list_orphans import listOrphans
from US31.US31_list_living_single import listLivingSinglesOver30
from US35.US35_list_recent_births import listRecentBirths


def main(file_name):
    list_indi, list_fam = parse(file_name)
    print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    
    
    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    print("DF \n ", df_indi, "\n")
    print("DF \n ", df_fam, "\n")

    listOrphans(df_indi,df_fam)


    # listLivingSinglesOver30(df_indi)
    # listRecentBirths(df_indi)

main('sa3.ged')