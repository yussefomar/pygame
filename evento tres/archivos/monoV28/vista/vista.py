# vista/sprites.py
import pygame


from vista.sprites_personajes.sprite_barriles import SpriteBarriles
from vista.sprites_personajes.sprite_bloque import SpriteBloque
from vista.sprites_personajes.sprite_donkingkong import SpriteDonkingkong
from vista.sprites_personajes.sprite_fondo import SpriteFondo
from vista.sprites_personajes.sprite_fuego import SpriteFuego
from vista.sprites_personajes.sprite_mario import SpriteMario


class Vista:
    """
    Vista que se encarga de:
      - Recibir el modelo
      - Crear sprites para cada personaje
      - Mantener un sprite.Group
      - Renderizar: fill() + draw() + flip()
    """

    def __init__(self, modelo, ventana):
        self.modelo = modelo
        self.ventana = ventana
        self.sprite_group = []
        self._crear_sprites()

    def _crear_sprites(self):
        personajes = self.modelo.get_personajes()
        ruta = "imagenesmono/hojasprite.png"
        color = (0, 0, 0)

        tipo_a_sprite = {
            "bloque": SpriteBloque,
            "barriles": SpriteBarriles,
            "mario": SpriteMario,
            "donkingkong": SpriteDonkingkong,
            "fuego": SpriteFuego,
            "ventana": SpriteFondo,
        }

        for p in personajes:
            clase_sprite = tipo_a_sprite.get(p.tipo)
            if clase_sprite:
                sprite = clase_sprite(p, ruta, color)
                self.sprite_group.append(sprite)


    def update(self):
        """
        Llama a update en los sprites para reflejar
        la posición actual del modelo.
        """
        for sprite in self.sprite_group:  
            sprite.update()

    def render(self):
        """
        Limpia, dibuja y voltea la pantalla.
        Al final del bucle, esta es la parte visual.
        """
        self.ventana.fill((0, 0, 0))
        for sprite in self.sprite_group:

            self.ventana.blit(
                sprite.obtener_superficie_actual(),
                (sprite.logico.posx, sprite.logico.posy),
            )
        
        if self.modelo.termino_juego==True:
                fuente = pygame.font.SysFont("Arial", 50)
                texto = fuente.render("¡Perdiste!", True, (255, 0, 0))
                self.ventana.blit(texto, (self.ventana.get_width() // 2 - 85, 50))        
        # self.ventana.fill((0, 0, 0))
        # self.sprite_group.draw(self.ventana)
        pygame.display.flip()
