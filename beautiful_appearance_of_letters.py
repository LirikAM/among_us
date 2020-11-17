class FiltrOfWords():
    message = 'Found a body!'
    last_update_time = 0
    index = 0

    def __init__(self):
        pass
        #self.message = msg

    def show(self):
        if millis() - self.last_update_time >= 100:
            self.last_update_time = millis()
            if self.index < len(self.message):
                self.index = self.index + 1
            else:
                self.message = 'Red was not The Impostor'
        fill(0,0,0)
        text(self.message[:self.index], width/2, height/2)
    
