# -*- coding: utf-8 -*-

#////////////////////////////////
#IMPORTACIONES BASICAS
import pygame
from pygame.locals import *
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from os.path import join                 #para ofrecer paths multisistema
from class_personaje import Personaje         #Clase base de los Sprites

from class_bala_simple import BalaSimple
import states_player
#from animacion import Animacion          #Para controlar las animaciones del player
#from engine.rectangulos import Zona
#from engine.NinjaSound_states import Normal


#CONSTANTES

class Player(Personaje):
    "Reprensenta a un personaje animado que controla el jugador mediante el teclado"
    
    def __init__ (self, escena,position_x,position_y):
        "Carga los recursos principales para comenzar el juego"        
        Personaje.__init__ (self, escena,position_x,position_y)        
        
                        
        self.vidas      = 3
        self.puntaje    = 0
        
        self.tick_para_disparar = 0
        self.cooldown_disparo   = 20
        self.esta_en_cd_disparo = False
        self.state = None

    def herir(self,cantidad):
        if Personaje.herir (self,cantidad):
            #self.esta_intocable=True
            pygame.mixer.Sound.play(self.escena.sonido_disparo_golpea_tanke)

    def get_rect_colision(self):
        return self.rect
    
    def update (self):
        "Actualiza el comportamiento del personaje"

        keys=pygame.key.get_pressed()
        self.state.update (keys) #actualizamos el estado
        self.animacion.advance () #actualizamos la animacion
        self.image = self.animacion.get_actual_frame () #actualizamos la imagen que se imprimira

        if self.esta_en_cd_disparo:
            self.tick_para_disparar += 1
            if self.tick_para_disparar > self.cooldown_disparo:
                self.tick_para_disparar = 0
                self.esta_en_cd_disparo = False

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

        if self.state:
            if isinstance(self.state,states_player.StandingStill):
                pygame.mixer.Sound.stop(self.escena.sonido_tanke_idle)
            else:
                pygame.mixer.Sound.stop(self.escena.sonido_tanke_driving)

        self.state = state
        
        if isinstance(self.state,states_player.StandingStill):
            pygame.mixer.Sound.play(self.escena.sonido_tanke_idle,-1)
        else:
            pygame.mixer.Sound.play(self.escena.sonido_tanke_driving,-1)


    def disparar(self):
        
        if self.esta_en_cd_disparo: return False

        dir = self.get_v_dir_from_face_dir(self.face_direction)

        nueva_bala = BalaSimple(dir,self.rect.center,self.escena)
        self.escena.add_bala(nueva_bala)
        self.esta_en_cd_disparo = True

        pygame.mixer.Sound.play(self.escena.sonido_disparar)
        return True

    def get_velocidad_movimiento(self):
        return 1;

    def move (self, x, y,forzar=False):
        "Intenta desplazar al personaje a una posición absoluta (x, y) sin exceder los bordes de pantalla"
        
        #ancho_screen,alto_screen=pygame.display.get_surface().get_size()
        
        
        if x < 0:
            return False
            #x = 0       
        elif x + self.rect.w > self.screen_rect.w:
            return False
            #x = self.screen_rect.w - self.rect.w
        elif y < 0:
            return False
            #y = 0
        elif y + self.rect.h > self.screen_rect.h:
            #y = self.screen_rect.h - self.rect.h
            return False


        #coordenadas del hotspot -pto de referencia-  en la pantalla, para detectar colicion con el entorno
        
        recttemp1 = self.rect.copy()

        self.rect.x = x 
        self.rect.y = y 
        
        enemigo_c = pygame.sprite.spritecollideany(self,self.escena.enemigos)

        if enemigo_c:
            self.rect = recttemp1
            return False

        #bloques_gropup_c = self.escena.nivel.collideany(self.rect)

        if self.escena.nivel.collideany(self.rect):
            self.rect = recttemp1
            return False

        self.x = x 
        self.y = y

        return True
        
    def move_ip (self, dx, dy):
        "Realiza un desplazamiento del personaje en el escenario"
        
        return self.move (self.x + dx, self.y + dy)


