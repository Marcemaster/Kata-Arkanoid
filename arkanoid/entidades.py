import pygame as pg
from pygame.sprite import Sprite

class Raqueta(Sprite):
    disfraces = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5

class Bola(Sprite):
    disfraces = "ball1.png"
    move_x = 1
    move_y = 1


    def __init__(self, **kwargs):
        self.image = pg.image.load(f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.x >= 600 or self.rect.x <= 0:
            self.move_x *= -1
        if self.rect.y >= 800 or self.rect.y <= 0:
            self.move_y *= -1
        
            