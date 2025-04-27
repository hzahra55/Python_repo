import socket
import sys

try:
    # AF_INET: address family ipv4 with INET, second param SOCK_STREAM: means tcp is used here)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('successfully created sockets')

except socket.error as err:
    print(f'failed creation {err}')

# set default port for socket,can get socket.gaie error(error with dns)
port = 80
try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving system')
    sys.exit()

# connect with server, and params tuple of host_ip and port
s.connect((host_ip,port))
print(f'socket has successfully connected to github at port  == {host_ip}')

#to get ip of a domain
ip= socket.gethostbyname('www.github.com')
print(ip)

