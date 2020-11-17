class ExitGame():
    x = 0
    y = 0
    rx = 0
    ry = 0

    def __init__(self, x, y, rx, ry):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry

    def show(self):
        stroke(0,0,0)
        fill(64,171,255)
        rect(self.x, self.y, self.rx, self.ry)

        fill(0,0,0)
        text('EXIT',self.x, self.y+(25/2))

    def push_button(self):
        if (mouseX > self.x - self.rx and mouseX < self.x + self.rx and
            mouseY > self.y - self.ry and mouseY < self.y + self.ry):
            exit()
            
