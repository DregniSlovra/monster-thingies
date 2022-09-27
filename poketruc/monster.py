import json
from random import randrange
from math import floor

import pygame

type_array = [
  [ 1, .5, 1, 2, 1, 1, .5, 2, 1 ],
  [ 2, 1, .5, 2, 1, .5, 1, .5, 2 ],
  [ 1, 2, 1, .5, 2, 2, .5, 1, 1 ],
  [ .5, .5, 2, .5, 2, 2, .5, 2, .5 ],
  [ 1, 1, 2, .5, 2, 0, 1, .5, 2 ],
  [ 1, 2, .5, 2, 2, 1, 0, 1, .5 ],
  [ 1, .5, 1, 2, .5, .5, 2, 1, 1 ],
  [ .5, 1, 1, .5, 1, 1, 2, .5, 2 ],
  [ 2, .5, 1, 1, 0, 1, 2, 2, .5 ],
]

Types = {
  'normal': 0,
  'fire': 1,
  'water': 2,
  'plant': 3,
  'electric': 4,
  'ground': 5,
  'air': 6,
  'light': 7,
  'dark': 8,
}

class Move(object):
  def __init__(self, id, name, dmg, type, style):
    self.id = id
    self.name = name
    self.dmg = dmg
    self.type = type
    self.style = style

def monster_from_json(filename):
  with open(filename) as monster_file:
    data = json.load(monster_file)
    moves = []
    for move in data["moves"]:
      moves.append(Move(move["id"], move["name"], move["dmg"], move["type"], move["style"]))
    monster = Monster(
      data["name"],
      data["image"],
      data["hp"],
      data["atk"],
      data["def"],
      data["spe"],
      data["spd"],
      data["crR"],
      data["crF"],
      data["types"],
      moves,
    )
  return monster

class Monster(object):
  def __init__(self, name, image, hp, atk, dfe, spe, spd, crR, crF, types, moves):
    self.name = name
    if isinstance(image, str):
      self.image = pygame.image.load("Assets/Monsters/Images/" + image)
    else:
      self.image = image
    self.hp = hp
    self.attack = atk
    self.defense = dfe
    self.special = spe
    self.speed = spd
    self.critRate = crR
    self.critFactor = crF
    self.types = types
    self.moves = moves

  def use(self, enemy, moveid):
    print("{} attacks {}!".format(self.name, enemy.name))
    move = self.moves[moveid]
    print("{} uses {} !".format(self.name, move.name))
    dmg = move.dmg * type_array[Types[move.type]][Types[enemy.types[0]]]
    if type_array[Types[move.type]][Types[enemy.types[0]]] > 1:
      print("It's super efficient !")
    elif type_array[Types[move.type]][Types[enemy.types[0]]] == 0:
      print("It doesn't affect {} !", enemy.name)
    elif type_array[Types[move.type]][Types[enemy.types[0]]] < 1:
      print("It's not very efficient")
    if move.style == 'physical':
      dmg *= self.attack
      dmg /= enemy.defense
    elif move.style == 'special':
      dmg *= self.special / enemy.special
    else:
      dmg = 0
    if self.critRate > randrange(0, 100):
      dmg *= self.critFactor
      print("It's a crit !")
    dmg = int(floor(dmg))
    print("{} dealt {} damage".format(self.name, dmg))
    return dmg

  def defend(self, dmg):
    print("{} is taking {} damage".format(self.name, dmg))
    self.hp -= dmg
    if (self.hp <= 0):
      print("{} fainted".format(self.name))
    else:
      print("{} has {} health left".format(self.name, self.hp))

  def is_alive(self):
    return (self.hp > 0)

  def __str__(self):
    return "{} has {} health and {} attack.".format(self.name, self.hp, self.attack)

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