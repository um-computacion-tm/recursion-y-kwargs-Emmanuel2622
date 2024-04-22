import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

class TestFibonacci(unittest.TestCase):
    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

class TestFibonacci(unittest.TestCase):
    def test_3(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)

class TestFibonacci(unittest.TestCase):
    def test_4(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)

class TestFibonacci(unittest.TestCase):
    def test_5(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)

class TestFibonacci(unittest.TestCase):
    def test_6(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)

class TestFibonacci(unittest.TestCase):
    def test_7(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 21)

class TestFibonacci(unittest.TestCase):
    def test_8(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34)

class TestFibonacci(unittest.TestCase):
    def test_9(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)

class TestFibonacci(unittest.TestCase):
    def test_10(self):
        resultado = fibonacci(11)
        self.assertEqual(resultado, 89)
unittest.main()