from modelo.personajes.personajes import Personaje


class Bloque(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(  posx, posy, scale_ancho, scale_alto, velocidad)
        
        # Obtener el diccionario de animaciones
       
        self.tipo="bloque"

    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
         
        self.actualizar_rectangulo_colision()