# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from class_animacion import Animacion

from pygame.sprite import Sprite         #Clase base de los Sprites


class Entidad(Sprite):
    """description of class"""

    def __init__ (self, escena,position_x,position_y):
        "Carga los recursos principales para comenzar el juego"        
        Sprite.__init__ (self)        
        self.escena = escena
        
        self.animacion = Animacion(escena.spritesheet)
 
        self.rect = self.animacion.get_rect () #Rectangulo que representa al personaje
        self.rect.x = position_x
        self.rect.y = position_y

        self.x = position_x
        self.y = position_y

        self.screen_rect = escena.get_rect_screen()


