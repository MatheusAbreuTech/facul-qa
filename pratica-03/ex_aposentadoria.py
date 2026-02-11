import unittest

REQUERER = 'Requerer aposentadoria'  
NAO_REQUERER = 'Não requerer'

def verificar_qualificacao_empregado(idade, tempo_de_servico):
    if type(idade) == int and type(tempo_de_servico) == int:
        if idade >= 65:
             return REQUERER
        elif tempo_de_servico >= 30:
            return REQUERER
        elif idade >= 60 and tempo_de_servico >= 25:
            return REQUERER
    
        return NAO_REQUERER
    else:
        raise TypeError(f'tipo incompatível')
        
class TestAposentadoria(unittest.TestCase):

    def test_verificar_qualificacao_empregado(self):
        self.assertEqual(verificar_qualificacao_empregado(0, 10), NAO_REQUERER)
        self.assertEqual(verificar_qualificacao_empregado(20, 0), NAO_REQUERER)

        self.assertRaises(TypeError, verificar_qualificacao_empregado, '65', 30)
        self.assertRaises(TypeError, verificar_qualificacao_empregado, 65, '30')
        self.assertEqual(verificar_qualificacao_empregado(65, 20), REQUERER)
        self.assertEqual(verificar_qualificacao_empregado(59, 30), REQUERER)
        self.assertEqual(verificar_qualificacao_empregado(60, 25), REQUERER)
        self.assertEqual(verificar_qualificacao_empregado(59, 24), NAO_REQUERER)

if __name__ == '__main__':
    unittest.main()