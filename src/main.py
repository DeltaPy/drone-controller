import socket
import pyshark
import time

droneIp = "172.16.10.1"
droneTcpPort = 8888
droneUdpPort = 8895

cmd = "20f41b0352cd342eb652e8d8080045000024c4c0400040112b0eac10e8d8ac100a0121db22bf00102384cc80800080008033"
cmd = bytes.fromhex(cmd)
# print(dir(shark_cap[6]))

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to drone...")
try:
    tcpSocket.connect((droneIp, droneTcpPort))
except:
    print("Connection failed")
    exit()
print("Connected to drone")
time.sleep(3)
print("Sending magic packet...")
# shark_cap = pyshark.FileCapture(r"dump.pcap", display_filter="tcp")
shark_cap = pyshark.FileCapture(r"dump.pcap", display_filter="ip.src==172.16.232.216 and tcp")
# for i in [3, 9, 16, 20, 22, 24, 26, 28 ,30 ,32, 34]:
for i in shark_cap:
    # print("Frame number: ",shark_cap[i].number)
    # print((shark_cap[i].tcp.payload).replace(":",""))
    # magicPacket = (shark_cap[i].tcp.payload).replace(":","")
    print("Frame number: ",i.number)
    try:
        print((i.tcp.payload).replace(":",""))
        magicPacket = (i.tcp.payload).replace(":","")
        tcpSocket.send(bytes.fromhex(magicPacket))
    except:
        print();

print("Sent!")

while True:
    data = tcpSocket.recv(255)
    print("Received:" ,data)
    print("Decoded in hex: ",data.hex())
    # udpSocket.sendto(cmd, (droneIp, droneUdpPort))
    time.sleep(0.1)


