
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
            scale_alto=mario_logico.scale_alto
        )
        
        
        
        # Iniciamos en la animación "reposo"
        self.animacion_actual = "reposo"
        self.frame = 0
        if "reposo" in self.superficies:
            self.image = self.superficies["reposo"][0]
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

        

        self.actualizar_frame()                # Incrementa el frame según el delay
        self.image = self.obtener_superficie_actual()  # Obtiene el frame actual de surfaces
