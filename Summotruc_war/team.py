from monster import Monster

class Team:
    def __init__(self, name : str):
        self.monsters : list[Monster] = []
        self.name : str = name

    def is_standing(self) -> bool :
        for monster in self.monsters:
            if (monster.hp > 0):
                return True
        return False

    def energy_refill(self):
        for monster in self.monsters:
            monster.energy += monster.speed + 100

    def add(self, monster):
        self.monsters.append(monster)

    def remove(self, monster):
        self.monsters.remove(monster)

    def next(self) -> Monster :
        result = self.monsters[0]
        for monster in self.monsters:
            if (result.energy < monster.energy):
                result = monster
        return result