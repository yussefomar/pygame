import pygame
from vista.animaciones import ANIMACIONES_BARRILES
from vista.sprites_personajes.sprites import SpriteBase


class SpriteBarriles(SpriteBase):
    def __init__(self, barriles_logico, ruta_imagen, color):
        super().__init__(barriles_logico, ruta_imagen, color)
        self.reflejos = {}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_BARRILES

    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo = self.hoja_sprite.subsurface(
            (sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"])
        )
        superficie_fondo_escalado = pygame.transform.scale(
            superficie_fondo, (self.logico.scale_ancho, self.logico.scale_alto)
        )
        return superficie_fondo_escalado

    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy