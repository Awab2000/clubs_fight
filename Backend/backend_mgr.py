import pygame
from Backend.Characters import Player
from Backend.Characters import enemy
from Backend.Characters import Trophy
from Backend.files_data import get_files_data
from Backend.Time import Time


class BackEndManager:

    def __init__(self):
        self.player1 = Player()
        self.enemies = [enemy() for i in range(11)]
        self.cup = Trophy()
        self._clock = pygame.time.Clock()
        self.time = Time()
        self.SCREEN_WIDTH = 1233
        self.SCREEN_HEIGHT = 640
        self.high_score_file, self.high_score, self.user_name_file, self.user_name = get_files_data()
        self.FPS = 60

    def delay_time(self, n, period):
        i = 0
        while i < n:
            pygame.time.delay(period)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = n + 1
                    pygame.quit()

    def write_on_high_score_file(self, high_score):
        with open(self.high_score_file, 'w', encoding='UTF-8') as file:
            file.write(str(high_score))

    def write_on_user_name_file(self, user_name):
        with open(self.user_name_file, 'w', encoding='UTF-8') as file:
            file.write(user_name)
        self.user_name = user_name

    @property
    def get_high_score(self):
        return self.high_score

    @property
    def get_high_score_user_name(self):
        return self.user_name

    def restart_all(self):
        self.time.restart_time()
        for ene in self.enemies:
            ene.restart_position()
        self.player1.restart_position()


    def collapse(self):
        for enemy in self.enemies:
            if self.player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > \
                    enemy.hitbox[1]:
                if self.player1.hitbox[0] + self.player1.hitbox[2] > enemy.hitbox[0] and self.player1.hitbox[0] < enemy.hitbox[0] + \
                        enemy.hitbox[2]:
                    return 2

        if self.player1.hitbox[1] < self.cup.hitbox[1] + self.cup.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > self.cup.hitbox[
            1]:
            if self.player1.hitbox[0] + self.player1.hitbox[2] > self.cup.hitbox[0] and self.player1.hitbox[0] < self.cup.hitbox[0] + self.cup.hitbox[
                2]:
                if self.player1.is_high_score(self.time.get_seconds, self.high_score):
                    self.high_score = self.time.get_seconds
                    return 4
                return 3
        return 0

    def game_scenario(self):
        self._clock.tick(self.FPS)
        self.time.start = True
        self.time.move_time()
        ret = self.collapse()
        if ret != 0:
            self.time.restart_time()
            return ret
        for enemy in self.enemies:
            enemy.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player1.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        return 1