from adventure import items


class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError
class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.witcherCoins = 100
        self.inventory = [items.CrustyBread(), items.CrustyBread(), items.CrustyBread(), items.HealingPotion, items.HealingPotion, items.HealingPotion]
