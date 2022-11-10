import socket

IP = '127.0.0.1'
PORT = 1234
SIZE = 1024
msg = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)

c, a = s.accept()
print('connection address:', a)
while 1:
    data = c.recv(SIZE)
    if not data:
        break
    msg = data.decode()
    print('received data:', msg)
    c.send(str(msg)[::-1].encode())
c.close()
