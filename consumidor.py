# -*- coding: utf-8 -*-
#Importando as bibliotecas necessárias
import socket
import sys

while True:
    HOST = input("\nInsira o endereço IPv4 do componente produtor: ")
    PORT = 6364

    try:
        #Criando o objeto socket TCP/IP e tenta se conectar ao servidor (produtor)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        break
    except ConnectionRefusedError:
        print(f"\n###ERRO: {sys.exc_info()[0]}")
        print("Por favor, verifique se o socket do produtor já foi criado")
    except (socket.gaierror, OSError):
        print(f"\n###ERRO: {sys.exc_info()[0]}")
        print("Por favor, verifique se o IPv4 foi digitado corretamente")

enderecoServidor = s.getpeername()
print(f"\nConexão com {enderecoServidor} foi estabelecida!")

while True:
    print("\nAguardando o número do produtor...")

    #Recebe 'num' do servidor (produtor)
    num = s.recv(1024).decode()
    if not num:
        print("\n### ERRO AO RECEBER O NÚMERO!")
        break

    print("\nNúmero recebido: ", num)

    soma = 0
    num = int(num)
    if num == 0:        #Condição para encerrar a conexão e o processo
        break

    num = num-1

    #Calcula a soma dos números primos menores que 'num'
    while num > 1:
        for i in range(2, num):
            if i != num and num%i == 0:    #Não é número primo
                num = num-1

        soma = soma + num
        num = num-1

    #Envia o resultado da soma para o servidor (produtor)
    print("\nEnviando o resultado...")
    s.send(str(soma).encode("utf-8"))

#Encerra a conexão com o servidor (produtor) e o processo
print("\nEncerrando a conexão com o produtor...")
soma = -1
s.send(str(soma).encode("utf-8"))
s.close()
print("\nEncerrando o processo...")
sys.exit()
