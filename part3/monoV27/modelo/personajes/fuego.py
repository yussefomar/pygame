
        
from modelo.personajes.personajes_movible import Personaje_movible


class Fuego(Personaje_movible):
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
        
    def controlador_automatico(self):
        self.contador_frames= self.contador_frames+1
        if self.contador_frames>=90:
            self.indice_direccion=self.indice_direccion+1
            if self.indice_direccion>=len(self.direcciones):
                self.indice_direccion=0
            self.contador_frames=0
        animacion= self.direcciones[self.indice_direccion]
            
        if animacion=="izquierda":
            self.posx -= self.velocidad
            
        elif animacion=="derecha":
            self.posx += self.velocidad

    def actualizar_posicion(self):
        self.controlador_automatico()
        # Guardar la posición anterior
        self.old_x = self.posx
        self.old_y = self.posy
        # Primero, procesar eventos para controlar a Mario
       
        
        # Actualizar la posición horizontal con la velocidad actual
        self.posx += self.velocidad_x
        
        # Actualizar la posición vertical:
        # Si se está saltando, aplicar la física del salto
       
        # Actualizar la posición vertical
        if self.esta_suelo== False  :
            self.posy += self.jump_velocity
            self.jump_velocity += self.gravity
        elif self.saltando==True:
            self.posy += self.jump_velocity
            self.jump_velocity += self.gravity
             
           

             # Aquí se podría detectar colisión con el suelo para terminar el salto
        
        self.posy += self.velocidad_y
        

       
 
        ##self.actualizar_mask()
        self.actualizar_rectangulo_colision()
            

       
    
        

