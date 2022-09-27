import pygame

from Engine.Event import Event
from Engine.Tools.Listener import Listener

class Button(object):
  def __init__(self):
    self.armed = False
    pass

  def is_clicked(self, event):
    if (event.type == pygame.MOUSEBUTTONDOWN):
      self.armed = True
    elif (self.armed and event.type == pygame.MOUSEBUTTONUP):
      if (self.rect.collidepoint(event.pos)):
        self.armed = False
        return True
    return False

  def change_image(self, image):
    self.image = image
    self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))

  def setup(self, pos, size, image, color, action):
    self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    self.image = image
    self.image = pygame.transform.scale(self.image, (size[0],size[1]))
    self.color = color
    self.action = Listener(action, self.is_clicked)
    Event.get_instance().set_listener(self.action)

  def deactivate(self):
    Event.get_instance().remove_listener(self.action)

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)
    screen.blit(self.image, self.rect)
