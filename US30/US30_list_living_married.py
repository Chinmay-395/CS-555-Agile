def list_living_married(indi_df, fam_df):
    living_people = [(row['ID'], row['AGE']) for index,row in indi_df.iterrows() if row['ALIVE']]
    married_people = []
    for index, row in indi_df.iterrows():
        if type(row['SPOUSE']) is list:
            for family in row['SPOUSE']:
                family_row = fam_df.loc[fam_df['ID'] == family]
                print("HHH\n",family_row)
                family_divorced = family_row.at[family_row.index[0], 'DIVORCE STATUS']
                print("HHHHHH \n",family_divorced)
                if not family_divorced:
                    married_people.append((row['ID'], row['AGE']))
                    break
    living_married = [x for x in living_people if x in married_people]

    print("US30: The list of living people that are married: " + str(living_married))