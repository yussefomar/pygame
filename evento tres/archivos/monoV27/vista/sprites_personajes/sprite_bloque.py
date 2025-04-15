# Ejemplo (podrías hacer lo mismo con Fuego, Barriles, etc.)
import pygame
from vista.animaciones import ANIMACIONES_BLOQUE
from vista.sprites_personajes.sprites import SpriteBase


class SpriteBloque(SpriteBase):
    def __init__(self, bloque_logico, ruta_imagen, color):
        super().__init__(bloque_logico, ruta_imagen, color)
        # Cargamos frames
        self.reflejos = {}

        self.cuadros_animacion = ANIMACIONES_BLOQUE

    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo = self.hoja_sprite.subsurface(
            (sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"])
        )
        superficie_fondo_escalado = pygame.transform.scale(
            superficie_fondo, (self.logico.scale_ancho, self.logico.scale_alto)
        )
        return superficie_fondo_escalado
