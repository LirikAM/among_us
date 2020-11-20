class CharacterSelection():
    x = 0
    y = 0
    rx = 0

    select           = False
    select_to_choose = 0

    x2 = 0
    y2 = 0
    rx2 = 0
    ry2 = 0

    def __init__(self, x, y, rx, ry, x2):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        ############
        self.x2 = x2
        self.y2 = y
        self.rx2 = rx
        self.ry2 = ry

    def show(self, p_rx, p_ry, player):
        noFill()
        strokeWeight(5)
        rect(self.x, self.y, self.rx, self.ry)

        rect(self.x2, self.y2, self.rx2, self.ry2)
        strokeWeight(0)

        fill(0,0,0)
        text('Choose a character', width/2, height/2-250)
        text('Crewmate', self.x, self.y-self.ry/2-50)
        text('Impostor', self.x2, self.y2-self.ry2/2-50)
        fill(255,255,255)

        image(player, self.x, self.y, p_rx, p_ry)
        image(player, self.x2, self.y2, p_rx, p_ry)

    def choose_button(self):

        if not self.select:

            if (mouseX > self.x-self.rx/2 and mouseX < self.x+self.rx/2 and
                mouseY > self.y-self.ry/2 and mouseY < self.y+self.ry/2):
                self.select_to_choose = 1
                self.select = not False

            elif (mouseX > self.x2-self.rx2/2 and mouseX < self.x2+self.rx2/2 and
                  mouseY > self.y2-self.ry2/2 and mouseY < self.y2+self.ry2/2):
                    self.select_to_choose = 2
                    self.select = not False
