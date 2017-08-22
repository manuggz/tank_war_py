# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from class_animacion import Animacion
from class_entidad import Entidad

from pygame.sprite import Sprite         #Clase base de los Sprites

class Personaje(Entidad):
    """description of class"""

    def __init__ (self, escena,position_x,position_y):
        "Carga los recursos principales para comenzar el juego"        
        Entidad.__init__ (self, escena,position_x,position_y)        
        self.face_direction = "top"
        self.esta_intocable=False #Esta variable controla el efecto a la imagen a mostrar y si se puede herir al personaje
        self.delay_proteccion=0
        self.nivel_hp = 100


    @staticmethod
    def get_v_dir_from_face_dir(face_dir):
        if face_dir == 'top':
            return (0,-1)
        elif face_dir == 'bottom':
            return (0,1)
        elif face_dir == 'left':
            return (-1,0)
        elif face_dir == 'right':
            return (1,0)

    @staticmethod
    def get_face_direction_from_v_dir(dir):
        if dir == (1,0):
            return 'right'
        elif dir == (-1,0):
            return 'left'
        elif dir == (0,1):
            return 'bottom'
        elif dir == (0,-1):
            return 'top'
    
    def set_face_direction(self,d):        
        self.face_direction = d
        #self.animacion.set_angle(self.)

    def herir(self,cantidad):
        if not self.esta_intocable:
            self.nivel_hp -= cantidad
            return True

        return False
            #self.esta_intocable=True