class Rover:

    def __init__(self, x, y, orientacion):
        self.x = x
        self.y = y
        self.orientacion = orientacion

    def posicion(self):
        return (self.x, self.y, self.orientacion)