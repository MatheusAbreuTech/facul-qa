# 3) Seja o código da função cubo a seguir:
# def cubo(x):
# returnx * x * X
# Dado o plano de teste com alguns casos de teste a seguir.
# cubo(x)
# #caso de teste Parâmetros de entrada Resultado esperado
# CT0001 X=0 0
# CT0002 x=1 1
# CT0003 x=2 8
# CТ0004 x=-2 -8
# CT0005 x=10 1000
# Pede-se:
# Escreva uma função de teste parametrizado para cada caso de teste.

import unittest


# ── Função sob teste ─────────────────────────────────────────────────────────
def cubo(x):
    return x * x * x


# ── Testes parametrizados ────────────────────────────────────────────────────
class TestCubo(unittest.TestCase):

    # subTest permite rodar todos os casos mesmo que um falhe,
    # mostrando qual caso de teste específico falhou.
    def test_casos_parametrizados(self):
        casos = [
            ("CT0001", 0,    0),
            ("CT0002", 1,    1),
            ("CT0003", 2,    8),
            ("CT0004", -2,  -8),
            ("CT0005", 10, 1000),
        ]

        for caso, x, esperado in casos:
            with self.subTest(caso=caso, x=x):
                resultado = cubo(x)
                self.assertEqual(
                    resultado, esperado,
                    f"[{caso}] cubo({x}): esperado {esperado}, obtido {resultado}"
                )

    # ── Um método por caso de teste (conforme enunciado) ─────────────────────
    def test_CT0001_x_zero(self):
        """CT0001 - cubo(0) deve retornar 0"""
        self.assertEqual(cubo(0), 0)

    def test_CT0002_x_um(self):
        """CT0002 - cubo(1) deve retornar 1"""
        self.assertEqual(cubo(1), 1)

    def test_CT0003_x_dois(self):
        """CT0003 - cubo(2) deve retornar 8"""
        self.assertEqual(cubo(2), 8)

    def test_CT0004_x_negativo(self):
        """CT0004 - cubo(-2) deve retornar -8"""
        self.assertEqual(cubo(-2), -8)

    def test_CT0005_x_dez(self):
        """CT0005 - cubo(10) deve retornar 1000"""
        self.assertEqual(cubo(10), 1000)


if __name__ == "__main__":
    unittest.main(verbosity=2)