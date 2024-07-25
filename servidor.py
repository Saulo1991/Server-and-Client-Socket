import socket

host = '127.0.0.1'
port = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, port))
servidor.listen(1)
print("Esperando a conexão")


conexao, endereco = servidor.accept()
print(f"Connection {endereco[0]}:::{endereco[1]}")


mensagem = conexao.recv(1024)

resposta = 'Mensagem recebida!'


conexao.sendall(resposta.encode())

conexao.close()
servidor.close()





