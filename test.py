from engine import Window
from engine import InputManager
from engine import Sprite
from entity import Entity
from entity import SpriteRendererComponent
import time

window = Window(1280, 720, "tkinter game engine")
inputManager = InputManager(window)

testSprite = Sprite("test.png", 1)
entityTest = Entity(window, 100, 100)
entityTest.addComponent(SpriteRendererComponent(testSprite))

while True:
    if inputManager.getKey("w"):
        entityTest.translate(0, 1)
    if inputManager.getKey("s"):
        entityTest.translate(0, -1)
    if inputManager.getKey("d"):
        entityTest.translate(1, 0)
    if inputManager.getKey("a"):
        entityTest.translate(-1, 0)
    window.update()
    time.sleep(1/240)