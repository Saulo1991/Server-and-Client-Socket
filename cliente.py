# O cliente deve conectar ao servidor na porta 12345.
# O cliente deve enviar a mensagem "Olá, servidor!" ao servidor.
# O cliente deve receber a resposta do servidor e exibi-la na tela.
# Após receber a resposta, o cliente deve fechar a conexão.
# Objetivo:
# Escreva dois programas: um para o servidor e outro para o cliente. Execute o servidor primeiro
# e depois o cliente para ver a comunicação entre eles.

# Essa abordagem vai te ajudar a entender o básico de sockets e como cliente e servidor podem se comunicar

'''
1. cliente, servidor, porta, mensagem
2. O cliente deve conectar o servidor na porta 12345, deve dizer a mensagem "olá servidor", deve receber
a resposta do servidor e exibíla na tela
3. O cliente não conectar o servidor na porta 12345, não enviar "Olá, servidor", receber a resposta de alguém
além do servidor, não exibir na tela, não fechar a conexão
4. Exibir a resposta do servidor na tela
5. Pseudocódigo
'''

import socket

host = '127.0.0.1'
port = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

mensagem = "Olá, servidor"

cliente.sendall(mensagem.encode())

resposta = cliente.recv(1024)

cliente.close()