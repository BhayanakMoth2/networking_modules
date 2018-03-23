import socket
from conversion  import *
import threading
import sys
import time

class Server:
    connNum = 10
    address = ""
    tcpPort = 9000
    udpPort = 9001
    addr = (address,udpPort)
    clientAddr = []
    ID = []
    tcpListen = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
    tcp = [socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)]
    udp = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
    connectionCounter = 0
    tcpListen = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
    def __init__(self):
        self.tcpListen.bind((self.address,self.tcpPort))
        self.tcpListen.listen(10)
        i = 0
        while i < 10:
            self.tcp.append(socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM))
            i = i+1
        i = 0
        self.udp.bind(('127.0.0.1',self.udpPort))
        

    def main(self):
        while self.connectionCounter < 10:
            print("ENTERING MAIN LOOP ITERATION: "+str(self.connectionCounter))
            print("RECVING MESSAGE FROM "+str(self.connectionCounter))
            buf, addr = self.RecvUDP()
            msg = buf.decode('utf-8')
            print('Client: '+str(addr)+' says: '+msg)
            self.clientAddr.append(addr)

            msg = "YOUVECOMEALONGLONGWAYTODAY"
            
            self.SendStringUDP(_str=msg,_id = self.connectionCounter)
            self.connectionCounter += 1


    #----These things work!----#    
    def SendStringTCP(self, _str = '', _id=0):
        buff = bytes(_str,'utf-8')
        self.tcp[_id].send(buff)     
    
    def RecvStringTCP(self,_id = 0):
        buff = self.tcp[_id].recv(1024)
        _msg = buff.decode('utf-8')
        return _msg

    def SendStringUDP(self ,_str = '', _id = 0):
        buff = bytes(_str ,'utf-8')
        print("SENDING SHIT TO "+str(self.clientAddr[_id]))
        self.udp.sendto(buff,self.clientAddr[_id])
        print("MESG SENT")
    
    def RecvUDP(self):
        print("Recving shit")
        buff,addr = self.udp.recvfrom(1024)
        return buff,addr
    #-----</these things>-----#


serv = Server()
serv.main()

