
from modelo.personajes.personajes import Personaje


class Fondo(Personaje):
    def __init__(self , posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(   posx, posy, scale_ancho, scale_alto, velocidad)
        
        self.tipo="ventana"
 
    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        #self.actualizar_mask()
        self.actualizar_rectangulo_colision()

