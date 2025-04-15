from modelo.personajes.personajes_movible import Personaje_movible


class Mario(Personaje_movible):
    def __init__(self, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(posx, posy, scale_ancho, scale_alto, velocidad)

        self.tipo = "mario"
