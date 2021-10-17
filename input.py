#import libraries
from pynput import keyboard
from pynput.keyboard import Listener
import logging

#basic log config
logging.basicConfig(filename=('keyLog.txt'), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

#defined pressed keynumbers
keyCodeNum = [87,65,83,68,49,50,51,52,53] #w,a,s,d,1,2,3,4,5

#define the function
def check (pressed_key,key):
    #check for only W,A,S,D for logging
    for i in keyCodeNum:
        if (pressed_key == i):
            logging.info(str(key))
def on_press(key):
    try:
        pressed_key = key.vk    #get the pressed key value
    except:
        pressed_key = key.value.vk    #if its an special key like esc
    print(pressed_key)
    check (pressed_key,key)   #check if pressed key is 1-5 or wasd
    
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


#Getting key strokes
with Listener(on_press=on_press, on_release = on_release) as listener:  #on_press=on_press is not calling them, creating it an instance.
    listener.join()


#key is pressed, calls listner, calls the function and saves the info