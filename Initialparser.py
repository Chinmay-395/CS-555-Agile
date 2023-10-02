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
  indi_id_name_hmap = {}
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
          person['ID'] = line.split()[1].replace('@','')
        #   person['index'] = i
        if 'NAME' in line.split():
          person['NAME'] = line.split('NAME')[1].replace('\n','')
          indi_id_name_hmap[person['ID']] = person['NAME']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['BIRTHDAY'] =  lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['DEATH'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['CHILD'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'SPOUSE' in person.keys():
              person['SPOUSE'].append(line.split()[2].replace('@',''))
          else :
              person['SPOUSE'] = [line.split()[2].replace('@','')]
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['ID'] = line.split()[1].replace('@','')
        #   person['index'] = i
        if 'NAME' in line.split():
          person['NAME'] = line.split('NAME')[1].replace('\n','')
          indi_id_name_hmap[person['ID']] = person['NAME']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['BIRTHDAY'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['DEATH'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['CHILD'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          if 'SPOUSE' in person.keys():
              person['SPOUSE'].append(line.split()[2].replace('@',''))
          else :
              person['SPOUSE'] = [line.split()[2].replace('@','')]

    if is_dead:
       person['ALIVE'] = False
       person['AGE'] = relativedelta(datetime.strptime(person['DEATH']," %d %b %Y"),datetime.strptime(person['BIRTHDAY']," %d %b %Y")).years
    else:
      person['ALIVE'] = True
      today = datetime.today()
      person['AGE'] = relativedelta(today, datetime.strptime(person['BIRTHDAY']," %d %b %Y")).years


    individuals.append(person)

  f.close()
      
  return (individuals,indi_id_name_hmap)

def dataFrameOfFamilies(file_name, indi_id_name_hmap):
  families = []
  f = open(file_name, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices.append(i)
  
  for i in indices:
    family = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['ID'] = line.split()[1].replace('@','')
        #   family['index'] = i
        if 'MARR' in line.split():
          family['MARRIED'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['DIVORCE STATUS'] = False
        if 'DIV' in line.split():
          family['DIVORCE'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['DIVORCE STATUS'] = True
        if 'HUSB' in line.split():
          family['HUSBAND ID'] = line.split()[2].replace('@','')
          try:
            family['HUSBAND NAME'] = indi_id_name_hmap[family['HUSBAND ID']]
          except KeyError:
            family['HUSBAND NAME'] = 'NA'
        if 'WIFE' in line.split():
          family['WIFE ID'] = line.split()[2].replace('@','')
          try:
            family['WIFE NAME'] = indi_id_name_hmap[family['WIFE ID']]
          except KeyError:
            family['WIFE NAME'] = 'NA'
        if 'CHIL' in line.split():
          if 'CHILDREN' in family: 
            family['CHILDREN'].append(line.split()[2].replace('@',''))
          else:
            family['CHILDREN'] = []
            family['CHILDREN'].append(line.split()[2].replace('@',''))
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['ID'] = line.split()[1].replace('@','')
        #   family['index'] = i
        if 'MARR' in line.split():
          family['MARRIED'] = lines[j+1].split('DATE')[1].replace('\n','')
          family['DIVORCE STATUS'] = False # this means they are previously divorced
        if 'DIV' in line.split():
          family['DIVORCE STATUS'] = True
          family['DIVORCE'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['HUSBAND ID'] = line.split()[2].replace('@','')
          try:
            family['HUSBAND NAME'] = indi_id_name_hmap[family['HUSBAND ID']]
          except KeyError:
            family['HUSBAND NAME'] = 'NA'
        if 'WIFE' in line.split():
          family['WIFE ID'] = line.split()[2].replace('@','')
          try:
            family['WIFE NAME'] = indi_id_name_hmap[family['WIFE ID']]
          except KeyError:
            family['WIFE NAME'] = 'NA'
        if 'CHIL' in line.split():
          if 'CHILDREN' in family: 
            family['CHILDREN'].append(line.split()[2].replace('@',''))
          else:
            family['CHILDREN'] = []
            family['CHILDREN'].append(line.split()[2].replace('@',''))

    families.append(family)

  f.close()

  return families

"""This function parses the GEDCOM File and returns 2 lists: one for individuals and another for families"""
def parse(file_name):
    (individual_list_of_list, indi_id_name_hmap) = dataFrameOfIndividuals(file_name)
    family_list_of_list = dataFrameOfFamilies(file_name, indi_id_name_hmap)
    return (individual_list_of_list, family_list_of_list)