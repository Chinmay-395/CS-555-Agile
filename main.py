from pandas import DataFrame
from Initialparser import parse
from US01.US01_dates_before_curr_date import dates_before_current_date
from US02.US02_birth_before_marriage import validateBirthBeforeMarriage
from US03.US03_birth_before_death import birthBeforeDeath
from US04.UseCase_04 import test_marriage_after_divorce
from US05.UseCase_05 import test_marriage_before_death
from US06.US_06 import test_divorce_before_death
from US07.US07_less_than_150 import less_than_150_years
from US08.US08_birth_before_marr import birth_before_marriage_of_parents
from US10.US10_Marriage_after_14 import listValidMarriages
from US12.US12_parents_not_too_old import parents_not_too_old
from US13.US_13 import check_sibling_birth_dates
# from US_16. #commented out because it is not completed
from US22.US22_unique_ids import check_unique_ids
from US27.US27_include_age import include_individual_ages
from US28.US28_order_siblings_by_age import order_siblings_by_age
from US29.US29_list_deceased import listDeceased
from US30.US30_list_living_married import list_living_married
from US31.US31_list_living_single import listLivingSinglesOver30
from US32.US32_List_multiple_births import *
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths
from US36.US36_list_recent_deaths import listRecentDeaths
from US37.US37_list_recent_Survivors import list_recent_survivors
from US38.US38_list_upcoming_birthdays import listUpcomingBirthdays
from US39.US39_list_upcoming_anniversaries import listUpcomingAnniversaries
from US40.US40_include_ip_lines import get_line
from US41.US41_include_partial_dates import parse_partial_date
from US42.US42_reject_illegitimate_dates import rejectIllegitimateDates

# US40 won't be included its a generic function for printing errors in dates of birth in individuals
# US41 won't be included its a generic function for to check valid dates

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
    listOrphans(df_indi, df_fam) # US33

    # # run Sachin_Devangan_CS_555_WS4.ged
    listLivingSinglesOver30(df_indi)
    listRecentBirths(df_indi)
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
    dates_before_current_date(df_indi,df_fam) # US01
    less_than_150_years(df_indi) # US07



main("sa4.ged")
