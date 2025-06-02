import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
EMAIL_TEST_MODE = os.getenv("EMAIL_TEST_MODE", "false").lower() == "true"

def send_alert(url, status, test_mode=EMAIL_TEST_MODE):
    subject = f"[ALERTA] Site fora do ar: {url}"
    body = f"O site {url} retornou status {status} e pode estar indisponível."

    if test_mode:
        print(f"[TESTE] Simulando envio de e-mail:\nAssunto: {subject}\nCorpo: {body}")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"✅ Alerta enviado para {RECIPIENT_EMAIL} sobre {url}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
