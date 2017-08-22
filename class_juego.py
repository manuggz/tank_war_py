# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


class Game:
    "Gestiona el bucle principal de un videojuego junto con el intercambio de escenas"
    
    def __init__ (self, title, author = None, size=(640,480), bpp = 16, mode = SWSURFACE, debug = False, fps = 70):
        "Inicia la ventana principal y los recursos basicos"
        
        pygame.init ()
        self.screen = pygame.display.set_mode (size, mode, bpp)
        self.clock = pygame.time.Clock ()
        self.size=size
        
        if author:
            caption = title + ' por ' + author
        else:
            caption = title
        
        pygame.display.set_caption (caption)
        self.quit = False
        self.fps = fps
        self.scene = None
        pygame.mouse.set_visible(False)

    def change_scene (self, new_scene):
        "Intercambia la escena actual del juego"
        
        if self.scene:
            self.scene.terminate ()
        self.scene = new_scene
        self.scene.entire_draw (self.screen)
        pygame.display.flip ()

    def run (self):
        "Inicia el bucle principal del programa"

        while not self.quit:
            
            for event in pygame.event.get ():
                if event.type == QUIT:
                    self.do_quit ()
            
            self.scene.update ()
            self.scene.draw (self.screen)
            self.clock.tick (self.fps)
        
        if self.scene:
            self.scene.terminate ()

    def do_quit (self):
        "Termina de ejecutar el programa"
        
        self.quit = True
