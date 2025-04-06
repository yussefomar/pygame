
 


from modelo.rectangulo import Rectangulo


class Personaje():
    def __init__(self , posx, posy, scale_ancho, scale_alto, velocidad):
       
        
        self.posx = posx
        self.posy = posy
        self.velocidad = velocidad
        self.scale_ancho = scale_ancho
        self.scale_alto = scale_alto
         
        # Usamos la clase Rectangulo para el manejo del rectángulo de colisión
        self.rectangulo_colision = Rectangulo(self.posx, self.posy, self.scale_ancho, self.scale_alto) 
        
        self.tipo=None
        
        # Variables para saber la posición anterior (útiles al detectar lados de colisión)
        self.old_x = self.posx
        self.old_y = self.posy

        
     
        
       
            
    def actualizar_posicion(self):
        pass

    def actualizar_rectangulo_colision(self):
        self.rectangulo_colision.actualizar(self.posx,self.posy)
        
       

    def hay_colision(self, otro_personaje):
        """Verifica si este personaje colisiona con otro y retorna True o None."""
        excepciones = [self.tipo, "ventana"]
        if otro_personaje.tipo not in excepciones:
            # Tomar (x, y, ancho, alto) del rectángulo de colisión
            x1 = self.rectangulo_colision.x
            y1 = self.rectangulo_colision.y
            w1 = self.rectangulo_colision.ancho
            h1 = self.rectangulo_colision.alto

            x2 = otro_personaje.rectangulo_colision.x
            y2 = otro_personaje.rectangulo_colision.y
            w2 = otro_personaje.rectangulo_colision.ancho
            h2 = otro_personaje.rectangulo_colision.alto
             
                

            return (
                x1 < x2 + w2 and
                x1 + w1 > x2 and
                y1 < y2 + h2 and
                y1 + h1 > y2
            )
        else:
             
            return None

        
    def colision_personajes(self,lista_bloques):
        
        for un_bloque in lista_bloques :
            if self.hay_colision(un_bloque):
                self.esta_suelo=True
                return True

        self.esta_suelo=False
        return False



    def colisiona_con(self, lista_personajes):
        """
        Determina el lado en el que self colisiona con otro_personaje.
        Retorna "arriba", "abajo", "izquierda" o "derecha".
        Se utiliza la aproximación de comparar los centros de ambos personajes.
        """
       
        
        self.colision_personajes(lista_personajes)
        print("colision",self.colision_personajes(lista_personajes))

        
        for otro_personaje in lista_personajes:
        
            if  self.hay_colision(otro_personaje):
                    # Chequear colisión basándote en la posición anterior
                if self.old_y + self.scale_alto <= otro_personaje.posy:
                    self.colision_con_parte_arriba(otro_personaje)
                elif self.old_y >= otro_personaje.posy + otro_personaje.scale_alto:
                    self.colision_con_parte_abajo(otro_personaje)
                elif self.old_x + self.scale_ancho <= otro_personaje.posx:
                    self.colision_con_parte_izquierda(otro_personaje)
                elif self.old_x >= otro_personaje.posx + otro_personaje.scale_ancho:
                    self.colision_con_parte_derecha(otro_personaje)

     
    def colision_con_parte_abajo(self,otro_personaje):
        print( self.tipo + "choque abajo con " +otro_personaje.tipo )

    def colision_con_parte_arriba(self,otro_personaje):
        print( self.tipo +"choque arriba"+otro_personaje.tipo)

    def colision_con_parte_derecha(self,otro_personaje):
        print( self.tipo +"choque derecha"+otro_personaje.tipo)    

    def colision_con_parte_izquierda(self,otro_personaje):
        print( self.tipo + "choque izquierda " +otro_personaje.tipo)

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
        

            

             
            

class Fondo(Personaje):
    def __init__(self , posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(   posx, posy, scale_ancho, scale_alto, velocidad)
        
        self.tipo="ventana"
 
    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        #self.actualizar_mask()
        self.actualizar_rectangulo_colision()


        
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

        

class Barriles(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(  posx, posy, scale_ancho, scale_alto, velocidad)
        
       
        self.tipo="barriles"
 
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        self.actualizar_rectangulo_colision()
    def get_accion(self):
        """
        Retorna la acción actual ("pecho" o "lanza_barril"),
        que la Vista usará para seleccionar la animación.
        """
        return self.direcciones[self.indice_direccion]
class Bloque(Personaje):
    def __init__(self,  posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__(  posx, posy, scale_ancho, scale_alto, velocidad)
        
        # Obtener el diccionario de animaciones
       
        self.tipo="bloque"

    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
         
        self.actualizar_rectangulo_colision()