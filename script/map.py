import pygame
from pygame.locals import *


class MapDraw(pygame.sprite.Sprite):
    def __init__(self, maps):
        super().__init__()
        self.dict = {1: "glass", 2: "null"}
        self.image = pygame.Surface([1080, 720])
        self.image.set_colorkey([0, 0, 0])
        self.rect = pygame.Rect((0, 0), (0, 0))
        c, r = 0, 0
        for i in maps:
            for j in i:
                if j == 0:
                    pass
                else:
                    image = pygame.image.load(r"resource\{}.png".format(self.dict[j]))
                    image = pygame.transform.scale2x(image)
                    rect = pygame.Rect((72 * r, 72 * c), (72, 72))
                    self.rect.union(rect)
                    print(72 * r, 72 * c)
                    self.image.blit(image, rect)
                r = r + 1
            r = 0
            c = c + 1


class Map(pygame.sprite.Group):
    def __init__(self, backward_map, forward_map=[[0 for i in range(15)] for i in range(10)]):
        super().__init__()
        # 背景
        m_b = MapDraw(backward_map)
        # 前景
        m_f = MapDraw(forward_map)
        self.add(m_b, m_f)
        # 前景允许精灵碰撞
        self.forward_map_rect = m_f.rect
