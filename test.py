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
    window.update()