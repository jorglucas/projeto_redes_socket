import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 20000))
server.listen()
print ('Aguardando conexões...\n')

connection, adress = server.accept()

namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

print (f'Arquivo> {namefile} enviado!')