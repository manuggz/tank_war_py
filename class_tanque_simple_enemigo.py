# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from random import randint

from os.path import join                 #para ofrecer paths multisistema
from class_personaje import Personaje         #Clase base de los Sprites

from class_bala_simple import BalaSimple

class TanqueSimpleEnemigo(Personaje):
    """Tanque que se mueve aleatoriamente en el mapa"""

    def __init__ (self, escena,position_x,position_y):
        "Carga los recursos principales para comenzar el juego"        
        Personaje.__init__ (self,escena,position_x,position_y)        
        
        self.esta_intocable=False #Esta variable controla el efecto a la imagen a mostrar y si se puede herir al personaje
        self.delay_proteccion=0
                        
        self.nivel_hp = 100

        self.tick_disparar = 0
        self.ticks_para_disparar = randint(100,115)
                

    def herir(self,cantidad):
        if Personaje.herir (self,cantidad):
            if not self.nivel_hp:
                self.kill()
                pygame.mixer.Sound.play(self.escena.sonido_tanke_explosion)
            else:
                pygame.mixer.Sound.play(self.escena.sonido_disparo_golpea_tanke)

    def get_rect_colision(self):
        return self.rect
    
    def update (self):
        "Actualiza el comportamiento del personaje"

        #keys=pygame.key.get_pressed()
        self.state.update () #actualizamos el estado
        self.animacion.advance () #actualizamos la animacion
        self.image = self.animacion.get_actual_frame () #actualizamos la imagen que se imprimira

        self.tick_disparar += 1
        if self.tick_disparar > self.ticks_para_disparar:
            self.disparar()
            self.tick_disparar = 0

        if self.esta_intocable:
            self.image.set_alpha(100) #aplicamos el efecto de desvanecido
            self.delay_proteccion+=1 #aumentamos el contador que controla el tiempo protegido

            #SI SE ALCANZO EL TIEMPO MAXIMO PARA ESTAR PROTEGIDO
            if self.delay_proteccion>100:
                self.delay_proteccion=0
                self.esta_intocable=False
        else:
            self.image.set_alpha(255)
        
    def change_state (self, state):
        "cambia el estado del personaje"
        self.state = state


    def disparar(self):
        
        dir = self.get_v_dir_from_face_dir(self.face_direction)
        nueva_bala = BalaSimple(dir,self.rect.center,self.escena,0)
        self.escena.add_bala(nueva_bala)

    def get_velocidad_movimiento(self):
        return 1;

    def move (self, x, y,forzar=False):
        "Intenta desplazar al personaje a una posición absoluta (x, y) sin exceder los bordes de pantalla"
        
        #ancho_screen,alto_screen=pygame.display.get_surface().get_size()
        
        
        if x < 0:
            return False
        elif x + self.rect.w > self.screen_rect.w:
            #x = self.screen_rect.w - self.rect.w
            return False
        elif y < 0:
            #y = 0
            return False
        elif y + self.rect.h > self.screen_rect.h:
            #y = self.screen_rect.h - self.rect.h
            return False

        
        recttemp1 = self.rect.copy()

        self.rect.x = x 
        self.rect.y = y 

        tanque_c = pygame.sprite.spritecollideany(self,self.escena.heroes)

        if tanque_c:
            self.rect = recttemp1
            return False

        #bloques_gropup_c = self.escena.nivel.collideany(self.rect)

        if self.escena.nivel.collideany(self.rect):
            self.rect = recttemp1
            return False

        #coordenadas del hotspot -pto de referencia-  en la pantalla, para detectar colicion con el entorno
        self.x = x 
        self.y = y
        return True
        
    def move_ip (self, dx, dy):
        "Realiza un desplazamiento del personaje en el escenario"
        
        return self.move (self.x + dx, self.y + dy)

    def set_face_direction(self,d):        
        # 1 - TOP , 2 - RIGHT , 3 - BOTTOM , 4 - LEFT
        self.face_direction = d

    

