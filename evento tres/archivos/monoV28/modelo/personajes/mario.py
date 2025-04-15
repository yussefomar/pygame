from modelo.personajes.personajes_movible import Personaje_movible


class Mario(Personaje_movible):
    def __init__(self, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(posx, posy, scale_ancho, scale_alto, velocidad)

        self.tipo = "mario"
        self.muerto=False
    
    def get_accion(self):
        if self.muerto:
            return "muerto"
        elif self.saltando:
            return "salto"
        elif self.velocidad_x > 0:
            return "derecha"
        elif self.velocidad_x < 0:
            return "izquierda"
        elif self.velocidad_y > 0:
            return "abajo"
        else:
            return "reposo"
    
    def colision_con_parte_arriba(self, otro_personaje):
        super().colision_con_parte_arriba(otro_personaje)
        if otro_personaje.tipo == "fuego":
            self.muerto = True
            print("choque con fuego")

    def colision_con_parte_abajo(self, otro_personaje):
        super().colision_con_parte_abajo(otro_personaje)
        if otro_personaje.tipo == "fuego":
            self.muerto = True
            print("choque con fuego")

    def colision_con_parte_izquierda(self, otro_personaje):
        super().colision_con_parte_izquierda(otro_personaje)
        if otro_personaje.tipo == "fuego":
            self.muerto = True
            print("choque con fuego")

    def colision_con_parte_derecha(self, otro_personaje):
        super().colision_con_parte_derecha(otro_personaje)
        if otro_personaje.tipo == "fuego":
            self.muerto = True
            print("choque con fuego")