import pygame

import Engine.SceneManager as SceneManager

import Engine.Tools.Font as Font
from Engine.Tools.Button import Button
from Engine.Tools.Colors import black
from Engine.SceneAbstract import SceneAbstract

class MainMenu(SceneAbstract):
    def __init__(self):
        self.speed = [ 1, 1 ]
        self.title = Font.get().render("Main Menu", True, (50,155,155))
        self.button = Button()

    @staticmethod
    def start_game():
        SceneManager.SceneManager.get_instance().set_scene(1)

    def setup(self, _):
        self.dragon = pygame.image.load("Assets/Monsters/Images/Dragon.png").convert_alpha()
        self.dragon = pygame.transform.scale(self.dragon, (200,200))
        self.button.setup((400,400), (200,100), Font.get().render("Start !", True, (0,0,0)), (255,255,255), self.start_game)

    def update(self, screen):
        screen.fill(black)
        screen.blit(self.dragon, self.dragon.get_rect())
        screen.blit(self.title, self.title.get_rect().move(400,100))
        self.button.update(screen)