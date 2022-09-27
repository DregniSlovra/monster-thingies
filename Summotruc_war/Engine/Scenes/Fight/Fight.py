from functools import partial
from math import floor
from random import randrange
import pygame

import Engine.SceneManager as SceneManager
from Engine.Scenes.Fight.Fighter import Fighter
from Engine.Scenes.Fight.Options import Options

from Engine.Event import Event
from Engine.Tools.Message import Message
from Engine.Tools.Colors import black, type_colors
from Engine.SceneAbstract import SceneAbstract
from monster import fight

class Fight(SceneAbstract):
    def __init__(self):
        self.players = []
        self.screen_size = pygame.display.get_surface().get_size()

    def attack(self):
        print("activating attacks")
        self.active.deactivate()
        self.active = self.make_attacks()

    def turn_attacks(self, move):
        if self.challenger.speed > self.foe.speed:
            self.foe.defend(self.challenger.use(self.foe, move.id - 1))
            if not self.foe.is_alive():
                print("Turn end !\n")
                return
            self.challenger.defend(self.foe.use(self.challenger, int(floor(randrange(0, 3)))))
        else:
            self.challenger.defend(self.foe.use(self.challenger, int(floor(randrange(0, 3)))))
            if not self.challenger.is_alive():
                print("Turn end !\n")
                return
            self.foe.defend(self.challenger.use(self.foe, move.id - 1))

    def move(self, move):
        print(self.challenger.name, "uses", move.name)
        self.turn_attacks(move)
        self.active.deactivate()
        self.active = self.make_options()

    def heal(self):
        print(self.challenger.hp)

    def give_up(self):
        # SceneManager.SceneManager.get_instance().set_scene(3, data={"won": False})
        SceneManager.SceneManager.get_instance().set_scene(0)

    def fight_end(self):
        won = True
        if self.challenger.hp <= 0:
            won = False
        SceneManager.SceneManager.get_instance().set_scene(3, data={"won": won})
    
    def make_objects(self):
        objects = Options((3*self.screen_size[0]/5, 3*self.screen_size[1]/5), (self.screen_size[0]/3, self.screen_size[1]/3))
        return objects

    def make_options(self):
        options = Options((3*self.screen_size[0]/5, 3*self.screen_size[1]/5), (self.screen_size[0]/3, self.screen_size[1]/3))
        options.add_option("attack", (200,200,200), self.attack)
        options.add_option("heal", (200,200,200), self.heal)
        options.add_option("give up", (100,100,100), self.give_up)
        return options

    def make_attacks(self):
        attacks = Options((3*self.screen_size[0]/5, 3*self.screen_size[1]/5), (self.screen_size[0]/3, self.screen_size[1]/3))
        for move in self.challenger.moves:
            attack = partial(self.move, move)
            attacks.add_option(move.name, type_colors[move.type], attack)
        return attacks

    def setup(self, data):
        self.players = data["players"]
        print(self.players[0])
        self.challenger = Fighter(self.players[0], (self.screen_size[0]/10, 3*self.screen_size[1]/5), (self.screen_size[0]/3, self.screen_size[1]/3))
        self.foe = Fighter(self.players[1], (3*self.screen_size[0]/5, self.screen_size[1]/10), (self.screen_size[0]/3, self.screen_size[1]/3))
        self.message = Message((10, 10), (self.screen_size[0]/2, self.screen_size[1]/3))
        self.message.add_content("Make your move")
        self.message.next()
        self.active = self.make_options()
        Event.get_instance().debug()

    def update(self, screen):
        screen.fill(black)
        self.challenger.update()
        self.challenger.display(screen)
        self.foe.update()
        self.foe.display(screen)
        self.message.update(screen)
        self.active.update(screen)
        if self.challenger.hp < 0 or self.foe.hp < 0:
            self.fight_end()
