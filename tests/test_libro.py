import sys
import os
import unittest

from src.libro import Libro

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
        

    def test_libro_atributos(self):
        libro = Libro("Libro 1", 2001, "Autor 1", 300)
        self.assertEqual(libro.titulo, "Libro 1")
        self.assertEqual(libro.anio_publicacion, 2001)
        self.assertEqual(libro.autor, "Autor 1")
        self.assertEqual(libro.numero_paginas, 300)

    def test_libro_mostrar_info(self):
        libro = Libro("Libro 2", 2002, "Autor 2", 400)
        self.assertEqual(libro.mostrar_info(),
                         "Título: Libro 2\nAño de Publicación: 2002\nAutor: Autor 2\nNúmero de Páginas: 400")


if __name__ == '__main__':
    unittest.main()
