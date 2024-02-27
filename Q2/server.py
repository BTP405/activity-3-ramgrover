import socket
import pickle
import types
import marshal

def run():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind(('localhost', 3003))
    serv_sock.listen()
    print('Listening for connections on port 3003...')

    while True:
        client_sock, client_addr = serv_sock.accept()
        print(f'Client {client_addr} has connected!')
        # read the message's length
        msg_len = int.from_bytes(client_sock.recv(4), byteorder='big')
        print(msg_len)
        # read the pickled message
        raw = client_sock.recv(msg_len)
        # unpickle the message
        bytecode, args = marshal.loads(raw)
        print('Bytecode: ', bytecode)
        print('Arguments: ', args)
        func = types.FunctionType(bytecode, globals(), 'task')
        # perform the task with given arguments
        result = func(*args)
        # pickle the result
        raw_result = pickle.dumps(result)
        # send the result's length
        client_sock.send(len(raw_result).to_bytes(4, byteorder='big'))
        # send the pickled result
        client_sock.send(raw_result)
        # close the connection
        client_sock.close()
        print(f'Client {client_addr} has disconnected!')

if __name__ == '__main__':
    run()