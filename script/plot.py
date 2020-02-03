import pygame
from pygame.locals import *


class Plot(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        # 加载剧情文件
        self.plot_text = open(r"resource\plot\{}.txt".format(path), "r", encoding="utf-8").read()
        self.plot_text = self.plot_text.split("\n")
        # 字序
        self.index = 0
        self.txt = self.plot_text[self.index]
        self.font = pygame.font.Font(r"resource\XBS.ttf", 30)
        # 图片层
        self.image = pygame.Surface([310, 200])
        self.image.fill([255, 255, 255])
        self.rect = Rect((770, 100), (300, 200))
        self.write()

    # 更新文字
    def next(self):
        if self.index < len(self.plot_text) - 1:
            self.index += 1
            self.txt = self.plot_text[self.index]
            self.write()
        else:
            return True

    # 在屏幕上输出多行文字
    def write(self):
        # 清空屏幕
        self.image.fill([255, 255, 255])
        # 每行十个字
        n = 0
        while n * 10 < len(self.txt) - 1:
            txt = self.txt[n * 10:(n + 1) * 10]
            text = self.font.render(txt, True, [10, 10, 10], [255, 255, 255])
            self.image.blit(text, (5, 10 + n * 32))
            n += 1
        else:
            txt = self.txt[n * 10:-1]
            text = self.font.render(txt, True, [10, 10, 10], [255, 255, 255])
            self.image.blit(text, (5, 10 + n * 32))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
