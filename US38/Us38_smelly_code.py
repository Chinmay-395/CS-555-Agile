# SMELLY CODE REASONS


#    1.  Meaningless Variable Names:
#         ind: Not descriptive. Consider using a more descriptive name like individuals_df.

#     2. Short and Non-Descriptive Variable Names:
#         i: Not descriptive. Use index for clarity.
#         r: Not descriptive. Use row for clarity.
#         bd: Not descriptive. Use birthdate for clarity.
#         res: Not descriptive. Use result for clarity.

#     3. Lack of Error Handling:
#         No error handling mechanisms are implemented, such as try-except blocks, to handle potential errors during execution, like invalid date formats.

#     4. Inefficient Date Comparison:
#         Dates are compared by subtracting them and checking the number of days. Consider using Python's timedelta for efficient date comparisons.

#     5. Lack of Comments:
#         While some comments exist, they don't provide sufficient explanation for complex logic. Add detailed comments to explain the purpose and reasoning behind the code.

#     6. Mixing Logic and Output:
#         The function performs data processing and directly returns output. Consider separating the logic that processes data from the logic that formats and presents the output. This separation of concerns improves code modularity.




# -------------------------------smelly code with no comments and made it harder to understand----------------------------------------------


import pandas as pd
from datetime import datetime as dt

def listUpcomingBirthdays(ind, d=30):
    if not isinstance(ind, pd.DataFrame):
        return "ERR: US38: Bad input."
    if len(ind) == 0:
        return "ANOMALY: US38: No data."

    res = []  
    now = dt.now() 

    for i, r in ind.iterrows():
        if r['BIRTHDAY'] != '':  
            # Parse the birthdate
            bd = dt.strptime(r['BIRTHDAY'], " %d %b %Y")
            
          
            next_bdy = bd.replace(year=now.year)
            if next_bdy < now:
                next_bdy = next_bdy.replace(year=now.year + 1)

            
            days_until_bdy = (next_bdy - now).days
            
            if 0 <= days_until_bdy <= d:
                
                res.append((r['ID'], r['BIRTHDAY'], r['NAME']))
                
    if len(res) > 0:
        return res
    else:
        return 'US38: No Upcoming Birthdays in GEDCOM file.'