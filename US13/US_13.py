from datetime import datetime, timedelta
import pandas as pd

def are_dates_valid(date1, date2):
    """Check if two dates are more than 8 months apart or less than 2 days apart"""
    difference = abs((date1 - date2).days)
    
    # 8 months is roughly approximated to 8*30 = 240 days for simplicity
    if difference > 2 and difference < 240:
        return False
    return True

def check_sibling_birth_dates(individuals, families):
    """Checks the birth dates of siblings to ensure they adhere to the specified conditions"""
    invalid_siblings = []
    seen = set()  # A set to keep track of combinations we've already added

    for index, family in families.iterrows():
        children = family['CHILDREN']

        if isinstance(children, list):
            siblings_dates = []

            # Extract birth dates of all children
            for child_id in children:
                for ind, individual in individuals.iterrows():
                    if individual['ID'] == child_id:
                        siblings_dates.append((child_id, datetime.strptime(individual['BIRTHDAY'], " %d %b %Y")))

            # Check every pair of sibling dates
            for i in range(len(siblings_dates)):
                for j in range(i + 1, len(siblings_dates)):
                    if not are_dates_valid(siblings_dates[i][1], siblings_dates[j][1]):
                        # Create a tuple of the family ID and the two child IDs
                        record = (family['ID'], siblings_dates[i][0], siblings_dates[j][0])
                        # Convert the tuple to a frozenset so it's hashable and can be added to the 'seen' set
                        record_set = frozenset(record)
                        # If we haven't seen this combination before, add it to the list and the set
                        if record_set not in seen:
                            seen.add(record_set)
                            invalid_siblings.append(record)
                        break  # Break out of the inner loop if an invalid pair is found

    return invalid_siblings
