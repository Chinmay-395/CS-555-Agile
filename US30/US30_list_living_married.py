def list_living_married(indi_df, fam_df):
    living_people = [(row['id'], row['age']) for index,row in indi_df.iterrows() if row['alive']]
    married_people = []
    for index, row in indi_df.iterrows():
        if type(row['spouse']) is list:
            for family in row['spouse']:
                family_row = fam_df.loc[fam_df['id'] == family]
                family_divorced = family_row.at[family_row.index[0], 'DIVORCE STATUS']
                if not family_divorced:
                    married_people.append((row['id'], row['age']))
                    break
    living_married = [x for x in living_people if x in married_people]

    print("US30: The list of living people that are married: " + str(living_married))