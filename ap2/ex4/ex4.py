# Bora Selenium - 04 de 04 da AP2
# 1 . Montar uma tela html com os seguintes elementos
# Observação: Não será aceito html igual ao de outro aluno

# Título – Avaliação disciplina automação de teste de software
# Nome – Texto
# RA – Texto
# Data de nascimento – Separado Dia / Mês / Ano
# Lista Curso – Opções (Análise e desenvolvimento de Sistemas ou Sistemas de
# Informação)
# Lista Aproveitamento do conteúdo – De Zero a Dez
# Sugestões de melhoria próximas turmas - Texto
# Observações – texto (não obrigatório)
# Enviar Feedback – Botão
# 2. Interação com elementos da página web
# Utilizando os localizadores, realize o cadastro da avaliação (não necessário criação de
# banco de dados, apenas a interação com a página.
# Utilize time.sleep(0.8) entre os elementos
# Entrega:
#  Print do formulário
#  Fonte py e html
#  Subir tudo em um único arquivo zip

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


# ─────────────────────────────────────────────
# DADOS DO ALUNO 
# ─────────────────────────────────────────────
DADOS = {
    "nome":          "Matheus Santos de Abreu",
    "ra":            "2400733",
    "dia":           "12",
    "mes":           "04",
    "ano":           "2004",
    "curso":         "ADS",       
    "nota":          "10",          
    "sugestoes":     "Ensinar sobre outras ferramenta de testes, como Cypress.",
    "observacoes":   "A disciplina atendeu bem às expectativas do mercado.",
}
# ─────────────────────────────────────────────


def abrir_navegador() -> webdriver.Chrome:
    """Abre o Chrome em modo janela normal."""
    opcoes = Options()
   
    opcoes.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opcoes)
    return driver


def preencher_formulario(driver: webdriver.Chrome, dados: dict) -> None:
    """Preenche todos os campos do formulário usando os localizadores."""

    # ── NOME ────────────────────────────────────
    print("[1/8] Preenchendo nome...")
    campo_nome = driver.find_element(By.ID, "nome")
    campo_nome.clear()
    campo_nome.send_keys(dados["nome"])
    time.sleep(0.8)

    # ── RA ──────────────────────────────────────
    print("[2/8] Preenchendo RA...")
    campo_ra = driver.find_element(By.ID, "ra")
    campo_ra.clear()
    campo_ra.send_keys(dados["ra"])
    time.sleep(0.8)

    # ── CURSO ───────────────────────────────────
    print("[6/8] Selecionando Curso...")
    select_curso = Select(driver.find_element(By.ID, "curso"))
    select_curso.select_by_value(dados["curso"])
    time.sleep(0.8)

    # ── DATA DE NASCIMENTO ───────────────────────
    print("[3/8] Selecionando Dia de nascimento...")
    select_dia = Select(driver.find_element(By.ID, "dia"))
    select_dia.select_by_value(dados["dia"])
    time.sleep(0.8)

    print("[4/8] Selecionando Mês de nascimento...")
    select_mes = Select(driver.find_element(By.ID, "mes"))
    select_mes.select_by_value(dados["mes"])
    time.sleep(0.8)

    print("[5/8] Selecionando Ano de nascimento...")
    select_ano = Select(driver.find_element(By.ID, "ano"))
    select_ano.select_by_value(dados["ano"])
    time.sleep(0.8)

    # ── APROVEITAMENTO (radio button) ────────────
    print("[7/8] Selecionando nota de aproveitamento:", dados["nota"])
    radio_nota = driver.find_element(
        By.CSS_SELECTOR, f'input[name="aproveitamento"][value="{dados["nota"]}"]'
    )
    driver.execute_script("arguments[0].click();", radio_nota)
    time.sleep(0.8)

    # ── SUGESTÕES ────────────────────────────────
    print("[8/8] Preenchendo sugestões de melhoria...")
    campo_sugestoes = driver.find_element(By.ID, "sugestoes")
    campo_sugestoes.clear()
    campo_sugestoes.send_keys(dados["sugestoes"])
    time.sleep(0.8)

    # ── OBSERVAÇÕES (opcional) ───────────────────
    if dados.get("observacoes"):
        print("[+] Preenchendo observações...")
        campo_obs = driver.find_element(By.ID, "observacoes")
        campo_obs.clear()
        campo_obs.send_keys(dados["observacoes"])
        time.sleep(0.8)

    # ── ENVIAR ───────────────────────────────────
    print("[→] Clicando em Enviar Feedback...")
    btn_enviar = driver.find_element(By.ID, "btn-enviar")
    btn_enviar.click()
    time.sleep(0.8)

    print("\n✓ Formulário enviado com sucesso!\n")


def main() -> None:
    dir_atual  = os.path.dirname(os.path.abspath(__file__))
    caminho_html = os.path.join(dir_atual, "form.html")
    url = f"file:///{caminho_html.replace(os.sep, '/')}"

    print("=" * 55)
    print("  AP2 - Automação de Teste de Software")
    print("  Selenium - Preenchimento de Formulário")
    print("=" * 55)
    print(f"\nAbrindo: {url}\n")

    driver = abrir_navegador()

    try:
        driver.get(url)
        time.sleep(1.5)

        preencher_formulario(driver, DADOS)

        print("Aguardando 3 s para visualização do resultado...")
        time.sleep(3)

    except Exception as erro:
        print(f"\n✗ Erro durante a execução: {erro}")
        raise

    finally:
        driver.quit()
        print("Navegador fechado. Fim da execução.")


if __name__ == "__main__":
    main()