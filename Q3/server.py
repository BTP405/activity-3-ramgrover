import socket

def run():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_addr = ('localhost', 3030)
    serv_sock.bind(serv_addr)
    serv_sock.listen()

    print('Now listening at port 3030...')

    while True:
        client_sock, client_addr = serv_sock.accept()
        print('Connected to: ', client_addr)

        data = client_sock.recv(1024)

        print('Received: ', data.decode())

        message = 'Received sussess!!'

        client_sock.sendall(message.encode())

        client_sock.close()

if __name__ == "__main__":
    run()