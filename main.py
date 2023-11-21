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
from US23.US23_list_unique_name_and_birthday import listUniqueNameAndBirthdays
from US27.US27_include_age import include_individual_ages
from US28.US28_order_siblings_by_age import order_siblings_by_age
from US29.US29_list_deceased import listDeceased
from US30.US30_list_living_married import list_living_married
from US31.US31_list_living_single import listLivingSinglesOver30
from US32.US32_List_multiple_births import listMultipleBirths
from US33.US33_list_orphans import listOrphans
from US35.US35_list_recent_births import listRecentBirths
from US36.US36_list_recent_deaths import listRecentDeaths
from US37.US37_list_recent_Survivors import list_recent_survivors
from US38.US38_list_upcoming_birthdays import listUpcomingBirthdays
from US39.US39_list_upcoming_anniversaries import listUpcomingAnniversaries
from US40.US40_include_ip_lines import get_line
from US41.US41_include_partial_dates import parse_partial_date
from US42.US42_reject_illegitimate_dates import rejectIllegitimateDates


def main(file_name):
    list_indi, list_fam = parse(file_name)
    # print("THE TOTAL NUMBER OF PEOPLE IN THE LIST", len(list_indi))

    df_indi = DataFrame(list_indi)
    df_fam = DataFrame(list_fam)
    print("The Individuals Table\n ", df_indi, "\n")
    df_indi.to_csv("individual_tb.csv", encoding="utf-8", index=False)
    print("The Family Table \n ", df_fam, "\n")
    df_fam.to_csv("family_tb.csv", encoding="utf-8", index=False)

    dates_before_current_date(df_indi, df_fam)  # US01
    validateBirthBeforeMarriage(df_indi, df_fam)  # US02

    print("US03: Birth before death")  # US03
    print("", birthBeforeDeath(df_indi))
    print("US04: Marriage after divorce")  # US04
    test_marriage_after_divorce(df_fam, df_indi)
    print("US05: MARRIED BEFORE DEATH")  # US05
    print("", test_marriage_before_death(df_indi, df_fam))

    print("US06: DIVORCE BEFORE DEATH")  # US06
    print("", test_divorce_before_death(df_fam, df_indi))

    less_than_150_years(df_indi)  # US07

    birth_before_marriage_of_parents(df_indi, df_fam)  # US08

    listValidMarriages(df_fam, df_indi)  # US10

    print("US12: parents not too old of the children")  # US12
    parents_not_too_old(df_indi, df_fam)

    print("US13: Siblings spacing")  # US13
    print("", check_sibling_birth_dates(df_indi, df_fam))

    check_unique_ids(df_indi, df_fam)  # US22

    print("US27: Include age of individuals:")  # US27
    include_individual_ages(df_indi, df_fam)

    result = order_siblings_by_age(df_indi, df_fam)  # US28
    print(result)

    print("US29: List of Deceased People:", listDeceased(df_indi))  # US29
    print("US30: List of living married people in the family")  # US30
    list_living_married(df_indi, df_fam)
    listLivingSinglesOver30(df_indi)  # US31
    print("US32: List of multiple births")
    listMultipleBirths(df_indi)  # US32
    listOrphans(df_indi, df_fam)  # US33
    listRecentBirths(df_indi)  # US35
    listRecentDeaths(df_indi)  # US36
    list_recent_survivors(df_indi, df_fam)  # US37
    print("US38: List of Upcoming Birthdays", listUpcomingBirthdays(df_indi))  # US38
    print("US39: List of Upcoming anverseries")  # US39
    print("", listUpcomingAnniversaries(df_indi, df_fam))  # US40
    print("US40: Line number where error is in GED file", get_line(2))

    print("US41: Parsing Partial Dates")  # US41
    print(parse_partial_date("1990"))  # Output: 1990-01-01
    print(parse_partial_date("MAR 1990"))  # Output: 1990-03-01
    print(parse_partial_date("15 MAR 1990"))  # Output: 1990-03-15
    print(parse_partial_date("JAN 15"))  # Output: None (Invalid, unable to parse)

    print("US42: Reject Illegitimate Dates")  # US42
    print(rejectIllegitimateDates(df_indi, df_fam))

    print(listUniqueNameAndBirthdays(df_indi))


main("test_ged_file.ged")
