import pygame


class ButtonPicture(pygame.sprite.Sprite):
    def __init__(self, path, local=(0, 0)):
        super().__init__()
        self.forward_image = pygame.image.load(r"resource\{}.png".format(path))
        self.image = pygame.Surface(self.forward_image.get_size())
        self.image.fill([200, 200, 200])
        self.image.blit(self.forward_image, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = local
        self.mouse_in = False

    def chick_in(self, x, y):
        if self.rect.x < x < self.rect.x + self.rect.width and self.rect.y < y < self.rect.height + self.rect.y:
            self.mouse_in = True
        else:
            self.mouse_in = False
        self.update()
        return self.mouse_in

    def update(self, *args):
        if self.mouse_in:
            self.image.fill([240, 200, 100])
            self.image.blit(self.forward_image, (0, 0))
        else:
            self.image.fill([200, 200, 200])
            self.image.blit(self.forward_image, (0, 0))


class ButtonText(pygame.sprite.Sprite):
    def __init__(self, txt, local=(0, 0), size=50):
        super().__init__()
        self.txt = txt
        self.size = size

        self.font = pygame.font.Font(r"resource\XBS.ttf", size)
        self.text = self.font.render(txt, True, [10, 10, 10], [255, 255, 255])
        self.image = pygame.Surface([len(txt)*size, size])
        self.image.blit(self.text, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = local
        self.mouse_in = False

    def chick_in(self, x, y):
        if self.rect.x < x < self.rect.x + self.rect.width and self.rect.y < y < self.rect.height + self.rect.y:
            self.mouse_in = True
        else:
            self.mouse_in = False
        self.update()
        return self.mouse_in

    def update(self, *args):
        if self.mouse_in:
            self.image.fill([240, 200, 100])
            self.text = self.font.render(self.txt, True, [240, 200, 100], [255, 255, 255])
            self.image.blit(self.text, (0, 0))
        else:
            self.image.fill([240, 200, 100])
            self.text = self.font.render(self.txt, True, [10, 10, 10], [255, 255, 255])
            self.image.blit(self.text, (0, 0))



