import unittest
from rover import Rover


class TestRover(unittest.TestCase):

    def test_informa_posicion_y_orientacion_inicial(self):
        rover = Rover(0, 0, "N")

        self.assertEqual(rover.posicion(), (0, 0, "N"))


if __name__ == "__main__":
    unittest.main()