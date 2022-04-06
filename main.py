from typing import List

import pygame

from enemy import Enemy
from player import Player
from util.attack_button import AttackButton
from util.attacks import Attacks
from util.button import Button
from util.references import References
from util.start_button import StartButton

pygame.init()

# initializations
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Elementalist")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
running = True

init_start = False

references = References()

# buttons

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        # Button Click Handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in references.buttons:
                if b.x <= pygame.mouse.get_pos()[0] <= b.x + b.width and b.y <= pygame.mouse.get_pos()[
                    1] <= b.y + b.height:
                    b.onClick(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)


    for b in references.buttons:
        b.render(screen)
        if b.x <= pygame.mouse.get_pos()[0] <= b.x + b.width and b.y <= pygame.mouse.get_pos()[1] <= b.y + b.height:
            b.onHover(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
            b.wasHovering = True
        elif b.wasHovering:
            b.wasHovering = False
            b.onStopHovering(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
    for a in references.animations:
        if a.update() == -1:
            references.animations.remove(a)
    if references.game_over:
        text = references.bold_font.render("GAME OVER", True, pygame.color.Color(255, 255, 255))
        screen.blit(text, (250, 300))
    references.enemy.render(screen)
    references.player.render(screen)

    if references.game_started:
        text_score = references.bold_font.render("Score: " + str(references.score), True,
                                                 pygame.color.Color(255, 255, 255))
        screen.blit(text_score, (300, 50))
    else:
        screen.blit(pygame.image.load("start_background.png"), (0,0))
        text_the_elementalist = references.bold_font.render("The Elementalist", True,
                                                            pygame.color.Color(255, 255, 255))
        screen.blit(text_the_elementalist, (200, 50))
        b = references.buttons[0]
        if b != None:
            b.render(screen)
            if b.x <= pygame.mouse.get_pos()[0] <= b.x + b.width and b.y <= pygame.mouse.get_pos()[1] <= b.y + b.height:
                b.onHover(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
                b.wasHovering = True
            elif b.wasHovering:
                b.wasHovering = False
                b.onStopHovering(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)

    if not references.game_started and not init_start:
        references.buttons.clear()

        start_button = StartButton(400 - 128, 400, 256, 64, pygame.image.load("start.png"), references)
        references.buttons.append(start_button)
        init_start = True

    pygame.display.update()
