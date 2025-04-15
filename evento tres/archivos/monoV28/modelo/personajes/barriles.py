from modelo.personajes.personajes import Personaje


class Barriles(Personaje):
    def __init__(self, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(posx, posy, scale_ancho, scale_alto, velocidad)

        self.tipo = "barriles"

    def actualizar_posicion(self):

        # Actualizar la máscara después de mover
        self.actualizar_rectangulo_colision()

    def get_accion(self):
        """
        Retorna la acción actual ("pecho" o "lanza_barril"),
        que la Vista usará para seleccionar la animación.
        """
        return self.direcciones[self.indice_direccion]
