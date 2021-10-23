#import libraries
import socket
from pynput import keyboard
from pynput.keyboard import Listener
import logging


#basic log config
logging.basicConfig(filename=('keyLog.txt'), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

#defined pressed keynumbers
keyCodeNum = [87,65,83,68,49,50,51,52,53,75] #w,a,s,d,1,2,3,4,5,k(kill the connection between client and server)

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT =  5050
FORMAT = 'utf-8'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #client object
client.connect(((IP,PORT)))  #connect client to the server

#check if only key we want are pressed
def check (pressed_key,key):
    #check for only W,A,S,D for logging and sending to the server
    for i in keyCodeNum:
        if (pressed_key == i):
            logging.info(str(key))
            if (pressed_key == 75):   #if k is pressed, the server connection closes
                client.send(bytes(str(75),FORMAT))
            else:   # else send the keycode
                client.send(bytes(str(pressed_key),FORMAT))

def on_press(key):
    try:
        pressed_key = key.vk    #get the pressed key value
    except:
        pressed_key = key.value.vk    #if its an special key like esc
    print(pressed_key)
    check (pressed_key,key)   #check if pressed key is 1-5 or wasd
    
def on_release(key):
    if key == keyboard.Key.esc:  #esc key stops the listner
        # Stop listener
        return False


#Getting key strokes
with Listener(on_press=on_press, on_release = on_release) as listener:  #on_press=on_press is not calling them, creating it an instance.
    listener.join()

#key is pressed, calls listner, calls the function