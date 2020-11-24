class Impostor():
    x = 0
    y = 0
    rx = 100
    ry = 150
    speed = 5
    name = ''
    dx = 0
    dy = 0

    xt = 0
    yt = 0
    wt = 0
    ht = 0

    x_experimental_for_impostor = 0
    y_experimental_for_impostor = 0

    def __init__(self, x, y, xt, yt, wt, ht):
        self.x = x
        self.y = y

        self.xt = xt
        self.yt = yt
        self.wt = wt
        self.ht = ht

    def show(self,impostor):
        image(impostor, self.x, self.y, self.rx, self.ry)
        fill(0,0,0)
        text(self.name, self.x, self.y-50, self.rx, self.ry)
        fill(255,255,255)

    def move(self,dir,bot_crewmate_x,bot_crewmate_y,bot_crewmate_speed,experimental_for_impostor_x,experimental_for_impostor_y,place_task_x,place_task_y):

        if dir == LEFT:
            place_task_x = place_task_x + self.speed
            ###
            experimental_for_impostor_x = experimental_for_impostor_x + self.speed
            ###
            bot_crewmate_x = bot_crewmate_x + bot_crewmate_speed
            ###
        elif dir == RIGHT:
            place_task_x = place_task_x - self.speed
            ###
            experimental_for_impostor_x = experimental_for_impostor_x - self.speed
            ###
            bot_crewmate_x = bot_crewmate_x - bot_crewmate_speed
            ###
        elif dir == UP:
            place_task_y = place_task_y + self.speed
            ###
            experimental_for_impostor_y = experimental_for_impostor_y + self.speed
            ###
            bot_crewmate_y = bot_crewmate_y + bot_crewmate_speed
            ###
        elif dir == DOWN:
            place_task_y = place_task_y - self.speed
            ###
            experimental_for_impostor_y = experimental_for_impostor_y - self.speed
            ###
            bot_crewmate_y = bot_crewmate_y - bot_crewmate_speed

        return bot_crewmate_x, bot_crewmate_y, experimental_for_impostor_x, experimental_for_impostor_y, place_task_x, place_task_y

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
