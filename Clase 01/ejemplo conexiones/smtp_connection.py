import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Este es el cuerpo del correo electrónico")
msg["Subject"] = "Asunto del correo electrónico"
msg["From"] = "from@example.com"
msg["To"] = "to@example.com"

smtp = smtplib.SMTP("smtp.google.com", 587)
smtp.starttls()
smtp.login("user", "password")
smtp.send_message(msg)
smtp.quit()
