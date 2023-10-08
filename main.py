from pandas import DataFrame, read_csv

import pandas as pd
from Initialparser import parse
from US03.US03_birth_before_death import birthBeforeDeath
from US29.US29_list_deceased import listDeceased
from US31.US31_list_living_single import listLivingSinglesOver30
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths
from US_04.UseCase_04 import test_marriage_after_divorce


def main(file_name):
    list_indi, list_fam = parse(file_name)
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))

    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    # print("DF \n ", df_indi, "\n")
    # print("DF \n ", df_fam, "\n")
    # run sa3.ged
    listOrphans(df_indi, df_fam)

    # run Sachin_Devangan_CS_555_WS4.ged
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)

    print("List of Deceased People:", listDeceased(df_indi))
    print("Death before birth:", birthBeforeDeath(df_indi))

    print("LIST OF ERRORS IN US_04 ",
          test_marriage_after_divorce(df_fam, df_indi))


main("Sachin_Devangan_CS_555_WS4.ged")
