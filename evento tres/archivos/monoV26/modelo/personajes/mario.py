
from modelo.personajes.personajes import Personaje


class Mario(Personaje):
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
        self.tipo="mario"
    


    
    def colision_con_parte_arriba(self,otro_personaje):
        
        if(otro_personaje.tipo=="bloque"):
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

    def get_accion(self):
        """
        Retorna el estado/acción de Mario. La Vista usará este valor
        para seleccionar la animación correspondiente.
        """
        if self.saltando:
            return "salto"
        elif self.velocidad_x > 0:
            return "derecha"
        elif self.velocidad_x < 0:
            return "izquierda"
        elif self.velocidad_y > 0:
            return "abajo"
        else:
            # Si no hay movimiento horizontal ni vertical, y no está saltando
            return "reposo"

    # Métodos para aumentar la velocidad (KEYDOWN)
    def aumevelocidadXRight(self):
        self.velocidad_x = self.velocidad
        

    def aumevelocidadXLeft(self):
        self.velocidad_x = -self.velocidad
        

    def aumevelocidadYDown(self):
        self.velocidad_y = self.velocidad
       
    def aumevelocidadYUp(self):
        # Para el salto: si no se está saltando, se activa el salto
        if self.saltando==False:
            self.saltando = True
            self.jump_velocity = -10
            
            self.frame = 0

    # Métodos para disminuir la velocidad (KEYUP)
    def dismivelocidadXRight(self):
        if self.velocidad_x > 0:
            self.velocidad_x = 0

    def dismivelocidadXLeft(self):
        if self.velocidad_x < 0:
            self.velocidad_x = 0

    def dismivelocidadYDown(self):
        if self.velocidad_y > 0:
            self.velocidad_y = 0

    def dismivelocidadYUp(self):
        if self.velocidad_y < 0:
            self.velocidad_y = 0
            

    
       