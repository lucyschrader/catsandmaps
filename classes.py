class Cat:
    def __init__(self, name, ap, money, level=1):
        self.name = name
        self.ap = ap
        self.level = level
        self.money = money

    def level_up(self):
        self.level += 1
        ap_up(self.level + 1)

    def ap_up(self, boost):
        self.ap += boost

    def deal(self):
        self.ap -= 1
        self.money += 20
        pass

    def scout(self):
        self.ap -= 1
        pass

    def sharpen(self):
        self.ap -= 1
        pass