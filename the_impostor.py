class Impostor():
    x = 0
    y = 0
    rx = 100
    ry = 150
    speed = 5
    name = ''

    xt = 0
    yt = 0
    wt = 0
    ht = 0

    xtask = 0
    ytask = 0

    x_experimental_for_impostor = 0
    y_experimental_for_impostor = 0

    y_bot_crewmate = 0

    def __init__(self, x, y, xt, yt, wt, ht, xtask, ytask, x_experimental_for_impostor, y_experimental_for_impostor, y_bot_crewmate):
        self.x = x
        self.y = y

        self.xt = xt
        self.yt = yt
        self.wt = wt
        self.ht = ht

        self.xtask = xtask
        self.ytask = ytask

        self.x_experimental_for_impostor = x_experimental_for_impostor
        self.y_experimental_for_impostor = y_experimental_for_impostor

        self.y_bot_crewmate = y_bot_crewmate

    def show(self,impostor):
        image(impostor, self.x, self.y, self.rx, self.ry)
        fill(0,0,0)
        text(self.name, self.x, self.y-50, self.rx, self.ry)
        fill(255,255,255)

    def move(self,dir):

        if dir == LEFT:
            self.xtask = self.xtask + self.speed
            ###
            self.x_experimental_for_impostor = self.x_experimental_for_impostor + self.speed
            ###
        elif dir == RIGHT:
            self.xtask = self.xtask - self.speed
            ###
            self.x_experimental_for_impostor = self.x_experimental_for_impostor - self.speed
            ###
        elif dir == UP:
            self.ytask = self.ytask + self.speed
            ###
            self.y_experimental_for_impostor = self.y_experimental_for_impostor + self.speed
            ###
            self.y_bot_crewmate = self.y_bot_crewmate + self.speed
            ###
        elif dir == DOWN:
            self.ytask = self.ytask - self.speed
            ###
            self.y_experimental_for_impostor = self.y_experimental_for_impostor - self.speed
            ###
            self.y_bot_crewmate = self.y_bot_crewmate - self.speed

    def him_tasks(self):
        fill(255,255,255)
        rect(self.xt, self.yt, self.wt, self.ht)

        textSize(20)
        fill(0,0,0)
        text('Fakes Tasks '+'\n'+'Clear a Astiroids', self.xt, self.yt-50)
        textSize(20)

    def distance(self, exp_x, exp_y, exp_rx, exp_ry):
        dx = abs(self.x - exp_x)
        dy = abs(self.y - exp_y)

        if dx <= self.rx/2 + exp_rx/2 and dy <= self.ry/2 + exp_ry/2:
            return True
        else:
            return False

    ### return function

    def return_task(self):
        return self.xtask, self.ytask

    def return_experimental_for_impostor(self):
        return self.x_experimental_for_impostor, self.y_experimental_for_impostor

    def return_bot_crewmate(self):
        return self.y_bot_crewmate
    ### return fucntion
