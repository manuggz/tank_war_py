# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from os.path import join


class SpriteSheet(object):
    """description of class"""

    def __init__ (self, path, colorkey, filas, cols):
        self.create_tiles (path, colorkey, filas, cols)

    def create_tiles (self, path, colorkey, filas, cols):
        "Genera dos listas con cuadros de animación 'recortando' una grilla"
        
        image, rect = self.load_image (path, colorkey)
        self.tiles = self.tile_image (image, filas, cols)
        del image

    def get_rect (self):
        return self.tiles [0].get_rect ()

    def get_frame(self, index):
        "Informa que cuadro debe ser mostrado"
        
        return self.tiles[index]

    def tile_image (self, image, filas, cols):
        "Genera una lista con los cuadros de animación en una grilla"
    
        tile_w = image.get_width () / cols
        tile_h = image.get_height () / filas
        tiles = []

        for c in xrange (cols):
            for r in xrange (filas):
                rect = c * tile_w , r * tile_h , tile_w, tile_h
                tiles.append (image.subsurface(rect).copy ())
    
        return tiles
    
    def load_image (self, name, colorkey = None):
        "Carga una imagen generando una superficie"
        
        fullname = join ('data', name)
    
        try:
            image = pygame.image.load (fullname)
        except pygame.error, message:
            print "Cannot load image: ", fullname
            raise SystemExit, message
    
        if colorkey is not None:
            image = image.convert ()
            if colorkey is -1:
                colorkey = image.get_at ((0, 0))
        
            image.set_colorkey (colorkey, RLEACCEL)
        else:
            if image.get_alpha () is None:
                image = image.convert ()
            else:
                image = image.convert_alpha ()
    
        return image, image.get_rect ()

    def draw_frame (self, dst, index, x, y):
        "Imprime sobre 'dst' un cuadro de animacion arbitrario indicado por 'index'"
        # Optimizar .coinvert() cahceando
        dst.blit (self.tiles [index], (x, y))

    def agregar_tiles(self, path, colorkey, filas, cols):
        "Genera dos listas con cuadros de animación 'recortando' una grilla"

        image, rect = self.load_image (path, colorkey)
        self.tiles+=self.tile_image (image, filas, cols)
