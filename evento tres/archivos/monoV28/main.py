# main.py
import pygame
from config import ANCHO_VENTANA, ALTO_VENTANA, FPS
from modelo.modelo import Modelo
from vista.vista import Vista
from controlador.controlador import Controlador


def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    clock = pygame.time.Clock()

    # 1) Crear Modelo
    modelo = Modelo()
    modelo.iniciar_personajes()

    # 2) Crear Vista (le pasamos el modelo y la ventana)
    vista = Vista(modelo, ventana)

    # 3) Crear Controlador (le pasamos el modelo)
    controlador = Controlador(modelo)

    corriendo = True
    while corriendo:
        clock.tick(FPS)

        # a) Controlador maneja eventos
        controlador.manejar_eventos()

        # b) Modelo se actualiza
        modelo.actualizar()

        # c) Vista se sincroniza y pinta
        vista.update()
        vista.render()

    pygame.quit()


if __name__ == "__main__":
    main()
