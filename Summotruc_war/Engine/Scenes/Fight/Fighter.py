import imp
import pygame
from monster import Monster
from Engine.Tools.Colors import black

class Fighter(Monster):
    def __init__(self, monster, pos, size):
        super().__init__(monster.name, monster.image, monster.hp, monster.attack, monster.defense, monster.special, monster.speed, monster.critRate, monster.critFactor, monster.types, monster.moves)
        self.surface = pygame.transform.scale(monster.image, size)
        self.pos = pygame.rect.Rect(pos, size)
        self.maxhp = self.hp
        self.hpbar = [
            pygame.rect.Rect((pos[0], pos[1]+size[1]+10), (size[0], 10)),
            pygame.rect.Rect((pos[0], pos[1]+size[1]+10), (size[0], 10))
        ]
        self.hpColor = 0, 200, 0

    def setColor(self):
        if self.hp <= 0:
            self.hpColor = black
            return
        self.hpColor = (200 - ((200 * self.hp) / self.maxhp), (200 * self.hp) / self.maxhp, 0)

    def update(self):
        self.hpbar[0].update((self.hpbar[1].left, self.hpbar[1].top), ((self.hpbar[1].width* self.hp) / self.maxhp, self.hpbar[1].height))
        self.setColor()

    def display(self, screen):
        pygame.draw.rect(screen, (50,50,50), self.hpbar[1])
        pygame.draw.rect(screen, self.hpColor, self.hpbar[0])
        screen.blit(self.surface, self.pos)