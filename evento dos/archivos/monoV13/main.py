import pygame
import time
from personajes import Mario, Donkingkong,Fondo
from config import ANCHO_VENTANA,ALTO_VENTANA,COLOR_BLANCO,COLOR_NEGRO,FPS
# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
clock = pygame.time.Clock()

# Crear personajees
velocidad=5
pos_x_don=35
pos_y_don=110
ancho=80
alto=80
 
fondo = Fondo("imagenesmono/hojasprite.png", COLOR_NEGRO, 0, 0, ANCHO_VENTANA, ALTO_VENTANA,velocidad)
donkingkong = Donkingkong("imagenesmono/hojasprite.png", COLOR_NEGRO, pos_x_don, pos_y_don, ancho, alto,velocidad)
mario = Mario("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 490, 85, 75,velocidad)

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(FPS)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar la posición del personaje  
    mario.actualizar_posicion()
    
    # Dibujar en la ventana
    ventana.blit(fondo.obtener_superficie_actual(), (fondo.posx, fondo.posy))
    ventana.blit(mario.obtener_superficie_actual(), (mario.posx, mario.posy))
    ventana.blit(donkingkong.obtener_superficie_actual(), (donkingkong.posx, donkingkong.posy))

    pygame.display.flip()

pygame.quit()
