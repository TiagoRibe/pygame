import pygame as py

class capy(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT/2
        self.vel = 4
        self.widht = 100
        self.height = 50

        self.capy1 = py.image.load ('capivara_para_direita.png')
        self.capy2 = py.image.load ('capivara_para_esquerda.png')
        self.capy1 = py.transform.scale(self.capy1,(self.widht,self.height))
        self.capy2 = py.transform.scale(self.capy2,(self.widht,self.height))
        self.image = self.capy1
        self.rect = self.image.get_rect()

    def update (self):
        self.movement()
        self.rect.center = (self.x,self.y)
    
    def movement (self):
        keys = py.key.get_pressed()
        if keys [py.K_LEFT]:
            self.x -= self.vel
        elif keys [py.K_RIGHT]:
            self.x += self.vel
        if keys [py.K_UP]:
            self.y -= self.vel
        elif keys [py.K_DOWN]:
            self.y += self.vel

WIDTH = 1280
HEIGHT = 720

py.init()

window= py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption ('Crossy Tiête')
clock = py.time.Clock ()

capy =capy()
capy_group = py.sprite.Group()
capy_group.add(capy)

game = True

while game :
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    window.fill((0,255,0))
    capy_group.draw(window)
    capy_group.update()
    py.display.update()
py.quit()