# -*- coding: utf-8 -*-

class Escena:
    "Representa un estado o escena del videojuego (menu, introduccion, etc.)"
    
    def __init__ (self):
        pass
    
    def update (self):
        "Actualización lógica"
        
        pass
    
    def draw (self, screen):
        "Actualización de pantalla o gráfica"
        
        pass

    def entire_draw (self, screen):
        "Imprime la escena completa sobre screen. Se invoca solamente al ingresar en la escena"
        
        pass

    def terminate (self):
        "Debe liberar los recursos solicitados por __init__"
        
        pass
