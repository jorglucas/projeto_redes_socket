import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 20000));
print ('Cliente conectado!\n')

namefile = input('Arquivo> ')

client.send(namefile.encode())

with open('../client_side/' + namefile, 'wb') as file:
    while 1:
        data = client.recv(5120)
        if not data:
            break
        file.write(data)

print ('Arquivo recebido!\n')