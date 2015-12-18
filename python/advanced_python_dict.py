
# PLACE YOUR CODE HERE
import csv
import advanced_python_regex as apr

Dict={}
BetterDict={}

def create_dictionary(ParseCSV_Obj):
  # Obtain indices
  degree_index=ParseCSV_Obj.parsed_data[0].index('degree')
  title_index=ParseCSV_Obj.parsed_data[0].index('title')
  name_index=ParseCSV_Obj.parsed_data[0].index('name')
  email_index=ParseCSV_Obj.parsed_data[0].index('email')

  # Create dictionary
  for i in ParseCSV_Obj.parsed_data[1:]:
    if(i[name_index].split()[-1] not in Dict.keys()):
      Dict[i[name_index].split()[-1]]=[]
    # Create dictionary value
    j=[i[degree_index],i[title_index][0:i[title_index].find('Professor')+len('Professor')],i[email_index]]
    # Store value into dictionary
    Dict[i[name_index].split()[-1]].append(j)

def create_better_dictionary(ParseCSV_Obj):
  # Obtain indices
  degree_index=ParseCSV_Obj.parsed_data[0].index('degree')
  title_index=ParseCSV_Obj.parsed_data[0].index('title')
  name_index=ParseCSV_Obj.parsed_data[0].index('name')
  email_index=ParseCSV_Obj.parsed_data[0].index('email')

  for i in ParseCSV_Obj.parsed_data[1:]:
    # Create dictionary key
    key=(' '.join(i[name_index].split()[0:-1]),i[name_index].split()[-1])
    # Create dictionary value
    j=[i[degree_index],i[title_index][0:i[title_index].find('Professor')+len('Professor')],i[email_index]]
    # Store dictionary key and value pair
    BetterDict[key]=j

a=apr.parsedata()
create_dictionary(a)
print Dict.items()[0:3]

create_better_dictionary(a)
for j in sorted(BetterDict.keys()):
  print j, BetterDict[j]
for j in sorted(BetterDict,key=lambda x: x[1]):
  print j, BetterDict[j]
