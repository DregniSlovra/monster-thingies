from random import randrange
from math import floor
from monster import Monster, monster_from_json
import os

from team import Team

def monster_select():
  lst = os.listdir('Assets/Monsters/')
  i = 0
  for monster in lst:
    i += 1
    print("{}: {}".format(i, monster.split('.')[0]))
  t1 = Team("player")
  t2 = Team("bot")
  for _ in range(0, 5):
    while True:
      try:
        choice = int(input("Choose a monster: "))
        if choice in range(1, i+1):
          t1.add(monster_from_json("Assets/Monsters/{}".format(lst[choice-1])))
          print("You chose : ", t1.monsters[choice - 1].name)
          break
        else:
          print("Invalid choice")
      except ValueError:
        print("Invalid choice")
    t2.add(monster_from_json("Assets/Monsters/{}".format(lst[randrange(0, i)])))
  return t1, t2

def choose_target(defending_team):
  for i in range(0, len(defending_team.monsters)):
    print(str(i+1) + " : " + defending_team.monsters[i].name)
  while True:
    try:
      choice = int(input("Choose a target: "))
      if choice in range(1, len(defending_team.monsters)+1):
        return defending_team.monsters[choice-1]
      else:
        print("Invalid choice")
    except ValueError:
      print("Invalid choice")

def fight(t1 : Team, t2 : Team):
  turn = 1
  while t1.is_standing() and t2.is_standing():
    t1.energy_refill()
    t2.energy_refill()
    if t1.next().energy >= t2.next().energy:
      attacker : Monster = t1.next()
      turn = 1
    else:
      attacker : Monster = t2.next()
      turn = 2
    print(attacker.name + " is attacking")

    if (turn == 1):
      defender : Monster = choose_target(t2)
    else:
      defender : Monster = t1.monsters[randrange(0, len(t1.monsters))]
    defender.defend(attacker.use(defender, int(floor(randrange(0, 3)))))

    if not defender.is_alive():
      if (turn == 2):
        t1.remove(defender)
      else:
        t2.remove(defender)
    if not t1.is_standing() or not t2.is_standing():
      print("Turn end !\n")
      continue
    print("Turn end !\n")
  if t1.is_standing():
    print("{} won !".format(t1.name))
  elif t2.is_standing():
    print("{} won !".format(t2.name))
  else:
    print("ohno they both died :I")

if __name__ == "__main__":
  t1, t2 = monster_select()
  fight(t1, t2)