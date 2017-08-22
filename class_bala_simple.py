import pygame
from pygame.locals import *
import math
from class_entidad import  Entidad

class BalaSimple(Entidad):
    """Bala Simple que se mueve linealmente hasta colisionar con un 'enemigo' o salir de pantalla"""

    def __init__(self,dir,pos,escena,colisiona_con_enemigos = 1):
        Entidad.__init__ (self,escena,pos[0],pos[1])
        
        self.d_x       = dir[0]
        self.d_y       = dir[1]
        self.acele     = 0
        self.velocidad = 2

        self.rect.center = pos
        self.power = 10
        
        self.colisiona_con_enemigos = colisiona_con_enemigos
        if dir == (1,0): #right
            self.animacion.set_frames([5*12])
        elif dir == (-1,0): #left
            self.animacion.set_frames([4*12])
        elif dir == (0,1): #bottom
            self.animacion.set_frames([6*12])
        elif dir == (0,-1): # top
            self.animacion.set_frames([3*12])
        self.image = self.animacion.get_actual_frame () #actualizamos la imagen que se imprimira

        
    def update(self):

        #self.animacion.advance () #actualizamos la animacion
        #self.image = self.animacion.get_actual_frame () #actualizamos la imagen que se imprimira

        self.velocidad += self.acele

        self.rect.move_ip(self.d_x*self.velocidad,self.d_y*self.velocidad)

        if not self.screen_rect.colliderect(self.rect) :
            self.kill();
        
        sprite_c = None 
        if self.colisiona_con_enemigos:
            sprite_c = pygame.sprite.spritecollideany(self,self.escena.enemigos)
        else:
            sprite_c = pygame.sprite.spritecollideany(self,self.escena.heroes)

        if sprite_c:
            sprite_c.herir(self.power)
            self.kill()
        
        bloques_gropup_c = self.escena.nivel.collide(self.rect)

        if bloques_gropup_c:
            self.kill()


