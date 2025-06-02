# 🌐 Monitor de Sites com Python, Dash, SQLite e Docker

Painel interativo que monitora a disponibilidade (uptime), tempo de resposta e gera alertas por e-mail em caso de falha. Interface em Dash, persistência com SQLite, exportação em CSV e empacotado via Docker.

![badge](https://img.shields.io/badge/Status-Online-brightgreen)
![badge](https://img.shields.io/badge/Monitoramento-Dash-blue)
![badge](https://img.shields.io/badge/Banco-SQLite-yellow)
![badge](https://img.shields.io/badge/Docker-Suportado-informational)

---

## 🚀 Funcionalidades

- ✅ Verifica status HTTP de sites
- ✅ Mede tempo de resposta (latência)
- ✅ Calcula percentual de uptime
- ✅ Salva histórico em banco SQLite
- ✅ Exporta histórico em CSV (`/export`)
- ✅ Envia alerta por e-mail (configurável via `.env`)
- ✅ Painel web com Dash (porta 8050)
- ✅ Totalmente dockerizado

---

## 🧪 Prévia

| URL                  | Status | Tempo (s) | Uptime (%) |
|----------------------|--------|-----------|------------|
| <https://google.com>   | 200    | 0.123     | 100.0%     |
| <https://sitefake.xyz> | DOWN   | -         | 0.0%       |

---

## 📁 Estrutura

```
site_monitor/
├── main.py              # Painel Dash
├── monitor.py           # Verificação e gravação
├── notifier.py          # Envio de alerta por e-mail
├── sites.json           # Lista de sites monitorados
├── monitor.db           # Banco SQLite local
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example         # Exemplo de configuração
└── README.md
```

---

## ▶️ Como executar localmente (sem Docker)

```bash
git clone https://github.com/WallanDavid/site_monitor.git
cd site_monitor

# Cria ambiente virtual
python -m venv venv
venv\Scripts\activate         # ou source venv/bin/activate

# Instala dependências
pip install -r requirements.txt

# Cria arquivo .env com suas credenciais
cp .env.example .env
```

---

## 🐳 Como rodar com Docker

```bash
docker compose up --build
```

Acesse em: [http://localhost:8050](http://localhost:8050)

---

## 📤 Exportar CSV

Acesse no navegador:

```
http://localhost:8050/export
```

---

## 💌 Alerta por e-mail

Sempre que um site estiver fora do ar (`status != 200`), um e-mail será enviado automaticamente para o destinatário configurado.

---

## 🔐 Configuração do `.env`

Crie um arquivo `.env` com base no modelo `.env.example`:

```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=seu.email@gmail.com
SENDER_PASSWORD=sua_senha_de_app
RECIPIENT_EMAIL=alerta@destinatario.com
EMAIL_TEST_MODE=true
```

| Variável         | Descrição                                       |
|------------------|-------------------------------------------------|
| SMTP_SERVER      | Servidor SMTP (ex: smtp.gmail.com)              |
| SMTP_PORT        | Porta SMTP (geralmente 587)                     |
| SENDER_EMAIL     | E-mail do remetente (precisa de senha de app)   |
| SENDER_PASSWORD  | Senha de app (ex: gerada no Gmail)              |
| RECIPIENT_EMAIL  | Quem receberá o alerta                          |
| EMAIL_TEST_MODE  | `true` para simular, `false` para enviar real   |

---

## ✅ Próximas melhorias

- Agendamento automático com `APScheduler`
- Gráficos de uptime com Plotly
- Painel com login
- Deploy gratuito (Railway, Render)

---

Feito com 💻 por [Wallan David](https://github.com/WallanDavid)
