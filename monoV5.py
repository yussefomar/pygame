import pygame
import time

# Configuración inicial
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
clock = pygame.time.Clock()

# Clase Fondo
class Fondo(pygame.sprite.Sprite):
    def __init__(self, ruta, posx, posy, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.carga = pygame.image.load(ruta).convert()
        self.superficie = pygame.transform.scale(self.carga, (width, height))
        self.posx = posx
        self.posy = posy

# Cargar el fondo
fondo = Fondo("imagenesmono/fondomonito.png", 0, 0, ANCHO_VENTANA, ALTO_VENTANA)

class Donkingkong(pygame.sprite.Sprite):
    def __init__(self, ruta, color, posx, posy, width, height,velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.carga = pygame.image.load(ruta).convert()
        self.carga.set_colorkey(color)
        self.superficie = pygame.transform.scale(self.carga, (width, height))
        self.velocidad=velocidad
        self.posx = posx
        self.posy = posy
        self.velocidad=velocidad

    def update(self):
        """Actualiza la posición del personaje basado en teclas presionadas."""
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.posx = self.posx - self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.posx =self.posx + self.velocidad
        if teclas[pygame.K_UP]:
            self.posy = self.posy - self.velocidad
        if teclas[pygame.K_DOWN]:
            self.posy = self.posy +self.velocidad
            
# Crear personaje
velocidad=5
pos_x_don=35
pos_y_don=110
ancho=80
alto=80
donkingkong = Donkingkong("imagenesmono/monito.png", COLOR_NEGRO, pos_x_don, pos_y_don, ancho, alto,velocidad)

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(60)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False

        

    # Actualizar la posición del personaje
    donkingkong.update()

    # Dibujar en la ventana
    ventana.blit(fondo.superficie, (fondo.posx, fondo.posy))
    ventana.blit(donkingkong.superficie, (donkingkong.posx, donkingkong.posy))

    pygame.display.flip()

pygame.quit()
