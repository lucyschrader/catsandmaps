class Cat:
    def __init__(self, name, ap, money, level=1, knowledge=1):
        self.name = name
        self.ap = ap
        self.level = level
        self.money = money
        self.knowledge = knowledge

    def level_up(self):
        self.level += 1
        ap_up(self.level + 1)

    def ap_up(self, boost):
        self.ap += boost

    def do(self, action):
        self.ap -=1
        if action == 'deal':
            self.money += 20
        elif action == 'scout':
            self.knowledge += 1
        else:
            pass

    def sharpen(self):
        self.ap -= 1
        pass