import random
from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
#ToDO:
# Make Inteface


class Character(ABC):

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def restart_position(self):
        pass

class Player(Character):
    def __init__(self,x = 0, y = 0, width = 31, height = 42):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.hitbox = (self.x , self.y, self.width, self.height)


    def get_position(self):
        return self.x, self.y


    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        elif Keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.vel

        elif Keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        elif Keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.vel

        self.hitbox = (self.x, self.y, self.width, self.height)


    def restart_position(self):
        self.x = 0
        self.y = 0
        self.hitbox = (self.x, self.y, self.width, self.height)


    def is_high_score(self, seconds, high_score):
        return seconds < high_score


class enemy(Character):
    def __init__(self, width = 31, height = 42):
        self.x = random.randint(200,1000)
        self.y = random.randint(200,500)
        self.width = width
        self.height = height
        self.speedx = 9
        self.speedy = 9
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
    def __init__(self, x = 1202, y = 587, width = 31, height = 53):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, self.width, self.height)


    def get_position(self):
        return self.x, self.y


    def restart_position(self):
        self.x = random.randint(200,1000)
        self.y = random.randint(200,500)
        self.hitbox = (self.x, self.y, self.width, self.height)