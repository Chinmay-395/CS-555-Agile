from dateutil import parser
from dateutil.relativedelta import relativedelta
import pandas as pd


def rejectIllegitimateDates(individuals, family):
    illegitimate_dates = []

    for index, row in individuals.iterrows():
        if not pd.isnull(row['BIRTHDAY']):
            try:
                parser.parse(row['BIRTHDAY'])
            except ValueError:
                illegitimate_dates.append(row['BIRTHDAY'])

        if not pd.isnull(row['DEATH']):
            try:
                parser.parse(row['DEATH'])
            except ValueError:
                illegitimate_dates.append(row['DEATH'])

    for index, row in family.iterrows():
        if not pd.isnull(row['MARRIED']):
            try:
                parser.parse(row['MARRIED'])
            except ValueError:
                illegitimate_dates.append(row['MARRIED'])

    if len(illegitimate_dates) == 0:
        return "US42: No illegitimate dates"
    else:
        return illegitimate_dates
