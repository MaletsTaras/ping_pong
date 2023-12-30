from pygame import *

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




win_height = 500
win_width = 700

bg = (200, 255, 255)

window = display.set_mode((win_width, win_height))

platform1 = Player("platform.png", 15, 200, 50, 150, 4)
platform2 = Player("platform.png", 625, 200, 50, 150, 4)

ball = GameSprite('ball.png', 200, 200, 50, 50, 4)

speed_x = 4
speed_y = 4

game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(bg)
        platform1.update_l()
        platform2.update_r()

        platform1.reset()
        platform2.reset()
        
        ball.reset()

    display.update()

    clock.tick(60)
