class TaskWeapons():
    x = 0
    y = 0
    r = 50
    speed = 0
    select = False
    x2 = 0
    y2 = 0
    r2 = 0

    def __init__(self,x,y,speed,x2,y2,r2):
        self.x = x
        self.y = y
        self.speed = speed

        self.x2 = x2
        self.y2 = y2
        self.r2 = r2

    def show(self):
        fill(0,0,0)
        rect(self.x, self.y, self.r, self.r,10)

    def move(self):

        self.x = self.x - self.speed    

    def show_on_background(self):
        if self.x < self.x2 + self.r2/2:
            return True

    def delite(self):
        return self.x2 - self.r2/2 > self.x    

    def boom(self):
        if (self.x - self.r/2 < mouseX and mouseX < self.x + self.r/2 and
            self.y - self.r/2 < mouseY and mouseY < self.y + self.r/2):
            self.select = True
