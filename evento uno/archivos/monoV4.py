import pygame
import time
ancho=800
alto=600
color_blanco=(255,255,255)
color_negro=(0,0,0)
pygame.init()
clock = pygame.time.Clock()
# Creamos una superficie 
ventana = pygame.display.set_mode((ancho,alto))

class Fondo(pygame.sprite.Sprite):
    def __init__(self,ruta,posx,posy, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.carga = pygame.image.load(ruta) 
        self.superficie = pygame.transform.scale(self.carga, (width, height))
        
         
        self.posx=posx
        self.posy=posy
         
         
        self.ancho=width
        self.alto=height
        
# cargamos el fondo y una imagen (se crea objetos "Surface"
#antes
#fondo = pygame.image.load("imagenesmono/fondomonito.png").convert()
#fondo = pygame.transform.scale(fondo, (ancho, alto))
#despues
fondo= Fondo("imagenesmono/fondomonito.png",0,0,ancho,alto)


donkingkong = pygame.image.load("imagenesmono/monito.png").convert()
donkingkong.set_colorkey(color_negro)

posicion_x_donking=35
posicion_y_donking=110
velocidad = 5


jugando = True
while jugando:
    
     
    clock.tick(60)   #60 FPS para movimiento fluido
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:  # Evento de cerrar ventana
            jugando = False
            
    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posicion_x_donking =posicion_x_donking- velocidad  # Mover a la izquierda (restar píxeles)
    if teclas[pygame.K_RIGHT]:
        posicion_x_donking =posicion_x_donking +velocidad  # Mover a la derecha (sumar píxeles)
    if teclas[pygame.K_UP]:
        posicion_y_donking = posicion_y_donking - velocidad  # Mover hacia arriba (restar píxeles)
    if teclas[pygame.K_DOWN]:
        posicion_y_donking = posicion_y_donking +velocidad  # Mover hacia abajo (sumar píxeles)

    #dibuja en la ventana las superficies cargadas
    #antes
    #########ventana.blit(fondo, (0, 0))
    #despues
    ventana.blit(fondo.superficie, (fondo.posx, fondo.posy))
    #######
    ventana.blit(donkingkong , (posicion_x_donking, posicion_y_donking))
    pygame.display.flip()

   
    
pygame.quit()


 

 
