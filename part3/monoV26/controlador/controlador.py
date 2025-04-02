# controlador/controlador.py
from modelo.personajes import Mario

class Controlador:
    def __init__(self, modelo):
        """
        Recibe el modelo completo y localiza a Mario u otros personajes controlables.
        """
        self.modelo = modelo
        self.mario_logico = next(
            (p for p in self.modelo.personajes if isinstance(p, Mario)),
            None
        )

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN:
                if self.mario_logico:
                    if evento.key == pygame.K_RIGHT:
                        self.mario_logico.mover_derecha()
                    elif evento.key == pygame.K_LEFT:
                        self.mario_logico.mover_izquierda()
                    elif evento.key == pygame.K_UP:
                        self.mario_logico.saltar()
                    elif evento.key == pygame.K_DOWN:
                        self.mario_logico.mover_abajo()

            elif evento.type == pygame.KEYUP:
                if self.mario_logico:
                    if evento.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        self.mario_logico.parar_mov_horizontal()
                    elif evento.key in (pygame.K_UP, pygame.K_DOWN):
                        self.mario_logico.parar_mov_vertical()
