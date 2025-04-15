from modelo.personajes.barriles import Barriles
from modelo.personajes.donkingkong import Donkingkong
from modelo.personajes.fondo import Fondo
from modelo.personajes.fuego import Fuego
from modelo.personajes.mario import Mario
from modelo.personajes.bloque import Bloque


class Modelo:
    def __init__(self):
        self.lista_personajes_logicos = []

    def iniciar_personajes(self):
        """
        Crea los personajes (Mario, Donkingkong, etc.) y bloques,
        y los agrega a la lista self.lista_personajes_logicos.
        """
        # Asegúrate de definir o importar ANCHO_VENTANA y ALTO_VENTANA
        # según tu proyecto; aquí están de ejemplo.
        ANCHO_VENTANA = 800
        ALTO_VENTANA = 600

        # Velocidad y dimensiones para Donkey Kong, fondo, etc.
        velocidad = 2
        pos_x_don = 70
        pos_y_don = 92
        ancho_don = 85
        alto_don = 95

        # Creamos los personajes principales:
        fondo = Fondo(
            posx=0,
            posy=0,
            scale_ancho=ANCHO_VENTANA,
            scale_alto=ALTO_VENTANA,
            velocidad=velocidad,  # Puedes dejarlo en 0 si tu fondo no se mueve
        )

        donkingkong = Donkingkong(
            posx=pos_x_don,
            posy=pos_y_don,
            scale_ancho=ancho_don,
            scale_alto=alto_don,
            velocidad=velocidad,
        )

        mario = Mario(
            posx=52, posy=493, scale_ancho=35, scale_alto=35, velocidad=velocidad
        )

        fuego = Fuego(posx=20, posy=386, scale_ancho=25, scale_alto=20, velocidad=1)
        fuego1 = Fuego(posx=320, posy=523, scale_ancho=25, scale_alto=20, velocidad=1)
        fuego2 = Fuego(posx=520, posy=463, scale_ancho=25, scale_alto=20, velocidad=1)

        barriles = Barriles(
            posx=1, posy=115, scale_ancho=55, scale_alto=68, velocidad=1
        )

        # Función para crear una lista de bloques en fila/columna
        def crear_lista_bloques(
            cantidad,
            clase_bloque,
            inicio_x,
            inicio_y,
            scale_ancho,
            scale_alto,
            espaciado_x=50,
            espaciado_y=0,
            velocidad=1,
        ):
            """
            Crea 'cantidad' de bloques, desplazados por espaciado_x e
            espaciado_y en cada iteración, y los devuelve en una lista.
            """
            lista = []
            for i in range(cantidad):
                x = inicio_x + i * espaciado_x
                y = inicio_y + i * espaciado_y
                bloque = clase_bloque(
                    posx=x,
                    posy=y,
                    scale_ancho=scale_ancho,
                    scale_alto=scale_alto,
                    velocidad=velocidad,
                )
                lista.append(bloque)
            return lista

        # Creamos las diferentes "filas" de bloques
        lista_bloques = crear_lista_bloques(
            cantidad=10,
            clase_bloque=Bloque,
            inicio_x=6,
            inicio_y=552,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=0,
            velocidad=1,
        )
        lista_bloques2 = crear_lista_bloques(
            cantidad=10,
            clase_bloque=Bloque,
            inicio_x=509,
            inicio_y=547,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=-5,
            velocidad=1,
        )
        lista_bloques3 = crear_lista_bloques(
            cantidad=14,
            clase_bloque=Bloque,
            inicio_x=6,
            inicio_y=464,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=2,
            velocidad=1,
        )
        lista_bloques4 = crear_lista_bloques(
            cantidad=14,
            clase_bloque=Bloque,
            inicio_x=61,
            inicio_y=418,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=-2,
            velocidad=1,
        )
        lista_bloques5 = crear_lista_bloques(
            cantidad=14,
            clase_bloque=Bloque,
            inicio_x=6,
            inicio_y=318,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=2,
            velocidad=1,
        )
        lista_bloques6 = crear_lista_bloques(
            cantidad=14,
            clase_bloque=Bloque,
            inicio_x=63,
            inicio_y=271,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=-2,
            velocidad=1,
        )
        lista_bloques7 = crear_lista_bloques(
            cantidad=12,
            clase_bloque=Bloque,
            inicio_x=4,
            inicio_y=190,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=0,
            velocidad=1,
        )
        lista_bloques8 = crear_lista_bloques(
            cantidad=3,
            clase_bloque=Bloque,
            inicio_x=604,
            inicio_y=190,
            scale_ancho=52,
            scale_alto=18,
            espaciado_x=50,
            espaciado_y=2,
            velocidad=1,
        )

        # Unimos todos los bloques en una lista
        lista_todos_los_bloques = (
            lista_bloques
            + lista_bloques2
            + lista_bloques3
            + lista_bloques4
            + lista_bloques5
            + lista_bloques6
            + lista_bloques7
            + lista_bloques8
        )

        # Creamos una sola lista de personajes
        lista_personajes = (
            []
            + lista_todos_los_bloques
            + [donkingkong, mario, fuego, fuego1, fuego2, barriles, fondo]
        )

        # Asignamos esa lista al atributo interno
        self.lista_personajes_logicos = lista_personajes

    def actualizar(self):
        """
        Llamado en cada frame: mueve personajes y chequea colisiones.
        """
        # 1) Mover personajes
        for personaje in self.lista_personajes_logicos:
            personaje.actualizar_posicion()

        # 2) Chequear colisiones
        for personaje in self.lista_personajes_logicos:
            if personaje.tipo == "mario" or personaje.tipo == "fuego":
                personaje.colisiona_con(self.get_personajes())

    def get_personajes(self):
        # Devolvemos la lista de personajes, por si la Vista los usa
        return self.lista_personajes_logicos
