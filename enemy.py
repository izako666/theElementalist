import pygame

from util.attacks import Attacks
import random


class Enemy:
    x = 0
    y = 0
    sprite_index = 0
    sprite_resources = ["enemy1.png","enemy2.png","enemy3.png","enemy4.png","enemy5.png"]
    sprite = pygame.image.load("enemy1.png")
    health = (10, 10)
    liked_category = Attacks.WEAPONRY
    disliked_category = Attacks.MAGIC
    references = None

    def __init__(self):
        choices = [-1,-2,-3]

        self.liked_category = Attacks.find_enum_from_value(random.choice(choices))
        choices.remove(self.liked_category.value)
        self.disliked_category = Attacks.find_enum_from_value(random.choice(choices))


    def render(self, scr):
        if self.health[0] <= 0:
            self.references.score += 1
            self.health = (self.health[1] + 5, self.health[1] + 5)
            self.references.player.health = (self.references.player.health[1], self.references.player.health[1]+5)
            choices = [0,1,2,3,4]
            choices.remove(self.sprite_index)
            current_sprite = self.sprite_resources[random.choice(choices)]
            self.sprite = pygame.image.load(current_sprite)
            choices_cat = [-1, -2, -3]

            self.liked_category = Attacks.find_enum_from_value(random.choice(choices_cat))
            choices_cat.remove(self.liked_category.value)
            self.disliked_category = Attacks.find_enum_from_value(random.choice(choices_cat))

        scr.blit(self.sprite, (self.x, self.y))
        pygame.draw.rect(scr, (255, 0, 0),
                         (560 + ((self.health[1] - self.health[0]) * (200 / self.health[1])), 15,
                          200 - ((self.health[1] - self.health[0]) * (200 / self.health[1])), 30))
        pygame.draw.rect(scr, (0, 0, 0), (560, 40, 200, 5))

    def get_attack(self):
        choices = []
        for i in range(-3,0,1):
            if self.liked_category == i:
                choices.extend([i,i,i,i,i])
            elif self.disliked_category == i:
                choices.extend([i])
            else:
                choices.extend([i,i,i])

        selected_category = random.choice(choices)

        if selected_category == -3:
            return random.choice([0,1,2])
        elif selected_category == -2:
            return random.choice([3,4,5])
        elif selected_category == -1:
            return random.choice([6,7,8])


        return 0
