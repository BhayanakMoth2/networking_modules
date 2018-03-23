import socket
import threading
import time
tcp = socket.socket(family = socket.AF_INET,type = socket.SOCK_STREAM )
udpSend = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)
tcpSend = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
tcpRecv = socket.socket(family= socket.AF_INET, type = socket.SOCK_STREAM)
udpRecv = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)
tcpSPort = 9000
udpSPort = 9002
tcpRPort = 9001
udpRPort = 9003 
intPayload  = 9161
stringPayload = "asda"
clientaddr = '127.0.0.5'
recvaddr = (clientaddr,tcpRPort)
sendaddr = (clientaddr,tcpSPort)

print("RECVING MESSAGE")
tcpRecv.bind(recvaddr)
tcpSend.bind(sendaddr)
tcpRecv.connect(('127.0.0.6',tcpSPort))
tcpSend.listen(10)
#--------RECV CHANNEL-------#
buf = tcpRecv.recv(1024)
msg = buf.decode('utf-8')
print("MESG "+msg)

#--------SEND CHANNEL-------#
conn, addr = tcpSend.accept()
tcpSend = conn

mesg = "FCKA YES"
buf = bytes(mesg,'utf-8')
print("Sending message")
tcpSend.send(buf)

print("Message Sent to endpoint"+str(tcpSend.getpeername()))

'''
def SendData():
    global intPayload
    global stringPayload
    buff2 = bytes(str(intPayload),'utf-8')
    tcp.send(buff2)
    buff3 = bytes(str(stringPayload),'utf-8')
    tcp.send(buff3)
'''

def RequestData():
    mesg = "Requesting Payload"
    buff = bytes(mesg,'utf-8')
    tcpSend.send(buff)
    
    buff = tcpRecv.recv(1024)
    if(buff.decode('utf-8')=='OK'):
        intBuff = tcpRecv.recv(1024)
        intPayload = int(intBuff.decode('utf-8'))
        strBuff = tcpRecv.recv(1024)
        stringPayload =  strBuff.decode('utf-8')
        print("Recvd Int: "+str(intPayload))
        print("Recvd str: "+stringPayload)
        
'''   
def ClientHandler():
    while True:
        buff = tcp.recv(1024)
        req = buff.decode('utf-8')
        if(req == 'Requesting Payload'):
            tcp.send(bytes('OK','utf-8'))
            SendData()
            print("**Sending Data to "+str(tcp.getpeername())+"**")
'''        
def InputHandler():
    while True:
        tcpSend.send(bytes('Req Data','utf-8'))
        print('Request Sent')
        start = time.time()
        buf = bytes()
        while buf.__len__() == 0:
            print('1st While: '+str(buf.__len__()))
            buf = tcpRecv.recv(100)
            timeElapsed = time.time() - start
            if(timeElapsed >= 2):
                break
        if(buf.decode('utf-8')=='OK'):
            start = time.time()
            buf = bytes()
            while buf.__len__() == 0:
                buf = tcpRecv.recv(100)
                timeElapsed = time.time() - start
                if(timeElapsed >= 2):
                    break
        
        if(buf.__len__()!=0):
            print(buf.decode('utf-8'))
            buf = bytes()
        
            
                  

        time.sleep(2)
                
     
print("Calling Loop")
InputHandler()
