from extract_data import extrair_dados
from upload_data import enviar_dados

def start():
    resultados = extrair_dados()
    enviar_dados(resultados)
if __name__ == "__main__":
    start()
