import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("HOST")
Puerto = os.getenv("Puerto")
USUARIO = os.getenv("USUARIO")
PASS = os.getenv("PASS")


destinatario = ["rubiomoises27@icloud.com ", "yimu2104@gmail.com", "04karenportillo@gmail.com"] 
asunto  = "Prueba de correo"
cuerpo = "Este es un correo de prueba enviado desde Python. Que tengas un buen dia!"
mensaje = f"Subject: {asunto}\n\n{cuerpo}"


# 
server = smtplib.SMTP(HOST, Puerto)
server.starttls()
server.login(USUARIO, PASS)
server.sendmail(USUARIO, destinatario, mensaje)
server.quit()
print("Correo enviado con exito") 