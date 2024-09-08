import sys
import os
import unittest

from src.publicacion import Publicacion

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
    def test_publicacion_atributos(self):
        pub = Publicacion("Publicacion 1", 2000)
        self.assertEqual(pub.titulo, "Publicacion 1")
        self.assertEqual(pub.anio_publicacion, 2000)

    def test_publicacion_mostrar_info(self):
        pub = Publicacion("Publicacion 2", 2010)
        self.assertEqual(pub.mostrar_info(), "Título: Publicacion 2\nAño de Publicación: 2010")


if __name__ == '__main__':
    unittest.main()
