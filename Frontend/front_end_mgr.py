import pygame
from pygame.locals import *

from data_helper import load_data, get_logos, get_small_stadiums, get_stadiums
from Backend.backend_mgr import BackEndManager

class FrontEndManager:

    def __init__(self):
        self.backend_mgr = BackEndManager()
        self.Display = None
        self.SCREEN_WIDTH = 1233
        self.SCREEN_HEIGHT = 640
        self.caption = "CLUBS FIGHT"
        self.time_x_pos = 600
        self.time_y_pos = 0
        self.p1_score_x_pos = 0
        self.p1_score_y_pos = 0
        self.p2_score_x_pos = 1000
        self.p2_score_y_pos = 0
        self.teams, self.background_img, self.cup_img = load_data()
        self.small_stadiums = get_small_stadiums()
        self.stadiums = get_stadiums()
        self.logos = get_logos()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.SILVER = (192, 192, 192)
        self.BUTTONS_WIDTH = 180
        self.BUTTONS_HEIGHT = 50
        self.user_text = ''

    @staticmethod
    def play_background_sound():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Frontend/sounds/Crowd Sound.mp3")
        pygame.mixer.music.play(-1)

    @staticmethod
    def check_quit():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

    def display_background_image(self):
        self.Display.blit(self.background_img, (0, 0))

    def display_image(self, img, pos):
        self.Display.blit(img, pos)

    def write_on_screen(self, font_type, font_size, font_color, message, pos_x, pos_y, take_width=False):
        font = pygame.font.SysFont(font_type, font_size)
        text = font.render(message, 1, font_color)
        if take_width:
            self.Display.blit(text, (616 - (text.get_width() / 2), pos_y))
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
            self.write_on_screen("comicsans", 70, self.WHITE, "CLUBS FIGHT", 616, 150, True)
            pygame.draw.rect(self.Display, self.WHITE, (305, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)) # 350 490
            self.write_on_screen("comicsans", 40, self.BLACK, "Play", 360, 395)     # 430, 475
            pygame.draw.rect(self.Display, self.WHITE, (710, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))    # 850, 490
            self.write_on_screen("comicsans", 33, self.BLACK, "High Score", 713, 398)       # 860, 485
            self.write_on_screen("comicsans", 22, self.WHITE,
                            "How To Play: Use the arrows to avoid the rival and reach the Champions league cup",
                            172, 574)   #150, 700
            self.check_quit()
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 305 + self.BUTTONS_WIDTH > cur[0] > 305 and self.BUTTONS_HEIGHT + 402 > cur[1] > 402:
                pygame.draw.rect(self.Display, self.SILVER, (305, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 40, self.BLACK, "Play", 360, 395)
                if click[0] == 1:
                    self.backend_mgr.delay_time(50, 5)
                    break
            if 710 + self.BUTTONS_WIDTH > cur[0] > 710 and self.BUTTONS_HEIGHT + 402 > cur[1] > 402:
                pygame.draw.rect(self.Display, self.SILVER, (710, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 33, self.BLACK, "High Score", 713, 398)
                if click[0] == 1:
                    self.view_high()
            pygame.display.update()


    def ai_or_p2(self):
        while True:
            self.display_background_image()
            self.write_on_screen("comicsans", 70, self.WHITE, "Choose Opponent", 616, 150, True)
            pygame.draw.rect(self.Display, self.WHITE, (305, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)) # 350 490
            self.write_on_screen("comicsans", 40, self.BLACK, "vs P2", 345, 395)     # 430, 475
            pygame.draw.rect(self.Display, self.WHITE, (710, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))    # 850, 490
            self.write_on_screen("comicsans", 40, self.BLACK, "vs AI", 745, 395)       # 860, 485
            self.write_on_screen("comicsans", 22, self.WHITE,
                            "**: If you choose P2, use w,a,s,d for movement",
                            380, 574)   #150, 700
            self.check_quit()
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 305 + self.BUTTONS_WIDTH > cur[0] > 305 and self.BUTTONS_HEIGHT + 402 > cur[1] > 402:
                pygame.draw.rect(self.Display, self.SILVER, (305, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 40, self.BLACK, "vs P2", 345, 395)
                if click[0] == 1:
                    self.backend_mgr.delay_time(50, 5)
                    self.backend_mgr.is_ai = False
                    break
            if 710 + self.BUTTONS_WIDTH > cur[0] > 710 and self.BUTTONS_HEIGHT + 402 > cur[1] > 402:
                pygame.draw.rect(self.Display, self.SILVER, (710, 402, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 40, self.BLACK, "vs AI", 745, 395)
                if click[0] == 1:
                    self.backend_mgr.delay_time(50, 5)
                    self.backend_mgr.is_ai = True
                    break
            pygame.display.update()

    def choose_player(self, player1 = False, player2 = False):
        choose = True
        while choose:
            self.display_background_image()
            positions = [(150, 220), (250, 220), (350, 220), (450, 220), (550, 220), (650, 220), (750, 220),
                             (850, 220), (950, 220), (1050, 220), (150, 384), (250, 384), (350, 384),
                             (450, 384), (550, 384), (650, 384), (750, 384), (850, 384), (950, 384),  (1050, 384),
                         (350, 548), (450, 548), (550, 548), (650, 548), (750, 548), (850, 548)
                         ]      # 300 to 246, 500 to 410


            for idx, team in enumerate(self.teams):
                team.display = self.Display
                team.pos_x, team.pos_y = positions[idx]
                team.draw_logo()
                if player1:
                    team.is_player1 = False
                elif player2:
                    team.is_player2 = False

            if player1:
                self.write_on_screen("comicsans", 50, self.WHITE, "Choose Player1 team", 170, 90, True)  # 230, 110
            elif player2:
                if self.backend_mgr.is_ai:
                    self.write_on_screen("comicsans", 50, self.WHITE, "Choose AI team", 170, 90, True)
                else:
                    self.write_on_screen("comicsans", 50, self.WHITE, "Choose Player2 team", 170, 90, True)
            self.check_quit()


            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            for team in self.teams:
                if team.pos_x + team.width > cur[0] > team.pos_x and team.height + team.pos_y > cur[1] > team.pos_y:
                    pygame.draw.rect(self.Display, self.GREEN, (team.pos_x - 3, team.pos_y - 3, team.width + 3, team.height + 3), 2)
                    if click[0] == 1:
                        if player1:
                            team.is_player1 = True
                        elif player2:
                            team.is_player2 = True
                        choose = False
                        break
            pygame.display.update()

    def choose_enemy(self):
        choose = True
        while choose:
            self.display_background_image()
            positions = [(150, 220), (250, 220), (350, 220), (450, 220), (550, 220), (650, 220), (750, 220),
                         (850, 220), (950, 220), (1050, 220), (150, 384), (250, 384), (350, 384),
                         (450, 384), (550, 384), (650, 384), (750, 384), (850, 384), (950, 384), (1050, 384),
                         (350, 548), (450, 548), (550, 548), (650, 548), (750, 548), (850, 548)
                         ] # 300 to 246, 500 to 410

            for idx, team in enumerate(self.teams):
                team.pos_x, team.pos_y = positions[idx]
                team.draw_logo()

            self.write_on_screen("comicsans", 50, self.WHITE, "Choose Enemy team", 170, 90, True)  # 230, 110

            self.check_quit()

            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            rival_image = None
            for idx, team in enumerate(self.teams):
                if team.pos_x + team.width > cur[0] > team.pos_x and team.height + team.pos_y > cur[1] > team.pos_y:
                    pygame.draw.rect(self.Display, self.GREEN,
                                     (team.pos_x - 3, team.pos_y - 3, team.width + 3, team.height + 3), 2)
                    if click[0] == 1:
                        rival_image = pygame.image.load(self.logos[idx])
                        choose = False
                        break

            for team in self.teams:
                if team.is_player1:
                    team.rival_image = rival_image
            pygame.display.update()


    def choose_stadium(self):
        choose = True
        while choose:
            self.display_background_image()
            positions = [(16, 105), (216, 105), (416, 105), (616, 105), (816, 105), (1016, 105),
                         (16, 205), (216, 205), (416, 205), (616, 205), (816, 205), (1016, 205),
                         (16, 305), (216, 305), (416, 305), (616, 305), (816, 305), (1016, 305),
                         (16, 405), (216, 405), (416, 405), (616, 405), (816, 405), (1016, 405),
                         (416, 505), (616, 505)]

            width = 200
            height = 100

            for idx, position in enumerate(positions):
                img = pygame.image.load(self.small_stadiums[idx])
                self.Display.blit(img, pygame.Rect(position[0], position[1], width, height))

            self.write_on_screen("comicsans", 50, self.WHITE, "Choose a Stadium", 170, 10, True)

            self.check_quit()

            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            stad_image = None

            for idx, position in enumerate(positions):
                if position[0] + width > cur[0] > position[0] and height + position[1] > cur[1] > position[1]:
                    pygame.draw.rect(self.Display, self.GREEN,
                                     (position[0] - 3, position[1] - 3, width + 3, height + 3), 2)
                    if click[0] == 1:
                        stad_image = pygame.image.load(self.stadiums[idx])
                        choose = False
                        break

            for team in self.teams:
                if team.is_player1:
                    team.stad_image = stad_image
                    if stad_image is not None:
                        self.backend_mgr.delay_time(30, 5)
                        team.play_chant()
            pygame.display.update()


    def loading(self, msg = "Loading"):
        self.display_background_image()


        # self.write_on_screen("comicsans", 50, self.WHITE, msg + ".", 320, 320, True)
        #
        # pygame.display.update()
        # self.write_on_screen("comicsans", 50, self.WHITE, msg + "..", 320, 320, True)
        # self.backend_mgr.delay_time(300, 5)
        # pygame.display.update()

        self.write_on_screen("comicsans", 50, self.WHITE, msg + "...", 320, 320, True)

        self.check_quit()

        pygame.display.update()
        self.backend_mgr.delay_time(300, 5)



    def view_high(self):
        while True:
            self.display_background_image()
            self.write_on_screen("comicsans", 50, self.WHITE, "HIGH SCORE", 420, 143, True)   #525, 175
            self.write_on_screen("comicsans", 50, self.WHITE, self.backend_mgr.get_high_score_user_name + ': ' + str(self.backend_mgr.get_high_score), 330, 280, True)     # 410, 340
            pygame.draw.rect(self.Display, self.WHITE, (515, 450, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))     # 620, 550
            self.write_on_screen("comicsans", 40, self.BLACK, "Back", 560, 445)     #680, 540
            self.check_quit()
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 515 + self.BUTTONS_WIDTH > cur[0] > 515 and self.BUTTONS_HEIGHT + 450 > cur[1] > 450:
                pygame.draw.rect(self.Display, self.SILVER, (515, 450, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))
                self.write_on_screen("comicsans", 40, self.BLACK, "Back", 560, 445)
                if click[0] == 1:
                    break
            pygame.display.update()


    def entry(self):
        while True:
            self.play_background_sound()
            self.display_background_image()
            self.write_on_screen("comicsans", 45, self.WHITE, "Type your name:", 390, 145, True)    # 490, 175
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

            self.write_on_screen("comicsans", 45, self.WHITE, self.user_text, 390, 280, True)
            pygame.draw.rect(self.Display, self.WHITE, (515, 450, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))  # 620, 550
            self.write_on_screen("comicsans", 40, self.BLACK, "Save", 560, 445)  # 680, 540

            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 515 + self.BUTTONS_WIDTH > cur[0] > 515 and self.BUTTONS_HEIGHT + 450 > cur[1] > 450:
                pygame.draw.rect(self.Display, self.SILVER,
                                 (515, 450, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT))  # 620, 550
                self.write_on_screen("comicsans", 40, self.BLACK, "Save", 560, 445)
                if click[0] == 1:
                    self.backend_mgr.write_on_user_name_file(self.user_text)
                    self.backend_mgr.write_on_high_score_file(self.backend_mgr.get_high_score)
                    break
            pygame.display.update()


    def game_over(self):
        self.write_on_screen("comicsans", 70, self.RED, "GAME OVER", 390, 280, True)
        pygame.display.update()
        self.backend_mgr.delay_time(200, 10)


    def won(self):
        p1_score, p2_score = self.backend_mgr.get_score_now
        if p1_score > p2_score:
            msg = "P1 WON!!"
        elif p2_score > p1_score:
            if self.backend_mgr.is_ai:
                msg = "AI WON!!"
            else:
                msg = "P2 WON!!"
        else:
            msg = "DRAW!!"
        self.write_on_screen("comicsans", 60, self.GREEN, msg, 390, 450, True)
        pygame.display.update()
        self.backend_mgr.delay_time(200, 10)


    def print_high_score(self):
        self.write_on_screen("comicsans", 55, self.YELLOW, "New High Score!!!", 390, 80, True)
        pygame.display.update()
        self.backend_mgr.delay_time(200, 10)

    def RedrawGameWindow(self):
        self.Display.fill(self.BLACK)
        for team in self.teams:
            if team.is_player1:
                team.draw_stad()
                break

        for team in self.teams:
            if team.is_player1:
                team.pos_x, team.pos_y = self.backend_mgr.player1.get_position()
                team.draw_logo()
                break

        for team in self.teams:
            if team.is_player2:
                if self.backend_mgr.is_ai:
                    team.pos_x, team.pos_y = self.backend_mgr.ai_player.get_position()
                else:
                    team.pos_x, team.pos_y = self.backend_mgr.player2.get_position()
                team.draw_logo()
                break

        for team in self.teams:
            if team.is_player1:
                for enemy in self.backend_mgr.enemies:
                    team.rival_pos_x, team.rival_pos_y= enemy.get_position()
                    team.draw_rival()
                break

        self.write_on_screen("comicsans", 45, self.WHITE, f'{self.backend_mgr.time.get_seconds}', self.time_x_pos, self.time_y_pos)
        self.write_on_screen("comicsans", 30, self.WHITE, f'P1 Score: {self.backend_mgr.get_score_now[0]}', self.p1_score_x_pos,
                             self.p1_score_y_pos)
        if self.backend_mgr.is_ai:
            self.write_on_screen("comicsans", 30, self.WHITE, f'AI Score: {self.backend_mgr.get_score_now[1]}',
                                 self.p2_score_x_pos,
                                 self.p2_score_y_pos)
        else:
            self.write_on_screen("comicsans", 30, self.WHITE, f'P2 Score: {self.backend_mgr.get_score_now[1]}',
                                 self.p2_score_x_pos,
                                 self.p2_score_y_pos)
        self.display_image(self.cup_img,self.backend_mgr.cup.get_position())    # Should i make cup class like team? i don't know

        pygame.display.update()


    def run(self):
        self.init_screen()
        while True:
            self.user_text = ''
            self.play_background_sound()
            self.game_intro()
            self.loading()
            self.ai_or_p2()
            self.loading()
            self.choose_player(player1=True)
            self.loading()
            self.choose_player(player2=True)
            self.loading()
            self.choose_enemy()
            self.loading()
            self.choose_stadium()
            self.loading('Starting')
            self.backend_mgr.restart_all()
            while True:
                self.RedrawGameWindow()
                action = self.backend_mgr.game_scenario()
                if action != 1:
                    self.game_over()
                    self.won()
                    if action == 3:
                        self.print_high_score()
                        self.entry()
                    break
                self.check_quit()
