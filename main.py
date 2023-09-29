from pandas import read_csv
from Initialparser import print_Indi, print_Fam, parse
from US33_list_orphans.US33_list_orphans import listOrphans


def main(file_name):
    list_indi, list_fam = parse(file_name)
    print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))
    print_Indi(list_indi)
    print_Fam(list_fam)
    df_indi = read_csv('individual_tb.csv')
    df_fam = read_csv('family_tb.csv')
    listOrphans(df_indi,df_fam)

main('sa3.ged')