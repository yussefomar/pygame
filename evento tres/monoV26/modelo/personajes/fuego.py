
        
from modelo.personajes.personajes import Personaje


class Fuego(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(   posx, posy, scale_ancho, scale_alto, velocidad)
        
        # Obtener el diccionario de animaciones
      
        # se agrego para movimiento automatico
        self.direcciones = ["derecha", "izquierda"]
        self.indice_direccion = 0
        self.contador_frames = 0
        self.tipo="fuego"
        
    def get_accion(self):
        """
        Retorna la acción actual ("pecho" o "lanza_barril"),
        que la Vista usará para seleccionar la animación.
        """
        return self.direcciones[self.indice_direccion]
        
    def actualizar_posicion(self):
        self.contador_frames= self.contador_frames+1
        if self.contador_frames>=70:
            self.indice_direccion=self.indice_direccion+1
            if self.indice_direccion>=len(self.direcciones):
                self.indice_direccion=0
            self.contador_frames=0
        animacion= self.direcciones[self.indice_direccion]
            
        if animacion=="izquierda":
            self.posx -= self.velocidad
            
        elif animacion=="derecha":
            self.posx += self.velocidad
            

        # Actualizar la máscara después de mover
        #self.actualizar_mask()
        self.actualizar_rectangulo_colision()
    def get_accion(self):
        """
        Retorna la dirección actual ("izquierda" o "derecha"),
        para que la Vista sepa qué animación usar.
        """
        return self.direcciones[self.indice_direccion]

        

