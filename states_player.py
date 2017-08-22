# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

#from rectangulos import Zona
#from NinjaSound_states import Matar
#from engine.rectangulos import Zona

#from animacion import Animacion
from os.path import join

class State:
    "Representación abstracta de un estado de personaje"
    
    def __init__ (self, player):
        "\param player Player "
        self.player     = player
                            
    def update (self):
        pass



class StandingStill(State):
    "Representa el estado 'parado'"
    
    def __init__ (self, player):
        "Inicia el estado"
        State.__init__ (self, player)

        if self.player.face_direction == "top":
            self.player.animacion.set_frames([14*12])
        elif self.player.face_direction == "bottom":
            self.player.animacion.set_frames([14*12 + 5])
        elif self.player.face_direction == "left":
            self.player.animacion.set_frames([17*12 + 2])
        elif self.player.face_direction == "right":
            self.player.animacion.set_frames([19*12 +3])


    def update (self,keys):

        if keys[K_UP]:
            self.player.change_state (MovingTop(self.player))
        elif keys[K_DOWN]:
            self.player.change_state (MovingBottom(self.player))
        elif keys[K_RIGHT]:
            self.player.change_state (MovingRight (self.player))
        elif keys[K_LEFT] :
            self.player.change_state (MovingLeft(self.player))
        
        if keys[K_a]:
            self.player.disparar()        

class MovingRight (State):
    "Controla al personaje mientras corre por el escenario"
    
    def __init__ (self, player):
        State.__init__ (self, player)
        self.player.set_face_direction('right')
        self.player.animacion.set_frames([15*12 + 2,15*12 + 3,15*12 + 4,15*12 + 5,15*12 + 6,15*12 + 7,15*12 + 8])

    def update (self,keys):
                     
        if keys[K_RIGHT]: 
            self.player.move_ip (self.player.get_velocidad_movimiento(), 0)
        else:
            self.player.change_state (StandingStill(self.player))

        if keys[K_a]:
            self.player.disparar()        

class MovingLeft(State):
    "Controla al personaje mientras corre por el escenario"
    
    def __init__ (self, player):
        State.__init__ (self, player)
        self.player.set_face_direction('left')
        self.player.animacion.set_frames([16*12 + 2,16*12 + 3,16*12 + 4,16*12 + 5,16*12 + 6,16*12 + 7,16*12 + 8])

    def update (self,keys):
                     
        if keys[K_LEFT]: 
            self.player.move_ip (-self.player.get_velocidad_movimiento(), 0)
        else:
            self.player.change_state (StandingStill(self.player))
        if keys[K_a]:
            self.player.disparar()        

class MovingTop (State):
    "Controla al personaje mientras corre por el escenario"
    
    def __init__ (self, player):
        State.__init__ (self, player)
        self.player.set_face_direction('top')
        self.player.animacion.set_frames([15*12,16*12,17*12,18*12,19*12,20*12,21*12])

    def update (self,keys):
                     
        if keys[K_UP]: 
            self.player.move_ip (0, -self.player.get_velocidad_movimiento())
        else:
            self.player.change_state (StandingStill(self.player))
        if keys[K_a]:
            self.player.disparar()        

class MovingBottom(State):
    "Controla al personaje mientras corre por el escenario"
    
    def __init__ (self, player):
        State.__init__ (self, player)
        self.player.set_face_direction('bottom')
        self.player.animacion.set_frames([15*12 +1,16*12+1,17*12+1,18*12+1,19*12+1,20*12+1,21*12+1])

    def update (self,keys):
                     
        if keys[K_DOWN]: 
            self.player.move_ip (0, self.player.get_velocidad_movimiento())
        else:
            self.player.change_state (StandingStill(self.player))
        if keys[K_a]:
            self.player.disparar()        
        