# Here are some "bad smells" in the code, which are indicators of potential problems in the design of the code:

# Hardcoded Magic Numbers: The number 9 is hardcoded to represent the number of months after a divorce. This can be 
# confusing to readers. It's better to declare it as a constant with a meaningful name at the beginning of the function 
# or outside the function.

# Repeated Date Conversion: The function convert_gedcom_date_to_datetime is called multiple times for the 
# same values (like each_indi['BIRTHDAY'] and family['MARRIED']). This is inefficient. We can compute these once 
# and store the results to be used later.

# Lack of Error Handling: Accessing the first row with .iloc[0] without checking if the DataFrame 
# contains any rows can raise an exception. There's no try-catch block to handle potential errors.

# Inefficient DataFrame Filtering: The line family = fam_df[fam_df['ID'] == family_id].iloc[0] filters the 
# DataFrame inside the loop. This might not be efficient, especially with large DataFrames.

# Unused Variables and Lists: The variable list_ans is populated but never used after that. Similarly, 
# list_of_errors is defined but not populated or used. This suggests that the code might be incomplete 
# or these lists might be remnants of earlier versions.

# Unnecessary Comments: The comment # 9 months in days is misleading because relativedelta(months=+9) adds 9 months, not days.

# Ambiguous Variable Names: The name list_ans is not descriptive enough. It's not clear what "ans" refers to.

# Hardcoded Column Names: The columns of the DataFrame are hardcoded at the end (data.columns= ["ID", "NAME", ...]). 
#If the structure of the input DataFrame changes, this will lead to errors.

# Direct Printing Inside Function: Directly printing from within a function can be considered a code smell, 
#especially if it's for debugging purposes. Instead, it's often better to return values or throw exceptions 
#and let the caller handle the display.

# Lack of Modularity: The function does a lot of tasks: it checks for anomalies based on birth dates, 
#creates new DataFrames, and prints results. Breaking the function into smaller, more specific functions 
#can improve readability and maintainability.

# No Docstring: There is no docstring for the function, making it harder for others to understand its 
#purpose, input parameters, and return values.
    
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from io import StringIO

def convert_gedcom_date_to_datetime(gedcom_date):
    return datetime.strptime(gedcom_date.strip(), '%d %b %Y')

def birth_before_marriage_of_parents(indi_df, fam_df):
    
    list_ans = []
    list_of_anomalies = []
    list_of_errors = []
    
    for index, each_indi in indi_df.iterrows():
        family_id = each_indi['CHILD']
        if pd.isna(family_id):
            list_ans.append(each_indi)
        else:
            family = fam_df[fam_df['ID'] == family_id].iloc[0]
            if convert_gedcom_date_to_datetime(each_indi['BIRTHDAY']) < convert_gedcom_date_to_datetime(family['MARRIED']):
                list_of_anomalies.append((each_indi['ID'], each_indi['AGE'], each_indi['NAME']))
            elif family['DIVORCE STATUS'] == True and convert_gedcom_date_to_datetime(each_indi['BIRTHDAY']) > convert_gedcom_date_to_datetime(family['MARRIED']) + relativedelta(months=+9):  # 9 months in days
                list_of_anomalies.append((each_indi['ID'], each_indi['AGE'], each_indi['NAME']))
            else:
                list_ans.append(each_indi)

    if len(list_of_anomalies) > 0:
        # data = pd.DataFrame(list_of_anomalies)
        # data.columns= ["ID","NAME","GENDER","BIRTHDAY","CHILD","ALIVE","AGE","SPOUSE","DEATH"]
        print("US08: BIRTH BEFORE MARRIAGE OF PARENTS ")
        # print(data)
        print(list_of_anomalies)
    elif len(list_of_anomalies) == 0:
        print("US08: No births before marriage of parents")