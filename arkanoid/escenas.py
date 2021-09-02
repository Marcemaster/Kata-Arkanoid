import pygame as pg
from . import FPS, ANCHO, ALTO
from .entidades import Raqueta


class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.logo = pg.image.load(
            'arkanoid/resources/images/arkanoid_name.png')
        font = pg.font.Font(
            "arkanoid/resources/fonts/CabinSketch-Bold.ttf", 45)
        self.callToAction = font.render(
            "Pulsa <SPC> para comenzar", True, (0, 0, 0))
        self.anchoTexto = self.callToAction.get_width()

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((80, 80, 255))
            self.pantalla.blit(self.logo, (140, 100))
            self.pantalla.blit(self.callToAction,
                               ((ANCHO-self.anchoTexto) // 2, 340))

            pg.display.flip()


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pg.image.load("arkanoid/resources/images/background.jpg")
        self.player = Raqueta(midbottom=(ANCHO/2, ALTO-15))

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.player.image, self.player.rect)
            pg.display.flip()


class Records(Escena):
    pass
