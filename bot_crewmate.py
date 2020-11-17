class BotCrewmate():
    x = 0
    y = 0
    w = 0
    h = 0
    speed = 0
    skin = 0
    dead_body = None

    def __init__(self, x, y, w, h, skin, speed, dead_body):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = skin
        self.speed = speed/2
        self.dead_body = dead_body

    def show(self):
        self.x = self.x - self.speed
        image(self.skin, self.x, self.y, self.w, self.h)

    def distance(self):
        if self.x < width and self.x > 0 and self.y < height and self.y > 0:
            return True
        else:
            return False

    def report(self):
        image(self.dead_body, width/2 , height/2, width, height/2)
