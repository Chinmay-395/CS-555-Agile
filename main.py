from pandas import DataFrame
from Initialparser import parse

from US03.US03_birth_before_death import birthBeforeDeath
from US04.UseCase_04 import test_marriage_after_divorce
from US05.UseCase_05 import test_marriage_before_death
from US06.US_06 import test_divorce_before_death
from US08.US08_birth_before_marr import birth_before_marriage_of_parents
from US13.US_13 import check_sibling_birth_dates
from US27.US27_include_age import include_individual_ages
from US29.US29_list_deceased import listDeceased
from US31.US31_list_living_single import listLivingSinglesOver30
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths

from US37.US37_list_recent_Survivors import list_recent_survivors
from US38.US38_list_upcoming_birthdays import listUpcomingBirthdays
from US39.US39_list_upcoming_anniversaries import listUpcomingAnniversaries
<<<<<<< HEAD
from US36.US36_list_recent_deaths import listRecentDeaths
from US42.US42_reject_illegitimate_dates import rejectIllegitimateDates

=======
# US40 won't be included its a generic function for printing errors in dates of birth in individuals
# US41 won't be included its a generic function for to check valid dates
>>>>>>> main

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
<<<<<<< HEAD
    print("US38: List of Upcoming Birthdays", listUpcomingBirthdays(df_indi))
    # Examples:
    # print(parse_partial_date("1990"))        # Output: 1990-01-01
    # print(parse_partial_date("MAR 1990"))    # Output: 1990-03-01
    # print(parse_partial_date("15 MAR 1990"))  # Output: 1990-03-15
    # print(parse_partial_date("JAN 15"))      # Output: None (Invalid, unable to parse)
    listValidMarriages(df_fam, df_indi)
    validateBirthBeforeMarriage(df_indi, df_fam)
    check_unique_ids(df_indi, df_fam)
    result = order_siblings_by_age(df_indi, df_fam)
    print(result)

    print("US29: List of Deceased People:", listDeceased(df_indi))
    # US04	Marriage before divorce
    # test_marriage_after_divorce(df_fam, df_indi)
    # US37	List recent survivors
=======

>>>>>>> main
    list_recent_survivors(df_indi, df_fam)

    # include_individual_ages(df_indi, df_fam) # this is from sprint-2 
    print("US03: Birth before death")
    print("", birthBeforeDeath(df_indi))
    
    birth_before_marriage_of_parents(df_indi,df_fam) # US08

    print("US06: DIVORCE BEFORE DEATH")
    print("",test_divorce_before_death(df_fam,df_indi))

    print("US13: Siblings spacing")
    print("",check_sibling_birth_dates(df_indi,df_fam))
    print("US27: Include age of individuals:")
    include_individual_ages(df_indi,df_fam)
    print("US05: MARRIED BEFORE DEATH")
    print("",test_marriage_before_death(df_indi,df_fam))
    print("US39: List of Upcoming anverseries")
    print("",listUpcomingAnniversaries(df_indi,df_fam))
    # 

    listRecentDeaths(df_indi)

    print(rejectIllegitimateDates(df_indi, df_fam))



main("sa4.ged")
# print("--------------------------------------------- \n")
# main("sa2.ged")
# print("--------------------------------------------- \n")
# main("sa3.ged")
# print("--------------------------------------------- \n")
# main("test_ged_file.ged")
