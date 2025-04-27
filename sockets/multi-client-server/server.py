import threading
import socket

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients = []
aliases = []

# a function which sends a message from server to all the connected clients: broadcast
def broadcast(message):
    for client in clients:
        client.send(message)

# handle connection of each client connection function, when client sends a message to another client, wrap code in try catch for it
def handle_client(client):
    while True:
        try:
            message = client.recv(1024) # no of bites client can send
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

# main function to recieve clients function
#recieve function 
def recieve():
    while True:
        print('server is running and listening for connections....')
        client, address = server.accept() # runs constantly and accepts clients
        print('connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))                #clients sends an alias too 
        alias = client.re