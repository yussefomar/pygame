import pygame
ancho=800
alto=600
color_blanco=(255,255,255)
color_negro=(0,0,0)
pygame.init()
# Creamos una superficie 
ventana = pygame.display.set_mode((ancho,alto))
# cargamos el fondo y una imagen (se crea objetos "Surface")
fondo = pygame.image.load("imagenesmono/fondomonito.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto)) 
donkingkong = pygame.image.load("imagenesmono/monito.png").convert()
donkingkong.set_colorkey(color_negro)
#dibuja en la ventana las superficies cargadas
ventana.blit(fondo, (0, 0))
ventana.blit(donkingkong , (35, 110))
pygame.display.flip()


jugando = True
while jugando:
    for evento in pygame.event.get():  # Captura eventos
        if evento.type == pygame.QUIT:  # Evento de cerrar ventana
            jugando = False
        elif evento.type == pygame.KEYDOWN:  # Tecla presionada
            print(f"Tecla presionada: {evento.key}")
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # Click del mouse
            print(f"Click en {evento.pos}")

pygame.quit()


 

 
