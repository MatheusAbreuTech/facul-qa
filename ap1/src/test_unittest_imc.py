import unittest
from imc import calcular_imc

class TestIMC(unittest.TestCase):

    def test_type_error(self):
        # Testa se informar string na altura gera TypeError
        with self.assertRaises(TypeError):
            calcular_imc("1.75", 70, "João")
            
        # Testa se informar string no peso gera TypeError
        with self.assertRaises(TypeError):
            calcular_imc(1.75, "70", "João")

    def test_informando_dados_corretos(self):
        # Testa informando altura (1.75), peso (70kg) e nome ("João")
        # O IMC será ~22.86 (Peso normal)
        nome, classificacao = calcular_imc(1.75, 70, "João")
        
        self.assertEqual(nome, "João")
        self.assertEqual(classificacao, "Peso normal")

if __name__ == "__main__":
    unittest.main()