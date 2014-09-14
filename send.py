import asynchat
import asyncore
import socket
import threading
 

class ChatClient(asynchat.async_chat):
 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator(b'\0')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        pass
 
    def found_terminator(self):
        pass
 
client = ChatClient('beta.shirhatti.com', 5051)
 
comm = threading.Thread(target=asyncore.loop)
comm.daemon = True
comm.start()
 
while True:
    msg = input('> ')
    client.push(bytearray(msg + '\0', 'utf-8'))