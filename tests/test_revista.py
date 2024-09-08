import sys
import os
import unittest

from src.revista import Revista

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
        
    def test_revista_atributos(self):
        revista = Revista("Revista 1", 2021, 101, "Nombre Revista 1")
        self.assertEqual(revista.titulo, "Revista 1")
        self.assertEqual(revista.anio_publicacion, 2021)
        self.assertEqual(revista.numero_revista, 101)
        self.assertEqual(revista.nombre_revista, "Nombre Revista 1")

    def test_revista_mostrar_info(self):
        revista = Revista("Revista 2", 2022, 102, "Nombre Revista 2")
        self.assertEqual(revista.mostrar_info(),
                         "Título: Revista 2\nAño de Publicación: 2022\nNúmero de la Revista: 102\nNombre de la Revista: Nombre Revista 2")

if __name__ == '__main__':
    unittest.main()
