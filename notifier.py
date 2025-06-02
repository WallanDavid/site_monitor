import smtplib
from email.mime.text import MIMEText

# Configurações do remetente (substitua com suas credenciais reais)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "seu.email@gmail.com"          # ex: meu.bot@gmail.com
SENDER_PASSWORD = "sua_senha_de_app"          # senha de app do Gmail
RECIPIENT_EMAIL = "destinatario@gmail.com"    # para quem vai o alerta

def send_alert(url, status):
    subject = f"[ALERTA] Site fora do ar: {url}"
    body = f"O site {url} retornou status {status} e pode estar indisponível."

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
