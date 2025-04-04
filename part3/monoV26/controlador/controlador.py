# controlador/controlador.py
from modelo.personajes import Mario
import pygame
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
                        self.mario_logico.aumevelocidadXRight()
                    elif evento.key == pygame.K_LEFT:
                        self.mario_logico.aumevelocidadXLeft()
                    elif evento.key == pygame.K_UP:
                        self.mario_logico.aumevelocidadYUp()
                    elif evento.key == pygame.K_DOWN:
                        self.mario_logico.aumevelocidadYDown()

            elif evento.type == pygame.KEYUP:
                if self.mario_logico:
                    if evento.key == pygame.K_RIGHT:
                        self.mario_logico.dismivelocidadXRight()
                    elif evento.key == pygame.K_LEFT:
                        self.mario_logico.dismivelocidadXLeft()
                    elif evento.key == pygame.K_UP:
                        self.mario_logico.dismivelocidadYUp()
                    elif evento.key == pygame.K_DOWN:
                        self.mario_logico.dismivelocidadYDown()