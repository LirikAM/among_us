class OnlineGame():
    xb = 0
    yb = 0
    wb = 0
    hb = 0

    def __init__(self, x, y, w, h):
        self.xb = x
        self.yb = y
        self.wb = w
        self.hb = h/2

    def show(self):
        fill(255,255,255)
        rect(self.xb, self.yb- (25/2), self.wb, self.hb)

        fill(0,0,0)
        text("ONLINE", self.xb, self.yb)

    ### logic_section()
    def pressing(self):
        if (mouseX > self.xb - self.wb and mouseX < self.xb + self.wb and 
            mouseX > self.xb - self.wb and mouseX < self.xb + self.wb):
            return True
        else:
            return False

    def work_of_online(self):
        pass
    ### logic_section()
