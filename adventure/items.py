class Weapon:
    def __init__(self, name, description, value, damage):
        raise NotImplementedError(f"Do not create raw Weapon objects ")

    def __str__(self):
        return self.name


class PatricksCyberSwordOfDestiny(Weapon):
    def __init__(self):
        self.name = "Patrick's Cyber Sword Of Destiny"
        self.description = "The Ultimate Weapon, with your bad breath being a close second"
        self.damage = 50
        self.value = 50

class JacksEnchantedHoboShotgun(Weapon):
    def __init__(self):
        self.name = "Jacks Enchanted Hobo Shotgun"
        self.description = "Jack's Enchanted Shotgun, Very powerful, smells"
        self.damage = 30
        self.value = 100
