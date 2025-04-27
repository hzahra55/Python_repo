import socket

s = socket.socket()
print('succesfful socket creation')
port = 56789
# bind has two param, ip and port(leave ip so server can listen to many requests)
s.bind(('',port))
print(f'socket binded to port {port}')

#put socket in llstening mode
s.listen(5) # means 5 connections limit for server, more will be refused
print('socket is listening') # socket is listening for any conenctions from client computer
while True:
    c, addr =  s.accept()
    print('got connection from ', addr)
    message = ('thank you for conencting with us')
    c.send(message.encode())     # doesnt in  string so use encode
    c.close()

# to interact with server, check connectivity of network
