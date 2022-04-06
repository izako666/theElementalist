import math
import pygame



class Button:
    x = 0
    y = 0
    width = 16
    height = 16
    sprite = pygame.image.load("icon.png")
    wasHovering = False
    references = None

    def __init__(self, x, y, width, height, sprite, references):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = sprite
        self.references = references

    def onClick(self, mX, mY, scr):
        self.onClickFunc(mX, mY, scr)
        return

    def onHover(self, mX, mY, scr):
        self.onHoverFunc(mX, mY, scr)
        return

    def onStopHovering(self, mX, mY, scr):
        self.onStopHoveringFunc(mX, mY, scr)
        return

    def render(self, scr):
        if self.wasHovering:
            new_sprite = pygame.transform.scale(self.sprite, (self.width * 1.1, self.height * 1.1))
            scr.blit(new_sprite, (self.x,self.y))
        new_sprite = pygame.transform.scale(self.sprite, (self.width,self.height))
        scr.blit(new_sprite, (self.x, self.y))

    def emptyFunc(self, mX, mY, scr):
        return

    onClickFunc = emptyFunc
    onHoverFunc = emptyFunc
    onStopHoveringFunc = emptyFunc
