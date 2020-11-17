class EnterName():
    x = 0
    y = 0
    w = 0
    h = 0
    select = False
    text_ = ''
    numb = 0

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self,t):
        rect(self.x, self.y, self.w, self.h)

        fill(0,0,0)
        if t != '':
            text(self.text_, self.x, self.y, self.w, self.h)
        else:
            if self.select:
                text(self.text_, self.x, self.y, self.w, self.h)
        fill(255,255,255)

    def pressing(self):
        if (mouseX > self.x - self.w/2 and mouseX < self.x + self.w/2 and
            mouseY > self.y - self.h/2 and mouseY < self.y + self.h/2):
            self.select = True
        else:
            self.select = False

    def replace(self):
        if self.select:
            pass
