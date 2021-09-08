import pygame as pg
from . import FPS, ANCHO, ALTO
from .entidades import Raqueta, Bola, Ladrillo, Marcador


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
        self.bola = Bola(center=(ANCHO/2, ALTO/2))
        self.puntos = 0

        self.cuentaVidas = Marcador(10, 10, "CabinSketch-Bold.ttf", 24, (255,255,255))
        self.cuentaPuntos = Marcador(1, 40, "LibreFranklin-VariableFont_wght.ttf", 24, (255,255,255))


        self.ladrillos = pg.sprite.Group()
        self.todos = pg.sprite.Group()



    def reset(self):
        self.vidas = 3 
        self.puntos = 0

        self.ladrillos.empty()
        self.todos.empty()

        self.bola.reset()
        self.player.reset()
        
        for f in range(3):
            for c in range(6):
                ladrillo = Ladrillo(c * 90 + 30, f * 30 + 10)
                self.ladrillos.add(ladrillo)

        self.todos.add(self.ladrillos, self.player, self.bola, self.cuentaPuntos, self.cuentaVidas, self.cuentaPuntos)

    def bucle_principal(self):
        self.reset()
        while self.vidas > 0:
            dt = self.reloj.tick(FPS)
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            

            self.cuentaPuntos.texto = self.puntos
            self.cuentaVidas.texto = self.vidas
            self.todos.update(dt)

            self.bola.comprobar_colision(self.player)

            tocados = pg.sprite.spritecollide(self.bola, self.ladrillos, True)
            if len(tocados) > 0:
                self.bola.move_y *= -1
                self.puntos += len(tocados) * 5

            if not self.bola.viva:
                self.vidas -= 1
                self.bola.viva = True
                self.player.reset()

            self.pantalla.blit(self.fondo, (0, 0))
            self.todos.draw(self.pantalla)

            pg.display.flip()


class Records(Escena):
    pass
