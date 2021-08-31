import pygame as pg

pg.init()

class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode((ANCHO,ALTO))

    def start(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla.fill((123, 123, 255))

            pg.display.flip()

        pg.quit()


