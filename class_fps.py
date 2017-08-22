# -*- coding: utf-8 -*-

from pygame.sprite import Sprite
import pygame

class Fps (Sprite):
    "Informa el rendimiento del programa mediante el indicador FPS (cuadros por segundo)"
    
    def __init__ (self, clock):
        "Inicia el controlador de rendimiento"
        
        Sprite.__init__ (self)
        self.clock = clock
        self.font = pygame.font.Font (None, 16)

    def update (self):
        "Obtiene el rendimiento del programa"
        
        fps = int (self.clock.get_fps ())
        self.image = self.font.render ('FPS: ' + str (fps), 1, (100, 100, 100))
        self.rect = self.image.get_rect ()