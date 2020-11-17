class UseButton():
    x = 0
    y = 0
    select = False
    select_button = True
    r_x = 0
    r_y = 0


    def __init__(self, x, y, r_x, r_y):
        self.x = x
        self.y = y
        self.r_x = r_x
        self.r_y = r_y
    

    def show(self, use_button):
        if self.select_button:
            image(use_button, self.x, self.y, self.r_x, self.r_y)
            
    def pressing(self):
        if self.select_button:
            if (self.x - self.r_x/2 < mouseX and mouseX < self.x + self.r_x/2 and
                self.y - self.r_y/2 < mouseY and mouseY < self.y + self.r_y/2):
                self.select = not self.select
