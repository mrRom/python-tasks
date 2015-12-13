import pickle
import socket

def serialize(data):
    data = pickle.dumps(data)
    return data

def deserialize(data):
    data = pickle.loads(data)
    return data

def do_something(deserialized_data):
    """Works with object on server side"""
    print "Working with data..."
    result = deserialized_data
    return result

def process_data(data):
    """Receives serialized object
        Returns serialized result
    
    """
    print "Deserializing data..."
    deserialized_data = deserialize(data)
    result = do_something(deserialized_data)
    print "Serializing data..."
    serialized_result = serialize(result)
    return serialized_result 

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
        resp = process_data(data)
        print "Sending response to client " + str(addr) + " ..."
        sock.send(resp)
    sock.close()
    
if __name__ == '__main__':
    start_server()
