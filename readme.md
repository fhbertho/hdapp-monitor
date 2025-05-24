# 🔍 Health Check Automático com Notificações

Este é um projeto simples e eficiente em Python para **verificar a disponibilidade de serviços web ou IPs** e **enviar alertas em caso de falha**, com logs e execução automática agendada.

---

## 🚀 Funcionalidades

- ✅ Verifica a disponibilidade de serviços HTTP (GET)
- ⚠️ Detecta falhas por status HTTP diferente de 200 ou timeout
- 📢 Envia alertas via Telegram
- 🕒 Executa periodicamente (agendado por código ou cron)
- 📜 Gera logs detalhados em arquivo
- 🔧 Configurável via arquivo `.env` e `config.yaml`

---

## 🧱 Estrutura do Projeto

healthcheck/
├── main.py # Código principal
├── config.yaml # Configurações dos serviços a monitorar
├── .env # Variáveis sensíveis (ex: token do Telegram)
├── requirements.txt # Bibliotecas necessárias
├── logs/
│ └── healthcheck.log # Logs com status dos serviços
└── README.md # Este arquivo


---

## ⚙️ Como Funciona

1. O script lê uma lista de URLs ou IPs do `config.yaml`.
2. Para cada serviço, ele faz um **request HTTP GET**.
3. Se a resposta não for 200 ou houver timeout, um alerta é enviado via Telegram.
4. Os resultados (sucesso/falha) são registrados com timestamp no arquivo de log.
5. O processo roda automaticamente em intervalos definidos (ex: a cada 5 minutos).

---

## ✅ Pré-requisitos

- Python 3.8+
- Conta no Telegram e um bot criado via [@BotFather](https://t.me/BotFather)
- Biblioteca `requests`, `python-dotenv`, `PyYAML`, `schedule`

---

## 🧪 Instalação

```bash
git clone https://github.com/seu-usuario/healthcheck-notifier.git
cd healthcheck-notifier
pip install -r requirements.txt

🔐 Configuração

TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id

config.yaml

intervalo: 5  # em minutos
servicos:
  - nome: Google
    url: https://www.google.com
  - nome: Meu site
    url: https://meusite.com


▶️ Como Executar
    python main.py


Melhorias Futuras
Suporte a outros métodos (ping, TCP, etc.)

Interface web para status em tempo real

Notificações por Slack ou Discord

Desenvolvido por @fhbertho em Colab @JM-Spinelli