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
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 500:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 610:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 250:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 610:
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

w1 = Wall(255, 255, 255, 250, 500, 400, 10)
w2 = Wall(255, 255, 255, 250, 500, 10, 150)
w3 = Wall(255, 255, 255, 250, 650, 400, 10)
w4 = Wall(255, 255, 255, 650, 500, 10, 160)

window = display.set_mode((900, 700))
display.set_caption('Sans')
backgroud = transform.scale(image.load('background.jpg'), (900, 700))

bones_gorisontal_up = sprite.Group()
bones_gorisontal_down = sprite.Group()

for i in range(1, 5):
    bone_gorisontal_down = Bones_gorisontal_down1('Кость_вертикальная.jpg', 670, 450, 10, 100, 3, 3, 7)
    bones_gorisontal_down.add(bone_gorisontal_down)

for i in range(1, 5):
    bone_gorisontal_up = Bones_gorisontal_up1('Кость_вертикальная.jpg', 230, 600, 10, 100, 3, 3, 7)
    bones_gorisontal_up.add(bone_gorisontal_up)

heart = Player('heart.jpg', 450, 550, 50, 50, 3, 3, 3)
sans_stoit = Image('Санс_стоит.jpg', 355, 200, 200, 300)
sans_pobezhden = Image('Санс_побежден.jpg', 355, 200, 200, 300)
sans_atakyet = Image('Санс_атакует.jpg', 355, 100, 200, 300)
textovoe_oblako = Image('Текстовое_облако.jpg', 570, 150, 200, 200)

clock = time.Clock()

mixer.init()
mixer.music.load('MEGALOVANIA.mp3')
mixer.music.play()

font.init()
font = font.SysFont('Comic Sans MS', 20)
ready = font.render('Are you ready?', True, (0, 0, 0))

game = True
finish = False
back = True
play = True
num_for_back = 180
num_for_back2 = 60

window.blit(backgroud, (0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        if num_for_back > 0:
            heart.reset()
            heart.update()

            sans_stoit.reset()
            textovoe_oblako.reset()
            window.blit(ready, (600, 230))

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()
            
            num_for_back -= 1
        else:
            finish = True
            back = False  

    if not back:
        if num_for_back2 > 0:
            window.blit(backgroud, (0, 0))

            num_for_back2 -=1
        else:
            back = True
            play = False
        
    if not play:
        window.blit(backgroud, (0, 0))

        heart.reset()
        heart.update()

        sans_atakyet.reset()

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
            if bone_gorisontal_down.rect.collidepoint(230, 450):
                bone_gorisontal_down.kill()
                bone_gorisontal_down = Bones_gorisontal_down1('Кость_вертикальная.jpg', 670, 450, 10, 100, 3, 3, 3)
                bones_gorisontal_down.add(bone_gorisontal_down)

        for bone_gorisontal_up in bones_gorisontal_up:
            if bone_gorisontal_up.rect.collidepoint(670, 450):
                bone_gorisontal_up.kill()
                bone_gorisontal_up = Bones_gorisontal_up1('Кость_вертикальная.jpg', 670, 450, 10, 100, 3, 3, 3)
                bones_gorisontal_up.add(bone_gorisontal_up)


    display.update()
    clock.tick(60)
    #Ping-pong
# from pygame import *
# font.init()
# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_weight, player_hight, player_speed, player_speed_x, player_speed_y):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (player_weight, player_hight))
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#         self.weight = player_weight
#         self.hight = player_hight 
#         self.speed = player_speed
#         self.speed_x = player_speed_x
#         self.speed_y = player_speed_y
#     def colliderect(self, rect):
#         return self.rect.colliderect(rect)
#     def reset(self):
#         main_win.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update_l(self):
#         keys = key.get_pressed()
#         if keys[K_w] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys[K_s] and self.rect.y < 395:
#             self.rect.y += self.speed

#     def update_r(self):
#         keys = key.get_pressed()
#         if keys[K_UP] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys[K_DOWN] and self.rect.y < 395:
#             self.rect.y += self.speed

# class Enemy(GameSprite):
#     def update(self):
#         ball.rect.x += self.speed_x
#         ball.rect.y += self.speed_y
#         if self.colliderect(platform_l.rect):
#             self.speed_x *= -1
#         if self.colliderect(platform_r.rect):
#             self.speed_x *= -1  
#         if self.rect.y > 450 or self.rect.y < 0:
#             self.speed_y *= -1 

# platform_l = Player('platform_l.png', 50, 50, 20, 100, 10, 4, 4)
# platform_r = Player('platform_r.png', 650, 50, 20, 100, 10, 4, 4)
# ball = Enemy('ball.png', 200, 100, 50, 50, 5, 4, 4)
# win_width = 700
# win_height = 500
# back = transform.scale(image.load("background.jpg"), (win_width, win_height)) 
# main_win = display.set_mode((win_width, win_height))
# clock = time.Clock()

# font_1 = font.Font(None, 35)
# font_2 = font.Font(None, 25)
# lose_1 = font_1.render('PLAYER 2 WIN', True, (180, 0, 0))
# lose_2 = font_1.render('PLAYER 1 WIN', True, (180, 0, 0))

# lost_l = 0
# lost_r = 0



# run = True
# finish = False
# while run:
#     main_win.blit(back, (0, 0))
    
#     for e in event.get():
#         if e.type == QUIT:
#             run = False

#     if not finish:
        
        
#         platform_l.reset()
#         platform_l.update_l()

#         platform_r.reset()
#         platform_r.update_r()
        
#         ball.reset()
#         ball.update()

#         lost_r_text = font_2.render('Очков:' + str(lost_r), True, (180, 0, 0))
#         lost_l_text = font_2.render('Очков:' + str(lost_l), True, (180, 0, 0))
         
#         main_win.blit(lost_r_text, (630, 20))
#         main_win.blit(lost_l_text, (10, 20))

#         if ball.rect.x < 0:
#             ball.rect.x, ball.rect.y = 200, 100
#             ball.speed_x *= -1
#             lost_r += 1
            
#         if ball.rect.x > 650:
#             ball.rect.x, ball.rect.y = 600, 100
#             ball.speed_x *= -1
#             lost_l += 1

#         if lost_l >= 3:
#             main_win.blit(lose_2, (200, 200))
#             run = False
            
#         if lost_r >= 3:
#             main_win.blit(lose_1, (200, 200))
#             run = False 

#         display.update()
#         clock.tick(60)
