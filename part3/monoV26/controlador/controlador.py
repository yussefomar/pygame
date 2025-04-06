# controlador/controlador.py
from modelo.personajes import Mario
import pygame
class Controlador:
    def __init__(self, modelo):
        """
        Recibe el modelo completo y localiza a Mario u otros personajes controlables.
        """
       
        self.modelo=modelo
        encontro = False
        i = 0
        self.mario_logico = None  # Inicializamos por si no se encuentra
        # Obtenemos la lista de personajes a través del método
        personajes = self.modelo.get_personajes()
        print(personajes)
        while i < len(personajes) and not encontro:
            if personajes[i].tipo == "mario":
                self.mario_logico = personajes[i]
                 
                encontro = True
            else:
                i += 1
        
         

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