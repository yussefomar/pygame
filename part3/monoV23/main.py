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
fuego = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 386, 25, 20,1)
fuego1 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 320, 523, 25, 20,1)
fuego2 = Fuego("imagenesmono/hojasprite.png",COLOR_NEGRO, 520, 463, 25, 20,1)
barriles = Barriles("imagenesmono/hojasprite.png",COLOR_NEGRO, 1, 115, 55, 68,1)

def crear_lista_bloques(cantidad, clase_bloque, imagen, color, inicio_x, inicio_y, ancho, alto, espaciado_x=50, espaciado_y=0, velocidad=1):
    """
    
    Retorna:
      Una lista con las instancias creadas.
    """
    lista = []
    for i in range(cantidad):
        x = inicio_x + i * espaciado_x
        y = inicio_y + i * espaciado_y
        bloque = clase_bloque(imagen, color, x, y, ancho, alto, velocidad)
        lista.append(bloque)
    return lista

lista_bloques = crear_lista_bloques(10, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 6, 552, 52, 18, espaciado_x=50, espaciado_y=0, velocidad=1)
lista_bloques2 = crear_lista_bloques(10, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 509, 547, 52, 18, espaciado_x=50, espaciado_y=-5, velocidad=1)
lista_bloques3 = crear_lista_bloques(14, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 6, 464, 52, 18, espaciado_x=50, espaciado_y=2, velocidad=1)
lista_bloques4 = crear_lista_bloques(14, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 61, 418, 52, 18, espaciado_x=50, espaciado_y=-2, velocidad=1)
lista_bloques5 = crear_lista_bloques(14, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 6, 318, 52, 18, espaciado_x=50, espaciado_y=2, velocidad=1)
lista_bloques6 = crear_lista_bloques(14, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 63, 271, 52, 18, espaciado_x=50, espaciado_y=-2, velocidad=1)
lista_bloques7 = crear_lista_bloques(12, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 4, 190, 52, 18, espaciado_x=50, espaciado_y=0, velocidad=1)
lista_bloques8 = crear_lista_bloques(3, Bloque, "imagenesmono/hojasprite.png", COLOR_NEGRO, 604, 190, 52, 18, espaciado_x=50, espaciado_y=2, velocidad=1)


lista_personajes = [ fondo, donkingkong, mario, fuego, fuego1, fuego2, barriles] + lista_bloques +lista_bloques2 +lista_bloques3 +lista_bloques4 +lista_bloques5+lista_bloques6+lista_bloques7+lista_bloques8
lista_bloques=[]+ lista_bloques +lista_bloques2 +lista_bloques3 +lista_bloques4 +lista_bloques5+lista_bloques6+lista_bloques7+lista_bloques8

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(FPS)  # Mantener 60 FPS
    
    
        
    # Procesa los eventos a través del método de Mario
    mario.procesar_eventos()    
 
    for un_personaje in lista_personajes:
        # Actualizar la posición del personaje 
        un_personaje.actualizar_posicion()
        # colision
       
    mario.colision_bloques(lista_bloques)

    for un_personaje in lista_personajes:
        
        # colision
        mario.colisiona_con(un_personaje)
       

    for un_personaje in lista_personajes:
        # Dibujar en la ventana
        ventana.blit(un_personaje.obtener_superficie_actual(), (un_personaje.posx, un_personaje.posy))
        
   
    
    pygame.display.flip()

pygame.quit()
