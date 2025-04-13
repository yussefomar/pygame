import pygame
import time
from personajes import Mario, Donkingkong,Fondo,Fuego,Barriles,Bloque
from config import ANCHO_VENTANA,ALTO_VENTANA,COLOR_BLANCO,COLOR_NEGRO,FPS
# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
clock = pygame.time.Clock()

# Crear personajees
velocidad=2
pos_x_don=70
pos_y_don=92
ancho=85
alto=95
 
fondo = Fondo("imagenesmono/hojasprite.png", COLOR_NEGRO, 0, 0, ANCHO_VENTANA, ALTO_VENTANA,velocidad)
donkingkong = Donkingkong("imagenesmono/hojasprite.png", COLOR_NEGRO, pos_x_don, pos_y_don, ancho, alto,velocidad)
mario = Mario("imagenesmono/hojasprite.png",COLOR_NEGRO, 52, 493, 35, 35,velocidad)
fuego = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 386, 35, 35,1)
fuego1 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 320, 523, 35, 35,1)
fuego2 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 520, 463, 35, 35,1)
barriles = Barriles("imagenesmono/hojasprite.png",COLOR_NEGRO, 1, 115, 55, 68,1)
un_bloque=Bloque("imagenesmono/hojasprite.png",COLOR_NEGRO, 6, 552, 52, 18,1)

lista_personajes=[fondo,donkingkong,mario,fuego,fuego1,fuego2,barriles,un_bloque]

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(FPS)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False
 
    for un_personaje in lista_personajes:
        # Actualizar la posición del personaje 
        un_personaje.actualizar_posicion()
        # colision
        mario.colisiona_con(un_personaje)
    
     

    for un_personaje in lista_personajes:
        # Dibujar en la ventana
        ventana.blit(un_personaje.obtener_superficie_actual(), (un_personaje.posx, un_personaje.posy))
        
    
    pygame.display.flip()

pygame.quit()
