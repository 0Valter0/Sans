from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_weight, player_hight, player_speed, player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_weight, player_hight))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.hight = player_hight 
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
        if keys[K_w] and self.rect.y > 510:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 625:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 260:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 625:
            self.rect.x += self.speed

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

w1 = Wall(0, 0, 0, 250, 500, 400, 10)
w2 = Wall(0, 0, 0, 250, 500, 10, 150)
w3 = Wall(0, 0, 0, 250, 650, 400, 10)
w4 = Wall(0, 0, 0, 650, 500, 10, 160)
window = display.set_mode((900, 700))
display.set_caption('Snas')
backgroud = transform.scale(image.load('background.jpg'), (900, 700))
heart = Player('heart.jpg', 450, 550, 25, 25, 3, 3, 3)
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(backgroud, (0, 0))

        heart.reset()
        heart.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        display.update()
        clock.tick(60)

# #Labirint from pygame import *
# window = display.set_mode((900, 700))
# display.set_caption('Maze')
# #задай фон сцены
# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (50, 50))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class ClassPlayer(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < 820:
#             self.rect.x += self.speed
#         if keys[K_UP] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys[K_DOWN] and self.rect.y < 820:
#             self.rect.y += self.speed

# class Enemy(GameSprite):
#     def update(self):
#         if self.rect.x <= 590:
#             self.direction = 'right'
#         if self.rect.x >= 815:
#             self.direction = 'left'

#         if self.direction == 'left':
#             self.rect.x -= self.speed
#         else:
#             self.rect.x += self.speed

# class Enemy2(GameSprite):
#     def update(self):
#         if self.rect.x >= 815:
#             self.direction = 'left'
#         if self.rect.x <= 590:
#             self.direction = 'right'

#         if self.direction == 'right':
#             self.rect.x += self.speed 
#         else:
#             self.rect.x -= self.speed

# class Wall(sprite.Sprite):
#     def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
#         super().__init__()
#         self.color_1 = color_1
#         self.color_2 = color_2
#         self.color_3 = color_3
#         self.height = wall_height
#         self.width = wall_width
#         self.image = Surface((self.width, self.height))
#         self.image.fill((color_1, color_2, color_3))
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y
#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# w1 = Wall(154, 205, 64, 50, 55, 10, 700)
# w2 = Wall(154, 205, 64, 110, 0, 10, 645)
# w3 = Wall(154, 205, 64, 175, 55, 10, 700)
# w4 = Wall(154, 205, 64, 240, 0, 10, 645)
# w5 = Wall(154, 205, 64, 305, 55, 10, 700)
# w6 = Wall(154, 205, 64, 370, 0, 10, 645)
# w7 = Wall(154, 205, 64, 430, 55, 10, 700)
# w8 = Wall(154, 205, 64, 495, 0, 10, 645)
# w9 = Wall(154, 205, 64, 555, 55, 10, 700)
# w10 = Wall(154, 205, 64, 555, 65, 270, 10)
# w11 = Wall(154, 205, 64, 640, 135, 260, 10)
# w12 = Wall(154, 205, 64, 555, 205, 270, 10)
# w13 = Wall(154, 205, 64, 640, 275, 260, 10)
# w14 = Wall(154, 205, 64, 555, 345, 270, 10)
# w15 = Wall(154, 205, 64, 640, 415, 260, 10)
# w16 = Wall(154, 205, 64, 555, 485, 270, 10)


# backgroud = transform.scale(image.load('background.jpg'), (900, 700))
# #создай 2 спрайта и размести их на сцене

# #обработай событие «клик по кнопке "Закрыть окно"»sprite1.GameSprite('hero.png', 50, 450, 5)
# player = ClassPlayer('hero.png', 0, 450, 5)
# enemy = Enemy('cyborg.png', 580, 510, 5)
# enemy2 = Enemy2('cyborg.png', 820, 605, 5)
# treasure = ClassPlayer('treasure.png', 750, 660, 0)

# #обработай событие «клик по кнопке "Закрыть окно"»
# game = True
# clock = time.Clock()
# fps = 60
# speed = 1
# finish = True
# mixer.init()
# mixer.music.load('Фоновая (3).ogg')
# mixer.music.play()
# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')

# walls = sprite.Group()
# walls.add(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16)
# font.init()
# font = font.Font(None, 70)
# win = font.render('YOU WIN', True, (200, 255, 255))
# lose = font.render('YOU LOSE', True, (200, 255, 255))
    

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
    
#     if finish == True:
#         if sprite.collide_rect(player, treasure):
#             window.blit(win, (200, 200))
#             finish == False
#             money.play()
    
#         window.blit(backgroud, (0, 0))
#         w1.draw_wall()
#         w2.draw_wall()
#         w3.draw_wall()
#         w4.draw_wall()
#         w5.draw_wall()
#         w6.draw_wall()
#         w7.draw_wall()
#         w8.draw_wall()
#         w9.draw_wall()
#         w10.draw_wall()
#         w11.draw_wall()
#         w12.draw_wall()
#         w13.draw_wall()
#         w14.draw_wall()
#         w15.draw_wall()
#         w16.draw_wall()

#         player.update()
#         enemy.update()
#         enemy2.update()

#         player.reset()
#         enemy.reset()
#         enemy2.reset()
#         treasure.reset()
        
#         if sprite.spritecollide(player, walls, True):
#             finish = False
#             window.blit(lose, (200, 200))
#             kick.play()

#         if sprite.collide_rect(player, enemy):
#             finish = False
#             window.blit(lose, (200, 200))
#             kick.play()

#         if sprite.collide_rect(player, enemy2):
#             finish = False
#             window.blit(lose, (200, 200))
#             kick.play()
        
#         if sprite.collide_rect(player, treasure):
#             finish = False
#             window.blit(win, (200, 200))
#             money.play()
            
#         clock.tick(60)
#         display.update()

#Arcanoid
# import pygame
# pygame.init()

# mw = pygame.display.set_mode((500, 500))
# mw.fill((200, 255, 200))
# clock = pygame.time.Clock()
# game_over = False

# class Area():
#     def __init__(self, x=0, y=0, width=10, height=10, color = (0, 0, 0)):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.fill_color = (200, 255, 200)
    
#     def fill(self):
#         pygame.draw.rect(mw, self.fill_color, self.rect)
    
#     def colliderect(self, rect):
#         return self.rect.colliderect(rect)

# class Label(Area):
#     def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
#         self.image = pygame.font.SysFont("verdana", fsize).render(text, True, text_color)

#     def draw(self, shift_x=0, shift_y=0):
#         self.fill()
#         mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# class Picture(Area):
#     def __init__(self, filename, x = 0, y = 0, width = 10, height = 10,):
#         Area.__init__(self, x=x, y=y, width=width, height=height)
#         self.image = pygame.image.load(filename)
    
#     def draw(self):
#         mw.blit(self.image, (self.rect.x, self.rect.y))


# racket_x = 200
# racket_y = 330
# right_move = False
# left_move = False
# speed_x = 2
# speed_y = 2

# ball = Picture("pngegg (1) (1).png", 140, 180, 50, 50)
# platform = Picture("platform.png", racket_x, racket_y, 100, 30)        
# time_text = Label(95, 170, 50, 50, (200, 255, 200))

# start_x = 5
# start_y = 5
# count = 9
# monsters = list()

# for i in range(3):
#     x = start_x + (27.5 * i)
#     y = start_y + (55 * i)
#     for j in range(count):
#         monster = Picture("enemy.png", x, y, 50, 50)
#         monsters.append(monster)
#         x += 55
#     count -= 1


# while not game_over:
#     ball.fill()
#     platform.fill()


#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over =  True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 right_move = True
#             if event.key == pygame.K_LEFT:
#                 left_move = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 right_move = False
#             if event.key == pygame.K_LEFT:
#                 left_move = False

#     if right_move:
#         platform.rect.x += 3

#     if left_move:
#         platform.rect.x -= 3

#     ball.rect.x += speed_x
#     ball.rect.y += speed_y

#     for m in monsters:
#         m.draw()
#         if m.rect.colliderect(ball.rect):
#             monsters.remove(m)
#             m.fill()
#             speed_y *= -1
     
#     if ball.colliderect(platform.rect):
#         speed_y *= -1
#     if ball.rect.x > 450 or ball.rect.x < 0:
#         speed_x *= -1
#     if ball.rect.y < 0:
#         speed_y *= -1
    
#     if ball.rect.y > 360:
#         time_text.set_text("YOU LOSE, BOTIK", 60, (255, 0, 0))
#         time_text.draw(10, 10)
#         game_over = True

#     if len(monsters) == 0:
#         time_text.set_text("YOU WIN, BRO", 60, (0, 255, 51))   
#         time_text.draw(10, 10)
#         game_over = True 

#     platform.draw()
#     ball.draw()
#     pygame.display.update()
#     clock.tick(141)

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
