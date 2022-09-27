from Engine.Tools.Button import Button
import Engine.Tools.Font as Font
from Engine.Tools.Colors import black

class Options(object):
    def __init__(self, pos, size):
        self.options = []
        self.pos = pos
        self.size = size
        self.option_size = [4*size[0]/10, 4*size[1]/10]
        self.positions = [
            [pos[0], pos[1]],
            [pos[0] + size[0]/2, pos[1]],
            [pos[0], pos[1] + size[1]/2],
            [pos[0]+ size[0]/2, pos[1] + size[1]/2]
        ]

    def add_option(self, text, color, action):
        if len(self.options) < 4:
            option = Button()
            option.setup(self.positions[len(self.options)], self.option_size, Font.get().render(text, True, black), color, action)
            self.options.append(option)
        else:
            raise Exception("Too many options")
    
    def deactivate(self):
        for option in self.options:
            option.deactivate()

    def update(self, screen):
        for option in self.options:
            option.update(screen)