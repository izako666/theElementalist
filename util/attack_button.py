import pygame

from util.animation import Animation
from util.attacks import Attacks
from util.button import Button


def update_attack_animation(self: Animation):
    # goal is 200,450
    self.x += (350 - self.x) / 10
    self.y += (150 - self.y) / 10
    if self.extra_info[0] > self.references.player.health[0] and self.currentTime > 80:
        return
    self.references.screen.blit(self.sprite, (self.x, self.y))

def update_attack_animation_enemy(self: Animation):
    # goal is 200,450
    self.x += (450 - self.x) / 10
    self.y += (150 - self.y) / 10
    if self.extra_info[0] == self.references.player.health[0] and self.currentTime > 80:
        return
    self.references.screen.blit(self.sprite, (self.x, self.y))


class AttackButton(Button):
    attack = Attacks.SWORD

    def click_handler(self, mx, my, scr):
        animation = Animation(mx, my, self.sprite, 60 * 1.5, self.references)
        animation.extra_info.append(self.references.player.health[0])
        animation.updateFunc = update_attack_animation
        if len(self.references.animations) == 0:
            self.references.animations.append(animation)
            enemy_attack = Attacks(self.references.enemy.get_attack())
            enemy_animation = Animation(self.references.enemy.x - 64, self.references.enemy.y,
                                       pygame.image.load(Attacks.find_sprite_from_enum(enemy_attack)),
                                       60 * 1.5, self.references)
            enemy_animation.updateFunc = update_attack_animation_enemy
            enemy_animation.extra_info.append(self.references.player.health[0])

            self.references.animations.append(enemy_animation)

            damage = Attacks.compareByCategory(self.attack.value, enemy_attack.value)
            if damage < 0:
                self.references.player.health = (
                    self.references.player.health[0] + damage, self.references.player.health[1])
            else:
                self.references.enemy.health = (
                    self.references.enemy.health[0] - damage, self.references.enemy.health[1])

        else:
            for a in self.references.animations:
                if a.updateFunc == update_attack_animation:
                    return
                else:
                    self.references.animations.append(animation)
                    enemy_attack = Attacks(self.references.enemy.get_attack())
                    enemy_animation = Animation(self.references.enemy.x - 64, self.references.enemy.y,
                                               pygame.image.load(Attacks.find_sprite_from_enum(enemy_attack)),
                    60 * 1.5, self.references)
                    enemy_animation.updateFunc = update_attack_animation_enemy
                    enemy_animation.extra_info.append(self.references.player.health[0])
                    self.references.animations.append(enemy_animation)
                    damage = Attacks.compareByCategory(self.attack.value, enemy_attack.value)
                    if damage < 0:
                        self.references.player.health = (
                            self.references.player.health[0] + damage, self.references.player.health[1])
                    else:
                        self.references.enemy.health = (
                            self.references.enemy.health[0] - damage, self.references.enemy.health[1])

    def __init__(self, x, y, width, height, sprite, references, attack):
        Button.__init__(self, x, y, width, height, sprite, references)
        self.onClickFunc = self.click_handler
        self.attack = attack
