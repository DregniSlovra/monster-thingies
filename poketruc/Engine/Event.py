import pygame

class Event(object):
  __instance = None

  def __init__(self):
    if Event.__instance is not None:
      raise Exception("This class is a singleton! Use get_instance() method.")

  @staticmethod
  def get_instance():
    if Event.__instance is None:
      Event.__instance = Event()
      Event.__instance.setup()
    return Event.__instance

  def debug(self):
    for listener in self.listeners:
      print(listener)

  def setup(self):
    self.listeners = []

  def set_listener(self, listener):
    self.listeners.append(listener)

  def remove_listener(self, listener):
    self.listeners.remove(listener)
  
  def clear(self):
    self.listeners.clear()

  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return False

      for listener in self.listeners:
        listener.update(event)
    return True