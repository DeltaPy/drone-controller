import socket
import time

droneIp = "172.16.10.1"
dronePort = 8888

magicPacket = b"/20/f4/1b/03/52/cd/34/2e/b6/52/e8/d8/08/00/45/00/00/3c/cb/cd/40/00/40/06/23/f4/ac/10/e8/d8/ac/10/0a/01/8f/77/22/b8/8c/1a/52/6e/00/00/00/00/a0/02/ff/ff/d2/94/00/00/02/04/05/b4/04/02/08/0a/00/14/99/a3/00/00/00/00/01/03/03/08/"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((droneIp, dronePort))
except:
    print("Failed to connect to drone!")
    print("Time out...")
    exit()

print("Connected to drone!")

time.sleep(3)
print("Sending magic packet...")
s.sendall(bytes(magicPacket))

while True:
    data = s.recv(1024)
    print(data)


