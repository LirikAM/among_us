class ButtonToStartGame():
    
    x  = 0
    y  = 0
    rx = 150
    ry = 100
    select_game = False
    
    def __init__(self, x2, y2):
    
        self.x = x2
        self.y = y2
        
    def show(self, start_button):
        image(start_button, self.x, self.y, self.rx, self.ry)

    def push_button(self):
        if (mouseX > self.x - self.rx and mouseX < self.x + self.rx and
            mouseY > self.y - self.ry and mouseY < self.y + self.ry):
            self.select_game = True
            delay(100)
        
