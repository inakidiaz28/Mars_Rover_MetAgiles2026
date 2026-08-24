class Rover:
    def __init__(self, x, y, orientacion):
        self.x = x
        self.y = y
        self.orientacion = orientacion

    def posicion(self):
        return (self.x, self.y, self.orientacion)

    def girar_izquierda(self):
        orientaciones = ["N", "E", "S", "O"]  # orden horario
        indice_actual = orientaciones.index(self.orientacion)
        nuevo_indice = (indice_actual - 1) % 4
        self.orientacion = orientaciones[nuevo_indice]

    def girar_derecha(self):
        orientaciones = ["N", "E", "S", "O"]  # orden horario
        indice_actual = orientaciones.index(self.orientacion)
        nuevo_indice = (indice_actual + 1) % 4
        self.orientacion = orientaciones[nuevo_indice]
        
    def avanzar(self):
        if self.orientacion == "N":
            self.y += 1