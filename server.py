import socket
import grabScreen
import cv2
import os

def makeAndEnterDirectory(directoryName):
   try:
       os.mkdir(directoryName)
   except:
        pass
   os.chdir(directoryName)
def server():
   socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socketServerNumber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       #creating end point for connection
   host = (input("please Enter the ip "))
   serverPort = 800
   serverPortNumber = 8000
   socketServer.bind((host,serverPort))
   socketServerNumber.bind((host,serverPortNumber))
   print("hosting at "+str(host) +":"+str(serverPortNumber))
       #port and address for the client to conect
   socketServer.listen(5)
   socketServerNumber.listen(5)
       #listener for the client to queue upto 5 requests
   (clientsocket , address) = socketServer.accept()
   clientSocketNumber , addr = socketServerNumber.accept()
       
   
   makeAndEnterDirectory("image")
       
   while True:
           p = grabScreen.grab_screen((0,0,800,800))
           p = cv2.cvtColor(p,cv2.COLOR_BGR2RGB)
           name = "roshan.png"
           cv2.imwrite(name ,p)
           file = open(name,"rb")
           fi = file.read()
           r = os.path.getsize(name)
           q = str(os.path.getsize(name))
           
           if int(q)>r*2/3:
               clientSocketNumber.send(str.encode(q))
               clientsocket.send(fi)
           file.close()

   clientsocket.close()

server()

    
