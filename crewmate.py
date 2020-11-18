class Crewmate():
    x = 400
    y = 300
    rx = 100
    ry = 150
    name = ''

    xt = 0
    yt = 0
    wt = 0
    ht = 0

    scalex = 0
    scaley = 0
    scalew = 0
    scaleh = 0

    xtask = 0
    ytask = 0

    speed = 5
    image_of_crewmate = None

    class Area():
        x = 0
        y = 0
        w = 0
        h = 0

        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w

    list_of_ghost_rect = []

    def __init__(self, player_crewmate_black, xt, yt, wt, ht, scalex, scaley, scalew, scaleh, xtask, ytask):
        self.image_of_crewmate = player_crewmate_black

        self.xt = xt
        self.yt = yt
        self.wt = wt
        self.ht = ht

        self.xtask = xtask
        self.ytask = ytask

        self.scalex = scalex
        self.scaley = scaley
        self.scalew = scalew
        self.scaleh = scaleh

        
        self.list_of_ghost_rect = [self.Area(self.x-width/2, self.y, width/2, height/2),
                                   self.Area(self.x+width/2, self.y, width/2, height/2),
                                   self.Area(self.x, self.y-300, width/2, height/2),
                                   self.Area(self.x, self.y+300, width/2, height/2)]

    def show(self):
        image(self.image_of_crewmate, self.x, self.y, self.rx, self.ry)
        textSize(24)
        fill(0,0,0)
        text(self.name, self.x, self.y-50, self.rx, self.ry)
        fill(255,255,255)

        ###ghost_rect_x_for_bot_impostor
        noFill()
        noStroke()
        for ghost_rect in self.list_of_ghost_rect:
            rect(ghost_rect.x, ghost_rect.y, ghost_rect.w, ghost_rect.h)
        stroke(0,0,0)
        fill(255,255,255)
        ###ghost_rect_x_for_bot_impostor

    def him_tasks(self):
        fill(255,255,255)
        rect(self.xt, self.yt, self.wt, self.ht)

        textSize(20)
        fill(0,0,0)
        text('Tasks '+'\n'+'Clear a Astiroids', self.xt, self.yt-50)
        textSize(20)

    def scale_(self):
        noFill()
        rect(self.scalex, self.scaley, self.scalew, self.scaleh)

    def scale_fill(self):
        fill(0,255,0)
        rect(self.scalex-self.scalew/3, self.scaley, self.scalew/3, self.scaleh)

    def move(self,dir):
        if dir == LEFT:
            self.xtask = self.xtask+self.speed

        elif dir == RIGHT:
            self.xtask = self.xtask-self.speed

        elif dir == UP:
            self.ytask = self.ytask+self.speed

        elif dir == DOWN:
            self.ytask = self.ytask-self.speed

    def return_task(self):
        return self.xtask, self.ytask
