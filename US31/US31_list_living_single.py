def listLivingSingles(individuals):
    living_singles = []
    for index, row in individuals.iterrows():
        if row['AGE'] >= 18 and row['ALIVE'] == True and len(row['SPOUSE']) == 0 :
            living_singles.append((row['ID'], row['AGE'], row['NAME']))
    if len(living_singles) > 0:
        print('US31: List of Living Singles:')
        print(living_singles)
