# import pandas as pd

# def check_unique_ids(individuals, families):
#     duplicate_individual_ids = individuals[individuals.duplicated(subset=['ID'], keep=False)]
#     duplicate_family_ids = families[families.duplicated(subset=['ID'], keep=False)]

#     errors = []

#     if not duplicate_individual_ids.empty:
#         errors.append(f"US22: Error: Duplicate individual IDs found: {duplicate_individual_ids['ID'].tolist()}")

#     if not duplicate_family_ids.empty:
#         errors.append(f"US22: Error: Duplicate family IDs found: {duplicate_family_ids['ID'].tolist()}")

#     if not errors:
#         return "US22: All individual and family IDs are unique."
#     else:
#         return "\n".join(errors)


def check_unique_ids(individuals, families):
    errors = []

    # Check for duplicate individual IDs
    duplicate_individual_ids = individuals[individuals.duplicated(subset=['ID'], keep=False)]
    if not duplicate_individual_ids.empty:
        unique_duplicate_ids = duplicate_individual_ids['ID'].unique()
        errors.append(f"US22: Error: Duplicate individual IDs found: {list(unique_duplicate_ids)}")

    # Check for duplicate family IDs
    duplicate_family_ids = families[families.duplicated(subset=['ID'], keep=False)]
    if not duplicate_family_ids.empty:
        unique_duplicate_ids = duplicate_family_ids['ID'].unique()
        errors.append(f"US22: Error: Duplicate family IDs found: {list(unique_duplicate_ids)}")

    if not errors:
        errors.append("US22: No duplicate IDs found.")
    
    return errors

