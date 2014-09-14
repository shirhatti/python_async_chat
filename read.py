import asynchat
import asyncore
import socket
 
class ChatClient(asynchat.async_chat):
 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator(b'\n')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        self.buffer.append(data)
 
    def found_terminator(self):
        msg = b''.join(self.buffer)
        print ('Received:', msg)
        self.buffer = []
 
client = ChatClient('beta.shirhatti.com', 5051)
 
print ('Listening on localhost:5051')
asyncore.loop()