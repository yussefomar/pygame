from vista.animaciones import ANIMACIONES_DONKEYKONG
from vista.sprites_personajes.sprites import SpriteBase


class SpriteDonkingkong(SpriteBase):
    def __init__(self, dk_logico, ruta_imagen, color_key=None):
        super().__init__(dk_logico, ruta_imagen, color_key)
        self.reflejos = {}

        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_DONKEYKONG,
            color=color_key,
            scale_ancho=dk_logico.scale_ancho,
            scale_alto=dk_logico.scale_alto,
        )

  