import envio
import os
import smtplib

pasta = os.chdir("Coloca o caminho para a pasta, tipo C:\Users\Family Member\Documents\RedCorrigidas") 
arquivos = os.scandir(pasta)
sua_conta = 'email@exemplo.com'
sua_senha = 'senha do e-mail'
mensagem = '''
Escreva um mensagem aqui, pode apertar enter se quiser mais de uma linha :)

Tipo assim ;)
'''
titulo = 'Escreva um título para o e-mail'


session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sua_conta, sua_senha)

envio.enviar_red(arquivos, sua_conta, sua_senha, mensagem, session, titulo)

session.quit()
