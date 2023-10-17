import sys
# this is done to import the code from module InitialParser.py
sys.path.insert(0,"/home/chinmay/Coding/Courses/CS555_WS4_Agile/Group_4_Assignment/")
filename = "Sachin_Devangan_CS_555_WS4.ged"
def get_line(date_1):
    f=open(filename).read()
    f_in_list=f.split("\n")
    for i in range(len(f_in_list)):
        if f_in_list[i].find(str(date_1))!=-1:
            return i
        else:
            pass
