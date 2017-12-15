import socket
import grab_screen
import cv2
import os

def make_and_enter_directory(directory_name):
   try:
       os.mkdir(directory_name)
   except:
        pass
   os.chdir(directory_name)
def server():
   socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket_server_number = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       #creating end point for connection
   host = (input("please Enter the ip: "))
   server_port = 800
   server_port_number = 8000
   socket_server.bind((host,server_port))
   socket_server_number.bind((host,server_port_number))
   print("hosting at "+str(host) +":"+str(server_port_number))
       #port and address for the client to conect
   socket_server.listen(5)
   socket_server_number.listen(5)
       #listener for the client to queue upto 5 requests
   (client_socket , address) = socket_server.accept()
   client_socket_number , addr = socket_server_number.accept()
       
   
   make_and_enter_directory("image")
       
   while True:
           p = grab_screen.grab_screen((0,0,800,800))
           p = cv2.cvtColor(p,cv2.COLOR_BGR2RGB)
           name = "roshan.png"
           cv2.imwrite(name ,p)
           file = open(name,"rb")
           fi = file.read()
           r = os.path.getsize(name)
           q = str(os.path.getsize(name))
           
           if int(q)>r*2/3:
               client_socket_number.send(str.encode(q))
               client_socket.send(fi)
           file.close()

   client_socket.close()
server()

    
