import pygame
from pygame.locals import *


class MapObject(pygame.sprite.Sprite):
    def __init__(self, key, x, y):
        super().__init__()
        dic = {0: "glass"}
        self.image = pygame.image.load("resource\{}.png".format(dic[key]))
        self.image = pygame.transform.scale2x(self.image)
        self.rect = Rect((x*72, y*72), (72, 72))


class Map(pygame.sprite.Group):
    def __init__(self, maps):
        super().__init__()
        c, r = 0, 0
        for maps_raw in maps:
            for maps_object in maps_raw:
                mo = MapObject(maps[r][c], c, r)
                self.add(mo)
                c = c + 1
            c = 0
            r = r + 1

    def map_move(self, x_to_map, y_to_map):
        if x_to_map > self.X_map - 540:
            lift = -(self.X_map - 540)
        elif x_to_map < 540:
            lift = 0
        else:
            lift = x_to_map - 540
        if y_to_map > self.Y_map - 540:
            up = -(self.X_map - 540)
        elif y_to_map < 360:
            up = 0
        else:
            up = y_to_map - 360
        return lift, up