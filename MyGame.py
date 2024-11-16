import pygame
from pygame.locals import *
import random

class Team:
    def __init__(self, logo_image, stad_image, chant, rival_image, pos_x, pos_y, rival_pos_x, rival_pos_y, is_turn = False, width = 40, height = 54):
        self.logo_image = pygame.image.load(logo_image)
        self.stad_image = pygame.image.load(stad_image)
        self.chant = chant
        self.rival_image = pygame.image.load(rival_image)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rival_pos_x = rival_pos_x
        self.rival_pos_y = rival_pos_y
        self.is_turn = is_turn
        self.width = width
        self.height = height

    def draw_logo(self):
        Display.blit(self.logo_image, (self.pos_x, self.pos_y))

    def draw_stad(self):
        Display.blit(self.stad_image, (0, 0))

    def play_chant(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.chant)
        pygame.mixer.music.play(-1)

    def draw_rival(self):
        Display.blit(self.rival_image, (self.rival_pos_x, self.rival_pos_y))


def play_background_sound():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("UEFA.mp3")
    pygame.mixer.music.play(-1)

def display_background_image():
    Display.blit(BACKGROUND, (0, 0))


def delay_time():
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 201
                pygame.quit()



def game_intro():
    global start_time
    intro = True
    while intro:
        start_time = False
        display_background_image()
        font2 = pygame.font.SysFont("comicsans", 100)
        text = font2.render("CLUBS FIGHT", 1, WHITE)
        Display.blit(text, (766 - (text.get_width() / 2), 175))
        pygame.draw.rect(Display, WHITE, (350, 490, 250, 60))
        text00= font00.render("Play", 1, BLACK)
        Display.blit(text00, (430 , 500))
        pygame.draw.rect(Display, WHITE, (850, 490, 250, 60))
        text01 = font00.render("High Score", 1, BLACK)
        Display.blit(text01, (865, 500))
        font4 = pygame.font.SysFont("comicsans", 50)
        text4 = font4.render("How to play: use the arrows to avoid the rival and reach the Champions league cup", 1, WHITE)
        Display.blit(text4, (766 - (text4.get_width() / 2), 700))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 + 250 > cur[0] > 350  and 60 + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, SILVER, (350, 490, 250, 60))
            text02 = font00.render("Play", 1, BLACK)
            Display.blit(text02, (430, 500))
            pygame.display.update()
            if click[0] == 1 :
                intro = False
        if 850 + 250 > cur[0] > 850  and 60 + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, SILVER, (850, 490, 250, 60))
            text03 = font00.render("High Score", 1, BLACK)
            Display.blit(text03, (865, 500))
            pygame.display.update()
            if click[0] == 1 :
                view_high()


def choose():
    choose = True
    while choose:
        start_time = False
        display_background_image()
        positions = [(300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (800, 300), (900, 300), (1000, 300), (300, 500), (400, 500), (500, 500),
                     (600, 500), (700, 500), (800, 500), (900, 500), (1000, 500), (1100, 500), (1100, 300), (1200, 300), (1200, 500)]

        for idx, team in enumerate(teams):
            team.pos_x, team.pos_y = positions[idx]
            team.draw_logo()
            team.is_turn = False

        font3 = pygame.font.SysFont("comicsans", 100)
        text3 = font3.render("Choose a team to start the game", 1, WHITE)
        Display.blit(text3, (766 - (text3.get_width() / 2), 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for team in teams:
            if team.pos_x + team.width > cur[0] > team.pos_x  and team.height + team.pos_y > cur[1] > team.pos_y :
                if click[0] == 1 :
                    team.is_turn = True
                    team.play_chant()
                    choose = False
                    break


def view_high():
    view = True
    while view:
        start_time = False
        display_background_image()
        text6 = font5.render("HIGH SCORE", 1, WHITE)
        Display.blit(text6, (766 - (text6.get_width() / 2), 175))
        text7 = font5.render(user_text + ': ' + str(highscore) + " seconds", 1, WHITE)
        Display.blit(text7, (766 - (text7.get_width() / 2), 340))
        pygame.draw.rect(Display, WHITE, (620, 550, 250, 60))
        text9 = font00.render("Back", 1, BLACK)
        Display.blit(text9, (685 , 565))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + 250 > cur[0] > 620 and 60 + 550 > cur[1] > 550 :
            pygame.draw.rect(Display, SILVER, (620, 550, 250, 60))
            text10 = font00.render("Back", 1, BLACK)
            Display.blit(text10, (685, 565))
            pygame.display.update()
            if click[0] == 1 :
                view = False

def entry():
    entry = True
    global user_text
    while entry:
        start_time = False
        display_background_image()
        text10 = font5.render("Type your name:", 1, WHITE)
        Display.blit(text10, (766 - (text10.get_width() / 2), 175))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                with open(Name, 'w', encoding='UTF-8') as file:
                    file.write(user_text)
        text11 = font5.render(user_text, 1, WHITE)
        Display.blit(text11, (766 - (text11.get_width() / 2), 340))
        pygame.draw.rect(Display, WHITE, (620, 550, 250, 60))
        text12 = font00.render("Save", 1, BLACK)
        Display.blit(text12, (685, 565))
        pygame.display.update()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + 250 > cur[0] > 620 and 60 + 550 > cur[1] > 550:
            pygame.draw.rect(Display, SILVER, (620, 550, 250, 60))
            text13 = font00.render("Save", 1, BLACK)
            Display.blit(text13, (685, 565))
            pygame.display.update()
            if click[0] == 1:
                entry = False

class player:
    def __init__(self,x = 0, y = 0, width = 40, height = 54):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 9
        self.hitbox = (self.x , self.y, self.width, self.height)

    def draw(self):
        for team in teams:
            team.pos_x = self.x
            team.pos_y = self.y
            if team.is_turn:
                team.draw_logo()
                break
        self.hitbox = (self.x , self.y, self.width, self.height)

    def hit(self):
        self.x = 0
        self.y = 0
        font1 = pygame.font.SysFont("comicsans",100)
        text = font1.render("YOU LOSE", 1, RED)
        Display.blit(text,(766 - (text.get_width()/2),350))
        pygame.display.update()
        delay_time()
        play_background_sound()
        game_intro()
        choose()

    def win(self):
        self.x = 0
        self.y = 0
        font2 = pygame.font.SysFont("comicsans",100)
        text2 = font2.render("CONGRATS , YOU WON", 1, RED)
        Display.blit(text2,(766 - (text2.get_width()/2),350))
        pygame.display.update()
        delay_time()


    def check_high(self):
        self.x = 0
        self.y = 0
        global highscore
        if time.seconds < highscore:
            highscore = time.seconds
            with open(High_score , 'w' , encoding= 'UTF-8') as file:
                file.write(str(highscore))
            self.win()
            text2 = font5.render("New High Score!!!", 1, RED)
            Display.blit(text2, (766 - (text2.get_width() / 2), 550))
            pygame.display.update()
            delay_time()
            play_background_sound()
            entry()
            game_intro()
            choose()
        else:
            self.win()
            play_background_sound()
            game_intro()
            choose()

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
            team.rival_pos_x = self.x
            team.rival_pos_y = self.y
            if team.is_turn:
                team.draw_rival()
                break
        self.hitbox = (self.x , self.y, self.width, self.height)

    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x <= 0 or self.x + self.width >= 1533:
            self.speedx = - self.speedx
        if self.y <= 0 or self.y + self.height >= 790:
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

class Time:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.seconds = 0
        self.milliseconds = 0

    def draw(self,Display):
        text5 = font5.render("{}".format(self.seconds), 1, WHITE)
        Display.blit(text5, (self.x, self.y))
        self.move_time()

    def move_time(self):
        if start_time:
            if self.milliseconds > 1000:
                self.seconds += 1
                self.milliseconds -= 1000
            self.milliseconds += clock.tick_busy_loop(60)

    def restart_time(self):
        self.seconds = 0
        self.milliseconds = 0


def RedrawGameWindow():
    Display.fill(BLACK)
    for team in teams:
        if team.is_turn:
            team.draw_stad()
            break
    time.draw(Display)
    player1.draw()
    for enemy in enemies:
        enemy.draw()
    cup.draw(Display)
    pygame.display.update()

def collapse():
    is_hit = False
    for enemy in enemies:
        if is_hit:
            break
        if player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > \
                enemy.hitbox[1]:
            if player1.hitbox[0] + player1.hitbox[2] > enemy.hitbox[0] and player1.hitbox[0] < enemy.hitbox[0] + \
                    enemy.hitbox[2]:
                is_hit = True
                time.restart_time()
                for ene in enemies:
                    ene.restart_position()
                player1.hit()

    if player1.hitbox[1] < cup.hitbox[1] + cup.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > cup.hitbox[1]:
        if player1.hitbox[0] + player1.hitbox[2] > cup.hitbox[0] and player1.hitbox[0] < cup.hitbox[0] + cup.hitbox[2]:
            player1.check_high()
            time.restart_time()
            for ene in enemies:
                ene.restart_position()


pygame.init()
pygame.key.set_repeat()
screen_width = 1533
screen_height = 790
Display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CLUBS FIGHT")

BACKGROUND = pygame.image.load("UCL2.PNG")
CUP = pygame.image.load("Cup2.PNG")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
FPS = 2000

Liv = Team("Liv2.PNG","Anfield14.PNG","YNWA.mp3","ManU.PNG", 0, 0, 0, 500)
ManU = Team("ManU.PNG","OldTrafford2.PNG","GloryManU.mp3", "ManCity2.PNG", 0, 0, 0, 500)
Atl = Team("Atleti4.PNG", "Wanda2.PNG", "AtletiSong.mp3", "Real4.PNG", 0, 0, 0, 500)
Rma = Team("Real4.PNG", "Santiago3.PNG", "HalaMadridSong.mp3", "Fcb2.PNG", 0, 0, 0, 500)
Fcb = Team("Fcb2.PNG", "CampNou3.PNG", "BarcaSong.mp3", "Real4.PNG", 0, 0, 0, 500)
Val = Team("Valencia2.PNG", "Mestalla4.PNG", "ValenciaSong.mp3", "Atleti4.PNG", 0, 0, 0, 500)
Int = Team("Inter3.PNG", "Meazza3.PNG", "InterSong.mp3", "Milan4.PNG", 0, 0, 0, 500)
Mil = Team("Milan4.PNG", "SanSiro3.PNG", "AcMilanSong.mp3", "Inter3.PNG", 0, 0, 0, 500)
Juv = Team("Juve2.PNG", "JuveStadium2.PNG", "JuveSong.mp3", "Inter3.PNG", 0, 0, 0, 500)
Rom = Team("Roma2.PNG", "Olympico2.PNG", "RomaSong.mp3", "Lazio2.PNG", 0, 0, 0, 500)
Laz = Team("Lazio2.PNG", "Olympico2.PNG", "LazioSong.mp3", "Roma2.PNG", 0, 0, 0, 500)
Ars = Team("Arsenal2.PNG", "Emirates3.PNG", "ArsenalSong.mp3", "Tottenham2.PNG", 0, 0, 0, 500)
Che = Team("Chelsea2.PNG", "StamfordBridge2.PNG", "ChelseaSong.mp3", "Arsenal2.PNG", 0, 0, 0, 500)
City = Team("ManCity2.PNG", "Ettihad2.PNG", "CitySong.mp3", "ManU.PNG", 0, 0, 0, 500)
Tot = Team("Tottenham2.PNG", "Spurs2.PNG", "SpursSong.mp3", "Arsenal2.PNG", 0, 0, 0, 500)
Bay = Team("Bayern2.PNG", "Allianz2.PNG", "BayernSong.mp3", "BVB2.PNG", 0, 0, 0, 500)
Bvb = Team("BVB2.PNG", "Signal3.PNG", "BVBSong.mp3", "Bayern2.PNG", 0, 0, 0, 500)
Ol = Team("OL2.PNG", "Groupama3.PNG", "OLSong.mp3", "Marseille2.PNG", 0, 0, 0, 500)
Om = Team("Marseille2.PNG", "Velodrome2.PNG", "OMSong.mp3", "OL2.PNG", 0, 0, 0, 500)
Psg = Team("PSG2.PNG", "Parc2.PNG", "PsgSong.mp3", "Marseille2.PNG", 0, 0, 0, 500)

teams = [Liv, ManU, Atl, Rma, Fcb, Val, Int, Mil, Juv, Rom, Laz, Ars, Che, City, Tot, Bay, Bvb, Ol, Om, Psg]


font5 = pygame.font.SysFont("comicsans", 60)
clock = pygame.time.Clock()

High_score = "High_score.txt"
with open(High_score, 'r', encoding='UTF-8') as file:
    highscore = int(file.readline())

Name = "Name.txt"
with open(Name, 'r', encoding='UTF-8') as file:
    user_text = file.readline()

font00 = pygame.font.SysFont("comicsans", 60)

play_background_sound()

player1 = player()
enemies = [enemy() for i in range(11)]
cup = Trophy(1493, 722, 40, 68)
time = Time(1450,0)
game_intro()
choose()
Run = True
if __name__ == '__main__':
    while Run:
        start_time = True
        clock.tick(FPS)
        collapse()
        for event in pygame.event.get():
            if event.type == QUIT:
                Run = False

        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT] and player1.x > 0 :
            player1.x -= player1.vel

        elif Keys [pygame.K_RIGHT] and player1.x < 1533 - player1.width:
            player1.x += player1.vel

        elif Keys [pygame.K_UP] and player1.y > 0 :
            player1.y -= player1.vel

        elif Keys [pygame.K_DOWN] and player1.y  < 790 - player1.height :
            player1.y += player1.vel

        RedrawGameWindow()

    pygame.quit()