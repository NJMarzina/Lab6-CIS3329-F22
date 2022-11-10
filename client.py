import socket

IP = '127.0.0.1'                                            #sets ip address
PORT = 1234                                                 #sets port address
SIZE = 1024                                                 #sets size
msg = input('Enter a message to be reversed: ')             #message

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #this is setting the TCP socket
s.connect((IP, PORT))                                       #this sends the request to connect to the server
s.send(str(msg).encode())                                   #this sends the message to be encoded
data = s.recv(SIZE)                                         
s.close()                                                   #closes

print('Response: ' + data.decode())