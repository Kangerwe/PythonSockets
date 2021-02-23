import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1234))
str = input ("Enter your Name")
while True:
    c.send(str.encode())
    msg = c.recv(1024)
    print("Message from Server" + msg.decode("utf-8"))
c.close

