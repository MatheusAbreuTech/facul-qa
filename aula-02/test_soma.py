import unittest

def soma(a,b):
    return a+b

class TestSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10, 20), 30)
        self.assertEqual(soma(10, 225), 235)

if __name__ == '__main__':
    unittest.main()