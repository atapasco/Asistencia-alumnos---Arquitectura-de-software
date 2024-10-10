import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

timers = {}

def send_email(user_id, fecha):
    sender_email = "lalechecongalletas21@gmail.com"
    sender_password = "ajlq dedy pxpz xvcd"

    recipient_email = user_id
    subject = "Aviso de asistencia"
    body = f"Se registro una falla el dia: {fecha} por favor comunicarse con el profesor responsable."

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Correo enviado a {recipient_email}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


def timer_finished(user_id):
    send_email(user_id)
    del timers[user_id]


def start_timer(user_id):
    if user_id in timers:
        print(f"Ya hay un temporizador activo para el usuario {user_id}")
        return

    timer = threading.Timer(3600, timer_finished, [user_id]) 
    timers[user_id] = timer
    timer.start()
    print(f"Temporizador iniciado para el usuario {user_id}")


def cancel_timer(user_id):
    if user_id in timers:
        timers[user_id].cancel()
        del timers[user_id]
        print(f"Temporizador cancelado para el usuario {user_id}")
    else:
        print(f"No hay temporizador activo para el usuario {user_id}")


