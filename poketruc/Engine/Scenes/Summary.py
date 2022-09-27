from Engine.Tools.Colors import black
from Engine.Tools.Message import Message

class Summary(object):
    def __init__(self):
        pass

    def setup(self, data):
        self.message = Message([50, 50], [500, 200])
        if data["won"]:
            gold = 0
            xp = 0
            self.message.add_content(f"You got {gold} gold !\nYour monster got {xp} experience points !")
            print("you win")
        else:
            self.message.add_content("You lost :c")
            print("you lost")
        self.message.next()
    
    def update(self, screen):
        screen.fill(black)
        self.message.update(screen)