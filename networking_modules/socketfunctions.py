import sys
import socket
import threading
import ipaddress            

class TCPSocket:
    rawSock = socket.socket(family = socket.AF_INET,type = socket.SOCK_STREAM)
    addrs = '127.0.0.1'
    port = 9000
    def __init__(self,sock=socket.socket(),addr = '127.0.0.1',port = 9000):
        self.addrs = addr
        self.port = port
        self.rawSock = sock

    def Connect(self):
        address = (self.addrs,self.port)
        print("Connecting to host: "+str(self.addrs)+" on port: "+str(self.port))
        self.rawSock.connect(address)

    def Write(self,buf = bytes(),len = 0):
        dataSent = 0
        while dataSent < len:
            retnValue = self.rawSock.send(buf)
            if(retnValue < 0):
                return dataSent
            else:
                dataSent += retnValue
        return dataSent

    def Read(self, len = 0):
        buff = bytes()
        #while buff.__len__() < len:
        retnValue = self.rawSock.recv(len)
         #   if(retnValue < 0):
          #      return buff
          #  else:
        buff += retnValue
        return buff

    def Bind(self):
        self.rawSock.bind((self.addrs,self.port))
        
class UDPSocket:
    rawSock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    addrs = '127.0.0.1'
    port = 9001

    def __init__(self,sock=socket.socket(family= socket.AF_INET,type = socket.SOCK_DGRAM),addr = '127.0.0.1',port = 9000):
        self.rawSock = sock
        self.addrs = addr
        self.port = port
    

    def Write(self,buf = bytes(),len = 0):
        retnValue = self.rawSock.sendto(data = buf,address = (self.addrs,self.port))
           
    def Read(self, len = 0):
        buff = bytes()
        while buff.__len__() < len:
            retnValue = self.rawSock.recvfrom(len, address = (self.addrs,self.port))
            if(retnValue < 0):
                return buff
            else:
                buff += retnValue
        return buff     
    
    def Bind(self):
        self.rawSock.bind((self.addrs,self.port))





'''
***TO DO***
#1:Test TCP-UDP Polling locally
#2:Test TCP-UDP over LAN
#3:Test Sending Data over LAN

'''