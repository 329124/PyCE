from engine import Window
from engine import Sprite
from engine import Entity
import time

window = Window(1280, 720, "tkinter game engine")
testSprite = Sprite("test.png", 1)
entityTopRight   = Entity(testSprite, window, 1280 - testSprite.width, 720 - testSprite.height)
entityBottomLeft = Entity(testSprite, window)
while True:
    window.update()
    time.sleep(1/144)