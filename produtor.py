# -*- coding: utf-8 -*-
#Importando as bibliotecas necessárias
import socket
import sys

#Pede para inserir o IPv4 do componente com o código do produtor
while True:
    HOST = input("\nInsira o endereço IPv4 do componente produtor: ")
    PORT = 6364

    try:
        #Criando o objeto socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        break
    except (socket.gaierror, OSError):
        print(f"\n### ERRO: {sys.exc_info()[0]}")
        print("Por favor, verifique se o IPv4 foi digitado corretamente")

print("\nO socket do produtor foi criado!")

#Escuta por (1) conexões do cliente (consumidor)
print("\nProcurando por conexões...")
s.listen(1)

#Aceita e estabelece uma conexão com o cliente (consumidor)
socketCliente, enderecoCliente = s.accept()
print(f"\nConexão com {enderecoCliente} foi estabelecida!")

while True:
    #Recebe um número inteiro maior que 1 ou 0
    while True:
        num = int(input("\nInsira um número: "))
        if num > 1 or num == 0:
            break

    #Envia 'num' para o cliente (consumidor)
    socketCliente.send(str(num).encode("utf-8"))
    print("\nEnviando o número para o consumidor...")

    #Recebe a soma do cliente (consumidor)
    soma = socketCliente.recv(1024).decode()
    if not soma:
        print("\n### ERRO AO RECEBER A SOMA!")
        break

    soma = int(soma)
    if soma == -1:      #Condição para encerrar a conexão e o processo
        break

    print("\nResultado recebido!")
    print(f"A soma dos números primos menores que {num} é: {soma}")

#Encerra a conexão com o cliente (consumidor) e o processo
print("\nEncerrando a conexão com o consumidor...")
num = 0
socketCliente.send(str(num).encode("utf-8"))
socketCliente.close()
print("\nEncerrando o processo...")
sys.exit()
