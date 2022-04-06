import pygame

from util.attack_button import AttackButton
from util.attacks import Attacks
from util.button import Button


class RetryButton(Button):
    def onClick(self, mX, mY, scr):
        self.references.game_over = False
        self.references.player.health = (self.references.player.health[1],self.references.player.health[1])
        self.references.enemy.health = (self.references.enemy.health[1],self.references.enemy.health[1])
        sword_button = AttackButton(12, 400, 64, 64, pygame.image.load("sword_button.png"), self.references, Attacks.SWORD)
        spear_button = AttackButton(88, 400, 64, 64, pygame.image.load("spear_button.png"), self.references, Attacks.SPEAR)
        shield_button = AttackButton(164, 400, 64, 64, pygame.image.load("shield_button.png"), self.references,
                                     Attacks.SHIELD)
        fire_button = AttackButton(288, 400, 64, 64, pygame.image.load("fire_button.png"), self.references, Attacks.FIRE)
        water_button = AttackButton(364, 400, 64, 64, pygame.image.load("water_button.png"), self.references, Attacks.WATER)
        wood_button = AttackButton(440, 400, 64, 64, pygame.image.load("wood_button.png"), self.references, Attacks.WOOD)
        gun_button = AttackButton(564, 400, 64, 64, pygame.image.load("gun_button.png"), self.references, Attacks.GUN)
        flamethrower_button = AttackButton(640, 400, 64, 64, pygame.image.load("flamethrower_button.png"), self.references,
                                           Attacks.FLAMETHROWER)
        bomb_button = AttackButton(716, 400, 64, 64, pygame.image.load("bomb_button.png"), self.references, Attacks.BOMB)

        self.references.buttons = [sword_button, spear_button, shield_button, fire_button, water_button, wood_button, gun_button,
                        flamethrower_button, bomb_button]