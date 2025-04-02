# vista/sprites.py
import pygame


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
        for p in self.modelo.personajes:
            if isinstance(p, Mario):
                sprite = SpriteMario(p)
                self.sprite_group.add(sprite)
            elif isinstance(p, BloqueLogico):
                sprite = SpriteBloque(p)
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
        self.sprite_group.draw(self.ventana)
        pygame.display.flip()
