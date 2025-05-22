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
└── README.md 


---

## 🚀 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/fhbertho/hdapp-monitor.git
cd hdapp-monitor

2. Crie e preencha o .env com seu bot e chat ID do Telegram:

ini
Copiar
Editar
TELEGRAM_BOT_TOKEN=seu_token
TELEGRAM_CHAT_ID=seu_chat_id

3. Edite o config.yaml com os serviços que quer monitorar:

yaml
Copiar
Editar
intervalo: 1  # minutos
servicos:
  - nome: Google
    url: https://www.google.com
  - nome: GitHub
    url: https://www.github.com

4. Instale os pacotes necessários:

bash
Copiar
Editar
pip install -r requirements.txt

5. Rode o script:

bash
Copiar
Editar
python main.py


Melhorias Futuras
Suporte a outros métodos (ping, TCP, etc.)

Interface web para status em tempo real

Notificações por Slack ou Discord

Desenvolvido por @fhbertho.
