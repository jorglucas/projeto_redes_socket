import os
import socket
import threading

IP = 'localhost'
PORT = 20000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"[NOVA CONEXAO ESTABELECIDA] {addr} se conectou ao servidor.")
    conn.send("OK@Bem-vindo ao servidor de arquivos. Digite ajuda para acessar os comandos.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        print (cmd)

        if cmd == 'listar':
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "O servidor está vazio."
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd == "enviar":
            name, text = data[1], data[2]
            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)

            send_data = "OK@Arquivo enviado!"
            conn.send(send_data.encode(FORMAT))

        elif cmd == "deletar":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"
            filename = data[1]
            print (f'filename = {filename}')
            if len(files) == 0:
                data += "O servidor está vazio."
            else:
                if filename in files:
                    os.system(f'del /f /a {filename}')
                    data += "Arquivo deletado!"
                else:
                    data += "Arquivo não encontrado."

        elif cmd == "sair":
            break
        elif cmd == "ajuda":
            data = "OK@"
            data += "listar: lista todos os arquivos do servidor.\n"
            data += "enviar <caminho/ate/o/arquivo>: enviar um arquivo para o servidor.\n"
            data += "deletar <nome_do_arquivo.extensao>: deleta um arquivo do servidor.\n"
            data += "sair: desconectar do servidor.\n"

            conn.send(data.encode(FORMAT))

    print(f"[DESCONECTADO] {addr} se desconectou do servidor.")
    conn.close()

def main():
    print("[INICIANDO] O Servidor está disponível para acesso!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[CONEXAO] O Servidor está aguardando por conexoes na porta {PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        count = threading.activeCount() - 1
        print(f"[CONEXOES ATIVA] {count}")  

if __name__ == "__main__":
    main()