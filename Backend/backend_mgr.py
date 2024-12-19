import pygame
import torch
from Backend.Characters import Player, Direction, AI_Player
from Backend.Characters import enemy
from Backend.Characters import Trophy
from Backend.model import Linear_QNet
from Backend.files_data import get_files_data
from Backend.Time import Time
import numpy as np


class BackEndManager:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player(1190, 50)
        self.ai_player = AI_Player()
        self.is_ai = False
        self.model = Linear_QNet(12, 256, 4)
        self.model.load_state_dict(torch.load("Backend/best_model/best_model.pth"))
        self.model.eval()
        self.enemies = [enemy() for i in range(5)]
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

    @property
    def get_score_now(self):
        if self.is_ai:
            return self.player1.score, self.ai_player.score
        else:
            return self.player1.score, self.player2.score

    def restart_all(self):
        self.time.restart_time()
        for ene in self.enemies:
            ene.restart_position()
        self.player1.restart_position()
        self.cup.restart_position()
        self.player1.reset_score()
        self.player2.restart_position(1190, 50)
        self.player2.reset_score()
        self.ai_player.restart_position(1190, 50)
        self.ai_player.reset_score()


    def get_player_direction(self):
        return self.ai_player.direction


    def get_adj_hitboxes(self, num):
        hb1 = (self.player1.x - num, self.player1.y, 31, 42)
        hb2 = (self.player1.x + num, self.player1.y, 31, 42)
        hb3 = (self.player1.x, self.player1.y - num, 31, 42)
        hb4 = (self.player1.x, self.player1.y + num, 31, 42)
        return hb1, hb2, hb3, hb4


    def get_state(self):
        point_l, point_r, point_u, point_d = self.get_adj_hitboxes(40)

        dir_l = self.get_player_direction == Direction.LEFT
        dir_r = self.get_player_direction == Direction.RIGHT
        dir_u = self.get_player_direction == Direction.UP
        dir_d = self.get_player_direction == Direction.DOWN

        state = [
            # Danger right
            self.collapse_AI(point_r),

            # Danger up
            self.collapse_AI(point_u),

            # Danger down
            self.collapse_AI(point_d),

            # Danger left
            self.collapse_AI(point_l),

            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # Cup location
            self.cup.x < self.ai_player.x,  # cup left
            self.cup.x > self.ai_player.x,  # cup right
            self.cup.y < self.ai_player.y,  # cup up
            self.cup.y > self.ai_player.y,  # cup down
            ]
        return np.array(state, dtype=int)


    def get_action(self, state):
        final_move = [0, 0, 0, 0]
        state0 = torch.tensor(state, dtype=torch.float)
        prediction = self.model(state0)
        move = torch.argmax(prediction).item()
        final_move[move] = 1

        return final_move


    def collapse_AI(self, hitbox):
        for enemy in self.enemies:
            if hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and hitbox[1] + hitbox[3] > \
                    enemy.hitbox[1]:
                if hitbox[0] + hitbox[2] > enemy.hitbox[0] and hitbox[0] < enemy.hitbox[0] + \
                        enemy.hitbox[2]:
                    return 1

        if hitbox[0] + hitbox[2] >= self.SCREEN_WIDTH or hitbox[0] <= 0:
            return 1

        elif hitbox[1] + hitbox[3] >= self.SCREEN_HEIGHT or hitbox[1] <= 0:
            return 1

        return 0


    def collapse(self):
        for enemy in self.enemies:
            if self.player1.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > \
                    enemy.hitbox[1]:
                if self.player1.hitbox[0] + self.player1.hitbox[2] > enemy.hitbox[0] and self.player1.hitbox[0] < enemy.hitbox[0] + \
                        enemy.hitbox[2]:
                    self.player1.restart_position()
            if self.is_ai:
                if self.ai_player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.ai_player.hitbox[1] + self.ai_player.hitbox[3] > \
                        enemy.hitbox[1]:
                    if self.ai_player.hitbox[0] + self.ai_player.hitbox[2] > enemy.hitbox[0] and self.ai_player.hitbox[0] < enemy.hitbox[0] + \
                            enemy.hitbox[2]:
                        self.ai_player.restart_position(1190,50)
            else:
                if self.player2.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.player2.hitbox[1] + self.player2.hitbox[3] > \
                        enemy.hitbox[1]:
                    if self.player2.hitbox[0] + self.player2.hitbox[2] > enemy.hitbox[0] and self.player2.hitbox[0] < enemy.hitbox[0] + \
                            enemy.hitbox[2]:
                        self.player2.restart_position(1190,50)


        if self.player1.hitbox[1] < self.cup.hitbox[1] + self.cup.hitbox[3] and self.player1.hitbox[1] + self.player1.hitbox[3] > self.cup.hitbox[
            1]:
            if self.player1.hitbox[0] + self.player1.hitbox[2] > self.cup.hitbox[0] and self.player1.hitbox[0] < self.cup.hitbox[0] + self.cup.hitbox[
                2]:
                self.cup.restart_position()
                self.player1.increase_score()

        if self.is_ai:
            if self.ai_player.hitbox[1] < self.cup.hitbox[1] + self.cup.hitbox[3] and self.ai_player.hitbox[1] + \
                    self.ai_player.hitbox[3] > self.cup.hitbox[
                1]:
                if self.ai_player.hitbox[0] + self.ai_player.hitbox[2] > self.cup.hitbox[0] and self.ai_player.hitbox[0] < \
                        self.cup.hitbox[0] + self.cup.hitbox[
                    2]:
                    self.cup.restart_position()
                    self.ai_player.increase_score()

        else:
            if self.player2.hitbox[1] < self.cup.hitbox[1] + self.cup.hitbox[3] and self.player2.hitbox[1] + self.player2.hitbox[3] > self.cup.hitbox[
                1]:
                if self.player2.hitbox[0] + self.player2.hitbox[2] > self.cup.hitbox[0] and self.player2.hitbox[0] < self.cup.hitbox[0] + self.cup.hitbox[
                    2]:
                    self.cup.restart_position()
                    self.player2.increase_score()

        if self.time.get_seconds == -1:
            if self.is_ai:
                if self.player1.is_high_score(self.high_score) or self.ai_player.is_high_score(self.high_score):
                    self.high_score = self.player1.score if self.player1.score > self.ai_player.score else self.ai_player.score
                    return 3
            else:
                if self.player1.is_high_score(self.high_score) or self.player2.is_high_score(self.high_score):
                    self.high_score = self.player1.score if self.player1.score > self.player2.score else self.player2.score
                    return 3
            return 2

        return 1

    def game_scenario(self):
        self._clock.tick(self.FPS)
        self.time.start = True
        self.time.move_time()
        for enemy in self.enemies:
            enemy.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        if self.is_ai:
            state = self.get_state()
            action = self.get_action(state)
            self.ai_player.move(action, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        else:
            self.player2.move_p2(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player1.move_p1(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        ret = self.collapse()
        if ret != 1:
            self.time.restart_time()
            return ret

        return ret
