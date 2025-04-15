class Rectangulo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

    def actualizar(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return (
            f"Rectangulo(x={self.x}, y={self.y}, ancho={self.ancho}, alto={self.alto})"
        )
