import socket

IP =  socket.gethostbyname(socket.gethostname())   #get computer IP
PORT = 5050
Format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #type and family
addr = (IP, PORT)
server.bind(addr)  #bind the socket with the server address, IP and port

directionNum = [87,65,83,68] # w,a,s,d  keycodes
speed = 0

def direction (speed, *dir):
    if(len(dir)<2): #if passed direction is length 1, only forward or reverse
        print((f'[{dir[0]}{speed}][{dir[0]}{speed}][{dir[0]}{speed}][{dir[0]}{speed}]'))
    else:
       print(f'[{dir[0]}{speed}][{dir[0]}{speed}][{dir[1]}{speed}][{dir[1]}{speed}]')

def roverOutput(msg):
    if (msg>=49 and msg<=53): #check if its the msg is for speed
        global speed
        speed = int(((msg-48)/5) * 255)  #map speed from 1-5 to 0 to 255
        print(f"Speed set to {speed}")
    else: #else its direction
        if (msg==directionNum[0]):  #forward
            direction(speed, 'f') #speed and state of each motor
        if (msg==directionNum[1]): #left
            direction(speed,'r','f') #speed and state of motor 1,2 and motor 3,4.
        if (msg==directionNum[2]):   #reverse
            direction(speed,'r')  #speed and state of each motor
        if (msg==directionNum[3]): #right
            direction(speed,'f','r')#speed and state of motor 1,2 and motor 3,4.


def server_client(conn, addr):  #individual client connection
    print(f"New Connection{addr} connected.")
    while True:
        #recieve client messagae, as bits 
        msg = conn.recv(1024)
        if msg: #check for not empty msg
            msg = int(str(msg, Format)) #convert msg to int number
            if (msg == 75):  #close the connection of the user from the server if 'k' is pressed
                break #break the loop
            print(f"[{addr}]: {msg}")  #see the send message
            roverOutput(msg)
    print("Connection Closed")
    conn.close()      #close the client connection to the server
     

print("Starting Server")
print(f"Server IP: {IP}")
server.listen() #listen for client to join
connection, address = server.accept() 
server_client(connection, address)