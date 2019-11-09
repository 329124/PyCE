from tkinter import Tk
from tkinter import Canvas
from PIL import Image
from PIL import ImageTk

class Window:
    """Creates and controls tkinter window."""
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title(title)
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, width = width, height = height, highlightthickness = 0)
        self.__canvas.pack()

    def update(self):
        self.__root.update()

class InputManager:
    """Keeps track of user input."""
    def __init__(self, window):
        window._Window__canvas.bind_all("<KeyPress>", self.__cbKeyPressEvent)
        window._Window__canvas.bind_all("<KeyRelease>", self.__cbKeyReleaseEvent)
        self.__newlyActiveKeys = []
        self.__activeKeys = []

    def __cbKeyPressEvent(self, event):
        if event.char not in self.__newlyActiveKeys and event.char not in self.__activeKeys:
            self.__newlyActiveKeys.append(event.char)

    def __cbKeyReleaseEvent(self, event):
        if event.char in self.__newlyActiveKeys:
            self.__newlyActiveKeys.remove(event.char)
        if event.char in self.__activeKeys:
            self.__activeKeys.remove(event.char)

    def getKeyDown(self, key):
        """Will return true only once per key press."""
        if key in self.__newlyActiveKeys:
            self.__newlyActiveKeys.remove(key)
            self.__activeKeys.append(key)
            return True
        else:
            return False

    def getKey(self, key):
        """Will always return true if key is held down."""
        if key in self.__newlyActiveKeys:
            self.__newlyActiveKeys.remove(key)
            self.__activeKeys.append(key)
            return True
        elif key in self.__activeKeys:
            return True
        else:
            return False

class Sprite:
    """Container for images."""
    def __init__(self, path, scale):
        baseImage = Image.open(path)
        resizedImage = baseImage.resize((baseImage.width * scale, baseImage.height * scale), Image.NEAREST)
        self.width = resizedImage.width
        self.height = resizedImage.height
        self.photoImage = ImageTk.PhotoImage(resizedImage)

class Entity:
    """Creates a transformable instance of a given sprite."""
    def __init__(self, sprite, window, x = 0, y = 0):
        self.x = x
        self.y = y
        self.__window = window
        self.id = window._Window__canvas.create_image(self.x, window.height - self.y, image = sprite.photoImage, anchor = "center")

    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.__window._Window__canvas.move(self.id, dx, -dy)

    def destroy(self):
        self.__window._Window__canvas.delete(self.id)