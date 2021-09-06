import pygame as pg
from pygame.sprite import Sprite
from . import ANCHO, ALTO, FPS


class Raqueta(Sprite):
    disfraces = ["electric00.png","electric01.png","electric02.png"]

    def __init__(self, **kwargs):
        self.imagenes = []
        for fichero in self.disfraces:
            self.imagenes.append(pg.image.load(
            f"arkanoid/resources/images/{fichero}"))

        self.imagen_activa = 0
        self.tiempo_transcurrido = 0
        self.tiempo_hasta_cambio_disfraz = 1000//FPS * 5
        self.image = self.imagenes[self.imagen_activa]

        self.rect = self.image.get_rect(**kwargs)

    def update(self, dt):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 7

        if self.rect.left <= 0:
            self.rect.left = 0
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 7
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO

        self.tiempo_transcurrido += dt
        if self.tiempo_transcurrido >= self.tiempo_hasta_cambio_disfraz:

            self.imagen_activa += 1
            if self.imagen_activa >= len(self.imagenes):
                self.imagen_activa = 0
            self.image = self.imagenes[self.imagen_activa]
            self.tiempo_transcurrido = 0



class Bola(Sprite):
    disfraces = "ball1.png"

    def __init__(self, **kwargs):
        self.image = pg.image.load(
            f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
        self.move_x = 4
        self.move_y = 4
        self.viva = True
        self.position = kwargs

    def update(self, dt):

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
