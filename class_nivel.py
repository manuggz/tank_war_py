# -*- coding: utf-8 -*-
import pygame

from os.path import join        #compatibilidad de paths con distintos sistemas
from class_animacion import Animacion #Para dibujar desde una grilla los bloques, los cuales estan en una sola grilla
from glob import glob           #para saber el numero maximo de niveles

TILE_SIZE  = 32
TILES_NO_PINTABLE = [0]
N_FILAS = 19
N_COLS = 12
class Nivel:
    "Representacion abstracta del entorno con el que interactua el player"
    
    def __init__ (self,parent_escena,numero_nivel):
        self.parent_escena = parent_escena #referencia a quien lo necesita, este puede ser cualquier escena
                
        self.datos_nivel = [
            11*12 +  1,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,1,0,0,0,11*12 +  1,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,11*12 +  1,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,11*12 +  1,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            ]

        self.screen = pygame.display.get_surface().convert()

    def draw(self, dst):
        "Imprime todo el escenario sobre la superficie 'dst'"
        dst.blit (self.screen,(0,0))
    
    def collideany(self,rect):
        # TOP LEFT
        valor_indice  = self.get_valor_tile_at_xy(rect.x,rect.y)

        if valor_indice not in TILES_NO_PINTABLE:
            return (valor_indice,(rect.x,rect.y))

        # TOP RIGHT
        valor_indice  = self.get_valor_tile_at_xy(rect.x + rect.w - 1,rect.y)

        if valor_indice not in TILES_NO_PINTABLE:
            return (valor_indice,(rect.x + rect.w - 1,rect.y))

        # BOTTOM LEFT
        valor_indice  = self.get_valor_tile_at_xy(rect.x,rect.y + rect.h - 1)

        if valor_indice not in TILES_NO_PINTABLE:
            return (valor_indice,(rect.x,rect.y + rect.h - 1))

        # BOTTOM RIGHT
        valor_indice  = self.get_valor_tile_at_xy(rect.x + rect.w - 1,rect.y + rect.h - 1)

        if valor_indice not in TILES_NO_PINTABLE:
            return (valor_indice,(rect.x + rect.w - 1,rect.y + rect.h - 1))
        
        return False
            
    def collide(self,rect):

        group_collide = []
        
        # TOP LEFT
        valor_indice  = self.get_valor_tile_at_xy(rect.x,rect.y)

        if valor_indice not in TILES_NO_PINTABLE:
            group_collide.append((valor_indice,(rect.x,rect.y)))

        # TOP RIGHT
        valor_indice  = self.get_valor_tile_at_xy(rect.x + rect.w - 1,rect.y)

        if valor_indice not in TILES_NO_PINTABLE:
            group_collide.append((valor_indice,(rect.x + rect.w - 1,rect.y)))

        # BOTTOM LEFT
        valor_indice  = self.get_valor_tile_at_xy(rect.x,rect.y + rect.h -1)

        if valor_indice not in TILES_NO_PINTABLE:
            group_collide.append((valor_indice,(rect.x,rect.y + rect.h - 1)))

        # BOTTOM RIGHT
        valor_indice  = self.get_valor_tile_at_xy(rect.x + rect.w - 1,rect.y + rect.h - 1)

        if valor_indice not in TILES_NO_PINTABLE:
            group_collide.append((valor_indice,(rect.x + rect.w - 1,rect.y + rect.h - 1)))
        
        return group_collide

    def get_valor_tile_at_xy(self,x,y):
        f   =  y  / TILE_SIZE
        c   =  x / TILE_SIZE
        indice        = f*N_COLS+c
        return self.datos_nivel[indice]

    def parsear_datos_nivel(self):
        "Esta funcion crea el fondo y agrega los sprites al nivel PD: todo a la vez para ahorrar tiempo ya que de una vez en los for se comprueba el cod del tile"
        #fondo=pygame.image.load(join("data","nivel","tiles","fondo1.jpg"))
        #self.screen.blit (fondo, (0, 0))
        
        
        for fila in range(N_FILAS):
            for columna in range(N_COLS):
                # calculo de la posición del tile
                x = columna * TILE_SIZE
                y = fila    * TILE_SIZE
                
                indice=self.datos_nivel[fila*N_COLS+columna]
                if indice not in TILES_NO_PINTABLE:
                    self.parent_escena.spritesheet.draw_frame (self.screen, indice, x, y)
                #elif indice == -1: # si es un tile para un enemigo
                    #pass
                    #self.parent_escena.add_sprite("ninja sonido",(x,y),500)
