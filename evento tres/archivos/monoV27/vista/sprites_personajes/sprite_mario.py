from vista.animaciones import ANIMACIONES_MARIO
from vista.sprites_personajes.sprites import SpriteBase


class SpriteMario(SpriteBase):
    def __init__(self, mario_logico, ruta_imagen, color):
        """
        :param mario_logico: referencia al objeto lógico (clase Mario del Modelo)
        :param ruta_imagen:  ruta al archivo .png o .bmp con la hoja de sprites
        :param color:        color key (ej. COLOR_NEGRO) para hacer transparente
        """
        super().__init__(mario_logico, ruta_imagen, color)

        # Diccionario que indica cuáles animaciones deben reflejarse.
        # Por ejemplo, si la animación "izquierda" es la versión flip de "derecha".
        self.reflejos = {"izquierda": "derecha", "arriba": "abajo"}

        # Cargamos las animaciones definidas en ANIMACIONES_MARIO (dict con frames)
        # Esto llena self.superficies, self.num_frames, self.frame_delays

        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_MARIO,
            color=color,
            scale_ancho=mario_logico.scale_ancho,
            scale_alto=mario_logico.scale_alto,
        )

        
 