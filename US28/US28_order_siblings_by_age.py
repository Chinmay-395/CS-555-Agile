import pandas as pd

def order_siblings_by_age(individuals, families):
    ordered_siblings = []
    
    # Iterate through families and order siblings by age
    for _, family_row in families.iterrows():
        family_id = family_row['ID']
        children_ids = family_row['CHILDREN']
        if children_ids:
            children_data = individuals[individuals['ID'].isin(children_ids)]
            # Sort children by age in descending order
            sorted_children = children_data.sort_values(by='BIRTHDAY', ascending=False)
            siblings_list = sorted_children['NAME'].tolist()
            ordered_siblings.append({'family_id': family_id, 'siblings': siblings_list})
    
    # Print US28 message just once outside the array
    print("US28: Order of siblings by decreasing age")
    return ordered_siblings
