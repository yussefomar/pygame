
from modelo.personajes.personajes_movible import Personaje_movible

class Mario(Personaje_movible):
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
            

    
       