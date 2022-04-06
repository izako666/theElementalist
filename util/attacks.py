from enum import Enum

class Attacks(Enum):
    WEAPONRY = -3
    MAGIC = -2
    SCIENCE = -1

    SWORD = 0
    SPEAR = 1
    SHIELD = 2

    FIRE = 3
    WATER = 4
    WOOD = 5

    GUN = 6
    FLAMETHROWER = 7
    BOMB = 8

    @staticmethod
    def compareByCategory(att1,att2):

        if att1 <= 2:
            if att2 <= 2:
                return Attacks.compareByAttack(att1,att2)
            elif 2 < att2 <= 5:
                return -2
            elif 5 < att2 <= 8:
                return 2
        elif 2<att1 <=5:
            if att2 <= 2:
                return 2
            elif 2 < att2 <= 5:
                return Attacks.compareByAttack(att1,att2)
            elif 5 < att2 <= 8:
                return -2
        elif 5<att1<=8:
            if att2 <= 2:
                return -2
            elif 2 < att2 <= 5:
                return 2
            elif 5 < att2 <= 8:
                return Attacks.compareByAttack(att1,att2)
    @staticmethod
    def compareByAttack(att1,att2):
        if att1 == 0 or att1 == 3 or att1 == 6:
            if att2 == att1 + 1:
                return -1
            else:
                return 1
        elif att1 == 1 or att1 == 4 or att1 == 7:
            if att2 == att1 + 1:
                return -1
            else:
                return 1
        else:
            if att2 == att1 - 1:
                return 1
            else:
                return -1


    @staticmethod
    def find_sprite_from_enum(attack):
        if attack.value == 0:
            return "sword_button.png"
        elif attack.value == 1:
            return "spear_button.png"
        elif attack.value == 2:
            return "shield_button.png"
        elif attack.value == 3:
            return "fire_button.png"
        elif attack.value == 4:
            return "water_button.png"
        elif attack.value == 5:
            return "wood_button.png"
        elif attack.value == 6:
            return "gun_button.png"
        elif attack.value == 7:
            return "flamethrower_button.png"
        elif attack.value == 8:
            return "bomb_button.png"

    @staticmethod
    def find_enum_from_value(val):
        if val == -3:
            return Attacks.WEAPONRY
        if val == -2:
            return Attacks.MAGIC
        if val == -1:
            return Attacks.SCIENCE
        if val == 0:
            return Attacks.SWORD
        if val == 1:
            return Attacks.SPEAR
        if val == 2:
            return Attacks.SHIELD
        if val == 3:
            return Attacks.FIRE
        if val == 4:
            return Attacks.WATER
        if val == 5:
            return Attacks.WOOD
        if val == 6:
            return Attacks.GUN
        if val == 7:
            return Attacks.FLAMETHROWER
        if val == 8:
            return Attacks.BOMB

