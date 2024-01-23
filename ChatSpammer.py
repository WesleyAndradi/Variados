import pyautogui as spam
import time

#Coloque o numero de mensagens e logo em seguida a quantidade desejada
limite_msg = input("Enter n de msgs: ")
msg = input("Coloque a msg: ")

#tempo de envio da mensagem
i = 0

#Tempo especificado até o programa começar a rodar 
time.sleep(3)

#Automatização
while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

    i+=1
