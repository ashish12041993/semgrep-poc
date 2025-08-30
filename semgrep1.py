import pickle
import socket

def receive_obj(sock):
    data = sock.recv(4096)
    # vulnerable: pickle can execute arbitrary code during deserialization
    obj = pickle.loads(data)
    return obj

