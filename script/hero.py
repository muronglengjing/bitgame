import pygame
from pygame.locals import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, hp, attract, defense, local):
        super().__init__()

        self.name = name

        self.hp = hp
        self.hp_max = hp

        self.attraction = attract
        self.defense = defense
        self.attract_init = attract
        self.defense__init = defense

        self.direction = 0

        self.image = pygame.transform.scale2x(pygame.image.load("resource\hero2.png"))
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = local

        self.player_information()

        self.hp_line()

        self.speed = 3
        self.speed__init = 3


    def hp_line(self):
        self.player_information()
        hp_percentage = self.hp / self.hp_max
        self.hp_band = pygame.Surface([880, 10])
        if self.hp >=0 :
            hp_band = pygame.Surface([880 * hp_percentage, 10])
            hp_band.fill([220, 100, 100])
            self.hp_band.blit(hp_band, (0, 0))
        self.hp_rect = Rect((100, 700), (880, 10))

    def player_information(self):
        txt = pygame.font.Font(r"resource\XBS.ttf", 22)
        text = txt.render(
            "{} 攻击力:{} 防御力:{} 血量 {}|{}".format(self.name, self.attraction, self.defense, self.hp, self.hp_max),
            True, [100, 100, 100], [230, 240, 250])
        self.txt_band = pygame.Surface([1080, 50])
        self.txt_band.fill([230, 240, 250])
        self.txt_band.blit(text, [608, 2])
        self.txt_rect = Rect((0, 670), (1080, 30))

    def attract(self, attract):
        self.hp = self.hp - (attract - self.defense)
        pygame.mixer.music.load(r"resource\bit.wav")
        pygame.mixer.music.play()
        self.update()

    def move(self, x, y):
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
            self.rect.centerx += -dx * self.speed
            self.rect.centery += -dy * self.speed

    def head_direction(self, x, y):
        arg1, arg2 = (x - self.rect.centerx) + (y - self.rect.centery), -(x - self.rect.centerx) + (
                    y - self.rect.centery)
        if arg1 >= 0 and arg2 >= 0:
            self.direction = 2
            return 2
        elif arg1 <= 0 <= arg2:
            self.direction = 3
            return 3
        elif arg1 <= 0 and arg2 <= 0:
            self.direction = 0
            return 0
        elif arg1 >= 0 >= arg2:
            self.direction = 1
            return 1
        else:
            return 0

    def key_head_direction(self, key):
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.direction = 0
        elif key[pygame.K_RIGHT]or key[pygame.K_d]:
            self.direction = 1
        elif key[pygame.K_DOWN]or key[pygame.K_s]:
            self.direction = 2
        elif key[pygame.K_LEFT]or key[pygame.K_a]:
            self.direction = 3

    def key_move(self, key):
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.centery -= self.speed
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.centerx += self.speed
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.centery += self.speed
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.centerx -= self.speed

    def update(self):
        self.image = pygame.transform.scale2x(pygame.image.load("resource\hero{}.png".format(self.direction)))
        self.hp_line()
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        elif self.rect.centerx > 1080:
            self.rect.centerx = 1080
        if self.rect.centery < 0:
            self.rect.centery = 0
        elif self.rect.centery > 720:
            self.rect.centery = 720
        hp_percent = self.hp / self.hp_max
        self.defense = int((self.defense__init * 8)/(hp_percent+1)-3 * self.defense__init)
        self.attraction = int(-0.5*self.attract_init * (hp_percent ** 2) + 1.5 * self.attract_init)
        self.speed = -1.3*self.speed__init*hp_percent**2 + 2.3*self.speed__init


class Hero_group(pygame.sprite.Group):
    def draw(self, surface):
        """draw all sprites onto the surface

        Group.draw(surface): return None

        Draws all of the member sprites onto the given surface.

        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            self.spritedict[spr] = surface_blit(spr.txt_band, spr.txt_rect)
            self.spritedict[spr] = surface_blit(spr.hp_band, spr.hp_rect)
        self.lostsprites = []

    def update(self, *args):
        super().update()
        for i in self.sprites():
            if i.hp <= 0:
                i.kill()
