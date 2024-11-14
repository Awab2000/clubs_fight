import pygame , sys
from  pygame.locals import *
pygame.init()
Display=pygame.display.set_mode((1533,790))
pygame.display.set_caption("CLUBS FIGHT")
Liv=pygame.image.load("Liv.JPG")
ManU = pygame.image.load("ManU.PNG")
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
FPS = 27
clock = pygame.time.Clock()
music = pygame.mixer.music.load("YNWA.mp3")
pygame.mixer.music.play(-1)

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.moving = False
        self.movecount = 0
        self.hitbox = (self.x , self.y, 40, 54)

    def draw(self,Display):
        Display.blit(Liv , (self.x,self.y))
        if self.moving == True and (((self.x != 0) and (self.x + self.width < 1533))and((self.y != 0) and (self.y + self.height < 790))) :
            if self.right == True:
                pygame.draw.line(Display,White,(0,self.y+23),(self.x + self.vel,self.y+23),1)
            elif self.left == True:
                pygame.draw.line(Display, White, (1533, self.y+23), ((self.x + self.width)  - self.vel, self.y+23), 1)
            elif self.up == True:
                pygame.draw.line(Display, White, (self.x, 790), (self.x, self.y - self.vel), 1)
            elif self.down == True:
                pygame.draw.line(Display, White, (self.x, 0), (self.x, self.y + self.vel), 1)
            # pygame.draw.line(Display,White,(self.x,self.y),(self.x + self.movecount - 40 , self.y + self.movecount - 54),1)
        self.hitbox = (self.x , self.y, 40, 54)
        #pygame.draw.rect(Display,Blue,self.hitbox,2)

    def hit(self):
        self.x = 0
        self.y = 0
        self.movecount = 0
        font1 = pygame.font.SysFont("comicsans",100)
        text = font1.render("YOU LOSE , GLORY MAN UNITED",1,Red)
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

class enemy:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.speedx = 10
        self.speedy = 8
        self.hitbox = (self.x, self.y, 40, 54)

    def draw(self,Display):
        self.move()
        Display.blit(ManU, (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 54)
        #pygame.draw.rect(Display, Blue, self.hitbox, 2)

    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x <= 0 or self.x + self.width >= 1533:
            self.speedx = - self.speedx
        if self.y <= 0 or self.y + self.height >= 790:
            self.speedy = -self.speedy

def RedrawGameWindow():
    Display.fill(Black)
    logo.draw(Display)
    logo2.draw(Display)
    pygame.display.update()

#MainLoop
font = pygame.font.SysFont("comicsans",25,True,True)
logo = player(0,0,40,54)
logo2 = enemy(700,400,40,54)
Run = True
while Run:
    clock.tick(FPS)
    if logo.hitbox[1] < logo2.hitbox[1] + logo2.hitbox[3] and logo.hitbox[1] + logo.hitbox[3] > logo2.hitbox[1]:
        if logo.hitbox[0] + logo.hitbox[2] > logo2.hitbox[0] and logo.hitbox[0] < logo2.hitbox[0] + logo2.hitbox[2]:
            logo.hit()

    for event in pygame.event.get():
        if event.type == QUIT:
            Run = False

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_LEFT] and logo.x > 0 :
        logo.x -= logo.vel
        logo.left = True
        logo.right = False
        logo.moving = True
        logo.movecount += 2
    elif Keys [pygame.K_RIGHT] and logo.x < 1533 - logo.width:
        logo.x += logo.vel
        logo.right = True
        logo.left = False
        logo.moving = True
        logo.movecount += 2

    elif Keys [pygame.K_UP] and logo.y > 0 :
        logo.y -= logo.vel
        logo.right = False
        logo.left = False
        logo.up = True
        logo.down = False
        logo.moving = True
        logo.movecount += 2

    elif Keys [pygame.K_DOWN] and logo.y  < 790 - logo.height :
        logo.y += logo.vel
        logo.moving = True
        logo.down = True
        logo.movecount += 2

    RedrawGameWindow()

pygame.quit()
