import pickle
import socket

def serialize(data):
    data = pickle.dumps(data)
    return data

def deserialize(data):
    data = pickle.loads(data)
    return data

def do_something(data):
    print "Deserializing data..."
    data = deserialize(data)
    print "Working with data..."
    print "Serializing data..."
    data = serialize(data)
    return data

def start_server():
    HOST = "127.0.0.1"
    PORT = 22222
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORT))
    print "Server is running. Host 127.0.0.1 Port 22222"
    srv.listen(1)
    while 1:
        sock, addr = srv.accept()
        print "Request was made."
        data = sock.recv(1024)
        resp = do_something(data)
        print "Sending response to client " + str(addr) + " ..."
        sock.send(resp)
    sock.close()
    
if __name__ == '__main__':
    start_server()