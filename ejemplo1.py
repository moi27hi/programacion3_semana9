import smtplib


HOST = "smtp.gmail.com" 
Puerto = 587
USUARIO = "abelinomoises@gmail.com"
PASS = "mpbx spvs nhxd lxrn"


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