import socket
import pickle

def receive_file(server_ip, server_port, save_directory):
    try:
        # Create server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a specific address and port
        server_socket.bind((server_ip, server_port))

        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {server_ip}:{server_port}")

        # Accept connection from client
        client_socket, addr = server_socket.accept()
        print(f"Connection established from {addr}")

        # Receive pickled file object
        pickled_data = client_socket.recv(4096)
        if not pickled_data:
            print("Error: No data received.")
            return

        # Unpickle the data
        try:
            file_data = pickle.loads(pickled_data)
        except pickle.UnpicklingError as e:
            print(f"Error unpickling data: {e}")
            return

        # Extract file content and filename
        content = file_data['content']
        filename = file_data['filename']

        # Save the file to the specified directory
        file_path = save_directory + filename
        with open(file_path, 'wb') as file:
            file.write(content)

        print(f"File received and saved at: {file_path}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection and server socket
       # client_socket.close()
        server_socket.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 1024
    save_directory = './pqr.txt'

    # Call the function to receive the file
    receive_file(server_ip, server_port, save_directory)

if __name__ == "__main__":
    main()
