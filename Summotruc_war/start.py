import pygame

from Engine.SceneManager import SceneManager

if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    scnmng = SceneManager.get_instance()
    scnmng.setup(screen)
    scnmng.draw()
    exit