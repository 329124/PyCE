from tkinter import Tk
from tkinter import Canvas
from PIL import Image
from PIL import ImageTk

class Window:
    """Window"""
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, width = width, height = height, highlightthickness = 0)
        self.canvas.pack()
        self.entityList = []

    def addEntity(self, entity):
        self.entityList.append(entity)

    def update(self):
        for entity in self.entityList:
            entity.updateComponents()
        self.root.update()

class InputManager:
    """Input Manager"""
    def __init__(self, window):
        self.window = window
        window.canvas.bind_all("<KeyPress>", self.cbKeyPressEvent)
        window.canvas.bind_all("<KeyRelease>", self.cbKeyReleaseEvent)
        window.canvas.bind("<Motion>", self.cbMotionEvent)
        window.canvas.bind("<Button-1>", self.cbLeftButtonPressEvent)
        window.canvas.bind("<ButtonRelease-1>", self.cbLeftButtonReleaseEvent)
        window.canvas.bind("<Button-3>", self.cbRightButtonPressEvent)
        window.canvas.bind("<ButtonRelease-3>", self.cbRightButtonReleaseEvent)
        self.newlyActiveKeys = []
        self.activeKeys = []
        self.mouseData = self.MouseData()

    class MouseData:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.leftActive = False
            self.leftNewlyActive = False
            self.rightActive = False
            self.rightNewlyActive = False

    def cbKeyPressEvent(self, event):
        if event.char not in self.newlyActiveKeys and event.char not in self.activeKeys:
            self.newlyActiveKeys.append(event.char)

    def cbKeyReleaseEvent(self, event):
        if event.char in self.newlyActiveKeys:
            self.newlyActiveKeys.remove(event.char)
        if event.char in self.activeKeys:
            self.activeKeys.remove(event.char)

    def cbMotionEvent(self, event):
        self.mouseData.x = event.x
        self.mouseData.y = self.window.height - event.y - 1

    def cbLeftButtonPressEvent(self, event):
        if not self.mouseData.leftActive:
            self.mouseData.leftNewlyActive = True
        self.mouseData.leftActive = True

    def cbLeftButtonReleaseEvent(self, event):
        self.mouseData.leftActive = False
        self.mouseData.leftNewlyActive = False
    
    def cbRightButtonPressEvent(self, event):
        if not self.mouseData.rightActive:
            self.mouseData.rightNewlyActive = True
        self.mouseData.rightActive = True
    
    def cbRightButtonReleaseEvent(self, event):
        self.mouseData.rightActive = False
        self.mouseData.rightNewlyActive = False

    def getMousePosition(self):
        """Returns tuple of the mouse's x and y position."""
        return (self.mouseData.x, self.mouseData.y)

    def getMouseLeftDown(self):
        """Will only return true once per left mouse button press."""
        if self.mouseData.leftNewlyActive:
            self.mouseData.leftNewlyActive = False
            return True
        else:
            return False

    def getMouseLeft(self):
        """Will always return true if left mouse button is held down."""
        return self.mouseData.leftActive

    def getMouseRightDown(self):
        """Will only return true once per right mouse button press."""
        if self.mouseData.rightNewlyActive:
            self.mouseData.rightNewlyActive = False
            return True
        else:
            return False
    
    def getMouseRight(self):
        """Will always return true if right mouse button is held down."""
        return self.mouseData.rightActive

    def getKeyDown(self, key):
        """Will only return true once per key press."""
        if key in self.newlyActiveKeys:
            self.newlyActiveKeys.remove(key)
            self.activeKeys.append(key)
            return True
        else:
            return False

    def getKey(self, key):
        """Will always return true if key is held down."""
        if key in self.newlyActiveKeys:
            self.newlyActiveKeys.remove(key)
            self.activeKeys.append(key)
            return True
        elif key in self.activeKeys:
            return True
        else:
            return False

class Sprite:
    """Sprite"""
    def __init__(self, path, scale):
        baseImage = Image.open(path)
        resizedImage = baseImage.resize((baseImage.width * scale, baseImage.height * scale), Image.NEAREST)
        self.width = resizedImage.width
        self.height = resizedImage.height
        self.photoImage = ImageTk.PhotoImage(resizedImage)