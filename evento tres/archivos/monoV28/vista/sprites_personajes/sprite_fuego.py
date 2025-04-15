from vista.animaciones import ANIMACIONES_FUEGO
from vista.sprites_personajes.sprites import SpriteBase


class SpriteFuego(SpriteBase):
    def __init__(self, dk_logico, ruta_imagen, color_key=None):
        super().__init__(dk_logico, ruta_imagen, color_key)
        self.reflejos = {"izquierda": "derecha"}

        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_FUEGO,
            color=color_key,
            scale_ancho=dk_logico.scale_ancho,
            scale_alto=dk_logico.scale_alto,
        )

