import socket
from _thread import *
import os
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7777))
server.listen(4)
print ('Aguardando conexões...\n')

coonnectionList = []

def SetNewThreads(connectionUser, address):
    while True:
        try:
            connectionUser.send("Bem Vindo".encode())
            namefile = connectionUser.recv(1024).decode()
            if(os.path.exists('../files/' + namefile)):
                with open('../files/' + namefile, 'rb') as file:
                    for data in file.readlines():
                        connectionUser.send(data)
                print (f'{namefile} enviado!')
            else:
                print("This archive don't exists in server's midia fold")
                server.close()
        except:
            if Exception:
                expt = sys.exc_info()
    
def AcceptConnectionThread():
    while True:
        connection, address = server.accept()
        print('User connected (address):', address)

        coonnectionList.append(connection)
        print("Clientes conectados:", len(coonnectionList))
        start_new_thread(SetNewThreads, (connection, address))



start_new_thread(AcceptConnectionThread, ())

exitCommand = input("Press 'ENTER' to exit\n")

