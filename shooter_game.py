

from pygame import *
from random import *
from time import time as tm

mixer.init()
font.init()
font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 70)

loose1 = font1.render('Villager looses (sadly)!', True, (255, 10, 255))
loose2 = font1.render('Knight looses (badly)!', True, (255, 255, 255))


#создай окно игры
window = display.set_mode((1000, 600))
display.set_caption('Понг Пинг')
background = transform.scale(image.load('Fallen kingdom.jpg'), (1000, 600))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 425:
            self.rect.y += self.speed
    
    def updateBAD(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed



# mixer.music.load('')
# mixer.music.play()
# mixer.music.set_volume(0.3)
# kick = mixer.Sound('fire.ogg')

speed_x = 3
speed_y = 3


clock = time.Clock()
game = True
finish = False


catBoes = Player('bobski.png', 0, 150, 10, 85, 175)
catVragec = Player('Knight.png', 915, 150, 10, 85, 175)
plagina = GameSprite('Plague.png', 500, 300, 12, 50, 50)

while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                pass
        if e.type == QUIT:
            game = False

    if finish != True:
        plagina.rect.x += speed_x
        plagina.rect.y += speed_y
        if plagina.rect.y <= 0:
            speed_y *= -1

        if plagina.rect.y >= 550:
            speed_y *= -1
    
        window.blit(background,(0,0))        
        catBoes.update()
        catBoes.reset()
        catVragec.updateBAD()
        catVragec.reset()
        plagina.reset()
        
        plagina.rect.x += speed_x

        plagina.rect.y += speed_y

        if plagina.rect.y <= 0:
            speed_y *= -1

        if plagina.rect.y >= 550:
            speed_y *= -1

        if plagina.rect.y <= 0:
            speed_y *= -1

        if plagina.rect.y >= 550:
            speed_y *= -1

        if sprite.collide_rect(catBoes, plagina) or sprite.collide_rect(catVragec, plagina):
            speed_x *= -1

        if plagina.rect.x > 1000:
            finish = True
            window.blit(loose2, (250, 300))
        
        if plagina.rect.x < -55:
            finish = True
            window.blit(loose1, (250, 300))

    display.update()
    clock.tick(40)



   

