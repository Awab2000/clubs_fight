import pygame
from pygame.locals import *
from Backend.Characters import Player






class BackEndManager:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.player1 = Player()
        enemies = [enemy() for i in range(11)]
        cup = Trophy(1493, 722, 40, 68)
        time = Time(1450, 0)

    def delay_time(self, n, period):
        i = 0
        while i < n:
            pygame.time.delay(period)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = n + 1
                    pygame.quit()

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

        if player1.hitbox[1] < cup.hitbox[1] + cup.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > cup.hitbox[
            1] and not is_hit:
            if player1.hitbox[0] + player1.hitbox[2] > cup.hitbox[0] and player1.hitbox[0] < cup.hitbox[0] + cup.hitbox[
                2]:
                player1.check_high()
                is_hit = True
                for ene in enemies:
                    ene.restart_position()
        return is_hit