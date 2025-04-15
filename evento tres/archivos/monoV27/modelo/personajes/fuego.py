from modelo.personajes.personajes_movible import Personaje_movible


class Fuego(Personaje_movible):
    def __init__(self, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(posx, posy, scale_ancho, scale_alto, velocidad)

        # Obtener el diccionario de animaciones

        # se agrego para movimiento automatico
        self.direcciones = ["derecha", "izquierda"]
        self.indice_direccion = 0
        self.contador_frames = 0
        self.tipo = "fuego"

    def controlador_automatico(self):
        self.contador_frames = self.contador_frames + 1
        if self.contador_frames >= 90:
            self.indice_direccion = self.indice_direccion + 1
            if self.indice_direccion >= len(self.direcciones):
                self.indice_direccion = 0
            self.contador_frames = 0
        animacion = self.direcciones[self.indice_direccion]

        if animacion == "izquierda":
            self.aumevelocidadXLeft()

        elif animacion == "derecha":
            self.aumevelocidadXRight()

    def actualizar_posicion(self):
        self.controlador_automatico()
        # Guardar la posición anterior
        super().actualizar_posicion()
