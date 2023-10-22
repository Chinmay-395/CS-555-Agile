from datetime import datetime

def listValidMarriages(families, individuals, min_age=14):
    valid_marriages = []
    current_date = datetime.now()

    for _, family_row in families.iterrows():
        husband_id = family_row['HUSBAND ID']
        wife_id = family_row['WIFE ID']

        husband_birthdate = individuals.loc[individuals['ID'] == husband_id]['BIRTHDAY'].values[0]
        wife_birthdate = individuals.loc[individuals['ID'] == wife_id]['BIRTHDAY'].values[0]

        if husband_birthdate != '' and wife_birthdate != '':
            # Convert birthdates to datetime objects
            husband_birthdate = datetime.strptime(husband_birthdate, " %d %b %Y")
            wife_birthdate = datetime.strptime(wife_birthdate, " %d %b %Y")
            # Remove extra spaces from 'MARRIED' column and then convert to datetime format
            married_date = family_row['MARRIED'].strip()
            family_row['MARRIED'] = datetime.strptime(married_date, '%d %b %Y')

            age_at_marriage_husband = (family_row['MARRIED'] - husband_birthdate).days // 365
            age_at_marriage_wife = (family_row['MARRIED'] - wife_birthdate).days // 365

            if age_at_marriage_husband >= min_age and age_at_marriage_wife >= min_age:
                valid_marriages.append((family_row['HUSBAND ID'], family_row['WIFE ID'], family_row['MARRIED']))

    if len(valid_marriages) > 0:
        print(f' US10: Valid Marriages: Couples married after both spouses turned {min_age} years old:')
        print(valid_marriages)
    else:
        print(f'US10: No valid marriages found where both spouses were at least {min_age} years old at the time of marriage.')
