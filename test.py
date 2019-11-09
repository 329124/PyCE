from engine import Window
from engine import Sprite
from engine import Entity
from engine import InputManager
import time

window = Window(1280, 720, "tkinter game engine")
testSprite = Sprite("test.png", 1)
entityTopRight   = Entity(testSprite, window, window.width - testSprite.width / 2, window.height - testSprite.height / 2)
entityBottomLeft = Entity(testSprite, window, testSprite.width / 2, testSprite.height / 2)
inputManager = InputManager(window)
while True:
    if inputManager.getKeyDown('e'):
        print("The 'e' key has just been pressed down!")
    elif inputManager.getKey('e'):
        print("The 'e' key is being held down!")
    window.update()
    time.sleep(1/144)