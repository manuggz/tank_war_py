# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from random import randint,choice
#from rectangulos import Zona
#from NinjaSound_states import Matar
#from engine.rectangulos import Zona

#from animacion import Animacion
from os.path import join

class State:
    "Representación abstracta de un estado de personaje"
    
    def __init__ (self, tanque):
        "\param tanque tanque "
        self.tanque             = tanque
        self.tick               = 0
        self.ticks_para_moverse = randint(150,300)

    def update (self):
        pass


class StandingStill(State):
    "Representa el estado 'parado'"
    
    def __init__ (self, tanque):
        "Inicia el estado"
        State.__init__ (self, tanque)
        if self.tanque.face_direction == "top":
            self.tanque.animacion.set_frames([17*12 + 4])
        elif self.tanque.face_direction == "bottom":
            self.tanque.animacion.set_frames([18*12 + 6])
        elif self.tanque.face_direction == "left":
            self.tanque.animacion.set_frames([17*12 + 7])
        elif self.tanque.face_direction == "right":
            self.tanque.animacion.set_frames([19*12 + 8])

    def update (self):

        self.tick += 1
        
        if self.tick > self.ticks_para_moverse:
            choices_vdirs = [(1,0),(-1,0),(0,1),(0,-1)]
            self.tanque.change_state (MoviendoseVector(self.tanque,choice(choices_vdirs)))
        
class MoviendoseVector(State):
    "Controla al personaje mientras corre por el escenario"
    
    def __init__ (self, tanque,dir):
        State.__init__ (self, tanque)
        self.set_dir(dir)

    def set_dir(self,dir):
        self.v_dir = dir

        face_dir = self.tanque.get_face_direction_from_v_dir(dir)
        self.tanque.set_face_direction(face_dir)
        if face_dir == "top":
            self.tanque.animacion.set_frames([15*12 + 9,16*12 + 9,17*12 + 9,18*12 + 9,19*12 + 9,20*12 + 9,21*12 + 9])
        elif face_dir == "bottom":
            self.tanque.animacion.set_frames([15*12 + 10,16*12 + 10,17*12 + 10,18*12 + 10,19*12 + 10,20*12 + 10,21*12 + 10])
        elif face_dir == "left":
            self.tanque.animacion.set_frames([20*12 +2,20*12 +3,20*12 +4,20*12 +5,20*12 +6,20*12 +7,20*12 +8])
        elif face_dir == "right":
            self.tanque.animacion.set_frames([21*12 +2,21*12 +3,21*12 +4,21*12 +5,21*12 +6,21*12 +7,21*12 +8])

    
    def update (self):
                     
        self.tick += 1

        ## Movemos el tanque
        vel = self.tanque.get_velocidad_movimiento()
        se_movio = self.tanque.move_ip (vel * self.v_dir[0],vel * self.v_dir[1])
        
        # Hey, si no lo podemos mover revertimos la dirección
        if not se_movio:
            self.set_dir((self.v_dir[0]*-1,self.v_dir[1]*-1))

        if self.tick > self.ticks_para_moverse:
            self.tanque.change_state (StandingStill(self.tanque))
