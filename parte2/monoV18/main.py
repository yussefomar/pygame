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
mario = Mario("imagenesmono/hojasprite.png",COLOR_NEGRO, 52, 493, 70, 70,velocidad)
fuego = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 386, 35, 35,1)
fuego1 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 320, 523, 35, 35,1)
fuego2 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 520, 463, 35, 35,1)
barriles = Barriles("imagenesmono/hojasprite.png",COLOR_NEGRO, 1, 115, 55, 68,1)
un_bloque=Bloque("imagenesmono/hojasprite.png",COLOR_NEGRO, 5, 542, 60, 32,1)

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(FPS)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar la posición del personaje  
    mario.actualizar_posicion()
    donkingkong.actualizar_posicion()
    fuego.actualizar_posicion()
    fuego1.actualizar_posicion()
    fuego2.actualizar_posicion()
    fondo.actualizar_posicion()
    un_bloque.actualizar_posicion()
    
    mario.colisiona_con(fuego1)
      
    mario.colisiona_con(donkingkong)
      
    mario.colisiona_con(un_bloque)
      
    
    # Dibujar en la ventana
    ventana.blit(fondo.obtener_superficie_actual(), (fondo.posx, fondo.posy))
    ventana.blit(un_bloque.obtener_superficie_actual(), (un_bloque.posx, un_bloque.posy))
    ventana.blit(barriles.obtener_superficie_actual(), (barriles.posx, barriles.posy))
    ventana.blit(mario.obtener_superficie_actual(), (mario.posx, mario.posy))
    ventana.blit(fuego.obtener_superficie_actual(), (fuego.posx, fuego.posy))
    ventana.blit(fuego1.obtener_superficie_actual(), (fuego1.posx, fuego1.posy))
    ventana.blit(fuego2.obtener_superficie_actual(), (fuego2.posx, fuego2.posy))
    ventana.blit(donkingkong.obtener_superficie_actual(), (donkingkong.posx, donkingkong.posy))

    pygame.display.flip()

pygame.quit()
