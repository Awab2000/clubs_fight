import pygame
from pygame.locals import *
pygame.init()
pygame.key.set_repeat()
Display = pygame.display.set_mode((1533,790))
pygame.display.set_caption("CLUBS FIGHT")
bg1 = pygame.image.load("UCL2.PNG")
Liv = pygame.image.load("Liv2.PNG")
ManU = pygame.image.load("ManU.PNG")
Atl = pygame.image.load("Atleti4.PNG")
Rma= pygame.image.load("Real4.PNG")
Fcb = pygame.image.load("Fcb2.PNG")
Val = pygame.image.load("Valencia2.PNG")
Int = pygame.image.load("Inter3.PNG")
Mil = pygame.image.load("Milan4.PNG")
Juv = pygame.image.load("Juve2.PNG")
Rom = pygame.image.load("Roma2.PNG")
Laz = pygame.image.load("Lazio2.PNG")
Ars = pygame.image.load("Arsenal2.PNG")
Che = pygame.image.load("Chelsea2.PNG")
City = pygame.image.load("ManCity2.PNG")
Tot = pygame.image.load("Tottenham2.PNG")
Bay = pygame.image.load("Bayern2.PNG")
Bvb = pygame.image.load("BVB2.PNG")
Ol = pygame.image.load("OL2.PNG")
Om = pygame.image.load("Marseille2.PNG")
Psg = pygame.image.load("PSG2.PNG")
Wanda = pygame.image.load("Wanda2.PNG")
Anfield = pygame.image.load("Anfield14.PNG")
CampNou = pygame.image.load("CampNou3.PNG")
Santiago = pygame.image.load("Santiago3.PNG")
Mestalla = pygame.image.load("Mestalla4.PNG")
Meazza = pygame.image.load("Meazza3.PNG")
SanSiro = pygame.image.load("SanSiro3.PNG")
JuveStad = pygame.image.load("JuveStadium2.PNG")
Olympico = pygame.image.load("Olympico2.PNG")
Emirates = pygame.image.load("Emirates3.PNG")
Stamford = pygame.image.load("StamfordBridge2.PNG")
Ettihad = pygame.image.load("Ettihad2.PNG")
OldTrafford = pygame.image.load("OldTrafford2.PNG")
TotStad = pygame.image.load("Spurs2.PNG")
Allianz = pygame.image.load("Allianz2.PNG")
Signal = pygame.image.load("Signal3.PNG")
Groupama = pygame.image.load("Groupama3.PNG")
Velodrome = pygame.image.load("Velodrome2.PNG")
Parc = pygame.image.load("Parc2.PNG")
Cup = pygame.image.load("Cup2.PNG")
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Silver = (192,192,192)
FPS = 2000
font5 = pygame.font.SysFont("comicsans", 60)
clock = pygame.time.Clock()
High_score = "High_score.txt"
f = open(High_score,'r')
s = f.readline()
highscore = int(s)
Name = "Name.txt"
f2 = open(Name,'r')
s2 = f2.readline()
name = s2
user_text = name
font00 = pygame.font.SysFont("comicsans", 60)
pygame.mixer.music.load("UEFA.mp3")
pygame.mixer.music.play(-1)
def game_intro():
    global start_time
    intro = True
    while intro:
        start_time = False
        Display.blit(bg1,(0,0))
        font2 = pygame.font.SysFont("comicsans", 100)
        text = font2.render("CLUBS FIGHT", 1, White)
        Display.blit(text, (766 - (text.get_width() / 2), 175))
        pygame.draw.rect(Display,White,(350,490,250,60))
        text00= font00.render("Play",1,Black)
        Display.blit(text00, (430 , 500))
        pygame.draw.rect(Display, White, (850, 490, 250, 60))
        text01 = font00.render("High Score", 1, Black)
        Display.blit(text01, (865, 500))
        font4 = pygame.font.SysFont("comicsans", 50)
        text4 = font4.render("How to play: use the arrows to avoid the rival and reach the Champions league cup",1,White)
        Display.blit(text4, (766 - (text4.get_width() / 2), 700))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 + 250 > cur[0] > 350  and 60 + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, Silver, (350, 490, 250, 60))
            text02 = font00.render("Play", 1, Black)
            Display.blit(text02, (430, 500))
            pygame.display.update()
            if click[0] == 1 :
                intro = False
        if 850 + 250 > cur[0] > 850  and 60 + 490 > cur[1] > 490 :
            pygame.draw.rect(Display, Silver, (850, 490, 250, 60))
            text03 = font00.render("High Score", 1, Black)
            Display.blit(text03, (865, 500))
            pygame.display.update()
            if click[0] == 1 :
                view_high()


def choose():
    global Atleti
    Atleti = False
    global Barcelona
    Barcelona = False
    global Real
    Real = False
    global Valencia
    Valencia = False
    global Inter
    Inter = False
    global Milan
    Milan = False
    global Juventus
    Juventus = False
    global Roma
    Roma = False
    global Lazio
    Lazio = False
    global Liver
    Liver = False
    global Arsenal
    Arsenal = False
    global Chelsea
    Chelsea = False
    global ManUnited
    ManUnited = False
    global ManCity
    ManCity = False
    global Tottenham
    Tottenham = False
    global Bayern
    Bayern = False
    global Borussia
    Borussia = False
    global Lyonnais
    Lyonnais = False
    global Paris
    Paris = False
    global Marseille
    Marseille = False
    choose = True
    while choose:
        start_time = False
        Display.blit(bg1, (0, 0))
        Display.blit(pygame.image.load("Atleti4.PNG"), (300, 300))
        Display.blit(pygame.image.load("Fcb2.PNG"), (400, 300))
        Display.blit(pygame.image.load("Real4.PNG"), (500, 300))
        Display.blit(pygame.image.load("Valencia2.PNG"), (600, 300))
        Display.blit(pygame.image.load("Inter3.PNG"), (700, 300))
        Display.blit(pygame.image.load("Juve2.PNG"), (800, 300))
        Display.blit(pygame.image.load("Lazio2.PNG"), (900, 300))
        Display.blit(pygame.image.load("Milan4.PNG"), (1000, 300))
        Display.blit(pygame.image.load("Roma2.PNG"), (300, 500))
        Display.blit(pygame.image.load("Arsenal2.PNG"), (400, 500))
        Display.blit(pygame.image.load("Chelsea2.PNG"), (500, 500))
        Display.blit(pygame.image.load("Liv2.PNG"), (600, 500))
        Display.blit(pygame.image.load("ManCity2.PNG"), (700, 500))
        Display.blit(pygame.image.load("ManU.PNG"), (800, 500))
        Display.blit(pygame.image.load("Tottenham2.PNG"), (900, 500))
        Display.blit(pygame.image.load("BVB2.PNG"), (1000, 500))
        Display.blit(pygame.image.load("Bayern2.PNG"), (1100, 500))
        Display.blit(pygame.image.load("OL2.PNG"), (1100, 300))
        Display.blit(pygame.image.load("Marseille2.PNG"), (1200, 300))
        Display.blit(pygame.image.load("PSG2.PNG"), (1200, 500))
        font3 = pygame.font.SysFont("comicsans", 100)
        text3 = font3.render("Choose a team to start the game", 1, White)
        Display.blit(text3, (766 - (text3.get_width() / 2), 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 300 + 40 > cur[0] > 300  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Atleti = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("AtletiSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 400 + 40 > cur[0] > 400  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Barcelona = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("BarcaSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 500 + 40 > cur[0] > 500  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Real = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("HalaMadridSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 600 + 40 > cur[0] > 600  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Valencia = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ValenciaSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 700 + 40 > cur[0] > 700  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Inter = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("InterSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 800 + 40 > cur[0] > 800  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Juventus = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("JuveSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 900 + 40 > cur[0] > 900 and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Lazio = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("LazioSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1000 + 40 > cur[0] > 1000  and 54 + 300 > cur[1] > 300:
            if click[0] == 1 :
                Milan = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("AcMilanSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 300 + 40 > cur[0] > 300  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Roma = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("RomaSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 400 + 40 > cur[0] > 400  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Arsenal = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ArsenalSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 500 + 40 > cur[0] > 500 and 54 + 500 > cur[1] > 500:
            if click[0] == 1 :
                Chelsea = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ChelseaSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 600 + 40 > cur[0] > 600  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Liver = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("YNWA.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 700 + 40 > cur[0] > 700  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                ManCity = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("CitySong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 800 + 40 > cur[0] > 800  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                ManUnited = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("GloryManU.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 900 + 40 > cur[0] > 900  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Tottenham = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("SpursSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1000 + 40 > cur[0] > 1000  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Borussia = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("BVBSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1100 + 40 > cur[0] > 1100  and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Bayern = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("BayernSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1100 + 40 > cur[0] > 1100  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Lyonnais = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("OLSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1200 + 40 > cur[0] > 1200  and 54 + 300 > cur[1] > 300 :
            if click[0] == 1 :
                Marseille = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("OMSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

        elif 1200 + 40 > cur[0] > 1200 and 54 + 500 > cur[1] > 500 :
            if click[0] == 1 :
                Paris = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("PsgSong.mp3")
                pygame.mixer.music.play(-1)
                choose = False

def view_high():
    view = True
    while view:
        start_time = False
        Display.blit(bg1, (0, 0))
        text6 = font5.render("HIGH SCORE", 1, White)
        Display.blit(text6, (766 - (text6.get_width() / 2), 175))
        text7 = font5.render(user_text + ': ' + str(highscore) + " seconds", 1, White)
        Display.blit(text7, (766 - (text7.get_width() / 2), 340))
        pygame.draw.rect(Display, White, (620, 550, 250, 60))
        text9 = font00.render("Back", 1, Black)
        Display.blit(text9, (685 , 565))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + 250 > cur[0] > 620 and 60 + 550 > cur[1] > 550 :
            pygame.draw.rect(Display, Silver, (620, 550, 250, 60))
            text10 = font00.render("Back", 1, Black)
            Display.blit(text10, (685, 565))
            pygame.display.update()
            if click[0] == 1 :
                view = False

def entry():
    entry = True
    global user_text
    while entry:
        start_time = False
        Display.blit(bg1, (0, 0))
        text10 = font5.render("Type your name:", 1, White)
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
        text11 = font5.render(user_text, 1, White)
        Display.blit(text11, (766 - (text11.get_width() / 2), 340))
        pygame.draw.rect(Display, White, (620, 550, 250, 60))
        text12 = font00.render("Save", 1, Black)
        Display.blit(text12, (685, 565))
        pygame.display.update()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 620 + 250 > cur[0] > 620 and 60 + 550 > cur[1] > 550:
            pygame.draw.rect(Display, Silver, (620, 550, 250, 60))
            text13 = font00.render("Save", 1, Black)
            Display.blit(text13, (685, 565))
            pygame.display.update()
            if click[0] == 1:
                entry = False

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.hitbox = (self.x , self.y, self.width, self.height)

    def draw(self,Display):
        if Atleti == True:
            Display.blit(Atl, (self.x, self.y))
        elif Barcelona == True:
            Display.blit(Fcb , (self.x,self.y))
        elif Real == True:
            Display.blit(Rma , (self.x,self.y))
        elif Valencia == True:
            Display.blit(Val , (self.x,self.y))
        elif Inter == True:
            Display.blit(Int , (self.x,self.y))
        elif Juventus == True:
            Display.blit(Juv , (self.x,self.y))
        elif Lazio == True:
            Display.blit(Laz , (self.x,self.y))
        elif Milan == True:
            Display.blit(Mil , (self.x,self.y))
        elif Roma == True:
            Display.blit(Rom , (self.x,self.y))
        elif Arsenal == True:
            Display.blit(Ars , (self.x,self.y))
        elif Chelsea == True:
            Display.blit(Che , (self.x,self.y))
        elif Liver == True:
            Display.blit(Liv , (self.x,self.y))
        elif ManCity == True:
            Display.blit(City , (self.x,self.y))
        elif ManUnited == True:
            Display.blit(ManU , (self.x,self.y))
        elif Tottenham == True:
            Display.blit(Tot , (self.x,self.y))
        elif Borussia == True:
            Display.blit(Bvb , (self.x,self.y))
        elif Bayern == True:
            Display.blit(Bay , (self.x,self.y))
        elif Lyonnais == True:
            Display.blit(Ol , (self.x,self.y))
        elif Marseille == True:
            Display.blit(Om , (self.x,self.y))
        elif Paris == True:
            Display.blit(Psg , (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)

    def hit(self):
        self.x = 0
        self.y = 0
        font1 = pygame.font.SysFont("comicsans",100)
        text = font1.render("YOU LOSE",1,Red)
        Display.blit(text,(766 - (text.get_width()/2),350))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("UEFA.mp3")
        pygame.mixer.music.play(-1)
        game_intro()
        choose()

    def win(self):
        self.x = 0
        self.y = 0
        font2 = pygame.font.SysFont("comicsans",100)
        text2 = font2.render("CONGRATS , YOU WON",1,Red)
        Display.blit(text2,(766 - (text2.get_width()/2),350))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()


    def high(self):
        self.x = 0
        self.y = 0
        global highscore
        if time.seconds < highscore:
            highscore = time.seconds
            with open(High_score , 'w' , encoding= 'UTF-8') as file:
                file.write(str(highscore))
            self.win()
            text2 = font5.render("New High Score!!!", 1, Red)
            Display.blit(text2, (766 - (text2.get_width() / 2), 550))
            pygame.display.update()
            i = 0
            while i < 200:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("UEFA.mp3")
            pygame.mixer.music.play(-1)
            entry()
            game_intro()
            choose()
        else:
            self.win()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("UEFA.mp3")
            pygame.mixer.music.play(-1)
            game_intro()
            choose()

class enemy:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedx = 13
        self.speedy = 13
        self.hitbox = (self.x , self.y, self.width, self.height)

    def draw(self,Display):
        self.move()
        if Atleti == True:
            Display.blit(Rma, (self.x, self.y))
        elif Barcelona == True:
            Display.blit(Rma, (self.x, self.y))
        elif Real == True:
            Display.blit(Fcb, (self.x, self.y))
        elif Valencia == True:
            Display.blit(Atl, (self.x, self.y))
        elif Inter == True:
            Display.blit(Mil, (self.x, self.y))
        elif Juventus == True:
            Display.blit(Int, (self.x, self.y))
        elif Lazio == True:
            Display.blit(Rom, (self.x, self.y))
        elif Milan == True:
            Display.blit(Int, (self.x, self.y))
        elif Roma == True:
            Display.blit(Laz, (self.x, self.y))
        elif Arsenal == True:
            Display.blit(Tot, (self.x, self.y))
        elif Chelsea == True:
            Display.blit(Ars, (self.x, self.y))
        elif Liver == True:
            Display.blit(ManU, (self.x, self.y))
        elif ManCity == True:
            Display.blit(ManU, (self.x, self.y))
        elif ManUnited == True:
            Display.blit(City, (self.x, self.y))
        elif Tottenham == True:
            Display.blit(Ars, (self.x, self.y))
        elif Borussia == True:
            Display.blit(Bay, (self.x, self.y))
        elif Bayern == True:
            Display.blit(Bvb, (self.x, self.y))
        elif Lyonnais == True:
            Display.blit(Om, (self.x, self.y))
        elif Marseille == True:
            Display.blit(Ol, (self.x, self.y))
        elif Paris == True:
            Display.blit(Om, (self.x, self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)

    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x <= 0 or self.x + self.width >= 1533:
            self.speedx = - self.speedx
        if self.y <= 0 or self.y + self.height >= 790:
            self.speedy = -self.speedy

class Trophy:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self,Display):
        Display.blit(Cup,(self.x,self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)

class Time:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.seconds = 0
        self.milliseconds = 0

    def draw(self,Display):
        text5 = font5.render("{}".format(self.seconds), 1, White)
        Display.blit(text5, (self.x, self.y))
        self.move_time()

    def move_time(self):
        if start_time:
            if self.milliseconds > 1000:
                self.seconds += 1
                self.milliseconds -= 1000
            self.milliseconds += clock.tick_busy_loop(60)


def RedrawGameWindow():
    Display.fill(Black)
    if Atleti == True:
        Display.blit(Wanda, (0,0))
    elif Barcelona == True:
        Display.blit(CampNou, (0,0))
    elif Real == True:
        Display.blit(Santiago, (0,0))
    elif Valencia == True:
        Display.blit(Mestalla, (0,0))
    elif Inter == True:
        Display.blit(Meazza, (0,0))
    elif Juventus == True:
        Display.blit(JuveStad, (0,0))
    elif Lazio == True:
        Display.blit(Olympico, (0,0))
    elif Milan == True:
        Display.blit(SanSiro, (0,0))
    elif Roma == True:
        Display.blit(Olympico, (0,0))
    elif Arsenal == True:
        Display.blit(Emirates, (0,0))
    elif Chelsea == True:
        Display.blit(Stamford, (0,0))
    elif Liver == True:
        Display.blit(Anfield, (0,0))
    elif ManCity == True:
        Display.blit(Ettihad, (0,0))
    elif ManUnited == True:
        Display.blit(OldTrafford, (0,0))
    elif Tottenham == True:
        Display.blit(TotStad, (0,0))
    elif Borussia == True:
        Display.blit(Signal, (0,0))
    elif Bayern == True:
        Display.blit(Allianz, (0,0))
    elif Lyonnais == True:
        Display.blit(Groupama, (0,0))
    elif Marseille == True:
        Display.blit(Velodrome, (0,0))
    elif Paris == True:
        Display.blit(Parc, (0,0))
    time.draw(Display)
    logo.draw(Display)
    logo2.draw(Display)
    logo3.draw(Display)
    logo4.draw(Display)
    logo5.draw(Display)
    logo6.draw(Display)
    logo7.draw(Display)
    logo8.draw(Display)
    logo9.draw(Display)
    logo10.draw(Display)
    logo11.draw(Display)
    logo12.draw(Display)
    cup.draw(Display)
    pygame.display.update()

def collapse():
    if logo.hitbox[1] < logo2.hitbox[1] + logo2.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo2.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo2.hitbox[0] and logo.hitbox[0] < logo2.hitbox[0] + logo2.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(555, 333, logo2.width, logo2.height)
            logo3.__init__(999, 666, logo3.width, logo3.height)
            logo4.__init__(1111, 100, logo4.width, logo4.height)
            logo5.__init__(375, 200, logo5.width, logo5.height)
            logo6.__init__(600, 600, logo6.width, logo6.height)
            logo7.__init__(1300, 0, logo7.width, logo7.height)
            logo8.__init__(550, 600, logo8.width, logo8.height)
            logo9.__init__(850, 700, logo9.width, logo9.height)
            logo10.__init__(190, 70, logo10.width, logo10.height)
            logo11.__init__(130, 35, logo11.width, logo11.height)
            logo12.__init__(700, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo3.hitbox[1] + logo3.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo3.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo3.hitbox[0] and logo.hitbox[0] < logo3.hitbox[0] + logo3.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(200, 400, logo2.width, logo2.height)
            logo3.__init__(400, 200, logo3.width, logo3.height)
            logo4.__init__(670, 20, logo4.width, logo4.height)
            logo5.__init__(800, 600, logo5.width, logo5.height)
            logo6.__init__(1300, 100, logo6.width, logo6.height)
            logo7.__init__(1000, 555, logo7.width, logo7.height)
            logo8.__init__(500, 100, logo8.width, logo8.height)
            logo9.__init__(850, 700, logo9.width, logo9.height)
            logo10.__init__(150, 70, logo10.width, logo10.height)
            logo11.__init__(60, 35, logo11.width, logo11.height)
            logo12.__init__(1200, 300, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo4.hitbox[1] + logo4.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo4.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo4.hitbox[0] and logo.hitbox[0] < logo4.hitbox[0] + logo4.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(700, 400, logo2.width, logo2.height)
            logo3.__init__(200, 400, logo3.width, logo3.height)
            logo4.__init__(300, 20, logo4.width, logo4.height)
            logo5.__init__(1000, 550, logo5.width, logo5.height)
            logo6.__init__(100, 700, logo6.width, logo6.height)
            logo7.__init__(1300, 0, logo7.width, logo7.height)
            logo8.__init__(899, 200, logo8.width, logo8.height)
            logo9.__init__(850, 700, logo9.width, logo9.height)
            logo10.__init__(330, 70, logo10.width, logo10.height)
            logo11.__init__(600, 35, logo11.width, logo11.height)
            logo12.__init__(1200, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo5.hitbox[1] + logo5.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo5.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo5.hitbox[0] and logo.hitbox[0] < logo5.hitbox[0] + logo5.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(350, 650, logo2.width, logo2.height)
            logo3.__init__(1000, 400, logo3.width, logo3.height)
            logo4.__init__(1400, 20, logo4.width, logo4.height)
            logo5.__init__(100, 550, logo5.width, logo5.height)
            logo6.__init__(777, 700, logo6.width, logo6.height)
            logo7.__init__(100, 100, logo7.width, logo7.height)
            logo8.__init__(500, 300, logo8.width, logo8.height)
            logo9.__init__(100, 700, logo9.width, logo9.height)
            logo10.__init__(150, 230, logo10.width, logo10.height)
            logo11.__init__(250, 35, logo11.width, logo11.height)
            logo12.__init__(1100, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo6.hitbox[1] + logo6.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo6.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo6.hitbox[0] and logo.hitbox[0] < logo6.hitbox[0] + logo6.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(900, 400, logo2.width, logo2.height)
            logo3.__init__(600, 200, logo3.width, logo3.height)
            logo4.__init__(500, 60, logo4.width, logo4.height)
            logo5.__init__(1000, 700, logo5.width, logo5.height)
            logo6.__init__(300, 700, logo6.width, logo6.height)
            logo7.__init__(1300, 100, logo7.width, logo7.height)
            logo8.__init__(100, 600, logo8.width, logo8.height)
            logo9.__init__(700, 700, logo9.width, logo9.height)
            logo10.__init__(150, 70, logo10.width, logo10.height)
            logo11.__init__(60, 35, logo11.width, logo11.height)
            logo12.__init__(1200, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo7.hitbox[1] + logo7.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo7.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo7.hitbox[0] and logo.hitbox[0] < logo7.hitbox[0] + logo7.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(1400, 100, logo2.width, logo2.height)
            logo3.__init__(200, 700, logo3.width, logo3.height)
            logo4.__init__(700, 20, logo4.width, logo4.height)
            logo5.__init__(500, 550, logo5.width, logo5.height)
            logo6.__init__(300, 300, logo6.width, logo6.height)
            logo7.__init__(900, 0, logo7.width, logo7.height)
            logo8.__init__(800, 400, logo8.width, logo8.height)
            logo9.__init__(400, 600, logo9.width, logo9.height)
            logo10.__init__(150, 555, logo10.width, logo10.height)
            logo11.__init__(60, 200, logo11.width, logo11.height)
            logo12.__init__(100, 400, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo8.hitbox[1] + logo8.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo8.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo8.hitbox[0] and logo.hitbox[0] < logo8.hitbox[0] + logo8.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(450, 400, logo2.width, logo2.height)
            logo3.__init__(1222, 400, logo3.width, logo3.height)
            logo4.__init__(300, 600, logo4.width, logo4.height)
            logo5.__init__(1000, 200, logo5.width, logo5.height)
            logo6.__init__(100, 700, logo6.width, logo6.height)
            logo7.__init__(1300, 250, logo7.width, logo7.height)
            logo8.__init__(800, 550, logo8.width, logo8.height)
            logo9.__init__(222, 333, logo9.width, logo9.height)
            logo10.__init__(150, 70, logo10.width, logo10.height)
            logo11.__init__(777, 199, logo11.width, logo11.height)
            logo12.__init__(900, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo9.hitbox[1] + logo9.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo9.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo9.hitbox[0] and logo.hitbox[0] < logo9.hitbox[0] + logo9.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(150, 333, logo2.width, logo2.height)
            logo3.__init__(1100, 700, logo3.width, logo3.height)
            logo4.__init__(700, 20, logo4.width, logo4.height)
            logo5.__init__(400, 550, logo5.width, logo5.height)
            logo6.__init__(900, 200, logo6.width, logo6.height)
            logo7.__init__(600, 0, logo7.width, logo7.height)
            logo8.__init__(1400, 500, logo8.width, logo8.height)
            logo9.__init__(850, 100, logo9.width, logo9.height)
            logo10.__init__(150, 600, logo10.width, logo10.height)
            logo11.__init__(766, 500, logo11.width, logo11.height)
            logo12.__init__(300, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo10.hitbox[1] + logo10.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo10.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo10.hitbox[0] and logo.hitbox[0] < logo10.hitbox[0] + logo10.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(600, 600, logo2.width, logo2.height)
            logo3.__init__(200, 200, logo3.width, logo3.height)
            logo4.__init__(100, 20, logo4.width, logo4.height)
            logo5.__init__(1000, 550, logo5.width, logo5.height)
            logo6.__init__(100, 700, logo6.width, logo6.height)
            logo7.__init__(900, 650, logo7.width, logo7.height)
            logo8.__init__(1400, 100, logo8.width, logo8.height)
            logo9.__init__(850, 700, logo9.width, logo9.height)
            logo10.__init__(700, 170, logo10.width, logo10.height)
            logo11.__init__(100, 100, logo11.width, logo11.height)
            logo12.__init__(444, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < logo11.hitbox[1] + logo11.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo11.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo11.hitbox[0] and logo.hitbox[0] < logo11.hitbox[0] + logo11.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(150, 600, logo2.width, logo2.height)
            logo3.__init__(400, 500, logo3.width, logo3.height)
            logo4.__init__(600, 20, logo4.width, logo4.height)
            logo5.__init__(800, 300, logo5.width, logo5.height)
            logo6.__init__(1000, 150, logo6.width, logo6.height)
            logo7.__init__(1200, 77, logo7.width, logo7.height)
            logo8.__init__(1400, 700, logo8.width, logo8.height)
            logo9.__init__(300, 100, logo9.width, logo9.height)
            logo10.__init__(500, 700, logo10.width, logo10.height)
            logo11.__init__(900, 35, logo11.width, logo11.height)
            logo12.__init__(700, 600, logo12.width, logo12.height)
            time.__init__(1450, 0)
            logo.hit()
    if logo.hitbox[1] < logo12.hitbox[1] + logo12.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo12.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo12.hitbox[0] and logo.hitbox[0] < logo12.hitbox[0] + logo12.hitbox[2]:
            time.__init__(1450, 0)
            logo2.__init__(1350, 650, logo2.width, logo2.height)
            logo3.__init__(1150, 450, logo3.width, logo3.height)
            logo4.__init__(950, 250, logo4.width, logo4.height)
            logo5.__init__(750, 50, logo5.width, logo5.height)
            logo6.__init__(650, 550, logo6.width, logo6.height)
            logo7.__init__(450, 0, logo7.width, logo7.height)
            logo8.__init__(250, 300, logo8.width, logo8.height)
            logo9.__init__(50, 600, logo9.width, logo9.height)
            logo10.__init__(830, 650, logo10.width, logo10.height)
            logo11.__init__(60, 35, logo11.width, logo11.height)
            logo12.__init__(90, 600, logo12.width, logo12.height)
            logo.hit()
    if logo.hitbox[1] < cup.hitbox[1] + cup.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > cup.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > cup.hitbox[0] and logo.hitbox[0] < cup.hitbox[0] + cup.hitbox[2]:
            logo.high()
            time.__init__(1450, 0)
            logo2.__init__(0, 500, logo2.width, logo2.height)
            logo3.__init__(200, 300, logo3.width, logo3.height)
            logo4.__init__(300, 20, logo4.width, logo4.height)
            logo5.__init__(500, 550, logo5.width, logo5.height)
            logo6.__init__(700, 200, logo6.width, logo6.height)
            logo7.__init__(1300, 100, logo7.width, logo7.height)
            logo8.__init__(500, 250, logo8.width, logo8.height)
            logo9.__init__(850, 150, logo9.width, logo9.height)
            logo10.__init__(150, 600, logo10.width, logo10.height)
            logo11.__init__(900, 35, logo11.width, logo11.height)
            logo12.__init__(1200, 400, logo12.width, logo12.height)


#MainLoop
logo = player(0, 0, 40, 54)
logo2 = enemy(700, 400, 40, 54)
logo3 = enemy(200, 400, 40, 54)
logo4 = enemy(300, 20, 40, 54)
logo5 = enemy(1000, 550, 40, 54)
logo6 = enemy(100, 700, 40, 54)
logo7 = enemy(1300, 0, 40, 54)
logo8 = enemy(500, 600, 40, 54)
logo9 = enemy(850, 700, 40, 54)
logo10 = enemy(150, 70, 40, 54)
logo11 = enemy(60, 35, 40, 54)
logo12 = enemy(1200, 600, 40, 54)
cup = Trophy(1493, 722, 40, 68)
time = Time(1450,0)
game_intro()
choose()
Run = True
while Run:
    start_time = True
    clock.tick(FPS)
    collapse()
    for event in pygame.event.get():
        if event.type == QUIT:
            Run = False

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_LEFT] and logo.x > 0 :
        logo.x -= logo.vel

    elif Keys [pygame.K_RIGHT] and logo.x < 1533 - logo.width:
        logo.x += logo.vel

    elif Keys [pygame.K_UP] and logo.y > 0 :
        logo.y -= logo.vel

    elif Keys [pygame.K_DOWN] and logo.y  < 790 - logo.height :
        logo.y += logo.vel

    RedrawGameWindow()

pygame.quit()