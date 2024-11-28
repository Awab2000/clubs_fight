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


def delay_time(n, period):
    i = 0
    while i < n:
        pygame.time.delay(period)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = n+1
                pygame.quit()


def write_on_screen(font_type, font_size, font_color, message, pos_x, pos_y, take_width = False):
    font = pygame.font.SysFont(font_type, font_size)
    text = font.render(message, 1, font_color)
    if take_width:
        Display.blit(text, (766 - (text.get_width() / 2), pos_y))
    else:
        Display.blit(text, (pos_x, pos_y))


def check_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

def game_intro():
    while True:
        display_background_image()
        write_on_screen("comicsans", 100, WHITE, "CLUBS FIGHT", 766 - (750 // 2), 150)
        pygame.draw.rect(Display, WHITE, (350, 490, BUTTONS_WIDTH, BUTTONS_HEIGHT))
        write_on_screen("comicsans", 55, BLACK, "Play", 430, 475)
        pygame.draw.rect(Display, WHITE, (850, 490, BUTTONS_WIDTH, BUTTONS_HEIGHT))
        write_on_screen("comicsans", 45, BLACK, "High Score", 860, 485)
        write_on_screen("comicsans", 30, WHITE, "Playing instruction: Use the arrows to avoid the rival and reach the Champions league cup", 150, 700)
        check_quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 + BUTTONS_WIDTH > cur[0] > 350  and BUTTONS_HEIGHT + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, SILVER, (350, 490, BUTTONS_WIDTH, BUTTONS_HEIGHT))
            write_on_screen("comicsans", 55, BLACK, "Play", 430, 475)
            if click[0] == 1 :
                delay_time(50,5)
                break
        if 850 + BUTTONS_WIDTH > cur[0] > 850  and BUTTONS_HEIGHT + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, SILVER, (850, 490, BUTTONS_WIDTH, BUTTONS_HEIGHT))
            write_on_screen("comicsans", 45, BLACK, "High Score", 860, 485)
            if click[0] == 1 :
                view_high()
        pygame.display.update()

def choose():
    choose = True
    while choose:
        display_background_image()
        positions = [(300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (800, 300), (900, 300), (1000, 300), (300, 500), (400, 500), (500, 500),
                     (600, 500), (700, 500), (800, 500), (900, 500), (1000, 500), (1100, 500), (1100, 300), (1200, 300), (1200, 500)]

        for idx, team in enumerate(teams):
            team.pos_x, team.pos_y = positions[idx]
            team.draw_logo()
            team.is_turn = False

        write_on_screen("comicsans", 70, WHITE, "Choose a team to start the game", 230, 110)
        check_quit()

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for team in teams:
            if team.pos_x + team.width > cur[0] > team.pos_x  and team.height + team.pos_y > cur[1] > team.pos_y :
                if click[0] == 1 :
                    team.is_turn = True
                    team.play_chant()
                    choose = False
                    delay_time(50, 5)
                    break
        pygame.display.update()


def view_high():
    while True:
        display_background_image()
        write_on_screen("comicsans", 70, WHITE, "HIGH SCORE", 525, 175)
        write_on_screen("comicsans", 70, WHITE, user_text + ': ' + str(HIGH_SCORE) + " seconds", 410, 340, True)
        pygame.draw.rect(Display, WHITE, (620, 550, BUTTONS_WIDTH, BUTTONS_HEIGHT))
        write_on_screen("comicsans", 55, BLACK, "Back", 680, 540)
        check_quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + BUTTONS_WIDTH > cur[0] > 620 and BUTTONS_HEIGHT + 550 > cur[1] > 550 :
            pygame.draw.rect(Display, SILVER, (620, 550, BUTTONS_WIDTH, BUTTONS_HEIGHT))
            write_on_screen("comicsans", 55, BLACK, "Back", 680, 540)
            if click[0] == 1 :
                break
        pygame.display.update()

def entry():
    global user_text
    while True:
        display_background_image()
        write_on_screen("comicsans", 60, WHITE, "Type your name:", 490, 175, True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        write_on_screen("comicsans", 60, WHITE, user_text, 490, 340, True)
        pygame.draw.rect(Display, WHITE, (620, 550, BUTTONS_WIDTH, BUTTONS_HEIGHT))
        write_on_screen("comicsans", 60, BLACK, "Save", 685, 530)

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + BUTTONS_WIDTH > cur[0] > 620 and BUTTONS_HEIGHT + 550 > cur[1] > 550:
            pygame.draw.rect(Display, SILVER, (620, 550, BUTTONS_WIDTH, BUTTONS_HEIGHT))
            write_on_screen("comicsans", 60, BLACK, "Save", 685, 530)
            if click[0] == 1:
                with open(player_name_file, 'w', encoding='UTF-8') as file:
                    file.write(user_text)
                with open(High_score_file, 'w', encoding='UTF-8') as file:
                    file.write(str(HIGH_SCORE))
                break
        pygame.display.update()

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
        if player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > \
                enemy.hitbox[1]:
            if player1.hitbox[0] + player1.hitbox[2] > enemy.hitbox[0] and player1.hitbox[0] < enemy.hitbox[0] + \
                    enemy.hitbox[2]:
                is_hit = True
                for ene in enemies:
                    ene.restart_position()
                player1.hit()
                break

    if player1.hitbox[1] < cup.hitbox[1] + cup.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > cup.hitbox[1] and not is_hit:
        if player1.hitbox[0] + player1.hitbox[2] > cup.hitbox[0] and player1.hitbox[0] < cup.hitbox[0] + cup.hitbox[2]:
            player1.check_high()
            is_hit = True
            for ene in enemies:
                ene.restart_position()
    return is_hit

pygame.init()
pygame.key.set_repeat()
SCREEN_WIDTH = 1533
SCREEN_HEIGHT = 790
Display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CLUBS FIGHT")

BACKGROUND = pygame.image.load("UCL2.PNG")
CUP = pygame.image.load("Cup2.PNG")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
BUTTONS_WIDTH = 250
BUTTONS_HEIGHT = 60
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

clock = pygame.time.Clock()

High_score_file = "Backend/High_score.txt"
with open(High_score_file, 'r', encoding='UTF-8') as file:
    HIGH_SCORE = int(file.readline())

player_name_file = "Backend/Name.txt"
with open(player_name_file, 'r', encoding='UTF-8') as file:
    user_text = file.readline()


player1 = Player()
enemies = [enemy() for i in range(11)]
cup = Trophy(1493, 722, 40, 68)
time = Time(1450,0)

if __name__ == '__main__':
    while True:
        play_background_sound()
        game_intro()
        choose()

        while True:
            RedrawGameWindow()
            time.start = True
            clock.tick(FPS)
            if (collapse()):
                time.restart_time()
                time.start = False
                break
            check_quit()
            player1.move()
