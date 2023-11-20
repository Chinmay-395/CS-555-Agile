# User Story 32

def listMultipleBirths(individuals):
    coveredBirthdays = []
    for index, row in individuals.iterrows():
        if row['BIRTHDAY'] not in coveredBirthdays:
            sameBirthdays = individuals[individuals['BIRTHDAY'] == row['BIRTHDAY']]
            coveredBirthdays.append(row['BIRTHDAY'])
            if len(sameBirthdays.index) > 1:
                print('US32: Has BIRTHDAY on ' + row['BIRTHDAY'] + ':')
                print(list(zip(sameBirthdays['ID'],sameBirthdays['AGE'])))