import pygame
from script.hero import *
from pygame.locals import *


class Enemy(Hero):
    def __init__(self, name, hp, attract, defense, local, path):
        super().__init__(name, hp, attract, defense, local)
        self.image = pygame.transform.scale2x(pygame.image.load("resource\{}.png".format(path)))

    def hp_line(self):
        super().hp_line()
        self.player_information()
        hp_percentage = self.hp / self.hp_max
        self.hp_band = pygame.Surface([500, 10])
        if self.hp >= 0:
            hp_band = pygame.Surface([500 * hp_percentage, 10])
            hp_band.fill([220, 100, 100])
            self.hp_band.blit(hp_band, (0, 0))
        self.hp_rect = Rect((570, 10), (500, 10))

    def attract(self, attract):
        self.hp = self.hp - (attract - self.defense)
        pygame.mixer.music.load(r"resource\cat_bit.wav")
        pygame.mixer.music.play()
        self.update()

    def player_information(self):
        txt = pygame.font.Font(r"resource\XBS.ttf", 22)
        text = txt.render(
            "{} 攻击力:{} 防御力:{} 血量 {}|{}".format(self.name, self.attraction, self.defense, self.hp, self.hp_max),
            True, [200, 200, 200], [100, 100, 100])
        self.txt_band = pygame.Surface([600, 50])
        self.txt_band.fill([100, 100, 100])
        self.txt_band.blit(text, [100, 22])
        self.txt_rect = Rect((480, 0), (600, 50))

    def move(self, x, y):
        self.head_direction(x, y)
        if self.rect.centerx == x and self.rect.centery == y:
            pass
        else:
            if self.rect.centerx == x:
                dx = 0
            else:
                dx = (self.rect.centerx - x) / abs(self.rect.centerx - x)
            if self.rect.centery == y:
                dy = 0
            else:
                dy = (self.rect.centery - y) / abs(self.rect.centery - y)
            self.rect.centerx += -dx
            self.rect.centery += -dy

    def update(self):
        self.hp_line()
        if self.hp <= 0:
            self.kill()
        hp_percent = self.hp/self.hp_max
        self.attraction = int(-3*self.attract_init*(hp_percent**2) + 4*self.attract_init)


class Enemy_group(Hero_group):
    def update(self, *args):
        super().update()

