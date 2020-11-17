class Tasker():
    x = 0
    y = 0
    rx = 0
    ry = 0
    
    x2 = 400
    y2 = 300
    r2 = 400
    
    the_sofa = None
    
    t_rx = 0
    t_ry = 0
    
    def __init__(self,x,y, the_sofa, rx, ry):
        self.x = x
        self.y = y
        self.the_sofa = the_sofa
        
        self.rx = rx
        self.ry = ry
        
        self.t_rx = rx
        self.t_ry = ry
        
    def show(self):
        image(self.the_sofa, self.x, self.y, self.rx, self.ry)
        
    def show_line(self):
        #line
        strokeWeight(7)
        line(self.x2-self.r2/2, mouseY, mouseX, mouseY)
        line(mouseX, self.y2-self.r2/2, mouseX, mouseY)
        line(self.x2+self.r2/2, mouseY, mouseX, mouseY)
        line(mouseX, self.y2+self.r2/2, mouseX, mouseY)
        
        noFill()
        rect(mouseX, mouseY, 100, 100)
        strokeWeight(0)
        #line
        
    def show_background(self):
        fill(79,170,19)
        rect(self.x2, self.y2, self.r2, self.r2)
        fill(255,255,255)

    def distance(self,player_crewmate_x, player_crewmate_y, player_crewmate_rx, player_crewmate_ry):

        dx = abs(player_crewmate_x - self.x)
        dy = abs(player_crewmate_y - self.y)
        
        if ((dy <= player_crewmate_ry/2 + self.t_ry/2) and
            (dx <= player_crewmate_rx/2 + self.t_rx/2)):
            return True
        else:
            return False
        
