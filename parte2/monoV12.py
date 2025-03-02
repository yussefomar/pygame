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
            0: {"x": 12, "y": 345, "sprite_ancho": 230  , "sprite_alto": 272}
        }
    def obtener_sprite_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.scale_ancho, self.scale_alto))
        return  superficie_fondo_escalado

# Cargar el fondo
fondo = Fondo("imagenesmono/hojasprite.png", 0, 0, ANCHO_VENTANA, ALTO_VENTANA)

class Mario(pygame.sprite.Sprite):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.hoja_sprite = pygame.image.load(ruta).convert()
        self.posx = posx
        self.posy = posy
        self.velocidad = velocidad
        self.scale_ancho = scale_ancho
        self.scale_alto = scale_alto
        self.frame = 0
        self.color = color
        
         
        self.animacion_actual = "reposo"  # Estado inicial
        self.definir_animaciones()
       # Inicializar animaciones
        self.superficies=None
        self.num_frames=None
        self.frame_delays=None
        
        animaciones = self.definir_animaciones()  # Obtener el diccionario de animaciones
        self.cargar_superficies_numframe_delays(animaciones)  # Pasar las animaciones para cargar superficies
       
    
    def definir_animaciones(self):
        animaciones = {
            "izquierda": {
                "frames": {
                    0: {"x": 10, "y": 190, "sprite_ancho": 20, "sprite_alto": 40},
                1: {"x": 30, "y": 190, "sprite_ancho": 20, "sprite_alto": 40},
                2: {"x": 50, "y": 190, "sprite_ancho": 20, "sprite_alto": 40}
                },
                "frame_delay": 8
            },
            "arriba": {
                "frames": {
                     0: {"x": 69, "y": 190, "sprite_ancho": 20, "sprite_alto": 40},
                     1: {"x": 87, "y": 190, "sprite_ancho": 20, "sprite_alto": 40},
                     2: {"x": 103, "y": 190, "sprite_ancho": 20, "sprite_alto": 40},
                     3: {"x": 126, "y": 190, "sprite_ancho": 20, "sprite_alto": 40}
                },
                "frame_delay": 12
            },
            "reposo": {
                "frames": {
                    0: {"x": 10, "y": 190, "sprite_ancho": 20, "sprite_alto": 40}
                },
                "frame_delay": 20
            },
            "golpe": {
                "frames": {
                    0: {"x": 12, "y": 225, "sprite_ancho": 20, "sprite_alto": 40},
                    1: {"x": 38, "y": 225, "sprite_ancho": 30, "sprite_alto": 40},
                    3: {"x": 64, "y": 225, "sprite_ancho": 26, "sprite_alto": 40},
                    2: {"x": 86, "y": 225, "sprite_ancho": 38, "sprite_alto": 40} 
                },
                "frame_delay": 15
            }
        }

        return animaciones
        

    def cargar_superficies_numframe_delays(self,animaciones):
        num_frames = {}
        frame_delays = {}
        superficies = {}

        for animacion, data in animaciones.items():
            num_frames[animacion] = len(data["frames"])
            frame_delays[animacion] = data["frame_delay"]

            # Cargar los frames de la animación
            superficies[animacion] = []
            for frame in data["frames"].values():
                clip = self.hoja_sprite.subsurface((frame["x"], frame["y"], frame["sprite_ancho"], frame["sprite_alto"]))
                clip.set_colorkey(self.color)
                superficies[animacion].append(pygame.transform.scale(clip, (self.scale_ancho, self.scale_alto)))

        # **Generar las versiones reflejadas**
        if "izquierda" in superficies:
            superficies["derecha"] = [pygame.transform.flip(img, True, False) for img in superficies["izquierda"]]
            num_frames["derecha"] = num_frames["izquierda"]  # Copiar cantidad de frames
            frame_delays["derecha"] = frame_delays["izquierda"]  # Copiar delay

        if "arriba" in superficies:
            superficies["abajo"] = [pygame.transform.flip(img, False, True) for img in superficies["arriba"]]
            num_frames["abajo"] = num_frames["arriba"]  # Copiar cantidad de frames
            frame_delays["abajo"] = frame_delays["arriba"]  # Copiar delay

        self.superficies = superficies
        
        self.num_frames=num_frames
        self.frame_delays=frame_delays
         
    
    def obtener_superficie_actual(self):
        superficie_actual = self.superficies[self.animacion_actual]  # si animacion_actual fuera izquierda
        delays=self.frame_delays[self.animacion_actual]# me devuelve 8 si es izquierda	
        clip=superficie_actual[self.frame // delays]  # Obtener el frame correspondiente
       
        return clip

    
    def actualizar_frame(self):
        self.frame = self.frame+ 1
        num_frame_actual=self.num_frames[self.animacion_actual]
        delay_actual=self.frame_delays[self.animacion_actual]
        
        if self.frame >= num_frame_actual * delay_actual:
            self.frame = 0

    
    def actualizar_posicion(self):
        """Actualiza la posición del personaje basado en teclas presionadas."""
        teclas = pygame.key.get_pressed()
        en_movimiento = False
        
        if teclas[pygame.K_LEFT]:
            self.posx -= self.velocidad
            self.animacion_actual = "izquierda"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_RIGHT]:
            self.posx += self.velocidad
            self.animacion_actual = "derecha"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_RIGHT]:
            self.posx += self.velocidad
            self.animacion_actual = "reposo"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_UP]:
            self.posy -= self.velocidad
            self.animacion_actual = "arriba"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_DOWN]:
            self.posy += self.velocidad
            self.animacion_actual = "abajo"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_SPACE]:  # Tecla de golpe
            self.animacion_actual = "golpe"
            self.actualizar_frame()
            en_movimiento = True
        
        if not en_movimiento:
            self.animacion_actual = "reposo"
            self.frame = 0  # Reiniciar el frame cuando no se presiona ninguna tecla

         

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
mario = Mario("imagenesmono/hojasprite.png",COLOR_NEGRO, 20, 490, 85, 75,velocidad)

# Bucle principal del juego
jugando = True
while jugando:
    clock.tick(60)  # Mantener 60 FPS
    
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:
            jugando = False

        

    # Actualizar la posición del personaje
     
    mario.actualizar_posicion()
    #donkingkong.update()
    # Dibujar en la ventana
    ventana.blit(fondo.obtener_sprite_actual(), (fondo.posx, fondo.posy))
    ventana.blit(mario.obtener_superficie_actual(), (mario.posx, mario.posy))
    ventana.blit(donkingkong.superficie, (donkingkong.posx, donkingkong.posy))

    pygame.display.flip()

pygame.quit()
