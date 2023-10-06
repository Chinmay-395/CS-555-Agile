import pandas as pd
from prettytable import PrettyTable

def printingAllTheStuff(US_name,indi_df, fam_df, errors, anomalies):
    """The output of the every table will be in a single as well as the console for logging the issues

    Args:
        US_name (str): name of the user story
        indi_df (pandas dataframe): valid dataframe of the individuals 
        fam_df (pandas dataframe): valid dataframe of the families
        errors (List[str]): list of all the errors in a string format
        anomalies (List[str]): list of all the anomalies in a string format
    """
    with open("output.txt", "w") as file:
        ans = indi_df.to_string(index=False)
        ans1 = fam_df.to_string(index=False) 
        s = f"USER STORY: {US_name}"
        print(s)
        file.write(s)
        file.write(ans)
        print(ans)
        file.write(ans1)
        print(ans1)
        for i in errors:
            print(f"ERROR: {i}")
            file.write(f"ERROR: {i}")

        for i in anomalies:
            print(f"ANOMALY: {i}")
            file.write(f"ANOMALY: {i}")