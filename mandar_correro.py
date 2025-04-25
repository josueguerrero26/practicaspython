import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    email = ""
    password = ""
    to_email = ""
    subject = "Prueba"
    message = "Este es un mensaje de prueba"
    msg = MIMEMultipart()
    msg["From"] = email 
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, to_email, text)
    server.quit()

if __name__ == "__main__":
    send_email()