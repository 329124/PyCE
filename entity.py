class Entity:
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
    def __init__(self, sprite):
        self.sprite = sprite
    
    def postInit(self, entity):
        self.entity = entity
        self.id = entity.window.canvas.create_image(entity.x, entity.window.height - entity.y, image = self.sprite.photoImage, anchor = "center")

    def update(self):
        currentPosition = self.entity.window.canvas.coords(self.id)
        dx = self.entity.x - currentPosition[0]
        dy = self.entity.y - self.entity.window.height + currentPosition[1] 
        if dx != 0 or dy != 0:
            self.entity.window.canvas.move(self.id, dx, -dy)

    def destroy(self):
        self.entity.window.canvas.delete(self.id)