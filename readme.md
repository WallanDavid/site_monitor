# 🌐 Monitor de Sites com Python + Dash

Ferramenta para monitorar a disponibilidade de sites (uptime), tempo de resposta e gerar alertas por e-mail em caso de falha. Com painel visual em Dash + exportação em CSV + Docker + histórico em SQLite.

![badge](https://img.shields.io/badge/Status-Online-brightgreen)
![badge](https://img.shields.io/badge/Monitoramento-Dash-blue)
![badge](https://img.shields.io/badge/Banco-SQLite-yellow)

---

## 🚀 Funcionalidades

- Verifica status HTTP de múltiplos sites
- Mede tempo de resposta (latência)
- Calcula percentual de uptime
- Exporta histórico em CSV
- Salva dados em `SQLite`
- Painel web com Dash
- Alerta por e-mail em caso de falha

---

## 📷 Interface

![screenshot](docs/screenshot.png) <!-- opcional -->

---

## 🛠 Tecnologias

- Python 3.10+
- Dash + Flask
- SQLite
- Pandas + Requests
- Docker

---

## ▶️ Executando localmente

```bash
git clone https://github.com/WallanDavid/site_monitor.git
cd site_monitor
python -m venv venv
venv\Scripts\activate   # ou source venv/bin/activate
pip install -r requirements.txt
python main.py
