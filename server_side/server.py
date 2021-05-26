import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 20000))
server.listen(4)
print ('Aguardando conexão...\n')

connection, adress = server.accept()

namefile = connection.recv(1024).decode()

if(os.path.exists('../files/' + namefile)):
    with open('../files/' + namefile, 'rb') as file:
        for data in file.readlines():
            connection.send(data)
    print (f'{namefile} enviado!')
else:
    print("This archive don't exists in server's midia fold")
    server.close()