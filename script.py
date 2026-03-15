from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import time

# ============ CONFIGURAÇÃO GOOGLE SHEETS ============
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
gc = gspread.authorize(creds)

ID_PLANILHA = "1atEG5uT1ue1xqjISAfNwEysbdLohf32TnBnu-yp-NLk"
sh = gc.open_by_key(ID_PLANILHA)

# Cria ou acessa aba com a data de hoje
data_hoje = datetime.now().strftime("%d-%m-%Y")
try:
    aba = sh.worksheet(data_hoje)
except gspread.exceptions.WorksheetNotFound:
    aba = sh.add_worksheet(title=data_hoje, rows="1000", cols="5")
    aba.append_row(["Ativo", "Preço", "Hora"])  # cabeçalho

# ============ SELENIUM ============
print("Abrindo Navegador.....")
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/finance/?hl=pt")
navegador.maximize_window()
time.sleep(8)

ativos = ["PETR4", "VALE3", "ITUB4", "TAEE11", "BBDC4", "BBAS3", "BPAC11", "EMBJ3", "Bitcoin", "Ethereum", "RADL3"]

def gerar_ativos(lista):
    for ativo in lista:
        yield ativo

meu_gerador = gerar_ativos(ativos)
wait = WebDriverWait(navegador, 15)
resultados = {}

while True:
    try:
        ativo = next(meu_gerador)
        navegador.get("https://www.google.com/finance/?hl=pt")
        time.sleep(3)

        barras = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Ax4B8"))
        )
        barra_pesquisa = barras[1]
        wait.until(EC.element_to_be_clickable(barra_pesquisa))
        barra_pesquisa.click()
        barra_pesquisa.clear()
        barra_pesquisa.send_keys(ativo)
        barra_pesquisa.send_keys(Keys.RETURN)
        time.sleep(5)

        container = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "AHmHk"))
        )
        preco_raw = container.find_element(By.CLASS_NAME, "YMlKec").text
        hora = datetime.now().strftime("%H:%M:%S")

        resultados[ativo] = preco_raw
        print(f"[{hora}] {ativo} | Preço: {preco_raw}")

        # ✅ Adiciona nova linha a cada execução
        aba.append_row([ativo, preco_raw, hora])

    except StopIteration:
        break
    except Exception as e:
        print(f"Erro ao capturar {ativo}: {e}")
        resultados[ativo] = "Erro"
        aba.append_row([ativo, "Erro", datetime.now().strftime("%H:%M:%S")])

print("\n✅ Resultados finais:")
for k, v in resultados.items():
    print(f"{k}: {v}")

navegador.quit()