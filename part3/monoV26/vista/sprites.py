# vista_sprites.py
import pygame
from animaciones import ANIMACIONES_MARIO, ANIMACIONES_DONKEYKONG
# Podrás importar ANIMACIONES_FONDO, ANIMACIONES_FUEGO, etc. si las usas
# from modelo.personajes import Mario, Donkingkong, ... 
# (Normalmente no necesitás importar las clases lógicas aquí, 
#  pero sí recibís sus instancias desde afuera.)

class SpriteBase(pygame.sprite.Sprite):
    """
    Clase base para Sprites con animaciones.
    Usa un diccionario de animaciones que mapea un 'estado' a
    una lista de frames (superficies) y un frame_delay.
    """
    def __init__(self, logico, ruta_imagen, color_key=None):
        super().__init__()
        self.logico = logico  # referencia al objeto del Modelo
        self.ruta_imagen = ruta_imagen
        self.hoja_sprite = pygame.image.load(ruta_imagen).convert()

        if color_key is not None:
            self.hoja_sprite.set_colorkey(color_key)

        # Diccionario para: self.animaciones[estado] = [surface1, surface2, ...]
        self.animaciones = {}
        # Diccionario para: self.frame_delays[estado] = int
        self.frame_delays = {}
        # Frame actual
        self.frame = 0
        # Estado (o acción) actual en la animación
        self.animacion_actual = "reposo"
        # Rect inicial del sprite. Sincronizará con self.logico.
        self.rect = pygame.Rect(self.logico.posx, self.logico.posy,
                                self.logico.scale_ancho, self.logico.scale_alto)

        # Superficie inicial (hasta que carguemos la animación real)
        self.image = pygame.Surface((self.logico.scale_ancho, self.logico.scale_alto))
        self.image.fill((255, 0, 0))  # Ejemplo: rojo. Lo reemplazaremos tras cargar.

    def cargar_animaciones(self, dict_animaciones):
        """
        dict_animaciones es algo como ANIMACIONES_MARIO o ANIMACIONES_DONKEYKONG,
        que tiene la forma:
            {
              'derecha': {
                'frame_delay': 5,
                'frames': {
                  0: {'x':..., 'y':..., 'sprite_ancho':..., 'sprite_alto':...},
                  1: {...}, ...
                }
              },
              'izquierda': {...},
              ...
            }
        """
        for nombre_accion, data_accion in dict_animaciones.items():
            frames_info = data_accion["frames"]
            delay = data_accion["frame_delay"]
            surfaces_accion = []
            # Recorremos cada frame y recortamos la hoja_sprite
            for frame_id, coords in frames_info.items():
                x = coords["x"]
                y = coords["y"]
                w = coords["sprite_ancho"]
                h = coords["sprite_alto"]
                recorte = self.hoja_sprite.subsurface((x, y, w, h))
                # Escalamos al tamaño deseado
                recorte = pygame.transform.scale(
                    recorte, (self.logico.scale_ancho, self.logico.scale_alto)
                )
                surfaces_accion.append(recorte)
            # Almacenar en self.animaciones
            self.animaciones[nombre_accion] = surfaces_accion
            self.frame_delays[nombre_accion] = delay

        # Para iniciar con el primer estado y frame 0
        self.animacion_actual = "reposo"
        self.frame = 0
        # Ajustar la imagen con el primer frame de 'reposo' (si existe)
        if "reposo" in self.animaciones:
            self.image = self.animaciones["reposo"][0]

    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy

        # Descubrir la acción actual del modelo
        if hasattr(self.logico, "get_accion"):
            estado = self.logico.get_accion()  # p.ej. 'derecha', 'salto', etc.
        else:
            estado = "reposo"  # Si no hay get_accion, usamos algo fijo.

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        # Avanzar el frame
        surfaces = self.animaciones.get(self.animacion_actual, [])
        delay = self.frame_delays.get(self.animacion_actual, 1)

        if surfaces:
            total_frames = len(surfaces) * delay
            self.frame = (self.frame + 1) % total_frames
            frame_idx = self.frame // delay
            self.image = surfaces[frame_idx]


class SpriteMario(SpriteBase):
    """
    Sprite especializado para Mario.
    Carga ANIMACIONES_MARIO y aplica reflejos si quieres.
    """
    def __init__(self, mario_logico, ruta_imagen, color_key=None):
        super().__init__(mario_logico, ruta_imagen, color_key)
        # Carga las animaciones definidas en ANIMACIONES_MARIO
        self.cargar_animaciones(ANIMACIONES_MARIO)
        # Si necesitás espejar frames, podés implementar lógica adicional aquí.


class SpriteDonkingkong(SpriteBase):
    def __init__(self, dk_logico, ruta_imagen, color_key=None):
        super().__init__(dk_logico, ruta_imagen, color_key)
        self.cargar_animaciones(ANIMACIONES_DONKEYKONG)
        # Donkingkong podría tener sus propios 'reflejos', 
        # o bien no hace falta si no se mueve lateralmente.


# Ejemplo (podrías hacer lo mismo con Fuego, Barriles, etc.)
