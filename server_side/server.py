import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 20000))
server.listen(4)
print ('Aguardando conexão...\n')

connection, adress = server.accept()

namefile = connection.recv(1024).decode()

with open(f'../midias/{namefile}', 'rb') as file:
    for data in file.readlines():
        connection.send(data)

print ('Arquivo enviado!')