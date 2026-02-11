import unittest

def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError(f'tipo incompatível')
    
class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual (soma(10, 5), 15)

    def test_excecao_tipo_incompativel(self):
        self.assertRaises(TypeError, soma, 10, '5')

    def test_excecao_tipo_float(self):
        self.assertRaises(TypeError, soma, 10.554, 5.12)

    def test_excecao_tipo_Boolean(self):
        self.assertRaises(TypeError, soma, True, False)

if __name__ == '__main__':
    unittest.main()

