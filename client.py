import socket
import cv2
import os
import pygame as py
def disp(img,gameDisplay):
        
        
        image = py.image.load(img)
        gameDisplay.blit(image,(0,0))
        py.display.update()
        a =True
        for event in py.event.get():
                if event.type == py.QUIT:
                    pygame.quit()
                    quit()
       
                
host = input("Enter the server ip")
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocketNumber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#end point for client
py.init()
gameDisplay = py.display.set_mode((800,800))

try:
    clientsocket.connect((host,800))
    clientSocketNumber.connect((host,8000))
    print("connected")
except:
    print("failed connecting to the server")
print("message")
try:
        os.mkdir("image")
except:
        pass
os.chdir("image")

def p():
        size = clientSocketNumber.recv(6)
        q = clientsocket.recv(int(size.decode()))       
        r= "roshan.png"
        fil = open(r,"wb")
        fil.write(q)
        fil.close()
        try:
                
                        disp(r,gameDisplay)
        except:
                        disp("Error.png",gameDisplay)
                
while True:
        p()
clientsocket.close()
