
from animaciones import ANIMACIONES_MARIO,ANIMACIONES_DONKEYKONG,ANIMACIONES_FONDO,ANIMACIONES_FUEGO,ANIMACIONES_BARRILES,ANIMACIONES_BLOQUE
import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.hoja_sprite = pygame.image.load(ruta).convert()
        self.posx = posx
        self.posy = posy
        self.velocidad = velocidad
        self.scale_ancho = scale_ancho
        self.scale_alto = scale_alto
        self.frame = 0
        self.color = color
        self.animacion_actual = "reposo"  # Estado inicial
        # Inicializar animaciones
        self.superficies=None
        self.num_frames=None
        self.frame_delays=None
        #rectangulo colision	
        #self.rectangulo_colision = pygame.Rect(self.posx, self.posy, self.scale_ancho, self.scale_alto)
        # La máscara se usará para colisiones precisas
        self.mascara = None
        self.tipo=None
        

    def actualizar_mask(self):
        """Actualiza la máscara basándose en la superficie actual."""
        superficie_actual = self.obtener_superficie_actual()
        self.mascara = pygame.mask.from_surface(superficie_actual)

    def obtener_superficie_actual(self):
        superficie_actual = self.superficies[self.animacion_actual]  # si animacion_actual fuera izquierda
        delays=self.frame_delays[self.animacion_actual]# me devuelve 8 si es izquierda	
        clip=superficie_actual[self.frame // delays]  # Obtener el frame correspondiente
       
        return clip

    def generar_superficies_reflejadas(self,superficies,num_frames,frame_delays):
        # **Generar las versiones reflejadas**
        for unMovimiento,opuesto in self.reflejos.items():
            superficies[opuesto] = [pygame.transform.flip(img, True, False) for img in superficies[unMovimiento]]
            num_frames[opuesto] = num_frames[unMovimiento]  
            frame_delays[opuesto] = frame_delays[unMovimiento]  

        self.superficies = superficies
        
        self.num_frames=num_frames
        self.frame_delays=frame_delays
        
    def cargar_superficies_numframe_delays(self,animaciones):
        num_frames = {}
        frame_delays = {}
        superficies = {}

        for animacion, data in animaciones.items():
            num_frames[animacion] = len(data["frames"])
            frame_delays[animacion] = data["frame_delay"]

            # Cargar los frames de la animación
            superficies[animacion] = []
            for frame in data["frames"].values():
                clip = self.hoja_sprite.subsurface((frame["x"], frame["y"], frame["sprite_ancho"], frame["sprite_alto"]))
                clip.set_colorkey(self.color)
                superficies[animacion].append(pygame.transform.scale(clip, (self.scale_ancho, self.scale_alto)))

        self.generar_superficies_reflejadas(superficies,num_frames,frame_delays)
    
    def actualizar_frame(self):
        self.frame = self.frame+ 1
        num_frame_actual=self.num_frames[self.animacion_actual]
        delay_actual=self.frame_delays[self.animacion_actual]
        
        if self.frame >= num_frame_actual * delay_actual:
            self.frame = 0
       
            
    def actualizar_posicion(self):
        pass

    def hay_colision(self, otro_personaje):
        """Verifica colisiones precisas usando la máscara y las posiciones."""
        excepciones=["mario","ventana"]
        
        if otro_personaje.tipo  not in excepciones : 
            offset_x = otro_personaje.posx - self.posx
            offset_y = otro_personaje.posy - self.posy
            return self.mascara.overlap(otro_personaje.mascara, (offset_x, offset_y))
        else:
            return None

        
        

    def colisiona_con(self, otro_personaje):
        """
        Determina el lado en el que self colisiona con otro_personaje.
        Retorna "arriba", "abajo", "izquierda" o "derecha".
        Se utiliza la aproximación de comparar los centros de ambos personajes.
        """
        if not self.hay_colision(otro_personaje):
            return None
        
        # Calcular el centro de self
        self_centro_x = self.posx + self.scale_ancho / 2
        self_centro_y = self.posy + self.scale_alto / 2
        
        # Calcular el centro de otro_personaje
        otro_centro_x = otro_personaje.posx + otro_personaje.scale_ancho / 2
        otro_centro_y = otro_personaje.posy + otro_personaje.scale_alto / 2

        dx = otro_centro_x - self_centro_x
        dy = otro_centro_y - self_centro_y

        if abs(dx) > abs(dy):
            if dx > 0:
                self.colision_con_parte_derecha(otro_personaje)
            else:
                self.colision_con_parte_izquierda(otro_personaje)
        elif abs(dy) > abs(dx):
            if dy > 0:
                self.colision_con_parte_abajo(otro_personaje)
            else:
                self.colision_con_parte_arriba(otro_personaje)
        else:
             # En caso de igualdad exacta, se puede retornar un valor por defecto
            return "indeterminado"
     
    def colision_con_parte_abajo(self,otro_personaje):
        print( self.tipo + "choque abajo con " +otro_personaje.tipo )

    def colision_con_parte_arriba(self,otro_personaje):
        print( self.tipo +"choque arriba"+otro_personaje.tipo)

    def colision_con_parte_derecha(self,otro_personaje):
        print( self.tipo +"choque derecha"+otro_personaje.tipo)    

    def colision_con_parte_izquierda(self,otro_personaje):
        print( self.tipo + "choque izquierda " +otro_personaje.tipo)

class Mario(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={"izquierda":"derecha","arriba":"abajo"}
        # Obtener el diccionario de animaciones
        self.cargar_superficies_numframe_delays(ANIMACIONES_MARIO)
        self.tipo="mario"
         # **Generar la máscara ya con el color key aplicado** 
        self.actualizar_mask()
        
    def actualizar_posicion(self):
        """Actualiza la posición del personaje basado en teclas presionadas."""
        teclas = pygame.key.get_pressed()
        en_movimiento = False
        
        if teclas[pygame.K_LEFT]:
            self.posx -= self.velocidad
            self.animacion_actual = "izquierda"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_RIGHT]:
            self.posx += self.velocidad
            self.animacion_actual = "derecha"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_RIGHT]:
            self.posx += self.velocidad
            self.animacion_actual = "reposo"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_UP]:
            self.posy -= self.velocidad
            self.animacion_actual = "arriba"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_DOWN]:
            self.posy += self.velocidad
            self.animacion_actual = "abajo"
            self.actualizar_frame()
            en_movimiento = True
        elif teclas[pygame.K_SPACE]:  # Tecla de golpe
            self.animacion_actual = "golpe"
            self.actualizar_frame()
            en_movimiento = True
        
        if not en_movimiento:
            self.animacion_actual = "reposo"
            self.frame = 0  # Reiniciar el frame cuando no se presiona ninguna tecla

        # Actualizar la máscara después de mover
        self.actualizar_mask()

    def colision_con_parte_abajo(self,otro_personaje):
        self.posy = otro_personaje.posy + otro_personaje.scale_alto - self.scale_alto -20
        print( self.tipo + "choque abajo con " +otro_personaje.tipo )
         

class Donkingkong(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cargar_superficies_numframe_delays(ANIMACIONES_DONKEYKONG)
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

        animacion= self.direcciones[self.indice_direccion]
        self.animacion_actual = animacion
        self.actualizar_frame()
        en_movimiento = True

        # Actualizar la máscara después de mover
        self.actualizar_mask()
        

            

             
            

class Fondo(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_FONDO
        self.tipo="ventana"

    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.scale_ancho, self.scale_alto))
        return  superficie_fondo_escalado
    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        self.actualizar_mask()


        
class Fuego(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={"izquierda":"derecha"}
        # Obtener el diccionario de animaciones
        self.cargar_superficies_numframe_delays(ANIMACIONES_FUEGO)
        # se agrego para movimiento automatico
        self.direcciones = ["derecha", "izquierda"]
        self.indice_direccion = 0
        self.contador_frames = 0
        self.tipo="fuego"
        
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
            self.animacion_actual = "izquierda"
            self.actualizar_frame()
            en_movimiento = True
        elif animacion=="derecha":
            self.posx += self.velocidad
            self.animacion_actual = "derecha"
            self.actualizar_frame()
            en_movimiento = True  

        # Actualizar la máscara después de mover
        self.actualizar_mask()

        

class Barriles(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_BARRILES
        self.tipo="barriles"

    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.scale_ancho, self.scale_alto))
        return  superficie_fondo_escalado
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        self.actualizar_mask()
    
class Bloque(Personaje):
    def __init__(self, ruta, color, posx, posy, scale_ancho, scale_alto, velocidad):
        super().__init__( ruta, color, posx, posy, scale_ancho, scale_alto, velocidad)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_BLOQUE
        self.tipo="bloque"

    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.scale_ancho, self.scale_alto))
        return  superficie_fondo_escalado
    
    def actualizar_posicion(self):
         

        # Actualizar la máscara después de mover
        self.actualizar_mask()