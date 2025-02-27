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
    def __init__(self, ruta, posx, posy, scale_ancho, scale_alto):
        pygame.sprite.Sprite.__init__(self)
        self.hoja_sprite = pygame.image.load(ruta).convert()
        #self.superficie = pygame.transform.scale(self.carga, (ancho, alto))
        self.posx = posx
        self.posy = posy
        self.scale_ancho=scale_ancho
        self.scale_alto=scale_alto
        self.cuadros_animacion = {
            0: {"x": 10, "y": 345, "sprite_ancho": 230  , "sprite_alto": 272}
        }
    def obtener_sprite_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.scale_ancho, self.scale_alto))
        return  superficie_fondo_escalado

# Cargar el fondo
fondo = Fondo("imagenesmono/hojasprite.png", 0, 0, ANCHO_VENTANA, ALTO_VENTANA)


class Mario(pygame.sprite.Sprite):
    def __init__(self, ruta,color, posx, posy, scale_ancho, scale_alto):
        pygame.sprite.Sprite.__init__(self)
        self.hoja_sprite = pygame.image.load(ruta).convert()
        #self.superficie = pygame.transform.scale(self.carga, (ancho, alto))
        self.posx = posx
        self.posy = posy
        self.scale_ancho=scale_ancho
        self.scale_alto=scale_alto
        self.frame = 0
        self.color=color
        self.num_frames=3
       
        self.cuadros_animacion = {
            0: {"x": 10, "y": 200, "sprite_ancho": 20  , "sprite_alto": 40},
            1: {"x": 30, "y": 200, "sprite_ancho": 20  , "sprite_alto": 40},
            2: {"x": 50, "y": 200, "sprite_ancho": 20  , "sprite_alto": 40}
        }
    def obtener_sprite_actual(self):
        clip = self.cuadros_animacion[self.frame  ]
        superficie_mario=self.hoja_sprite.subsurface((clip["x"], clip["y"], clip["sprite_ancho"], clip["sprite_ancho"]))
        superficie_mario.set_colorkey(self.color)
        superficie_mario_escalado=pygame.transform.scale(superficie_mario, (self.scale_ancho, self.scale_alto))
        return  superficie_mario_escalado
    
    def actualizar_frame(self):
        self.frame += 1
        if self.frame >= self.num_frames  :
            self.frame = 0

class Donkingkong(pygame.sprite.Sprite):
    def __init__(self, rutas, color, posx, posy, ancho, alto,velocidad):
        pygame.sprite.Sprite.__init__(self)
        #self.carga = pygame.image.load(ruta).convert()
        #self.carga.set_colorkey(color)
        #self.superficie = pygame.transform.scale(self.carga, (ancho, alto))
        self.velocidad=velocidad
        self.posx = posx
        self.posy = posy
        self.velocidad=velocidad

         # Diccionario para almacenar los sprites
        self.superficies = {}
        self.cargar_superficies(rutas, color, ancho, alto)

        # Superficie por defecto (reposo)
        self.superficie = self.superficies["reposo"]

    def cargar_superficie(self, ruta, color, ancho, alto):
        """Carga una superficie, aplica transparencia y escala."""
        superficie = pygame.image.load(ruta).convert()
        superficie.set_colorkey(color)  # Hacer transparente el fondo
        return pygame.transform.scale(superficie, (ancho, alto))

    def cargar_superficies(self, rutas, color, ancho, alto):
        """Carga las superficies y genera automáticamente las reflejadas."""
        for movimiento, ruta in rutas.items():
            self.superficies[movimiento] = self.cargar_superficie(ruta, color, ancho, alto)

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
# Cargar el fondo
mario = Mario("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 509, 90, 40)

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(60)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False

        

    # Actualizar la posición del personaje
    donkingkong.update()
    mario.actualizar_frame()
    # Dibujar en la ventana
    ventana.blit(fondo.obtener_sprite_actual(), (fondo.posx, fondo.posy))
    ventana.blit(mario.obtener_sprite_actual(), (mario.posx, mario.posy))
    ventana.blit(donkingkong.superficie, (donkingkong.posx, donkingkong.posy))

    pygame.display.flip()

pygame.quit()