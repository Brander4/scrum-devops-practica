
import unittest
from calculadora import calcular_promedio


class TestCalculadora(unittest.TestCase):

    def test_calcular_promedio(self):
        resultado = calcular_promedio(80, 90, 100)
        self.assertEqual(resultado, 90)


if __name__ == "__main__":
    unittest.main()
