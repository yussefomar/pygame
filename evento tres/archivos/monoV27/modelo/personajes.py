
 


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

        
    def colision_personajes(self,lista_personajes):
        
        for un_personaje in lista_personajes :
            if self.hay_colision(un_personaje):
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
