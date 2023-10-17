import pytest
import pandas as pd
import sys
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/")
from US27_include_age import include_individual_ages

def test_individual_ages1():
    details = [{
           'NAME': ' Sachin /Shard/',
           'ID': 'I3',
            
            'AGE': 28}]
    print(include_individual_ages(details))
    str1= str(include_individual_ages(details)) 
    strout="Name: Sachin  Shard --->Age:28"
    
    print("-->"+str1)
    assert strout == include_individual_ages(details)
    