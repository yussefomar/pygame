# vista/sprites.py
import pygame

 
from vista.sprites_personajes.sprite_barriles import SpriteBarriles 
from vista.sprites_personajes.sprite_bloque import  SpriteBloque 
from vista.sprites_personajes.sprite_donkingkong import   SpriteDonkingkong 
from vista.sprites_personajes.sprite_fondo import   SpriteFondo 
from vista.sprites_personajes.sprite_fuego import   SpriteFuego 
from vista.sprites_personajes.sprite_mario import   SpriteMario
 


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
        self.sprite_group = pygame.sprite.Group()
        self._crear_sprites()

    def _crear_sprites(self):
        personajes = self.modelo.get_personajes()
        for p in personajes:
            
            if p.tipo=="bloque":
                sprite = SpriteBloque(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite)
            elif p.tipo=="barriles":
                sprite = SpriteBarriles(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite)
             
            elif p.tipo=="mario":
                sprite = SpriteMario(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite)
            elif p.tipo=="donkingkong":
                sprite = SpriteDonkingkong(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite)
            elif p.tipo=="fuego":
                sprite = SpriteFuego(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite)
            elif p.tipo=="ventana":
                sprite = SpriteFondo(p,"imagenesmono/hojasprite.png", (0, 0, 0))
                self.sprite_group.add(sprite) 
            # Agregar más elif para otros personajes lógicos que tengas

    def update(self):
        """
        Llama a update en los sprites para reflejar
        la posición actual del modelo.
        """ 
        self.sprite_group.update()

    def render(self):
        """
        Limpia, dibuja y voltea la pantalla.
        Al final del bucle, esta es la parte visual.
        """
        self.ventana.fill((0, 0, 0))
        for sprite in self.sprite_group:
            print("que empezara", sprite.logico.tipo)
            self.ventana.blit(sprite.obtener_superficie_actual(),(sprite.logico.posx, sprite.logico.posy))
        #self.ventana.fill((0, 0, 0))
        #self.sprite_group.draw(self.ventana)
        pygame.display.flip()
