import smtplib
import ssl
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = "smtp.gmail.com"
port = 465

username = config['EMAIL']['LOGIN']
email_pass = config['EMAIL']['PASSWORD']


def send_message_by_email(message: str) -> tuple:
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(username, email_pass)
            server.sendmail(username, username, message)

        return True, 0
    except Exception as e:
        return False, e
