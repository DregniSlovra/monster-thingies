import pygame

class Listener(object):
  def __init__(self, action, predicate):
    self.action = action
    self.predicate = predicate

  def update(self, event):
    if (self.predicate(event)):
      self.action()