import sys
import socket
from enum import Enum
class Header(Enum):
    TEST = "TEST"
    POLL = "POLL"
    OK = "OK"
    NULL = "NULL"
    VAL = "VAL"

def PackettoBytes(p = Header.NULL.value):
    val = str(p.value)
    buff = bytes(val,'UTF-8')
    return buff

def BytesToPacket(buff = bytes()):
    val = buff.decode('UTF-8')
    val = int(val)
    p = Header(val)
    return p

def IntToBytes(i):
    val = str(i)
    buff = bytes(val,'UTF-8')
    return buff

def BytesToInt(buff = bytes()):
    val = buff.decode('UTF-8')
    i = int(val)
    return i

def FloatToBytes(i=float()):
    val = str(i)
    buff = bytes(val,'UTF-8')
    return buff

def BytesToFloat(buff=bytes()):
    val = buff.decode('UTF-8')
    f = float(val)
    return f
 