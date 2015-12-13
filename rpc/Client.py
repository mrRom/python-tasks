import pickle
import socket

def serialize(data):
    data = pickle.dumps(data)
    return data

def deserialize(data):
    data = pickle.loads(data)
    return data

def do_something(data):
    HOST = "127.0.0.1" 
    PORT = 22222 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(serialize(data))
    result = sock.recv(1024)
    sock.close()
    return deserialize(result)

if __name__ == '__main__':
    a = {"1": "1", "somelist": [1, 2, 4], "2": "2", 3: 3, "sometuple": ("a", 1)} 
    resp = do_something(a)
    print resp
