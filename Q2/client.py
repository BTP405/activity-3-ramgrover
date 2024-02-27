import socket
import pickle
import marshal

def task(*l):
    even = 0
    odd = 0
    for item in l:
        if item % 2 == 0:
            even+=1
        else:
            odd+=1
    return {'even': even, 'odd': odd}

args = ([1,2,3,4,5,6])

def run():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 3003))
    print('Connected to the server!')

    # pickle the task along with its arguments
    raw_msg = marshal.dumps((task.__code__, args))
    # send the length of the message
    print(len(raw_msg))
    client_sock.send(len(raw_msg).to_bytes(4, byteorder='big'))
    # send the pickled message
    client_sock.send(raw_msg)
    # read the length of the result
    result_len = int.from_bytes(client_sock.recv(4), byteorder='big')
    # read the pickled result
    raw_result = client_sock.recv(result_len)
    # unpickle the result
    result = pickle.loads(raw_result)
    print(f'Result: ', result)
    # close the connection
    client_sock.close()

if __name__ == '__main__':
    run()


