from django.test import TestCase

# Create your tests here.
import json
import random
""""
[
  {
    "pk": 1,
    "model": "adventure.Room",
    "fields":{
      "id":1,
      "title":"Room 1"
      "monster": "Default Monster",
      "item": "Default Item",
      "x": 0,
      "y": 100,
      "height": 100,
      "width": 100,
      "background": "Default Background",
      "n": 5,
      "s": 0,
      "e": 8,
      "w": 0
    }json_data = '{"pk": 1, "model": 2, "fields": 3, "d": 4, "e": 5}'
  }
]


"""

class Room_Mutated(object):
    id = None
    title= None
    description=None
    monster=""
    item=""
    x=0
    y=0
    height=0
    width=0
    background=0
    n=0
    s=0
    e=0
    w=0

import csv


"""
0=monster name
Name
ChallengeRating
ChallengeXP
ACType
AC
STR
STRMod
DEX
DEXMod
CON
CONMod
INT
INTMod
WIS
WISMod
CHA
CHAMod
HPDice
HP



"""

Monster_Dict={}
Background=[]
count=0
with open('monsters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        Monster_Dict[row[0]] = row[-2]
    # print(f'Processed {line_count} lines.')
    # print(Monster_Dict)

with open('../rooms.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    count += 1
    Background.append(distro["fields"]['background'])


print(set(Background))
    # for key in distro.keys():
    #     print(f"key = {key}")
    #
    #     print(distro[key])
    #     for each in distro.items():
    #         print(each)
    #
    #         pass


# randomlist = []
# for i in range(0,5):
