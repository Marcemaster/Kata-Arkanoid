import pygame as pg
from . import ANCHO, ALTO
from arkanoid.escenas import Portada

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla)]

    def start(self):
        self.escenas[0].bucle_principal()
        pg.quit()

