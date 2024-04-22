import unittest
from kwargs import buscador_datos
from kwargs import db

class test_kwargs(unittest.TestCase):
    
    def test_1(self):
        result = buscador_datos("Pablo", "Diego", "Maradona", "Messi", **db)
        self.assertEqual(result, {'Persona 0': {'primer_nombre': 'Pablo', 'segundo_nombre': 'Diego', 'primer_apellido': 'Maradona', 'segundo_apellido': 'Messi'}})

    def test_2(self):
        result = buscador_datos("Jose", "Lucas", "Mosca", "Nono", **db)
        self.assertEqual(result, {'Persona  1': {'primer_nombre': 'Jose', 'segundo_nombre': 'Lucas', 'primer_apellido': 'Mosca', 'segundo_apellido': 'Nono'}})

    def test_3(self):
        result = buscador_datos("Jose", **db)
        self.assertEqual(result, {})

    def test_4(self):
        result = buscador_datos("Jose", "Lucas", "Maradona", "Messi", **db)
        self.assertEqual(result, {})

    def test_5(self):
        result = buscador_datos("Jose", "Pedro", "Rodriguez", "Luca", **db)
        self.assertEqual(result, {'Persona  2': {'primer_nombre': 'Jose', 'segundo_nombre': 'Pedro', 'primer_apellido': 'Rodriguez', 'segundo_apellido': 'Luca'}})
unittest.main()