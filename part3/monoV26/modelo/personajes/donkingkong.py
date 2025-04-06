         

from modelo.personajes.personajes import Personaje


class Donkingkong(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(   posx, posy, scale_ancho, scale_alto, velocidad)
        
        # se agrego para movimiento automatico
        self.direcciones = ["pecho", "lanza_barril"]
        self.indice_direccion = 0
        self.contador_frames = 0
        self.tipo="donkingkong"
    def actualizar_posicion(self):
        self.contador_frames= self.contador_frames+1
        if self.contador_frames>=70:
            self.indice_direccion=self.indice_direccion+1
            if self.indice_direccion>=len(self.direcciones):
                self.indice_direccion=0
            self.contador_frames=0

       
        # Actualizar la máscara después de mover
        
        self.actualizar_rectangulo_colision()
    
    def get_accion(self):
        """
        Retorna la acción actual ("pecho" o "lanza_barril"),
        que la Vista usará para seleccionar la animación.
        """
        return self.direcciones[self.indice_direccion]
        

            

             
            
