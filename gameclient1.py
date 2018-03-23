from networking_modules.socketfunctions import TCPSocket,UDPSocket
from networking_modules.conversion  import *
import threading
import math
import time
import random
class client:
    host = '127.0.0.1'
    clientaddr = '127.0.0.6'
    engageFlag = 1
    tcpPort = 9000
    udpPort = 9001
    udpSend = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)
    tcpSend = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
    tcpRecv = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
    udpRecv = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)
    tcpSPort = 9000
    udpSPort = 9002
    tcpRPort = 9001
    udpRPort = 9003 
    recvaddr = (clientaddr,tcpRPort)
    sendaddr = (clientaddr,tcpSPort)
    intPayload = 10
    stringPayload = "Yolo"
    def __init__(self,hostaddr = '127.0.0.6'):
        self.clientaddr = hostaddr
        print('hostaddr/clientaddr'+str(self.clientaddr))
        self.recvaddr = (self.clientaddr,self.tcpRPort)
        self.sendaddr = (self.clientaddr,self.tcpSPort)
        print('send addr'+str(self.sendaddr))
        self.tcpSend.bind((self.clientaddr,self.tcpSPort))
        self.tcpRecv.bind(self.recvaddr)
        
    def Connect(self,ip='127.0.0.1'):
        self.tcpRecv.connect((ip,self.tcpSPort))
        
    def Listen(self):
        self.tcpSend.listen(1)
        conn, endPointAddr = self.tcpSend.accept()
        self.tcpSend = conn

    def SetIP(self, ip='127.0.0.1'):
        self.clientaddr = ip    
        self.recvaddr = (self.clientaddr,self.tcpRPort)
        self.sendaddr = (self.clientaddr,self.tcpSPort)
        self.tcpSend.bind(self.sendaddr)
        self.tcpRecv.bind(self.recvaddr)

    def SendData(self, buf = bytes()):
        self.tcpSend.send(buf)
        print("Data Sent") 

    
    def RecvData(self):
        start = time.time()
        buf = bytes()
        while buf.__len__() == 0:
            print('Entering While: '+str(buf.__len__()))
            buf = self.tcpRecv.recv(100)
            timeElapsed = time.time() - start
            if(timeElapsed >= 2):
                break
        if(buf.__len__()!=0):
            return buf
        else:
            return -1
        
    def TCPSendData(self,buf=bytes()):
        self.tcpSend.send(buf)

    
'''
print("Making Client Handler Thread: ")
th = threading.Thread(target = c.ClientHandler)
th.start()

print("Running Main Loop")
c.Loop()
'''

