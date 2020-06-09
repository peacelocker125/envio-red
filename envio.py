import smtplib
import os
import docx
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviar_red(arquivos, sender_address, sender_pass, mail_content, session, title):
    for file in arquivos:
        if file.name.endswith('.docx') and  file.is_file():
            doc = docx.Document(file.name)
            receiver_address = doc.paragraphs[-1].text
            message = MIMEMultipart()
            message['From'] =  sender_address
            message['To'] = receiver_address
            message['Subject'] = title
            message.attach(MIMEText(mail_content, 'plain'))
            payload = MIMEBase('application', 'octate-stream')
            attach_file = open(file.name, 'rb')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=file.name)
            message.attach(payload)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
