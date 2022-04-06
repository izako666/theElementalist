import pygame

from enemy import Enemy
from player import Player
from util.attack_button import AttackButton
from util.attacks import Attacks


class References:
    def __init__(self):
        sword_button = AttackButton(12, 400, 64, 64, pygame.image.load("sword_button.png"), self, Attacks.SWORD)
        spear_button = AttackButton(88, 400, 64, 64, pygame.image.load("spear_button.png"), self, Attacks.SPEAR)
        shield_button = AttackButton(164, 400, 64, 64, pygame.image.load("shield_button.png"), self,
                                     Attacks.SHIELD)
        fire_button = AttackButton(288, 400, 64, 64, pygame.image.load("fire_button.png"), self, Attacks.FIRE)
        water_button = AttackButton(364, 400, 64, 64, pygame.image.load("water_button.png"), self, Attacks.WATER)
        wood_button = AttackButton(440, 400, 64, 64, pygame.image.load("wood_button.png"), self, Attacks.WOOD)
        gun_button = AttackButton(564, 400, 64, 64, pygame.image.load("gun_button.png"), self, Attacks.GUN)
        flamethrower_button = AttackButton(640, 400, 64, 64, pygame.image.load("flamethrower_button.png"), self,
                                           Attacks.FLAMETHROWER)
        bomb_button = AttackButton(716, 400, 64, 64, pygame.image.load("bomb_button.png"), self, Attacks.BOMB)

        self.buttons = [sword_button, spear_button, shield_button, fire_button, water_button, wood_button, gun_button,
                   flamethrower_button, bomb_button]

        self.player.x = 135
        self.player.y = 210
        self.player.references = self

        self.enemy = Enemy()
        self.enemy.x = 800 - 135 - 64
        self.enemy.y = 210
        self.enemy.references = self
        self.bold_font = pygame.font.SysFont(pygame.font.get_default_font(), 72)

        self.animations = []

    screen = pygame.display.set_mode((800, 600))
    icon = pygame.image.load('icon.png')
    background = pygame.image.load('background.png')

    player = Player()

    enemy = Enemy()

    buttons = []
    animations = []

    score = 0
    bold_font = None
    game_over = False
    game_started = False
