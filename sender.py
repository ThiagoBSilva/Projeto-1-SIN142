# -*- coding: utf-8 -*-
#Importando as bibliotecas necessárias
import random
import signal
import os
import sys
import time

#Recebe o PID do processo receptor
while True:
    pid = int(input("Insira o PID do receiver: "))

    #Verifica se um processo com tal PID existe
    try:
        os.kill(pid, 0)
    except OSError:
        print("Nenhum processo corresponde ao PID", pid)
    else:
        print("Processo correspondente ao PID", pid, "encontrado!")
        break

while True:

    #Gera um número entre 1 e 10, que correspondem a um sinal diferente
    #De 1 a 6 = SIGINT, 7 e 8 = SIGQUIT, 9 e 10 = SIGKILL
    sinalGerado = random.randint(1, 10)

    #Verifica qual sinal corresponde ao número gerado
    if sinalGerado in (9,10):
        print("Enviado: (SIGKILL) - Matar o processo")
        os.kill(pid, signal.SIGKILL)  #Mata o processo
        sys.exit()

    elif sinalGerado in (7,8):
        print("Enviado: (SIGQUIT) - Finalizar o processo")
        os.kill(pid, signal.SIGQUIT)  #Finaliza o processo
        sys.exit()

    else:
        print("Enviado: (SIGINT) - Interromper o processo")
        os.kill(pid, signal.SIGINT)   #Interrompe o processo

    #Dorme por um período entre 1 a 10 segundos antes de enviar outro sinal
    time.sleep(random.randint(1, 10))
