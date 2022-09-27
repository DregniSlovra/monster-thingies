from random import randrange
from math import floor
from monster import monster_from_json
import os

def monster_select():
  lst = os.listdir('Monsters/')
  i = 0
  for monster in lst:
    i += 1
    print("{}: {}".format(i, monster.split('.')[0]))
  while True:
    try:
      choice = int(input("Choose a monster: "))
      if choice in range(1, i+1):
        m1 = monster_from_json("Monsters/{}".format(lst[choice-1]))
        break
      else:
        print("Invalid choice")
    except ValueError:
      print("Invalid choice")
  m2 = monster_from_json("Monsters/{}".format(lst[randrange(0, i)]))
  return m1, m2

def fight(m1, m2):
  while m1.is_alive() and m2.is_alive():
    if m1.speed > m2.speed:
      m2.defend(m1.use(m2, int(floor(randrange(0, 3)))))
      if not m2.is_alive():
        print("Turn end !\n")
        continue
      m1.defend(m2.use(m1, int(floor(randrange(0, 3)))))
    else:
      m1.defend(m2.use(m1, int(floor(randrange(0, 3)))))
      if not m1.is_alive():
        print("Turn end !\n")
        continue
      m2.defend(m1.use(m2, int(floor(randrange(0, 3)))))
    print("Turn end !\n")
  if m1.is_alive():
    print("{} won !".format(m1.name))
  elif m2.is_alive():
    print("{} won !".format(m2.name))
  else:
    print("ohno they both died :I")

if __name__ == "__main__":
  m1, m2 = monster_select()
  fight(m1, m2)