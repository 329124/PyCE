from tkinter import Tk
from tkinter import Canvas
from PIL import Image
from PIL import ImageTk

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, width = width, height = height)
        self.canvas.pack()

    def update(self):
        self.root.update()

class Sprite:
    def __init__(self, path, scale):
        baseImage = Image.open(path)
        resizedImage = baseImage.resize((baseImage.width * scale, baseImage.height * scale), Image.NEAREST)
        self.width = resizedImage.width
        self.height = resizedImage.height
        self.photoImage = ImageTk.PhotoImage(resizedImage)

class Entity:
    def __init__(self, sprite, window, x = 0, y = 0):
        self.x = x
        self.y = y
        self.window = window
        self.id = window.canvas.create_image(self.x + 10, self.window.height - self.y - 6, image = sprite.photoImage)
    
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.window.canvas.move(self.id, dx, -dy)
    
    def destroy(self):
        self.window.canvas.delete(self.id)