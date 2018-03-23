# Basic Pacman
import pygame, sys, os
from pygame.locals import *
from gameclient1 import client 
import threading
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

ghostcolor = {}
ghostcolor[0] = (255, 0, 0, 255)
ghostcolor[1] = (255, 128, 255, 255)
ghostcolor[2] = (128, 255, 255, 255)
ghostcolor[3] = (255, 128, 0, 255)
ghostcolor[4] = (50, 50, 255, 255)
ghostcolor[5] = (255, 255, 255, 255) # white, flashing ghost
pygame.init()
endpoint = client('127.0.0.7')
class game ():
    def __init__ (self):
        self.gmode = 0


buffOK = bytes('OK','utf-8')
buffInit = bytes('Init','utf-8')
buffACK = bytes('ACK','utf-8')
    
    

class pacman ():

    def __init__ (self):
        self.x = 200
        self.y = 200
        self.velx = 0
        self.vely = 0
        self.speed = 6
        
        self.nearestRow = 0
        self.nearestCol = 0
        
        self.baseX = 0
        self.baseY = 0

        self.currentPath = ""

        self.pac_anim_left = {}
        self.pac_anim_right = {}
        self.pac_anim_up = {}
        self.pac_anim_down = {}
        self.pac_anim_exist = {}
        self.pac_anim_current = {}

        for i in range(1, 9):
            self.pac_anim_left[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_left_f" + str(i) + ".gif")).convert()
            self.pac_anim_right[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_right_f" + str(i) + ".gif")).convert()
            self.pac_anim_up[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_up_f" + str(i) + ".gif")).convert()
            self.pac_anim_down[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_down_f" + str(i) + ".gif")).convert()
            self.pac_anim_exist[i] = pygame.image.load(os.path.join(image_path,"pacman","pacman_exist.gif")).convert()

        self.pac_anim_current = self.pac_anim_right
        self.animFrame = 3
        
    def Draw (self):
        screen.blit(self.pac_anim_current[self.animFrame], (self.x,self.y))
        self.animFrame += 1
        if self.animFrame == 9:
            self.animFrame = 1

    def Move (self):
        self.x += self.velx
        self.y += self.vely
    
    def RecvUpdate(self):
        if pygame.key.get_pressed()[ pygame.K_RIGHT ]:
            self.MoveRight()
        
        elif pygame.key.get_pressed()[ pygame.K_LEFT ]:
            self.MoveDown()
            
        elif pygame.key.get_pressed()[ pygame.K_UP ]:
            self.MoveUp()
            
        elif pygame.key.get_pressed()[ pygame.K_DOWN ]:
            self.MoveDown()
        

    def MoveUp(self):
        self.pac_anim_current = player.pac_anim_up
        self.velx=0
        self.vely=-player.speed    

    def MoveDown(self):
        self.pac_anim_current = player.pac_anim_down
        self.velx = 0
        self.vely =player.speed

    def MoveLeft(self):
        self.pac_anim_current = player.pac_anim_left
        self.velx = -player.speed
        self.vely = 0

    def MoveRight(self):
        self.pac_anim_current = player.pac_anim_left
        self.velx = player.speed
        self.vely = 0    

class pacman2:
    endpoint = client(hostaddr='127.0.0.5')
    x = 200
    y = 200
    velx = 0
    vely = 0
    speed = 6
        
    nearestRow = 0
    nearestCol = 0
        
    baseX = 0
    baseY = 0

    currentPath = ""

    pac_anim_left = {}
    pac_anim_right = {}
    pac_anim_up = {}
    pac_anim_down = {}
    pac_anim_exist = {}
    pac_anim_current = {}
    animFrame = 3
    lastInput = 0
    def __init__ (self,_client = client()):
        self.endpoint = _client
        buf = bytes('Init','utf-8')
        _client.SendData(buf)
        buf = _client.RecvData()
        print('init: '+buf.decode('utf-8'))

        
    def Draw (self):
        print('Drawing Player2 AnimFram: '+str(self.animFrame))
        screen.blit(self.pac_anim_current[self.animFrame], (self.x,self.y))
        self.animFrame += 1
        if self.animFrame == 9:
            self.animFrame = 1

    def Update(self):
        self.x += self.velx
        self.y += self.vely
        print("Moving Player 2 by: "+str(self.velx))
        print("Moving Player 2 by: "+str(self.vely))

    def RecvUpdate(self):
        if pygame.key.get_pressed()[ pygame.K_RIGHT ]:
            self.MoveRight()
        
        elif pygame.key.get_pressed()[ pygame.K_LEFT ]:
            self.MoveDown()
            
        elif pygame.key.get_pressed()[ pygame.K_UP ]:
            self.MoveUp()
            
        elif pygame.key.get_pressed()[ pygame.K_DOWN ]:
            self.MoveDown()
        

    def MoveUp(self):
        self.pac_anim_current = player.pac_anim_up
        self.velx=0
        self.vely=-player.speed    

    def MoveDown(self):
        self.pac_anim_current = player.pac_anim_down
        self.velx = 0
        self.vely =player.speed

    def MoveLeft(self):
        self.pac_anim_current = player.pac_anim_left
        self.velx = -player.speed
        self.vely = 0

    def MoveRight(self):
        self.pac_anim_current = player.pac_anim_left
        self.velx = player.speed
        self.vely = 0
player = pacman()
     
class iNetwork():
    ip = '127.0.0.5'
    listen_t = threading.Thread()
    handler_t = threading.Thread()
    def __init__(self):
        endpoint.SetIP(ip=self.ip)
        self.listen_t = threading.Thread(target = self.Listen)
        self.handler_t = threading.Thread(target = self.EndPointHandler)
        self.listen_t.start()
        print('iNet INIT SUCCESSFULL')
    
    def Listen(self):
        print('Startin Listener')
        endpoint.Listen()
        print('Startin Handler')
        self.handler_t.start()
        
        


    def EndPointHandler(self):
        while True:
            buf = endpoint.RecvData()
            _msg = buf.decode('utf-8')
            self.ProcessMsg(msg= _msg)
            print('Msg Recvd: '+_msg)

    def ProcessMsg(self,msg):
            if(msg == 'Init'):
                playerInit = 0
                while playerInit == 0:
                    endpoint.SendData(buffOK)
                    buffX = bytes(str(player.x))
                    endpoint.SendData(buffX)
                    recvBuff = endpoint.RecvData()
                    if(recvBuff == buffACK):
                        recvBuff = bytes()
                        buffY = bytes(str(player.y))
                        endpoint.SendData(buffY)
                        buffFrame = bytes(str(player.animFrame))
                        endpoint.SendData(buffFrame)
                        recvBuff = endpoint.RecvData()
                        if(recvBuff == buffACK):
                            print('Player 2 has connected')

iNet = iNetwork()                




window_size = (800,500)
player_scale = (30,30)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pacman Multiplayer(lol)")
screen = pygame.display.get_surface()
bg = pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'bg1.png')), window_size).convert()
screen.blit(bg, (0,0))


def UpdatePlayer1():
    while 1:
        screen.blit(bg, (0,0))
        pygame.event.pump()
        player.RecvUpdate()
        player.Move()
        player.Draw()
        pygame.time.delay(30)
        pygame.display.update()

player1_t = threading.Thread(target = UpdatePlayer1)
player1_t.start()