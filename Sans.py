from pygame import *
from time import sleep

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_height, player_speed, player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.height = player_height 
        self.speed = player_speed
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_gorisontal(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 500:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 610:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 250:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 610:
            self.rect.x += self.speed

    def update_vertival(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 150:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 510:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 375:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 485:
            self.rect.x += self.speed

class Image():
    def __init__(self, image1, image_x, image_y, image_weight, image_height):
        self.weight = image_weight
        self.height = image_height
        self.image = transform.scale(image.load(image1), (image_weight, image_height))
        self.rect = self.image.get_rect()
        self.rect.x = image_x
        self.rect.y = image_y   
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.height = wall_height
        self.width = wall_width
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bones_gorisontal_up1(GameSprite):
    def update(self):
        self.rect.x += self.speed

class Bones_gorisontal_down1(GameSprite):
    def update(self):
        self.rect.x -= self.speed

class Bones_vertical_right1(GameSprite):
    def update(self):
        self.rect.y -= self.speed

class Bones_vertical_left1(GameSprite):
    def update(self):
        self.rect.y += self.speed

w1 = Wall(255, 255, 255, 250, 500, 400, 10)
w2 = Wall(255, 255, 255, 250, 500, 10, 150)
w3 = Wall(255, 255, 255, 250, 650, 400, 10)
w4 = Wall(255, 255, 255, 650, 500, 10, 160)

w5 = Wall(255, 255, 255, 375, 150, 150, 10)
w6 = Wall(255, 255, 255, 375, 150, 10, 400)
w7 = Wall(255, 255, 255, 375, 550, 150, 10)
w8 = Wall(255, 255, 255, 525, 150, 10, 410)

window = display.set_mode((900, 700))
display.set_caption('Sans')
backgroud = transform.scale(image.load('background.jpg'), (900, 700))

bones_gorisontal_up = sprite.Group()
bones_gorisontal_down = sprite.Group()
bones_vertical_left = sprite.Group()
bones_vertical_right = sprite.Group()

for i in range(1, 5):
    bone_gorisontal_down = Bones_gorisontal_down1('Кость_вертикальная.jpg', 670, 600, 10, 100, 7, 7, 7)
    bones_gorisontal_down.add(bone_gorisontal_down)

for i in range(1, 5):
    bone_gorisontal_up = Bones_gorisontal_up1('Кость_вертикальная.jpg', 230, 450, 10, 100, 7, 7, 7)
    bones_gorisontal_up.add(bone_gorisontal_up)

for i in range(1, 5):
    bone_vertical_left = Bones_vertical_left1('Кость_горизонтальная.jpg', 335, 130, 100, 10, 7, 7, 7)
    bones_vertical_left.add(bone_vertical_left)

for i in range(1, 5):
    bone_vertical_right = Bones_vertical_right1('Кость_горизонтальная.jpg', 490, 555, 100, 10, 7, 7, 7)
    bones_vertical_right.add(bone_vertical_right)

heart = Player('heart.jpg', 450, 550, 50, 50, 3, 3, 3)
sans_stoit = Image('Санс_стоит.jpg', 355, 200, 200, 300)
sans_pobezhden = Image('Санс_побежден.jpg', 355, 200, 200, 300)
sans_atakyet_gorisontal = Image('Санс_атакует.jpg', 355, 100, 200, 300)
sans_atakyet_vertical_right = Image('Санс_атакует.jpg', 600, 180, 200, 300)
sans_atakyet_vertical_left = Image('Санс_атакует.jpg', 100, 180, 200, 300)
textovoe_oblako = Image('Текстовое_облако.jpg', 570, 150, 200, 200)

clock = time.Clock()

font.init()
font = font.SysFont('Comic Sans MS', 20)
ready = font.render('Are you ready?', True, (0, 0, 0))

game = True
finish = False
play = True
play_again = True
num_one = True
num_two = True

num_for_one = 180
num_for_two = 250
num_for_background1 = 60
num_for_background2 = 60


window.blit(backgroud, (0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        if num_for_one > 0:
            heart.reset()
            heart.update_gorisontal()

            sans_stoit.reset()
            textovoe_oblako.reset()
            window.blit(ready, (600, 230))

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()
            
            num_for_one -= 1
        else:
            finish = True
            num_one = False  

    if not num_one:
        if num_for_background1 > 0:
            window.blit(backgroud, (0, 0))

            num_for_background1 -=1
        else:
            num_one = True
            play = False
        
    if not play:
        if num_for_two > 0:   
            window.blit(backgroud, (0, 0))

            heart.reset()
            heart.update_gorisontal()

            sans_atakyet_gorisontal.reset()

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()

            for b in bones_gorisontal_down:
                b.update()
            bones_gorisontal_down.draw(window)


            bones_gorisontal_up.draw(window)
            for b in bones_gorisontal_up:
                b.update()

            for bone_gorisontal_down in bones_gorisontal_down:
                if bone_gorisontal_down.rect.collidepoint(230, 600):
                    bone_gorisontal_down.kill()
                    bone_gorisontal_down = Bones_gorisontal_down1('Кость_вертикальная.jpg', 670, 600, 10, 100, 7, 7, 7)
                    bones_gorisontal_down.add(bone_gorisontal_down)

            for bone_gorisontal_up in bones_gorisontal_up:
                if bone_gorisontal_up.rect.collidepoint(670, 450):
                    bone_gorisontal_up.kill()
                    bone_gorisontal_up = Bones_gorisontal_up1('Кость_вертикальная.jpg', 230, 450, 10, 100, 7, 7, 7)
                    bones_gorisontal_up.add(bone_gorisontal_up)
            num_for_two -= 1
        else:
            num_two = False
            play = True

    if not num_two:
        if num_for_background2 > 0:
            window.blit(backgroud, (0, 0))
            num_for_background2 -=1
        else:
            num_two = True
            play_again = False
    
    if not play_again:
        window.blit(backgroud, (0, 0))

        heart.reset()
        heart.update_vertival()

        sans_atakyet_vertical_right.reset()
        sans_atakyet_vertical_left.reset()

        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        bones_vertical_left.draw(window)
        for b in bones_vertical_left:
            b.update()

        bones_vertical_right.draw(window)
        for b in bones_vertical_right:
            b.update()

        for bone_vertical_right in bones_vertical_right:
            if bone_vertical_right.rect.collidepoint(490, 130):
                bone_vertical_right.kill()
                bone_vertical_right = Bones_vertical_right1('Кость_горизонтальная.jpg', 490, 555, 100, 10, 7, 7, 7)
                bones_vertical_right.add(bone_vertical_right)

        for bone_vertical_left in bones_vertical_left:
            if bone_vertical_left.rect.collidepoint(335, 555):
                bone_vertical_left.kill()
                bone_vertical_left = Bones_vertical_left1('Кость_горизонтальная.jpg', 335, 130, 100, 10, 7, 7, 7)
                bones_vertical_left.add(bone_vertical_left)

    display.update()
    clock.tick(60)
