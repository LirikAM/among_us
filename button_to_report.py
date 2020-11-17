class ButtonToReport():
    x = 0
    y = 0
    w = 0
    h = 0
    select_to_show_back = False

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show_report(self, report_skin):
        image(report_skin, self.x, self.y, self.w, self.h)

    def pressing(self):
        if (mouseX > self.x - self.w/2 and mouseX < self.x + self.w/2 and
            mouseY > self.y - self.h/2 and mouseY < self.y + self.h/2):
            self.select_to_show_back = True
        else:
            self.select_to_show_back = False
