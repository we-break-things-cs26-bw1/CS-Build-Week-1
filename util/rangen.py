import json
import random
import csv
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

    #
    # with open(, 'r') as f:
    #     distros_dict = json.load(f)
    #
    # for distro in distros_dict:
    #     print(distro)\
Monster_Dict={}


with open('monsters.csv')as f:
    reader = csv.reader(f, delimiter=';', quotechar='\'')
    for row in reader:
        # print(f"zero-{row[0]}")
        # print(f"seventeen-{row[17]}")
        Monster_Dict[row[0]] = row[17]
        # for item in range(len(row)):
        #     print(f"item {row[item]} and {item}")
        # print(f"-2{sauce}")
        # print(row)
print(Monster_Dict)
#
# randomlist = []
# for i in range(0,5):
#     n = random.randint(1,30)
# randomlist.append(n)
# print(randomlist)



# def background_randomizer(room):
#     randomlist = [1,5,2,34,4,1,34]
#     print(randomlist)
#     n = random.shuffle(randomlist)
#     randomlist.append(n)
#     print(randomlist)
#     print(randomlist.pop())
#     print(randomlist)
#
#
# background_randomizer(3)



