import socket

def run():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3030)
    client_socket.connect(server_address)
    
    message = "hello"

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)

    print('Received: ', data.decode())

    client_socket.close()

if __name__ == '__main__':
    run()