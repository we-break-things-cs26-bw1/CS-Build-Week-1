class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects")

    def __str__(self):
        return f"{self.name}(+{self.healing_value})"


class CrustyBread(Consumable):

    def __init__(self):
        self.name = "Crusty Loaf"
        self.healing_value = 10
        self.value = 5


class HealingPotion(Consumable):

    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
