from functools import partial
from math import ceil, sqrt
import os
import pygame

from monster import monster_from_json

import Engine.SceneManager as SceneManager
from Engine.Tools.Button import Button
from Engine.Tools.Colors import black
from Engine.SceneAbstract import SceneAbstract

def grid_size(length):
  x = ceil(sqrt(length))
  y = round(sqrt(length))
  return x, y

class CharacterSelect(SceneAbstract):
  def __init__(self):
    self.monsters = []
    self.players = []

  def Selected(self, monster):
    print("Selected :", monster.name)
    self.players.append(monster)
    if (len(self.players) == 2):
      SceneManager.SceneManager.get_instance().set_scene(2, data={"players": self.players})

  def grid(self):
    sw, sh = pygame.display.get_surface().get_size()
    w, h = self.grid_size
    for x in range(0, w):
      for y in range(0, h):
        if (y*w+x < len(self.monsters)):
          action = partial(self.Selected, self.monsters[y*w+x][0])
          self.monsters[y*w+x][1].setup((x * sw/w, y * sh/h), (sw/w/1.5,sh/h/1.5), self.monsters[y*w+x][0].image, black, action)

  def setup(self, _):
    self.monsters = []
    self.players = []
    monster_list = os.listdir("Assets/Monsters")
    for monster_file in monster_list:
      if os.path.isdir("Assets/Monsters/" + monster_file):
        continue
      monster = monster_from_json("Assets/Monsters/" + monster_file)
      self.monsters.append([
        monster,
        Button(),
      ])
    self.grid_size = grid_size(len(self.monsters))
    self.grid()

  def update(self, screen):
    screen.fill(black)
    for monster in self.monsters:
      monster[1].update(screen)