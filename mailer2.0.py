from email.message import EmailMessage
import smtplib

remitente = "josezurita1991@gmail.com"
destinatario = input("Escribe el correo del destinatario: ")
mensaje = input("Escribe el mensaje: ")

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = input("Escribe el asunto: ")
email.set_content(mensaje,)# subtype="html")

# with open("texto.txt", "rb") as f:
#     email.add_attachment(
#         f.read(),
#         filename="texto.txt",
#         maintype="text",
#         subtype="txt"
#     )

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "yktmvqgxrbirrafy")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
