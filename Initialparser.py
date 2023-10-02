from datetime import datetime
from dateutil.relativedelta import relativedelta
# list of headers in individual tables
'''
Individual Table:
ID, NAME, Gender, Birthday, Age, Alive, Death, Child, Spouse

Families
ID, Married, Divorced, Husband ID, Husband Name, Wife ID, Wife Name, Children
'''

"""This function creates a new list for an individual"""
def dataFrameOfIndividuals(file_name):
  individuals = []
  individuals_id_and_name = {}
  f = open(file_name, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices.append(i)

  for i in indices:
    is_dead = False
    person = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        #   person['index'] = i
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] =  lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'spouse' in person.keys():
              person['spouse'].append(line.split()[2].replace('@',''))
          else :
              person['spouse'] = [line.split()[2].replace('@','')]
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        #   person['index'] = i
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'spouse' in person.keys():
              person['spouse'].append(line.split()[2].replace('@',''))
          else :
              person['spouse'] = [line.split()[2].replace('@','')]

    if is_dead:
       person['alive'] = False
       person['age'] = relativedelta(datetime.strptime(person['death']," %d %b %Y"),datetime.strptime(person['birthday']," %d %b %Y")).years
    else:
      person['alive'] = True
      today = datetime.today()
      person['age'] = relativedelta(today, datetime.strptime(person['birthday']," %d %b %Y")).years


    individuals.append(person)

  f.close()
      
  return (individuals,individuals_id_and_name)

"""This function parses the GEDCOM File and returns 2 lists: one for individuals and another for families"""
def parse(file_name):
    (individual_list_of_list, indi_name_id) = dataFrameOfIndividuals(file_name)
    return (individual_list_of_list, indi_name_id)