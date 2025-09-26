import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
puerto = 587
usuario = "abelinomoises@gmail.com"
password = "mpbx spvs nhxd lxrn"
destinatario = "smss217724@ugb.edu.sv"
mensaje = MIMEMultipart('alternative')
mensaje["From"] = usuario
mensaje["To"] = destinatario
mensaje["Subject"] = "Probando el uso de MIME"
cuerpo = "Este es un correo por MIME"
texto = MIMEText(cuerpo, 'plain')
mensaje.attach(texto)
html = ""  \
"<html"  \
"<body>" \
"<h1> Hola! <\h1>" \
"<p> Este correo se puede dinamizar por medio del html </p>" \
"<img src= 'https://ugb.edu.sv/https-ugb-edu-sv/campus1/.png'><img>"
"</body>"
"</html>"
""

texto_html = MIMEText(html,'html')
mensaje.attach(texto_html)



server = smtplib.SMTP(host, puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario, mensaje.as_string())
server.quit()
print('Mensaje enviado')



