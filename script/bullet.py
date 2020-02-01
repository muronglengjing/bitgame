import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, color):
        # 继承父类
        super().__init__()

        # direction
        self.direction = direction
        if direction % 2 == 0:
            self.image = pygame.Surface([5, 10])
        else:
            self.image = pygame.Surface([10, 5])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        self.used = False

    def update(self):
        if self.direction == 0:
            self.rect.y -= self.speed
        elif self.direction == 1:
            self.rect.x += self.speed
        elif self.direction == 2:
            self.rect.y += self.speed
        elif self.direction == 3:
            self.rect.x -= self.speed


class Bullet_Group(pygame.sprite.Group):
    def update(self, *args):
        super().update()

        for i in self.sprites():
            if i.rect.x < -10 or i.rect.y < -10 or i.rect.x > 1080:
                i.kill()


