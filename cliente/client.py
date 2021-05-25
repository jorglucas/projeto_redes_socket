import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 20000));
print ('Cliente conectado!\n')

namefile = input('Arquivo> ')

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print (f'Arquivo> {namefile} recebido!\n')