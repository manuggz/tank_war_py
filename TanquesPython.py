# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


from class_juego import Game         #Clase base Game
from class_escena import Escena        #Clase base Escena
from class_fps import Fps           #Clase Fps que solo muestra los fps en pantalla
from class_nivel import Nivel       # Clase para adiministrar el envolvente
from class_player import Player         #Clase Player
from states_player import StandingStill #Estado inicial donde cae el personaje de arriba de la pantalla

from class_tanque_simple_enemigo import TanqueSimpleEnemigo

import states_tanque_simple_enemigo
#from engine.texto import Texto
#from engine.efectos import Efecto
#from engine.animacion import Animacion
from os.path import join
from class_spritesheet import SpriteSheet

class TanquesPython (Escena):
    "Representa un escenario con plataformas y un personaje que se puede controlar con el teclado"

    
    def __init__ (self, game):
        "Inicia el nivel con algunas plataformas y el personaje"        
        Escena.__init__ (self)

        self.game = game

        self.spritesheet = SpriteSheet('tiles_tanques.png',None,12,22)

        self.sonido_disparar             = pygame.mixer.Sound(join('data',"ShotFiring.wav"))
        #pygame.mixer.Sound.set_volume(self.sonido_disparar,0.5)

        self.sonido_disparo_golpea_tanke = pygame.mixer.Sound(join('data',"ShellExplosion.wav"))
        #pygame.mixer.Sound.set_volume(self.sonido_disparo_golpea_tanke,0.5)

        self.sonido_tanke_explosion      = pygame.mixer.Sound(join('data',"TankExplosion.wav"))
        #pygame.mixer.Sound.set_volume(self.sonido_tanke_explosion,0.5)

        self.sonido_tanke_idle           = pygame.mixer.Sound(join('data',"EngineIdle.wav"))
        #pygame.mixer.Sound.set_volume(self.sonido_tanke_idle,0.1)

        self.sonido_tanke_driving        = pygame.mixer.Sound(join('data',"EngineDriving.wav"))
        #pygame.mixer.Sound.set_volume(self.sonido_tanke_driving,0.1)

        #CONTENEDORES DE LOS SPRITES
        self.sprites  = pygame.sprite.OrderedUpdates()
        self.enemigos = pygame.sprite.Group()
        self.heroes   = pygame.sprite.Group()
        
        self.pop_mnsg_fin_nivel = False

        self.fps = Fps (game.clock) #para mostrar los fps del juego

        self.nivel_actual = 1
        self.nivel     = None
        self.establecer_nivel(1)

        self.sprites.add (self.fps)
    
    def add_sprite(self,cod,*args):
        "Anyade un enemigo a el juego:NS: es para anyadir un Ninja del sonido con argumenmtos pasados por args"
        nuevo=None
                    
        if nuevo:
            self.sprites.add (nuevo)
        else:
            print "Warning: cod:\"" + str(cod) + "\" No reconocido"
    
    def get_rect_screen(self):
        return self.game.screen.get_rect()       
        
    def establecer_nivel(self,numero_nivel):
        "aumenta  la etapa y si es 4 el nivel"

        self.nivel_actual = numero_nivel
        self.nivel = Nivel(self,self.nivel_actual)
        self.nivel.parsear_datos_nivel();

        self.player1 = Player(self,32*3,32*3)
        self.player1.change_state(StandingStill(self.player1));
        self.heroes.add(self.player1)
        self.sprites.add(self.player1)

        tanque1 = TanqueSimpleEnemigo(self,250,50)
        tanque1.change_state(states_tanque_simple_enemigo.StandingStill(tanque1));
        self.enemigos.add(tanque1)
        self.sprites.add(tanque1)

        tanque2 = TanqueSimpleEnemigo(self,350,50)
        tanque2.change_state(states_tanque_simple_enemigo.StandingStill(tanque2));
        self.enemigos.add(tanque2)
        self.sprites.add(tanque2)

        tanque3 = TanqueSimpleEnemigo(self,100,50)
        tanque3.change_state(states_tanque_simple_enemigo.StandingStill(tanque3));
        self.enemigos.add(tanque3)
        self.sprites.add(tanque3)

        #self.effect_txt_nivel=Texto("Nivel %d"%(self.num_nivel),(640/2,480/2),74,(0,255,0))
        #self.sprites.add(self.effect_txt_nivel,Efecto(640/2,480/2,Animacion (join("sfx_imgs","sfx_azul1.bmp"), -1, 1, 3),[0,0,1,1,2,2]))


        #Esto es para borrar el anterior fondo y dibujar el siguiente
        self.create_background()

        pygame.mixer.music.load(join('data','BackgroundMusic.wav'))
        #pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        
    def update (self):
        "Actualiza la logica de la escena"
        self.sprites.update()

        if not self.enemigos.sprites() and not self.pop_mnsg_fin_nivel:
            self.pop_mnsg_fin_nivel = True
            #self.sprites.add(Texto("Nivel Completado",(640/2,480/2),74,(0,255,0),self.establecer_nivel))

    
    def create_background (self):
        self.background = pygame.display.get_surface ().convert ()
        self.nivel.draw (self.background)
    
    def add_bala(self,bala):
        self.sprites.add(bala)

    def draw (self, screen):
        "Imprime todos los objetos en pantalla"
        self.sprites.clear(screen, self.background)
        #self.nivel.draw (screen)
        #self.sprites.draw(screen)
        #pygame.display.flip()
        pygame.display.update (self.sprites.draw (screen))
        
    def entire_draw (self, screen):
        screen.blit (self.background, (0, 0))


    def terminate (self):
        "Libera los recursos de la escena"
        pass

    def detectar_colision_enemigos(sprite,self):
        for enemigo in self.enemigos:
            if pygame.sprite.collide_rect(self.sprite.rect,enemigo.rect):

                #enemigo.rect.clip(self.rect) #Rectangulo resultado de la interseccion de los 2 rectangulos
                
                return enemigo
                #enemigo.herir(20,rect_coli_real.right,rect_coli_real.centery)
if __name__ == '__main__':
    game = Game ('Tanques Python', 'Manuel Gonzalez',(640,480),bpp=16,mode=HWSURFACE|DOUBLEBUF|ANYFORMAT,fps = 100)
    plataform = TanquesPython (game)
    game.change_scene (plataform)
    game.run ()
    pygame.quit()
