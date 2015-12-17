# -*- coding: utf-8 -*-

#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

mylist=[]
score_diff=[]

def read_data(data):
  with open(data,'r') as f: #open file in read only mode
    csvreader=csv.reader(f)
    for row in csvreader:
      mylist.append(row)

#function to return index of team with min diff
def get_min_score_difference(parsed_data):
  
  # Obtains indices
  team_index=parsed_data[0].index('Team')
  goals_index=parsed_data[0].index('Goals')
  goalsallowed_index=parsed_data[0].index('Goals Allowed')

  # Separate lists
  team= [x[team_index] for x in parsed_data[1:]]
  goals = [x[goals_index] for x in parsed_data[1:]]
  goalsallowed = [x[goalsallowed_index] for x in parsed_data[1:]]

  # determine minimum number of for-against goals
  for i,x in enumerate(goals):
    score_diff.append((team[i],int(goals[i])-int(goalsallowed[i])))
  min_value=min(score_diff, key=lambda x :x[1])
  
  # return index of minimum number of for-against goals
  return score_diff.index(min_value)+1

#function to obtain name of team for specific index
def get_team(index_value, parsed_data):
  return parsed_data[index_value][0]


read_data('football.csv')
min_index=get_min_score_difference(mylist)
print get_team(min_index,mylist)

 
