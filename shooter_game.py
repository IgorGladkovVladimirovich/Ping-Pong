#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as tm

mixer.init()
font.init()
font1 = font.SysFont('Arial', 100)
font2 = font.SysFont('Arial', 40)

win = font1.render('YOU WIN!', True, (255, 10, 255))
loose = font1.render('YOU LOOSE!', True, (255, 255, 255))


#создай окно игры
window = display.set_mode((1800, 1200))
display.set_caption('Понг Пинг')
background = transform.scale(image.load('Fallen kingdom.jpg'), (1800, 1200))

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

        if key_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed

        if key_pressed[K_d] and self.rect.x < 1030:
            self.rect.x += self.speed
    




# mixer.music.load('')
# mixer.music.play()
# mixer.music.set_volume(0.3)
# kick = mixer.Sound('fire.ogg')




clock = time.Clock()
game = True
finish = False


catBoes = Player('bobski.png', 600, 690, 10, 70, 110)


while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                pass
        if e.type == QUIT:
            game = False

    if finish != True:
        
        window.blit(background,(0,0))        
        catBoes.update()
        catBoes.reset()
        

        


    display.update()
    clock.tick(40)



   

