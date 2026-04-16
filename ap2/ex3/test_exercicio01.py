"""
d) Testes de unidade dos elementos web do form1.html
Executar com: python -m pytest test_form1.py -v
              ou: python test_form1.py
"""

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def _url_html() -> str:
    """Retorna a URL file:// do form1.html (mesmo diretório)."""
    dir_atual    = os.path.dirname(os.path.abspath(__file__))
    caminho_html = os.path.join(dir_atual, "exercicio01.html")
    return f"file:///{caminho_html.replace(os.sep, '/')}"


class TestExercicio01(unittest.TestCase):
    """Testes de unidade para os elementos web de exercicio01.html."""

    @classmethod
    def setUpClass(cls):
        """Abre o navegador UMA vez antes de todos os testes."""
        opcoes = Options()
        opcoes.add_argument("--headless")          # sem janela nos testes
        opcoes.add_argument("--disable-gpu")
        opcoes.add_argument("--no-sandbox")
        cls.driver = webdriver.Chrome(options=opcoes)
        cls.driver.get(_url_html())

    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após todos os testes."""
        cls.driver.quit()

    # ── a) Título ────────────────────────────────────────────────────
    def test_a_titulo_pagina(self):
        """Verifica se o título da página está correto."""
        titulo = self.driver.title
        self.assertEqual(titulo, "Exercício 01",
                         f"Título esperado 'Exercício 01', obtido '{titulo}'")

    # ── b) TAG_NAME ──────────────────────────────────────────────────
    def test_b_conteudo_por_tag_name(self):
        """Verifica o texto do parágrafo usando localizador TAG_NAME."""
        elemento = self.driver.find_element(By.TAG_NAME, "p")
        self.assertEqual(elemento.text, "O conteúdo do site vem aqui",
                         f"Texto inesperado via TAG_NAME: '{elemento.text}'")

    def test_b_paragrafo_existe_via_tag_name(self):
        """Verifica se o elemento <p> existe na página."""
        elementos = self.driver.find_elements(By.TAG_NAME, "p")
        self.assertGreater(len(elementos), 0,
                           "Nenhum elemento <p> encontrado na página.")

    # ── c) CSS_SELECTOR ──────────────────────────────────────────────
    def test_c_conteudo_por_css_selector(self):
        """Verifica o texto do parágrafo usando CSS_SELECTOR 'p.content'."""
        elemento = self.driver.find_element(By.CSS_SELECTOR, "p.content")
        self.assertEqual(elemento.text, "O conteúdo do site vem aqui",
                         f"Texto inesperado via CSS_SELECTOR: '{elemento.text}'")

    def test_c_classe_content_existe(self):
        """Verifica se existe um elemento com a classe 'content'."""
        elementos = self.driver.find_elements(By.CSS_SELECTOR, "p.content")
        self.assertGreater(len(elementos), 0,
                           "Nenhum elemento 'p.content' encontrado na página.")

    def test_c_atributo_class_correto(self):
        """Verifica se o atributo class do parágrafo é 'content'."""
        elemento = self.driver.find_element(By.CSS_SELECTOR, "p.content")
        classe = elemento.get_attribute("class")
        self.assertEqual(classe, "content",
                         f"Classe esperada 'content', obtida '{classe}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)