# from datetime import datetime
# import math

# def clean_date(date_string):
#     # Check if the input is NaN, and return None if it is
#     if isinstance(date_string, float) and math.isnan(date_string):
#         return None
    
#     # Convert to string if the input is a float
#     if isinstance(date_string, float):
#         date_string = str(int(date_string))
    
#     # Handle list of dates
#     if isinstance(date_string, list):
#         cleaned_dates = []
#         for date in date_string:
#             cleaned_date = date.strip()
#             try:
#                 cleaned_dates.append(datetime.strptime(cleaned_date, '%d %b %Y'))
#             except ValueError:
#                 # Handle any other date formats as needed
#                 pass
#         return cleaned_dates if cleaned_dates else None
    
#     # Handle single date
#     cleaned_date = date_string.strip()
#     try:
#         return datetime.strptime(cleaned_date, '%d %b %Y')
#     except ValueError:
#         # Handle any other date formats as needed
#         return None

# def validateBirthBeforeMarriage(individuals):
#     errors = []
    
#     for _, row in individuals.iterrows():
#         if row['BIRTHDAY'] != '':
#             birthdate = clean_date(row['BIRTHDAY'])
#             spouse_dates = clean_date(row['SPOUSE'])
            
#             if birthdate and spouse_dates:
#                 # Handle list of dates
#                 if isinstance(spouse_dates, list):
#                     for spouse_date in spouse_dates:
#                         if birthdate > spouse_date:
#                             errors.append(f"Error: Individual {row['ID']} ({row['NAME']}) has birthdate {row['BIRTHDAY']} after marriage date {spouse_date.strftime('%b %d %Y')}.")
#                 else:
#                     # Handle single date
#                     if birthdate > spouse_dates:
#                         errors.append(f"Error: Individual {row['ID']} ({row['NAME']}) has birthdate {row['BIRTHDAY']} after marriage date {spouse_dates.strftime('%b %d %Y')}.")
    
#     if errors:
#         print("US02: Birth before marriage errors:")
#         for error in errors:
#             print(error)
#     else:
#         print("US02: No birth before marriage  errors found.")



from datetime import datetime

def clean_date(date_string, family_table):
    if isinstance(date_string, list):
        cleaned_dates = []
        for date in date_string:
            family_id = date.strip("['@']")
            marriage_date = family_table.loc[family_table['ID'] == f'@{family_id}@', 'MARRIED'].values
            if len(marriage_date) > 0:
                cleaned_dates.append(datetime.strptime(marriage_date[0], '%Y %b %d'))
        return cleaned_dates if cleaned_dates else None
    return None

def validateBirthBeforeMarriage(individuals, families):
    errors = []
    for _, row in individuals.iterrows():
        if row['BIRTHDAY'] != '':
            birthdate = clean_date(row['BIRTHDAY'], families)
            spouse_dates = clean_date(row['SPOUSE'], families)

            if birthdate and spouse_dates:
                if isinstance(spouse_dates, list):
                    for spouse_date in spouse_dates:
                        if birthdate > spouse_date:
                            errors.append(f"Error: Individual {row['ID']} ({row['NAME']}) has birthdate {row['BIRTHDAY']} after marriage date {spouse_date.strftime('%b %d %Y')}.")
                else:
                    if birthdate > spouse_dates:
                        errors.append(f"Error: Individual {row['ID']} ({row['NAME']}) has birthdate {row['BIRTHDAY']} after marriage date {spouse_dates.strftime('%b %d %Y')}.")
    
    if errors:
        print("US02: Birth before marriage errors:")
        for error in errors:
            print(error)
    else:
        print("US02: No birth before marriage errors found.")

