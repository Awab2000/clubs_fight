import pygame
from pygame.locals import *

from ..utilities import load_data
from ..Backend.backend_mgr import BackEndManager


class FrontEndManager:

    def __init__(self):
        self.bacend_mgr = BackEndManager()
        self.Display = None
        self.SCREEN_WIDTH = 1533
        self.SCREEN_HEIGHT = 790
        self.caption = "CLUBS FIGHT"
        self.teams, self.background, self.cup = load_data()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.SILVER = (192, 192, 192)
        self.BUTTONS_WIDTH = 250
        self.BUTTONS_HEIGHT = 60
        self.FPS = 2000

    @staticmethod
    def play_background_sound():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("UEFA.mp3")
        pygame.mixer.music.play(-1)

    @staticmethod
    def check_quit():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def display_background_image(self):
        self.Display.blit(self.background, (0, 0))

    def write_on_screen(self, font_type, font_size, font_color, message, pos_x, pos_y, take_width=False):
        font = pygame.font.SysFont(font_type, font_size)
        text = font.render(message, 1, font_color)
        if take_width:
            self.Display.blit(text, (766 - (text.get_width() / 2), pos_y))
        else:
            self.Display.blit(text, (pos_x, pos_y))


    def init_screen(self):
        pygame.init()
        pygame.key.set_repeat()
        self.Display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("CLUBS FIGHT")

    def game_intro(self):
        while True:
            self.display_background_image()
            self.write_on_screen("comicsans", 100, self.WHITE, "CLUBS FIGHT", 766 - (750 // 2), 150)
            pygame.draw.rect(self.Display, self.WHITE, (350, 490, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
            self.write_on_screen("comicsans", 55, self.BLACK, "Play", 430, 475)
            pygame.draw.rect(self.Display, self.WHITE, (850, 490, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
            self.write_on_screen("comicsans", 45, self.BLACK, "High Score", 860, 485)
            self.write_on_screen("comicsans", 30, self.WHITE,
                            "Playing instruction: Use the arrows to avoid the rival and reach the Champions league cup",
                            150, 700)
            self.check_quit()
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 350 + self.BUTTONS_WIDTH > cur[0] > 350 and self.BUTTONS_HEIGHT + 490 > cur[1] > 490:
                pygame.draw.rect(self.Display, self.SILVER, (350, 490, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 55, self.BLACK, "Play", 430, 475)
                if click[0] == 1:
                    delay_time(50, 5)
                    break
            if 850 + self.BUTTONS_WIDTH > cur[0] > 850 and self.BUTTONS_HEIGHT + 490 > cur[1] > 490:
                pygame.draw.rect(self.Display, self.SILVER, (850, 490, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 45, self.BLACK, "High Score", 860, 485)
                if click[0] == 1:
                    self.view_high()
            pygame.display.update()

    def choose(self):
        choose = True
        while choose:
            self.display_background_image()
            positions = [(300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (800, 300), (900, 300),
                         (1000, 300), (300, 500), (400, 500), (500, 500),
                         (600, 500), (700, 500), (800, 500), (900, 500), (1000, 500), (1100, 500), (1100, 300),
                         (1200, 300), (1200, 500)]

            for idx, team in enumerate(self.teams):
                team.pos_x, team.pos_y = positions[idx]
                team.draw_logo()
                team.is_turn = False

            self.write_on_screen("comicsans", 70, self.WHITE, "Choose a team to start the game", 230, 110)
            self.check_quit()

            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            for team in self.teams:
                if team.pos_x + team.width > cur[0] > team.pos_x and team.height + team.pos_y > cur[1] > team.pos_y:
                    if click[0] == 1:
                        team.is_turn = True
                        team.play_chant()
                        choose = False
                        delay_time(50, 5)
                        break
            pygame.display.update()

    def view_high(self):
        while True:
            self.display_background_image()
            self.write_on_screen("comicsans", 70, self.WHITE, "HIGH SCORE", 525, 175)
            self.write_on_screen("comicsans", 70, self.WHITE, user_text + ': ' + str(HIGH_SCORE) + " seconds", 410, 340, True)
            pygame.draw.rect(self.Display, self.WHITE, (620, 550, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
            self.write_on_screen("comicsans", 55, self.BLACK, "Back", 680, 540)
            self.check_quit()
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 620 + self.BUTTONS_WIDTH > cur[0] > 620 and self.BUTTONS_HEIGHT + 550 > cur[1] > 550:
                pygame.draw.rect(self.Display, self.SILVER, (620, 550, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 55, self.BLACK, "Back", 680, 540)
                if click[0] == 1:
                    break
            pygame.display.update()


    def entry(self):
        global user_text
        while True:
            self.display_background_image()
            self.write_on_screen("comicsans", 60, self.WHITE, "Type your name:", 490, 175, True)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

            self.write_on_screen("comicsans", 60, self.WHITE, user_text, 490, 340, True)
            pygame.draw.rect(self.Display, self.WHITE, (620, 550, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
            self.write_on_screen("comicsans", 60, self.BLACK, "Save", 685, 530)

            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 620 + self.BUTTONS_WIDTH > cur[0] > 620 and self.BUTTONS_HEIGHT + 550 > cur[1] > 550:
                pygame.draw.rect(self.Display, self.SILVER, (620, 550, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 60, self.BLACK, "Save", 685, 530)
                if click[0] == 1:
                    with open(player_name_file, 'w', encoding='UTF-8') as file:
                        file.write(user_text)
                    with open(High_score_file, 'w', encoding='UTF-8') as file:
                        file.write(str(HIGH_SCORE))
                    break
            pygame.display.update()


    def RedrawGameWindow(self):
        self.Display.fill(self.BLACK)
        for team in self.teams:
            if team.is_turn:
                team.draw_stad()
                break
        time.draw(self.Display)
        player1.draw()
        for enemy in enemies:
            enemy.draw()
        self.cup.draw(self.Display)
        pygame.display.update()


    def run(self):


        while True:
            self.play_background_sound()
            self.game_intro()
            self.choose()

            while True:
                self.RedrawGameWindow()
                time.start = True
                clock.tick(self.FPS)
                if (collapse()):
                    time.restart_time()
                    time.start = False
                    break
                self.check_quit()
                player1.move()