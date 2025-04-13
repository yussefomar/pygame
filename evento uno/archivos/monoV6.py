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
    def __init__(self, rutas, color, posx, posy, width, height,velocidad):
        pygame.sprite.Sprite.__init__(self)
        #self.carga = pygame.image.load(ruta).convert()
        #self.carga.set_colorkey(color)
        #self.superficie = pygame.transform.scale(self.carga, (width, height))
        self.velocidad=velocidad
        self.posx = posx
        self.posy = posy
        self.velocidad=velocidad

         # Diccionario para almacenar los sprites
        self.superficies = {}
        self.cargar_superficies(rutas, color, width, height)

        # Superficie por defecto (reposo)
        self.superficie = self.superficies["reposo"]

    def cargar_superficie(self, ruta, color, width, height):
        """Carga una superficie, aplica transparencia y escala."""
        superficie = pygame.image.load(ruta).convert()
        superficie.set_colorkey(color)  # Hacer transparente el fondo
        return pygame.transform.scale(superficie, (width, height))

    def cargar_superficies(self, rutas, color, width, height):
        """Carga las superficies y genera automáticamente las reflejadas."""
        for movimiento, ruta in rutas.items():
            self.superficies[movimiento] = self.cargar_superficie(ruta, color, width, height)

        # Genera automáticamente las reflejadas
        self.superficies["derecha"] = pygame.transform.flip(self.superficies["izquierda"], True, False)
        self.superficies["abajo"] = pygame.transform.flip(self.superficies["subir"], False, True)

    

    def update(self):
        """Actualiza la posición del personaje basado en teclas presionadas."""
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.posx = self.posx - self.velocidad
            self.superficie = self.superficies["izquierda"]
        elif teclas[pygame.K_RIGHT]:
            self.posx =self.posx + self.velocidad
            self.superficie = self.superficies["derecha"]
        elif teclas[pygame.K_UP]:
            self.posy = self.posy - self.velocidad
            self.superficie = self.superficies["subir"]
        elif teclas[pygame.K_DOWN]:
            self.posy = self.posy +self.velocidad
            self.superficie = self.superficies["abajo"]
        else:
            self.superficie = self.superficies["reposo"]  # Si no se mueve, usa la imagen de reposo
            
# Crear personaje
velocidad=5
pos_x_don=35
pos_y_don=110
ancho=80
alto=80
# Diccionario con las rutas de los sprites organizados por acción
rutas_mono = {
    "reposo": "imagenesmono/monito.png",
    "izquierda": "imagenesmono/izquierdamono.png",
    "subir": "imagenesmono/arribamono.png"
}
donkingkong = Donkingkong(rutas_mono, COLOR_NEGRO, pos_x_don, pos_y_don, ancho, alto,velocidad)

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
