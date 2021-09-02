import pygame as pg
from pygame.sprite import Sprite

class Raqueta(Sprite):
    disfraces = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"arkanoid/resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
