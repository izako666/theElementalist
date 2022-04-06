import pygame.image


class Animation():
    x = 0
    y = 0
    sprite = pygame.image.load("button.png")
    time = 20
    currentTime = 0
    references = None
    extra_info = []
    def empty(self):
        return
    updateFunc =empty

    def __init__(self, x, y, sprite, time,references):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.time = time
        self.references = references

    def update(self):
        self.updateFunc(self)
        self.currentTime += 1
        if self.currentTime >= self.time:
            return -1
        return 0
