import socket

IP = 'localhost'
PORT = 20000
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DESCONECTADO":
            print(f"[SERVIDOR]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "ajuda":
            client.send(cmd.encode(FORMAT))
        elif cmd == "sair":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "listar":
            client.send(cmd.encode(FORMAT))
        elif cmd == "deletar":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "enviar":
            path = data[1]

            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))

    print("Desconectado do servidor.")
    client.close()

if __name__ == "__main__":
    main()
