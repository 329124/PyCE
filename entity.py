class Entity:
    """Entity"""
    def __init__(self, window, x = 0, y = 0):
        self.x = x
        self.y = y
        self.window = window
        self.window.addEntity(self)
        self.components = []

    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def updateComponents(self):
        for component in self.components:
            component.update()

    def addComponent(self, component):
        component.postInit(self)
        self.components.append(component)

class SpriteRendererComponent:
    """Sprite Renderer Component"""
    def __init__(self, sprite):
        self.sprite = sprite
    
    def postInit(self, entity):
        self.entity = entity
        self.lastX = entity.x
        self.lastY = entity.y
        self.id = entity.window.canvas.create_image(entity.x, entity.window.height - entity.y, image = self.sprite.photoImage, anchor = "center")

    def update(self):
        dx = self.entity.x - self.lastX
        dy = self.entity.y - self.lastY
        if dx != 0 or dy != 0:
            self.entity.window.canvas.move(self.id, dx, -dy)

    def destroy(self):
        self.entity.window.canvas.delete(self.id)