# modules
from pygame import *
from random import randint
#class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # function for output player
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # function for moving the player right
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# text
font.init()
font1 = font.SysFont(None, 36)

lose1 = font1.render("PLAYER 1 LOSE", True, (0, 0, 0)) 
lose2 = font1.render("PLAYER 2 LOSE", True, (0, 0 ,0)) 

#windows size
win_height = 500
win_width = 700

# background color
bg = (200, 255, 255)

window = display.set_mode((win_width, win_height))

# create player and ball
platform1 = Player("platform.png", 15, 200, 50, 150, 4)
platform2 = Player("platform.png", 625, 200, 50, 150, 4)

ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

# speed ball
speed_x = 4
speed_y = 4

# game settings
game = True
finish = False
FPS = 60
clock = time.Clock()
while game:
    # clode game if QUIT
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.fill(bg)

        platform1.update_l()
        platform2.update_r()

        # moving ball
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y *= -1

        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish =  True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width - 50:
            finish =  True
            window.blit(lose2, (200, 200))



        platform1.reset()
        platform2.reset()
        
        ball.reset()

    display.update()

    clock.tick(FPS)
