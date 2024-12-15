import random
from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
from enum import Enum
import numpy as np


class Direction(Enum):
    # STAND = 0
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Character(ABC):

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def restart_position(self):
        pass

class Player(Character):
    def __init__(self,x = 12, y = 50, width = 31, height = 42):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.score = 0
        self.hitbox = (self.x , self.y, self.width, self.height)

    def get_position(self):
        return self.x, self.y

    def move_p1(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        elif Keys[pygame.K_RIGHT] and self.x < (SCREEN_WIDTH - self.width - 2):
            self.x += self.vel

        elif Keys[pygame.K_UP] and self.y > 2:
            self.y -= self.vel

        elif Keys[pygame.K_DOWN] and self.y < (SCREEN_HEIGHT - self.height - 4):
            self.y += self.vel

        self.hitbox = (self.x, self.y, self.width, self.height)

    def move_p2(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel

        elif Keys[pygame.K_d] and self.x < (SCREEN_WIDTH - self.width - 2):
            self.x += self.vel

        elif Keys[pygame.K_w] and self.y > 2:
            self.y -= self.vel

        elif Keys[pygame.K_s] and self.y < (SCREEN_HEIGHT - self.height - 4):
            self.y += self.vel

        self.hitbox = (self.x, self.y, self.width, self.height)

    def restart_position(self, x = 12, y = 50):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, self.width, self.height)

    def is_high_score(self, high_score):
        return self.score > high_score

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0


class AI_Player(Character):
    def __init__(self,x = 1190, y = 50, width = 31, height = 42):   # 1202, 50
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.score = 0
        self.direction = Direction.DOWN
        self.hitbox = (self.x , self.y, self.width, self.height)

    def get_position(self):
        return self.x, self.y

    def move(self, action, SCREEN_WIDTH, SCREEN_HEIGHT):

        dirs = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        self.direction = dirs[np.argmax(action)]


        self._move(SCREEN_WIDTH, SCREEN_HEIGHT)

    def _move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.direction == Direction.LEFT and self.x > 0:
            self.x -= self.vel
        elif self.direction == Direction.RIGHT and self.x < (SCREEN_WIDTH - self.width - 2):
            self.x += self.vel
        elif self.direction == Direction.DOWN and self.y < (SCREEN_HEIGHT - self.height - 4):
            self.y += self.vel
        elif self.direction == Direction.UP and self.y > 2:
            self.y -= self.vel

        self.hitbox = (self.x, self.y, self.width, self.height)

    def restart_position(self, x = 1190, y = 50):
        self.x = x   # 1202
        self.y = y
        self.direction = Direction.DOWN
        self.hitbox = (self.x, self.y, self.width, self.height)

    def is_high_score(self, high_score):
        return self.score > high_score

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0


class enemy(Character):
    def __init__(self, width = 31, height = 42):
        self.x = random.randint(200,1000)
        self.y = random.randint(200,500)
        self.width = width
        self.height = height
        self.speedx = 10
        self.speedy = 10
        self.hitbox = (self.x, self.y, self.width, self.height)


    def get_position(self):
        return self.x, self.y

    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.speedx
        self.y += self.speedy
        if self.x <= 0 or self.x + self.width >= SCREEN_WIDTH:
            self.speedx = - self.speedx
        if self.y <= 0 or self.y + self.height >= SCREEN_HEIGHT:
            self.speedy = -self.speedy

        self.hitbox = (self.x, self.y, self.width, self.height)

    def restart_position(self):
        self.x = random.randint(200,1000)
        self.y = random.randint(200,500)
        self.hitbox = (self.x, self.y, self.width, self.height)


class Trophy(Character):
    def __init__(self, x = 0, y = 0, width = 31, height = 53):
        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 585)
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.width, self.height)


    def get_position(self):
        return self.x, self.y


    def restart_position(self):
        self.x = random.randint(0,1200)
        self.y = random.randint(0,585)
        self.hitbox = (self.x, self.y, self.width, self.height)