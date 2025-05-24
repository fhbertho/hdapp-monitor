import requests 
import yaml
import time 
import logging
import os
from dotenv import load_dotenv  

#carrega variaveis de ambiente
load_dotenv()

# Configurações de logging
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/healthcheck.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Função carregar arquivo de configuração    
def carregar_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)
    
#Função para verificar o status do serviço
def verificar_servico(nome, url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            logging.info(f"[OK] {nome} está online ({url})")
        else:
            logging.warning(f"[FAIL] {nome} retornou status {resposta.status_code}")
            enviar_alerta(f"[ALERTA] {nome} retornou status {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"[ERROR] {nome} está offline - {e}")
        enviar_alerta(f"[ALERTA] {nome} está offline - {e}")

#Função para enviar alerta
def enviar_alerta(mensagem):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        logging.warning("Token ou Chat ID do Telegram não configurados.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensagem}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            logging.error(f"Erro ao enviar alerta Telegram: {response.text}")
    except Exception as e:
        logging.error(f"Exceção ao enviar alerta Telegram: {e}")

#Função principal
def main():
    config = carregar_config()
    intervalo = config.get("intervalo", 5)
    servicos = config.get("servicos", [])

    while True:
        for servico in servicos:
            nome = servico.get("nome")
            url = servico.get("url")
            if nome and url:
                verificar_servico(nome, url)
        time.sleep(intervalo * 30)

enviar_alerta("🚨 Teste de alerta Telegram funcionando!")

if __name__ == "__main__":
    main()