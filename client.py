import socket
import os
import pygame as py
def disp(img,game_display):
        image = py.image.load(img)
        game_display.blit(image,(0,0))
        py.display.update()
        for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

host = input("Enter the server ip: ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket_number = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#end point for client
py.init()
game_display = py.display.set_mode((800,800))

try:
    client_socket.connect((host,800))
    client_socket_number.connect((host,8000))
    print("connected")
except:
    print("failed connecting to the server")
try:
        os.mkdir("image")
except:
        pass
os.chdir("image")

def p():
        size = client_socket_number.recv(6)
        q = client_socket.recv(int(size.decode()))       
        r= "roshan.png"
        fil = open(r,"wb")
        fil.write(q)
        fil.close()
        try:
                disp(r,game_display)
        except:
                disp("Error.png",game_display)
                
while True:
        p()
client_socket.close()
