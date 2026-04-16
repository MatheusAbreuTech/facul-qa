# Para este exercício, crie um arquivo exercicio01.html conforme o código a
# seguir:
# exercicio01.html

# &lt;html&gt;
# &lt;title&gt;Exercício 01&lt;/title&gt;
# &lt;body&gt;
# &lt;p class=&quot;content&quot;&gt;O conteúdo do site vem aqui&lt;/p&gt;
# &lt;/form&gt;
# &lt;/body&gt;
# &lt;/html&gt;

# Pede-se:
# a) Escreva um script que leia o arquivo local exercicio01.html, mostre o título da
# página.
# b) Após finalizar o item a), mostre o conteúdo do parágrafo, utilizando o
# localizador TAG_NAME.
# c) Após finalizar o item b), mostre o conteúdo do parágrafo, utilizando o
# localizador CSS_SELECTOR com o seletor &#39;p.content&#39;.
# d) Criar um arquivo chamado test_exercicio01.py que realiza o teste de unidade dos
# elementos web do arquivo local exercicio01.html.


"""
Exercício 01 - Selenium
a) Lê o arquivo local exercicio01.html e mostra o título da página.
b) Mostra o conteúdo do parágrafo usando TAG_NAME.
c) Mostra o conteúdo do parágrafo usando CSS_SELECTOR 'p.content'.
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def abrir_driver() -> webdriver.Chrome:
    opcoes = Options()
    opcoes.add_argument("--start-maximized")
    # opcoes.add_argument("--headless")  # descomente para rodar sem janela
    return webdriver.Chrome(options=opcoes)


def main():
    # Monta o caminho absoluto para o HTML (mesmo diretório do script)
    dir_atual    = os.path.dirname(os.path.abspath(__file__))
    caminho_html = os.path.join(dir_atual, "exercicio01.html")
    url          = f"file:///{caminho_html.replace(os.sep, '/')}"

    driver = abrir_driver()

    try:
        driver.get(url)
        time.sleep(1)

        # ── a) Título da página ──────────────────────────────────────
        titulo = driver.title
        print(f"[a] Título da página : '{titulo}'")
        time.sleep(0.8)

        # ── b) Conteúdo do parágrafo via TAG_NAME ────────────────────
        paragrafo_tag = driver.find_element(By.TAG_NAME, "p")
        print(f"[b] TAG_NAME        : '{paragrafo_tag.text}'")
        time.sleep(0.8)

        # ── c) Conteúdo do parágrafo via CSS_SELECTOR ────────────────
        paragrafo_css = driver.find_element(By.CSS_SELECTOR, "p.content")
        print(f"[c] CSS_SELECTOR    : '{paragrafo_css.text}'")
        time.sleep(0.8)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()