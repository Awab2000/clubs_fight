
class Time:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.seconds = 0
        self.milliseconds = 0
        self.start = False

    def draw(self,Display):
        write_on_screen("comicsans", 60, WHITE, f'{self.seconds}', self.x, self.y)
        self.move_time()

    def move_time(self):
        if self.start:
            if self.milliseconds > 1000:
                self.seconds += 1
                self.milliseconds -= 1000
            self.milliseconds += clock.tick_busy_loop(60)

    def restart_time(self):
        self.seconds = 0
        self.milliseconds = 0