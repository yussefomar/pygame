
from modelo.personajes.personajes import Personaje


class Personaje_movible(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(   posx, posy, scale_ancho, scale_alto, velocidad)
        self.actualizar_rectangulo_colision()

         # Variables para el salto
        self.saltando = False
        self.jump_velocity = 0
        self.gravity = 1

        # Variables para el movimiento
        self.velocidad_x = 0
        self.velocidad_y = 0
        # variable para ver si colision con el suelo
        self.esta_suelo=False    
    
    def colision_con_parte_arriba(self,otro_personaje):
        
        if(otro_personaje.tipo=="bloque"):
            print("colsion arriba")
            self.posy = otro_personaje.posy  - self.scale_alto
            self.saltando = False
            self.jump_velocity = 0
            #self.animacion_actual = "reposo" 
            self.esta_suelo=True

    def colision_con_parte_derecha(self,otro_personaje):
        print("colisione derecha")
        if  otro_personaje.tipo=="bloque"  :
            self.posy = otro_personaje.posy  - self.scale_alto
            self.saltando = False
            self.jump_velocity = 0
            
    def colision_con_parte_abajo(self,otro_personaje):
        print("colisione abajo")
        if(otro_personaje.tipo=="bloque"):
            self.posy = otro_personaje.posy  + self.scale_alto
            self.saltando = False
            self.jump_velocity = 0
            
            self.esta_suelo=True

    def colision_con_parte_izquierda(self,otro_personaje):
        print("colisione izquierda")
        if(otro_personaje.tipo=="bloque"):
            self.posy = otro_personaje.posy  - self.scale_alto
            self.saltando = False
            self.jump_velocity = 0
           

    def actualizar_posicion(self):
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
