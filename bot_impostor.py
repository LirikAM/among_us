class BotImpostor():
    x = 0
    y = 0
    w = 0
    h = 0
    speed = 2
    time = 0
    select = False
    after_kill_u = False
    dir_of_bot_impstor = None
    select_impostor = False
    dir_list = ["LEFT","RIGHT","UP","DOWN"]
    skin = None

    xb = 0
    yb = 0
    wb = 0
    hb = 0

    def __init__(self, x, y, w, h, skin, xb, yb, wb, hb):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = skin

        self.xb = xb
        self.yb = yb
        self.wb = wb
        self.hb = hb

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)

    def show_to_hide_impostor(self):
        rect(self.xb, self.yb, self.wb, self.hb)
        fill(0,0,0)
        text('Press to hide The impostor', self.xb, self.yb, self.wb, self.hb)

    def press_to_hide_impostor(self):
        if mouseX > self.xb - self.wb/2 and mouseX < self.xb + self.wb/2 and mouseY > self.yb - self.hb/2 and mouseY < self.yb + self.hb/2:
            self.select_impostor = True

    def move(self):
        if (millis() - self.time) >= 1000:
            self.time = millis()
            self.dir_of_bot_impstor = self.dir_list[int(random(0,4))]

        if self.dir_of_bot_impstor == self.dir_list[0]:
            self.x = self.x - self.speed
        elif self.dir_of_bot_impstor == self.dir_list[1]:
            self.x = self.x + self.speed
        elif self.dir_of_bot_impstor == self.dir_list[2]:
            self.y = self.y - self.speed
        elif self.dir_of_bot_impstor == self.dir_list[3]:
            self.y = self.y + self.speed

        if self.x > width:
            self.dir_of_bot_impstor = self.dir_list[0]
        elif self.x < 0:
            self.dir_of_bot_impstor = self.dir_list[1]
        elif self.y > height:
            self.dir_of_bot_impstor = self.dir_list[2]
        elif self.y < 0:
            self.dir_of_bot_impstor = self.dir_list[3]

    def kill_player(self, list_of_rect):
        if self.x > list_of_rect[0]:
            self.x = self.x + self.speed
        elif self.x < list_of_rect[1]:
            self.x = self.x - self.speed
        elif self.y > list_of_rect[2]:
            self.y = self.y + self.speed
        elif self.x < list_of_rect[3]:
            self.y = self.y - self.speed

    def distance(self, player_x, player_y, player_w, player_h):
        dx = abs(player_x - self.x)
        dy = abs(player_y - self.y)
        if dx <= player_w/2+self.w/2 and dy <= player_h/2+self.h/2:
            self.select = True

    def kill_you(self):
        textSize(45)
        fill(0,0,0)
        text('YOU ARE DEAD', width/2, height/2-150)
        textSize(24)
        self.after_kill_u = True
