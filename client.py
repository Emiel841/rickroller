import socket
import webbrowser
from time import sleep
from pynput.keyboard import Key, Controller
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 6789))

keyboard = Controller()

def lock_keyboard():
    keyboard.press(Key.f6)
    sleep(0.01)
    keyboard.release(Key.f6)
    print("locking")
    """ did not work
    keyboard.press(Key.alt)
    keyboard.press(Key.ctrl)
    keyboard.press("l")
    sleep(0.01)
    #
    keyboard.release(Key.alt)
    keyboard.release(Key.ctrl)
    keyboard.release("l")
    """


locked = False

while True:

    msg = s.recv(1024)
    if msg != 0:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        x = 0
        while x <= 50:
            keyboard.press(Key.media_volume_up)
            sleep(0.001)
            keyboard.release(Key.media_volume_up)
        if not locked:
            lock_keyboard() #and mouse
            locked = True

print("done")

