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
            estado = "izquierda"  # Si no hay get_accion, usamos algo fijo.

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        self.actualizar_frame()  # Incrementa el frame según el delay
        self.image = (
            self.obtener_superficie_actual()
        )  # Obtiene el frame actual de surfaces
