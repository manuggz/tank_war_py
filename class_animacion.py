# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


from os.path import join


class Animacion:
    "Permite controlar animaciones almacenadas en una grilla de cuadros"
    
    def __init__ (self, spritesheet):
        "Genera una animacion en base a una grilla de cuadros"
        
        self.spritesheet = spritesheet
        self.index = 0
        self.step = 0
        self.delay = 10
        self.counter_delay = 0
        self.dx = 0
        self.dy = 0

    def get_rect (self):
        return self.spritesheet.get_rect ()

    def get_actual_frame (self):
        "Informa que cuadro debe ser mostrado"
        
        return self.spritesheet.get_frame(self.index)
    
    def set_frames (self, new_frames):
        "Define la secuencia de cuadros para la animación actual, por ejemplo [0, 1, 2]"
        
        self.frames = new_frames
        self.step = 0
        self.counter_delay = 0
        self.index = self.frames [0]


    def advance (self):
        "Avanza un cuadro de animación hacia adelante, retorna 1 si llegó al final de animación y se reinicia"
        
        if self.counter_delay < self.delay:
            self.counter_delay += 1
            return 0
        else:
            self.counter_delay = 0
            self.step += 1
            
            if self.step > len (self.frames) - 1:
                self.step = 0
                self.index = self.frames [self.step]
                return 1
            else:
                self.index = self.frames [self.step]
                return 0

