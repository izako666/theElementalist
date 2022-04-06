import pygame

from util.button import Button
from util.retry_button import RetryButton


class Player:
    x = 0
    y = 0
    sprite = pygame.image.load("player.png")
    health = (10, 10)
    references = None

    def render(self, scr):
        if self.health[0] <= 0 and not self.references.game_over:
            self.references.game_over = True
            self.references.buttons.clear()
            retry_button = RetryButton(400-64, 400, 128, 64, pygame.image.load("retry.png"), self.references)
            self.health = (self.health[1], self.health[1])
            self.references.buttons.append(retry_button)
            self.references.enemy.health = (10,10)
            self.references.score = 0
        scr.blit(self.sprite, (self.x, self.y))
        pygame.draw.rect(scr, (255, 0, 0),
                         (40, 15, 200 - ((self.health[1] - self.health[0]) * (200 / self.health[1])), 30))
        pygame.draw.rect(scr, (0, 0, 0), (40, 40, 200, 5))
