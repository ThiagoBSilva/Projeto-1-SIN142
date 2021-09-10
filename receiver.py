# -*- coding: utf-8 -*-
#Importando as bibliotecas necessárias
import signal
import os
import sys

#Tratando o sinal de interrupção do processo
def interromper_processo(num_sinal, frame):
    print("\nRecebido: (SIGINT) - Interrompendo o processo...")
    print(f"{num_sinal, frame}")

#Tratando o sinal de finalização do processo
def finalizar_processo(num_sinal, frame):
    print("\nRecebido: (SIGQUIT) - Finalizando o processo...")
    print(f"{num_sinal, frame}")
    sys.exit()

#Registrando os tratamentos aos seus respectivos sinais
signal.signal(signal.SIGINT, interromper_processo)
signal.signal(signal.SIGQUIT, finalizar_processo)

#Exibe o PID para a ser passado ao sender
print("Meu PID: ", os.getpid())

#Dorme até receber um sinal
while True:
    print("Em espera...")
    signal.pause()
