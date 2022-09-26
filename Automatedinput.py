from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time



def coords(x,y,z,e, n, f):
    mouse = MouseController()
    keyboard =  KeyboardController()
    # SET mouse to position
    mouse.position = (789, 639)

    #highlight text
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)

    #Clear Text Line
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    #typecast values
    x = str(x)
    y = str(y)
    z = str(z)
    e = str(e)
    f = str(f)
    # enter coordinates then send

    keyboard.type('G0 ' + 'X'+ x +  ' Y' + y + ' Z' +z + ' E' + e + ' F' + f)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    #Clear Text Line
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    time.sleep(n)
