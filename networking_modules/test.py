from enum import Enum
import socket
class TEST(Enum):
    POLL = "POLL"
    OK = "OK"
    VAL = "VAL"

f = 1442.123
s = str(f)
buff = bytes(s,'UTF-8')


sock = socket.socket()
sock.bind(('127.0.0.1',9001))
sock.listen(10)

    client1,addr = sock.accept()
    sent = client1.send(buff) 
    print(sent)
    sock.close()
    client1.close()
from enum import Enum
import socket
class TEST(Enum):
    POLL = "POLL"
    OK = "OK"
    VAL = "VAL"

f = 1442.123
s = str(f)
buff = bytes(s,'UTF-8')


sock = socket.socket()
sock.bind(('127.0.0.1',9001))
sock.listen(10)
client1,addr = sock.accept()
sent = client1.send(buff) 
print(sent)
sock.close()
client1.close()

