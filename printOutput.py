import pandas as pd
from prettytable import PrettyTable

def printingAllTheStuff(US_name,indi_df, fam_df, errors, anomalies):
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