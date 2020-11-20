class ButtonForKill():
    x = 0
    y = 0
    w = 0
    h = 0
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self, kill_button):
        image(kill_button, self.x, self.y, self.w, self.h)

    def pressing(self):
        if (mouseX > self.x - self.w/2 and mouseX < self.x + self.w/2 and
            mouseY > self.y - self.h/2 and mouseY < self.y + self.h/2):
            return True
