import pygame
import time
from pygame.locals import *
import random

class Base(object):
    def __init__(self, step, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.step = step

class BasePlane(object):
    def __init__(self, step, screen, x, y, image_path):
        Base.__init__(self, step, screen, x, y, image_path)
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.step = step
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for i in self.bullet_list:
            i.display()
            i.move()
            if i.judge():
                self.bullet_list.remove(i)


class HeroPlane(BasePlane):
    def __init__(self, step, screen):
        BasePlane.__init__(self, step, screen, 210, 700, "./feiji/hero1.png")

    def move_left(self):
        if self.x - self.step >= 0:
            self.x -= self.step

    def move_right(self):
        if self.x < 380:
            self.x += self.step

    def move_up(self):
        if self.y >= 0:
            self.y -= self.step

    def move_down(self):
        if self.y + self.step <= 852 - 124:
            self.y += self.step

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, 7, self.x, self.y))


class EnemyPlane(BasePlane):
    def __init__(self, step, screen):
        BasePlane.__init__(self, step, screen, 0, 0, "./feiji/enemy0.png")
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += self.step
            if (self.x > 480 - 50):
                self.direction = "left"
        else:
            self.x -= self.step
            if (self.x <= 0):
                self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 2 or random_num == 8:
            self.bullet_list.append(BulletEnemy(self.screen, 7, self.x, self.y))


class BaseBullet(object):
    def __init__(self, screen, step, x, y, img_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(img_path)
        self.step = step

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, screen, step, x, y):
        BaseBullet.__init__(self, screen, step, x + 40, y - 20, "./feiji/bullet.png")

    def judge(self):
        if (self.y <= 0):
            return True
        else:
            return False

    def move(self):
        self.y -= self.step


class BulletEnemy(BaseBullet):
    def __init__(self, screen, step, x, y):
        BaseBullet.__init__(self, screen, step, x + 25, y + 40, "./feiji/bullet1.png")

    def judge(self):
        if (self.y > 852):
            return True
        else:
            return False

    def move(self):
        self.y += self.step


def key_control(hero):
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print("kongge")
                hero.fire()
            elif event.key == K_w or event.key == K_UP:
                hero.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                hero.move_down()


def main():
    # 1.创建一个窗口,用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2.创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    # 3.把背景图片放到窗口中显示

    # 创建飞机
    hero = HeroPlane(10, screen)
    enemy = EnemyPlane(5, screen)

    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        # 更新视图
        pygame.display.update()
        # 获取事件，比如按键等
        key_control(hero)
        time.sleep(0.016)


if __name__ == '__main__':
    main()
