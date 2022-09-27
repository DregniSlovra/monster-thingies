from math import ceil, floor, sqrt

def grid(length):
  x = ceil(sqrt(length))
  y = round(sqrt(length))
  return x, y

def grid_test():
  for i in range(0, 101):
    x, y = grid(i)
    print("nb :", i, "values", x, y)

class Monster():
  def __init__(self, spd) -> None:
      self.speed = spd
      self.energy = 0
      self.turns = 0

def energy_test():
  monsters = []
  for i in range(10):
    monsters.append(Monster(5 + i * 3))
    print(str(i) + " : " + str(monsters[i].speed), end=", ")
  print("")
  for i in range(100):
    x = 0
    print("turn " + str(i), end=" : ")
    for monster in monsters:
      monster.energy += monster.speed + 100
      print(str(x) + " : " + str(monster.energy), end=", ")
      x += 1
    attacker = monsters[0]
    for monster in monsters:
      if attacker.energy < monster.energy:
        attacker = monster
    attacker.energy = 0
    attacker.turns += 1
    print("")
  x = 0
  for monster in monsters:
    print(str(x) + " : " + str(monster.turns))
    x += 1
energy_test()