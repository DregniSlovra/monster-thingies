from abc import ABC, abstractmethod

import pygame

class SceneAbstract(ABC):

    @abstractmethod
    def setup(data=None):
        pass

    @abstractmethod
    def update(screen):
        pass
