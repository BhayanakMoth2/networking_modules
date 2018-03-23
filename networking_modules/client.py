import socket
import sys
import threading
from enum import Enum

class Packet(Enum):
    Poll = 1
    OK = 2
    Stream = 3
    Message = 4
    MICCHECK = 5

def PacketToBytes(p):
    val = str(int(p))
    buff = bytes(val,'UTF-8')
    return buff

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s = sock
print(str(s.proto))
host = '127.0.0.1' # needs to be in quote
port = 9001
print("Starting up!")
s.connect((host, port))
print (s.recv(1024))
poll = Packet.Poll
miccheck = Packet.MICCHECK
def RecvStuff():
    while True:
        buf = bytes()
        buf = s.recv(sys.getsizeof(Packet))
        val = Packet(int(str(buf.decode('utf-8'))))
        print(val)
        if(val == poll):
            val = Packet.OK
            print("OK")
            buf = bytes(str(val.value),'UTF-8')
            s.send(buf)
            print("Polling")
        if(val == miccheck):
            val = miccheck
            buf = bytes(str(val.value),'UTF-8')
            s.send(buf)
            print("Reconnecting")

            
        


clientThread=threading.Thread(target = RecvStuff)
clientThread.start()

print("press any key to continue")
while True:
    rawbuf = input("")
    buf = bytes(rawbuf,'UTF-8')
    s.send(buf)

