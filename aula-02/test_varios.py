
import unittest

# Função que queremos testar
def soma(a, b):
    return a + b

# Classe de testes
class TesteSoma(unittest.TestCase):

    # ct01 - teste correto
    def test_soma_correta(self):
        resultado = soma(10, 20)
        self.assertEqual(resultado, 30)   # verifica se resultado == 30

    # ct02 - teste que deve falhar
    def test_soma_errada(self):
        resultado = soma(10, 225)
        self.assertNotEqual(resultado, 30)   # esse vai falhar de propósito

# Executa os testes
if __name__ == "__main__":
    unittest.main()
    