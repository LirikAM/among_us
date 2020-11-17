class ExperimentalForImpostor():
    x = 0
    y = 0
    select = True

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_alive(self, alive, rx, ry):
        if self.select:
            image(alive, self.x, self.y, rx, ry)

    def show_not_alive(self, notalive, rx, ry):
        if not self.select:
            image(notalive, self.x, self.y, rx, ry)
