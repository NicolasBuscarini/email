import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


def carregar_configuracoes():
    """Carrega variáveis de ambiente conforme o ambiente definido."""
    ambiente = os.getenv("APP_ENV", "development")
    arquivo_env = f".env.{ambiente}"

    if not os.path.exists(arquivo_env):
        raise FileNotFoundError(f"Arquivo de ambiente '{arquivo_env}' não encontrado.")

    load_dotenv(dotenv_path=arquivo_env)

    return {
        "smtp_server": os.getenv("SMTP_SERVER"),
        "smtp_port": int(os.getenv("SMTP_PORT", 587)),
        "email_user": os.getenv("EMAIL_USER"),
        "email_password": os.getenv("EMAIL_PASSWORD"),
        "email_assunto": os.getenv("EMAIL_ASSUNTO"),
        "email_destinatarios": [
            destinatario.strip()
            for destinatario in os.getenv("EMAIL_DESTINATARIOS", "").split(",")
            if destinatario.strip()
        ]
    }


def carregar_corpo_email(caminho_arquivo: str) -> str:
    """Lê o corpo do e-mail de um arquivo de texto."""
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read().strip()


def enviar_email(destinatarios: list[str], assunto: str, corpo: str):
    """Envia um e-mail via Outlook/Office365 para uma lista de destinatários."""
    config = carregar_configuracoes()

    if not all([
        config["smtp_server"],
        config["smtp_port"],
        config["email_user"],
        config["email_password"]
    ]):
        raise EnvironmentError("Variáveis de ambiente de e-mail não configuradas corretamente.")

    mensagem = MIMEMultipart()
    mensagem["From"] = config["email_user"]
    mensagem["To"] = ", ".join(destinatarios)
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain", "utf-8"))

    with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as servidor:
        servidor.ehlo()
        servidor.starttls()
        servidor.ehlo()
        servidor.login(config["email_user"], config["email_password"])
        servidor.send_message(mensagem)
        print(f"E-mail enviado com sucesso para: {', '.join(destinatarios)}")


if __name__ == "__main__":
    config = carregar_configuracoes()
    corpo = carregar_corpo_email("body.txt")

    enviar_email(
        destinatarios=config["email_destinatarios"],
        assunto=config["email_assunto"],
        corpo=corpo
    )
