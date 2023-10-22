from pandas import DataFrame, read_csv

import pandas as pd
from Initialparser import parse
from US03.US03_birth_before_death import birthBeforeDeath
from US29.US29_list_deceased import listDeceased
from US31.US31_list_living_single import listLivingSinglesOver30
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths
from US04.UseCase_04 import test_marriage_after_divorce

from US38.US38_list_upcoming_birthdays import listUpcomingBirthdays
from US41.US41_include_partial_dates import parse_partial_date
from US10.US10_Marriage_after_14 import listValidMarriages

from US37.US37_list_recent_Survivors import list_recent_survivors
# from US27.US27_include_age import include_individual_ages
from US05.UseCase_05 import test_marriage_before_death
from US39.US39_list_upcoming_anniversaries import listUpcomingAnniversaries


def main(file_name):
    list_indi, list_fam = parse(file_name)
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))

    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    print("DF indi\n ", df_indi, "\n")
    print("DF fam \n ", df_fam, "\n")
    # run sa3.ged
    listOrphans(df_indi, df_fam)

    # run Sachin_Devangan_CS_555_WS4.ged
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)
    print("US38: List of Upcoming Birthdays",listUpcomingBirthdays(df_indi) )
    # Examples:
    # print(parse_partial_date("1990"))        # Output: 1990-01-01
    # print(parse_partial_date("MAR 1990"))    # Output: 1990-03-01
    # print(parse_partial_date("15 MAR 1990"))  # Output: 1990-03-15
    # print(parse_partial_date("JAN 15"))      # Output: None (Invalid, unable to parse)
    listValidMarriages(df_fam,df_indi)


    print("US29: List of Deceased People:", listDeceased(df_indi))
    # US04	Marriage before divorce
    # test_marriage_after_divorce(df_fam, df_indi)
    # US37	List recent survivors
    list_recent_survivors(df_indi, df_fam)

    # include_individual_ages(df_indi, df_fam)  # this is from sprint-2
    print("US03: Birth before death \n", birthBeforeDeath(df_indi))
    test_marriage_before_death(df_fam, df_indi)

    # list upcoming anniversaries
    print("US39: List Upcoming Anniverseries: ",
          listUpcomingAnniversaries(df_indi, df_fam))


main("Sachin_Devangan_CS_555_WS4.ged")
# print("--------------------------------------------- \n")
# main("sa2.ged")
# print("--------------------------------------------- \n")
# main("sa3.ged")
# print("--------------------------------------------- \n")
# main("test_ged_file.ged")
