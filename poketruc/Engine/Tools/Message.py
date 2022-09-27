import pygame

import Engine.Tools.Font as Font

class Message(object):
    def __init__(self, pos, size):
        self.content = ""
        self.queue = []
        self.box = pygame.rect.Rect(pos, size)
        self.text = Font.get().render("", True, (0,0,0))
        self.color = 200,200,200

    def add_content(self, content):
        self.queue.append(content)

    def next(self):
        if self.queue:
            self.content = self.queue.pop()
            self.text = Font.get().render(self.content, True, (0,0,0))

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.box)
        screen.blit(self.text, self.box)
