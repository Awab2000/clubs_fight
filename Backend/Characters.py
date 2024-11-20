
#ToDO:
# Make Inteface

class Player:
    def __init__(self,x = 0, y = 0, width = 40, height = 54):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 9
        self.hitbox = (self.x , self.y, self.width, self.height)

    def draw(self):
        for team in teams:
            if team.is_turn:
                team.pos_x = self.x
                team.pos_y = self.y
                team.draw_logo()
                break
        self.hitbox = (self.x , self.y, self.width, self.height)

    def hit(self):
        self.x = 0
        self.y = 0
        write_on_screen("comicsans", 100, RED, "YOU LOSE", 490, 350, True)
        pygame.display.update()
        delay_time(200,10)


    def move(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        elif Keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.vel

        elif Keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        elif Keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.vel


    def win(self):
        self.x = 0
        self.y = 0
        write_on_screen("comicsans", 100, RED, "CONGRATS , YOU WON", 490, 350, True)
        pygame.display.update()
        delay_time(200,10)


    def check_high(self):
        self.x = 0
        self.y = 0
        self.win()
        global HIGH_SCORE
        if time.seconds < HIGH_SCORE:
            HIGH_SCORE = time.seconds
            write_on_screen("comicsans", 60, RED, "New High Score!!!", 490, 550, True)
            pygame.display.update()
            delay_time(200,10)
            play_background_sound()
            entry()



class enemy:
    def __init__(self, width = 40, height = 54):
        self.x = random.randint(200,1200)
        self.y = random.randint(200,730)
        self.width = width
        self.height = height
        self.speedx = 13
        self.speedy = 13
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self):
        self.move()
        for team in teams:
            if team.is_turn:
                team.rival_pos_x = self.x
                team.rival_pos_y = self.y
                team.draw_rival()
                break
        self.hitbox = (self.x , self.y, self.width, self.height)

    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x <= 0 or self.x + self.width >= SCREEN_WIDTH:
            self.speedx = - self.speedx
        if self.y <= 0 or self.y + self.height >= SCREEN_HEIGHT:
            self.speedy = -self.speedy

    def restart_position(self):
        self.x = random.randint(200,1200)
        self.y = random.randint(200,730)


class Trophy:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self,Display):
        Display.blit(CUP, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)