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

    ghost_rect_x1_for_bot_impostor = 0
    ghost_rect_y1_for_bot_impostor = 0
    ghost_rect_w1_for_bot_impostor = 0
    ghost_rect_h1_for_bot_impostor = 0

    ghost_rect_x2_for_bot_impostor = 0
    ghost_rect_y2_for_bot_impostor = 0
    ghost_rect_w2_for_bot_impostor = 0
    ghost_rect_h2_for_bot_impostor = 0

    ghost_rect_x3_for_bot_impostor = 0
    ghost_rect_y3_for_bot_impostor = 0
    ghost_rect_w3_for_bot_impostor = 0
    ghost_rect_h3_for_bot_impostor = 0

    ghost_rect_x4_for_bot_impostor = 0
    ghost_rect_y4_for_bot_impostor = 0
    ghost_rect_w4_for_bot_impostor = 0
    ghost_rect_h4_for_bot_impostor = 0

    list_of_ghost_rect_x_for_bot_impostor = []
    list_of_ghost_rect_y_for_bot_impostor = []
    list_of_ghost_rect_w_for_bot_impostor = []
    list_of_ghost_rect_h_for_bot_impostor = []

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

        self.ghost_rect_x1_for_bot_impostor = self.x-width/2
        self.ghost_rect_x2_for_bot_impostor = self.x+width/2
        self.ghost_rect_x3_for_bot_impostor = self.x
        self.ghost_rect_x4_for_bot_impostor = self.x

        self.ghost_rect_y1_for_bot_impostor = self.y
        self.ghost_rect_y2_for_bot_impostor = self.y
        self.ghost_rect_y3_for_bot_impostor = self.y-300
        self.ghost_rect_y4_for_bot_impostor = self.y+300

        self.ghost_rect_w1_for_bot_impostor = width/2
        self.ghost_rect_w2_for_bot_impostor = width/2
        self.ghost_rect_w3_for_bot_impostor = width/2
        self.ghost_rect_w4_for_bot_impostor = width/2

        self.ghost_rect_h1_for_bot_impostor = height/2
        self.ghost_rect_h2_for_bot_impostor = height/2
        self.ghost_rect_h3_for_bot_impostor = height/2
        self.ghost_rect_h4_for_bot_impostor = height/2

        self.list_of_ghost_rect_x_for_bot_impostor = [self.ghost_rect_x1_for_bot_impostor, self.ghost_rect_x2_for_bot_impostor, 
                                                      self.ghost_rect_x3_for_bot_impostor, self.ghost_rect_x4_for_bot_impostor]
        self.list_of_ghost_rect_y_for_bot_impostor = [self.ghost_rect_y1_for_bot_impostor, self.ghost_rect_y2_for_bot_impostor, 
                                                      self.ghost_rect_y3_for_bot_impostor, self.ghost_rect_y4_for_bot_impostor]
        self.list_of_ghost_rect_w_for_bot_impostor = [self.ghost_rect_w1_for_bot_impostor, self.ghost_rect_w2_for_bot_impostor, 
                                                      self.ghost_rect_w3_for_bot_impostor, self.ghost_rect_w4_for_bot_impostor]
        self.list_of_ghost_rect_h_for_bot_impostor = [self.ghost_rect_h1_for_bot_impostor, self.ghost_rect_h2_for_bot_impostor,
                                                      self.ghost_rect_h3_for_bot_impostor, self.ghost_rect_h4_for_bot_impostor]

    def show(self):
        image(self.image_of_crewmate, self.x, self.y, self.rx, self.ry)
        textSize(24)
        fill(0,0,0)
        text(self.name, self.x, self.y-50, self.rx, self.ry)
        fill(255,255,255)

        ###ghost_rect_x_for_bot_impostor
        rectMode(RIGHT)
        noFill()
        noStroke()
        #for (x in range(0, len(self.list_of_ghost_rect_x_for_bot_impostor)) and y in range(0, len(self.list_of_ghost_rect_y_for_bot_impostor)) and 
        #     w in range(0, len(self.list_of_ghost_rect_w_for_bot_impostor)) and h in range(0, len(self.list_of_ghost_rect_h_for_bot_impostor))):
        #rect(self.list_of_ghost_rect_x_for_bot_impostor, self.list_of_ghost_rect_y_for_bot_impostor, self.list_of_ghost_rect_w_for_bot_impostor, self.list_of_ghost_rect_h_for_bot_impostor)
        noStroke()
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
        numb = 30
        rectMode(LEFT)
        if self.scalew < numb:
            self.scalew = self.scalew - 5
            fill(0,255,0)
            rect(self.scalex, self.scaley, self.scalew, self.scaleh)
        rectMode(CENTER)

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
