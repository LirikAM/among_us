class BotImpostor():
    x = 0
    y = 0
    w = 0
    h = 0
    skin = None

    def __init__(self, x, y, w, h, skin):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = skin

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)

    def move(self):
        pass

    def kill_player(self):
        pass
