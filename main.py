# coding=utf-8
from os.path import exists
from script.bullet import *
from script.enemy import *
from script.button import *
from script.map import *
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode([1080, 720])
screen.fill([255, 255, 255])
pygame.display.set_caption("crazy cat")
pygame.display.set_icon(pygame.image.load(r"resource\cat.png"))


def welcome():
    screen.fill([255, 255, 255])
    font = pygame.font.Font(r"resource\XBS.ttf", 100)
    text1 = font.render("Crazy Cat", True, [10, 10, 10], [255, 255, 255])
    screen.blit(text1, (300, 100))
    font2 = pygame.font.Font(r"resource\XBS.ttf", 30)
    text2 = font2.render("software developed by RQY", True, [200, 200, 200], [255, 255, 255])
    screen.blit(text2, (380, 650))
    welcome.button1 = ButtonText("开始", (480, 500), 60)
    welcome.button2 = ButtonText("关于", (480, 565), 60)
    welcome.button_group = pygame.sprite.Group()
    welcome.button_group.add(welcome.button1)
    welcome.button_group.add(welcome.button2)
    welcome.button_group.draw(screen)


def about():
    screen.fill([255, 255, 255])
    font = pygame.font.Font(r"resource\XBS.ttf", 50)
    if exists(r"resource\love_song.txt"):
        txt = open(r"resource\love_song.txt", "r", encoding='UTF-8').read()
    else:
        txt = ""
    text = font.render(txt, True, [10, 10, 10], [255, 255, 255])
    txt = ""
    screen.blit(text, (200, 250))
    about.button = ButtonText("返回", (480, 565), 60)
    about.button_group = pygame.sprite.Group()
    about.button_group.add(about.button)
    about.button_group.draw(screen)


def start():
    screen.fill([255, 255, 255])
    font = pygame.font.Font(r"resource\XBS.ttf", 50)
    text = font.render("选择一个合适的移动/攻击方式", True, [10, 10, 10], [255, 255, 255])
    screen.blit(text, (200, 100))
    start.button1 = ButtonPicture("key_mouse", (10, 350))
    start.button2 = ButtonPicture("mouse_key", (560, 350))
    start.button_group = pygame.sprite.Group()
    start.button_group.add(start.button1)
    start.button_group.add(start.button2)
    start.button_group.draw(screen)


def fileopen():
    file = open(r"resource\data.txt", "r").read()
    file = file.split("\n")
    data = []
    for i in file:
        i = i.split(",")
        data.append(i)
    return data


def game():
    data = fileopen()
    screen.fill([255, 255, 255])
    game.x, game.y = 540, 320
    game.hero = Hero("思蜀", eval(data[0][0]), eval(data[0][1]), eval(data[0][2]), (game.x, game.y))
    game.hero_group = Hero_group()
    game.hero_group.add(game.hero)
    game.hero_speed = eval(data[0][3])
    game.speed = eval(data[2][0])
    game.cat_speed = eval(data[1][3])
    game.cat_group = Enemy_group()
    maps = [[0 for i in range(15)] for i in range(10)]
    game.mapper = Map(maps)
    game.hero_bullet = Bullet_Group()
    game.cat_bullet = Bullet_Group()
    game.clock = pygame.time.Clock()
    game.time_counter = 0
    game.cat = Enemy("Crazy Cat", eval(data[1][0]), eval(data[1][1]), eval(data[1][2]), (500, 50), "cat")
    game.cat_group.add(game.cat)
    game.game_time = pygame.time.Clock()
    game.game_time.get_time()


def data_save(times):
    file = open(r"resource\game_data.txt", "a+")
    file.write("\n" + str(times))
    file.close()


def data_open():
    if exists(r"resource\game_data.txt"):
        file = open(r"resource\game_data.txt", "r")
        data = file.readlines()
        file.close()
        game_data = []
        for i in data:
            if i.rstrip("\n") == "":
                game_data.append(3600)
            else:
                game_data.append(eval(i.rstrip("\n")))
        print(game_data)
        return min(game_data)
    else:
        file = open(r"resource\game_data.txt", "w")
        file.write("3600")
        file.close()


def game_over(win):
    end_time = time.process_time()
    times = end_time - start_time
    surface = pygame.Surface([450, 720])
    surface.fill([255, 255, 255])
    screen.blit(surface, (630, 0))
    font = pygame.font.Font(r"resource\XBS.ttf", 50)
    if win:
        text1 = font.render("恭喜你胜利了！", True, [200, 10, 10], [255, 255, 255])
        data_save(times)
    else:
        text1 = font.render("很遗憾失败了！", True, [100, 100, 100], [255, 255, 255])
    screen.blit(text1, (700, 100))
    font = pygame.font.Font(r"resource\XBS.ttf", 30)
    text2 = font.render("总共耗时{}s".format(times), True, [100, 100, 100], [255, 255, 255])
    text3 = font.render("最佳记录{}s".format(data_open()), True, [100, 100, 100], [255, 255, 255])
    screen.blit(text2, (700, 250))
    screen.blit(text3, (700, 300))
    game_over.button1 = ButtonText("重新开始", (800, 400))
    game_over.button2 = ButtonText("回到主页", (800, 500))
    game_over.button_group = pygame.sprite.Group()
    game_over.button_group.add(game_over.button1)
    game_over.button_group.add(game_over.button2)
    game_over.button_group.draw(screen)


welcome_windows = True
about_windows = False
load_in = False
gaming = False
last = False
end = False
move_motion = 0

x_part, y_part = 500, 500

welcome()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出游戏
            pygame.quit()
            break

        if event.type == MOUSEBUTTONDOWN:
            if welcome_windows:
                if welcome.button1.chick_in(x, y):
                    print("点击开始")
                    start()
                    load_in = True
                    welcome_windows = False
                if welcome.button2.chick_in(x, y):
                    print("点击关于")
                    about()
                    about_windows = True
                    welcome_windows = False
            elif about_windows:
                if about.button.chick_in(x, y):
                    print("点击返回")
                    welcome()
                    about_windows = False
                    welcome_windows = True
            elif load_in:
                if start.button1.chick_in(x, y):
                    print("键盘移动、鼠标攻击")
                    move_motion = 0
                    game()
                    game.mapper.draw(screen)
                    load_in = False
                    gaming = True
                    start_time = time.process_time()
                elif start.button2.chick_in(x, y):
                    print("鼠标移动、键盘攻击")
                    move_motion = 1
                    game()
                    game.mapper.draw(screen)
                    load_in = False
                    gaming = True
                    start_time = time.process_time()
            elif gaming:
                if move_motion == 0:
                    game.hero.head_direction(x, y)
                    hero_bullet = Bullet(game.hero.rect.centerx, game.hero.rect.centery, game.hero.direction,
                                         game.hero_speed, [100, 100, 240])
                    game.hero_bullet.add(hero_bullet)
            elif end:
                if game_over.button1.chick_in(x, y):
                    game()
                    gaming = True
                    end = False
                    start_time = time.process_time()
                elif game_over.button2.chick_in(x, y):
                    welcome()
                    welcome_windows = True
                    end = False
        if event.type == MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if last:
                end = True
            if welcome_windows:
                welcome.button_group.update()
                welcome.button_group.draw(screen)
                if welcome.button1.chick_in(x, y):
                    if pygame.mixer.music.get_busy():
                        pass
                    else:
                        pygame.mixer.music.load(r"resource\start.mp3")
                        pygame.mixer.music.play()
                welcome.button2.chick_in(x, y)
            elif about_windows:
                about.button_group.update()
                about.button_group.draw(screen)
                about.button.chick_in(x, y)
            elif load_in:
                start.button_group.update()
                start.button_group.draw(screen)
                start.button1.chick_in(x, y)
                start.button2.chick_in(x, y)
            if last:
                game_over(win)
                last = False
            if end:
                game_over.button_group.update()
                game_over.button_group.draw(screen)
                game_over.button1.chick_in(x, y)
                game_over.button2.chick_in(x, y)

        elif event.type == KEYDOWN:
            key = pygame.key.get_pressed()
            if gaming:
                if move_motion == 1:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        hero_bullet = Bullet(game.hero.rect.centerx, game.hero.rect.centery, game.hero.direction,
                                             game.hero_speed, [100, 100, 240])
                        game.hero_bullet.add(hero_bullet)

    key = pygame.key.get_pressed()

    if gaming:
        if move_motion == 0:
            game.hero.key_move(key)

        if move_motion == 1:
            game.hero.key_move(key)
            game.hero.head_direction(game.cat.rect.centerx, game.cat.rect.centery)

        if game.cat.alive():
            if game.time_counter > game.speed / 8:
                game.cat.move(game.hero.rect.centerx, game.hero.rect.centery)
            if game.time_counter > game.speed:
                cat_bullet = Bullet(game.cat.rect.centerx, game.cat.rect.centery, game.cat.direction, game.cat_speed, [100, 100, 100])
                game.cat_bullet.add(cat_bullet)
                game.time_counter = 0
            else:
                game.time_counter += game.clock.get_time()
        else:
            print("win")
            gaming = False
            last = True
            win = True

        if game.hero.alive():
            pass
        else:
            gaming = False
            last = True
            win = False

        # 检测攻击
        if pygame.sprite.spritecollide(game.cat, game.hero_bullet, True):
            game.cat.attract(game.hero.attraction)

        if pygame.sprite.spritecollide(game.hero, game.cat_bullet, True):
            game.hero.attract(game.cat.attraction)

        game.mapper.draw(screen)
        game.hero_bullet.update()
        game.cat_bullet.update()
        game.hero_group.update()
        game.cat_group.update()
        game.hero_bullet.draw(screen)
        game.cat_bullet.draw(screen)
        game.hero_group.draw(screen)
        game.cat_group.draw(screen)
        game.clock.tick()

    pygame.display.update()
    pygame.time.Clock().tick()
