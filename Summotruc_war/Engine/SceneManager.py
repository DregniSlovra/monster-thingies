import pygame

from Engine.Event import Event
from Engine.Scenes.MainMenu import MainMenu
from Engine.Scenes.CharacterSelect import CharacterSelect
from Engine.Scenes.Fight.Fight import Fight
from Engine.Scenes.Summary import Summary

class SceneManager(object):
    __instance = None

    def __init__(self):
        if SceneManager.__instance is not None:
            raise Exception("This class is a singleton! Use get_instance() method.")

    @staticmethod
    def get_instance():
        if SceneManager.__instance is None:
            SceneManager.__instance = SceneManager()
        return SceneManager.__instance

    def setup(self, screen):
        self.screen = screen
        self.scenes = []
        self.scenes.append(MainMenu())
        self.scenes.append(CharacterSelect())
        self.scenes.append(Fight())
        self.scenes.append(Summary())
        self.current_scene = self.scenes[0]
        self.current_scene.setup(None)
        self.playing = True
        self.events = Event.get_instance()

    def set_scene(self, id, data=None):
        self.events.clear()
        self.current_scene = self.scenes[id]
        self.current_scene.setup(data)

    def draw(self):
        while self.playing:
            self.playing = self.events.update()
            self.current_scene.update(self.screen)
            pygame.display.update()
            pygame.time.Clock().tick(60)