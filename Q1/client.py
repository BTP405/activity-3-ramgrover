import socket
import pickle

def send_file(file_path, server_ip, server_port):
    try:
        # Create client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_ip, server_port))

        # Read the file content
        with open(file_path, 'rb') as file:
            content = file.read()

        # Get the filename from the file path
        filename = file_path.split("/")[-1]

        # Create a dictionary with file content and filename
        file_data = {'content': content, 'filename': filename}

        # Pickle the file data
        pickled_data = pickle.dumps(file_data)

        # Send the pickled data to the server
        client_socket.sendall(pickled_data)

        print("File sent successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

def main():
    file_path = './abc.txt'
    server_ip = '127.0.0.1'
    server_port = 1024

    # Call the function to send the file
    send_file(file_path, server_ip, server_port)

if __name__ == "__main__":
    main()
