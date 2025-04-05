# vista_sprites.py
import pygame
from vista.animaciones import ANIMACIONES_BARRILES, ANIMACIONES_BLOQUE, ANIMACIONES_FONDO, ANIMACIONES_FUEGO, ANIMACIONES_MARIO, ANIMACIONES_DONKEYKONG
# Podrás importar ANIMACIONES_FONDO, ANIMACIONES_FUEGO, etc. si las usas
# from modelo.personajes import Mario, Donkingkong, ... 
# (Normalmente no necesitás importar las clases lógicas aquí, 
#  pero sí recibís sus instancias desde afuera.)

class SpriteBase(pygame.sprite.Sprite):
    """
    Clase base para la Vista de un personaje.
    Se encarga de:
      - Cargar la hoja de sprites con pygame
      - Almacenar superficies recortadas
      - Manejar un frame counter (self.frame)
      - Definir self.animacion_actual
      - Actualizar rect.x / rect.y con la posición del personaje lógico
    """
    def __init__(self, personaje_logico, ruta_imagen, color):
        super().__init__()
        self.logico = personaje_logico  # referencia al personaje lógico, que NO depende de Pygame
        self.hoja_sprite = pygame.image.load(ruta_imagen).convert()
        self.hoja_sprite.set_colorkey(color)

        # Atributos para animaciones
        self.superficies = {}
        self.num_frames = {}
        self.frame_delays = {}
        self.frame = 0
        self.animacion_actual = "reposo"

        # Creamos un rect para que pygame pueda dibujarlo y detectar colisiones sprite-sprite si quisieras
        self.rect = pygame.Rect(
            self.logico.posx,
            self.logico.posy,
            self.logico.scale_ancho,
            self.logico.scale_alto
        )

        # Superficie inicial (hasta cargar animaciones)
        self.image = pygame.Surface((self.logico.scale_ancho, self.logico.scale_alto))
        self.image.fill((100, 100, 100))  # color gris de placeholder

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
        
    def cargar_superficies_numframe_delays(self,animaciones, color,scale_ancho , scale_alto ):
        num_frames = {}
        frame_delays = {}
        superficies = {}
        print("hola entro items ",animaciones.items() )
        print("hola",animaciones.items() )
        for animacion, data in animaciones.items():
            print("hola entro animacion  data " ,data )
            num_frames[animacion] = len(data["frames"])
            frame_delays[animacion] = data["frame_delay"]

            # Cargar los frames de la animación
            superficies[animacion] = []
            for frame in data["frames"].values():
                clip = self.hoja_sprite.subsurface((frame["x"], frame["y"], frame["sprite_ancho"], frame["sprite_alto"]))
                clip=pygame.transform.scale(clip, ( scale_ancho,  scale_alto))
                clip.set_colorkey( color)
                superficies[animacion].append(clip)

        self.generar_superficies_reflejadas(superficies,num_frames,frame_delays)
    def actualizar_frame(self):
        self.frame = self.frame+ 1
        num_frame_actual=self.num_frames[self.animacion_actual]
        delay_actual=self.frame_delays[self.animacion_actual]
        
        if self.frame >= num_frame_actual * delay_actual:
            self.frame = 0
            
    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy

         


class SpriteMario(SpriteBase):
    def __init__(self, mario_logico, ruta_imagen, color):
        """
        :param mario_logico: referencia al objeto lógico (clase Mario del Modelo)
        :param ruta_imagen:  ruta al archivo .png o .bmp con la hoja de sprites
        :param color:        color key (ej. COLOR_NEGRO) para hacer transparente
        """
        super().__init__(mario_logico, ruta_imagen, color)
        
        # Diccionario que indica cuáles animaciones deben reflejarse.
        # Por ejemplo, si la animación "izquierda" es la versión flip de "derecha".
        self.reflejos = {"izquierda": "derecha", "arriba": "abajo"}
        
        # Cargamos las animaciones definidas en ANIMACIONES_MARIO (dict con frames)
        # Esto llena self.superficies, self.num_frames, self.frame_delays
         
        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_MARIO,
            color=color,
            scale_ancho=mario_logico.scale_ancho,
            scale_alto=mario_logico.scale_alto
        )
        
        
        
        # Iniciamos en la animación "reposo"
        self.animacion_actual = "reposo"
        self.frame = 0
        if "reposo" in self.superficies:
            self.image = self.superficies["reposo"][0]
    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy

        # Descubrir la acción actual del modelo
        if hasattr(self.logico, "get_accion"):
            estado = self.logico.get_accion()  # p.ej. 'derecha', 'salto', etc.
        else:
            estado = "reposo"  # Si no hay get_accion, usamos algo fijo.

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        

        self.actualizar_frame()                # Incrementa el frame según el delay
        self.image = self.obtener_superficie_actual()  # Obtiene el frame actual de surfaces

class SpriteFuego(SpriteBase):
    def __init__(self, dk_logico, ruta_imagen, color_key=None):
        super().__init__(dk_logico, ruta_imagen, color_key)
        self.reflejos={"izquierda": "derecha" }
       
        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_FUEGO,
            color=color_key,
            scale_ancho=dk_logico.scale_ancho,
            scale_alto=dk_logico.scale_alto
        )
    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy

        # Descubrir la acción actual del modelo
        if hasattr(self.logico, "get_accion"):
            estado = self.logico.get_accion()  # p.ej. 'derecha', 'salto', etc.
        else:
            estado = "izquierda"  # Si no hay get_accion, usamos algo fijo.

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        

        self.actualizar_frame()                # Incrementa el frame según el delay
        self.image = self.obtener_superficie_actual()  # Obtiene el frame actual de surfaces
        
class SpriteDonkingkong(SpriteBase):
    def __init__(self, dk_logico, ruta_imagen, color_key=None):
        super().__init__(dk_logico, ruta_imagen, color_key)
        self.reflejos={}
       
        self.cargar_superficies_numframe_delays(
            animaciones=ANIMACIONES_DONKEYKONG,
            color=color_key,
            scale_ancho=dk_logico.scale_ancho,
            scale_alto=dk_logico.scale_alto
        )
    def update(self):
        """
        - Sincroniza la posición con self.logico.
        - Pregunta al Modelo qué acción/estado tiene.
        - Avanza el frame y actualiza self.image.
        """
        # Sincronizar rect
        self.rect.x = self.logico.posx
        self.rect.y = self.logico.posy

        # Descubrir la acción actual del modelo
        if hasattr(self.logico, "get_accion"):
            estado = self.logico.get_accion()  # p.ej. 'derecha', 'salto', etc.
        else:
            estado = "pecho"  # Si no hay get_accion, usamos algo fijo.

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        

        self.actualizar_frame()                # Incrementa el frame según el delay
        self.image = self.obtener_superficie_actual()  # Obtiene el frame actual de surfaces


# Ejemplo (podrías hacer lo mismo con Fuego, Barriles, etc.)
class SpriteBloque(SpriteBase):
    def __init__(self, bloque_logico, ruta_imagen, color):
        super().__init__(bloque_logico, ruta_imagen, color)
        # Cargamos frames
        self.reflejos={}
        print("holaaa animacion bloque",ANIMACIONES_BLOQUE)
        self.cuadros_animacion = ANIMACIONES_BLOQUE
    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.logico.scale_ancho, self.logico.scale_alto))
        return  superficie_fondo_escalado    
     
    
class SpriteBarriles(SpriteBase):
    def __init__(self, barriles_logico, ruta_imagen, color):
        super().__init__(barriles_logico, ruta_imagen, color)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_BARRILES
    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.logico.scale_ancho, self.logico.scale_alto))
        return  superficie_fondo_escalado    

class SpriteFondo(SpriteBase):
    def __init__(self, fondo_logico, ruta_imagen, color):
        super().__init__(fondo_logico, ruta_imagen, color)
        self.reflejos={}
        # Obtener el diccionario de animaciones
        self.cuadros_animacion = ANIMACIONES_FONDO
    def obtener_superficie_actual(self):
        sprite = self.cuadros_animacion[0]
        superficie_fondo=self.hoja_sprite.subsurface((sprite["x"], sprite["y"], sprite["sprite_ancho"], sprite["sprite_alto"]))
        superficie_fondo_escalado=pygame.transform.scale(superficie_fondo, (self.logico.scale_ancho, self.logico.scale_alto))
        return  superficie_fondo_escalado    

     