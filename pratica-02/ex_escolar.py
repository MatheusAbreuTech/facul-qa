import unittest

#função: avaliar_notas

#entrada: Três notas obtidas por um aluno em provas e a média dos exercícios.
#saída: conceito (A, B, C ou D)
#Restrição: as notas n1, n2 e n3, assim como a média são valores entre 0,0 e 10,0.

def avaliar_notas(n1, n2, n3, media_exercicios):
    if n1 < 0 or n1 > 10:
        raise ValueError('Valor inválido para n1')

    if n2 < 0 or n2 > 10:
        raise ValueError('Valor inválido para n2')

    if n3 < 0 or n3 > 10:
        raise ValueError('Valor inválido para n3')

    if media_exercicios < 0 or media_exercicios > 10:
        raise ValueError('Valor inválido para media_exercicios')

    media_aproveitamento = (n1 + 2*n2 + 3*n3 + media_exercicios)/7

    if media_aproveitamento >= 9.0:
        return 'A'
    elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
        return 'B'
    elif media_aproveitamento >= 6.0 and media_aproveitamento < 7.5:
        return 'C'
    elif media_aproveitamento < 6.0:
        return 'D' 

class TestEscolar(unittest.TestCase):
    def test_notes_negatives_incorrects(self):
         self.assertRaises(ValueError, avaliar_notas, -1, 0, 0, 0)
         self.assertRaises(ValueError, avaliar_notas, 0, -1, 0, 0)
         self.assertRaises(ValueError, avaliar_notas, 0, 0, -1, 0)
    
    def test_correct_media(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')
        self.assertEqual(avaliar_notas(9, 9, 9, 9), 'A')
        self.assertEqual(avaliar_notas(8.9, 8.9, 8.9, 8.9), 'B')
        self.assertEqual(avaliar_notas(7.5, 7.5, 7.5, 7.5), 'B')
        self.assertEqual(avaliar_notas(7.4, 7.4, 7.4, 7.4), 'C')
        self.assertEqual(avaliar_notas(6, 6, 6, 6), 'C')
        self.assertEqual(avaliar_notas(5.9, 5.9, 5.9, 5.9), 'D')
        self.assertEqual(avaliar_notas(0, 0, 0, 0), 'D')

if __name__ == '__main__':
    unittest.main()
