import pygame as pg
from pygame.sprite import Sprite
from . import ANCHO, ALTO


class Raqueta(Sprite):
    disfraces = "electric00.png"

    def __init__(self, **kwargs):
        self.image = pg.image.load(
            f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5

        if self.rect.left <= 0:
            self.rect.left = 0
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO


class Bola(Sprite):
    disfraces = "ball1.png"

    def __init__(self, **kwargs):
        self.image = pg.image.load(
            f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
        self.move_x = 3
        self.move_y = 3
        self.viva = True
        self.position = kwargs

    def update(self):

        self.rect.x -= self.move_x
        self.rect.y -= self.move_y

        if self.rect.x >= ANCHO-30 or self.rect.x <= 0:
            self.move_x *= -1
        if self.rect.y <= 0:
            self.move_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.rect = self.image.get_rect(**self.position)
            self.move_y *= -1
            self.move_x *= -1

    def comprobar_colision(self, otro):
        if self.rect.right >= otro.rect.left and self.rect.left <= otro.rect.right and \
                self.rect.bottom >= otro.rect.top and self.rect.top <= otro.rect.bottom:
            self.move_y *= -1
