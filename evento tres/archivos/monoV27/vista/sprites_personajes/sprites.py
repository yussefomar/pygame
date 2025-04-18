# vista_sprites.py
import pygame


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
        self.logico = (
            personaje_logico  # referencia al personaje lógico, que NO depende de Pygame
        )
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
            self.logico.scale_alto,
        )

        # Superficie inicial (hasta cargar animaciones)
        self.image = pygame.Surface((self.logico.scale_ancho, self.logico.scale_alto))
        self.image.fill((100, 100, 100))  # color gris de placeholder

    def obtener_superficie_actual(self):
        superficie_actual = self.superficies[
            self.animacion_actual
        ]  # si animacion_actual fuera izquierda
        delays = self.frame_delays[
            self.animacion_actual
        ]  # me devuelve 8 si es izquierda

        clip = superficie_actual[
            self.frame // delays
        ]  # Obtener el frame correspondiente

        return clip

    def generar_superficies_reflejadas(self, superficies, num_frames, frame_delays):
        # **Generar las versiones reflejadas**
        for unMovimiento, opuesto in self.reflejos.items():
            superficies[opuesto] = [
                pygame.transform.flip(img, True, False)
                for img in superficies[unMovimiento]
            ]
            num_frames[opuesto] = num_frames[unMovimiento]
            frame_delays[opuesto] = frame_delays[unMovimiento]

        self.superficies = superficies

        self.num_frames = num_frames
        self.frame_delays = frame_delays

    def cargar_superficies_numframe_delays(
        self, animaciones, color, scale_ancho, scale_alto
    ):
        num_frames = {}
        frame_delays = {}
        superficies = {}
        
        for animacion, data in animaciones.items():
             
            num_frames[animacion] = len(data["frames"])
            frame_delays[animacion] = data["frame_delay"]

            # Cargar los frames de la animación
            superficies[animacion] = []
            for frame in data["frames"].values():
                clip = self.hoja_sprite.subsurface(
                    (
                        frame["x"],
                        frame["y"],
                        frame["sprite_ancho"],
                        frame["sprite_alto"],
                    )
                )
                clip = pygame.transform.scale(clip, (scale_ancho, scale_alto))
                clip.set_colorkey(color)
                superficies[animacion].append(clip)

        self.generar_superficies_reflejadas(superficies, num_frames, frame_delays)

    def actualizar_frame(self):
        self.frame = self.frame + 1
        num_frame_actual = self.num_frames[self.animacion_actual]
        delay_actual = self.frame_delays[self.animacion_actual]

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

        # Descubrir la acción actual del modelo
         
        estado = self.logico.get_accion()  # p.ej. 'derecha', 'salto', etc.
         

        # Si cambió el estado, reseteamos el frame
        if estado != self.animacion_actual:
            self.animacion_actual = estado
            self.frame = 0

        self.actualizar_frame()  # Incrementa el frame según el delay
        self.image = (
            self.obtener_superficie_actual()
        )  # Obtiene el frame actual de surfaces
