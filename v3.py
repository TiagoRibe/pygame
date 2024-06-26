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
        self.correction()
        self.rect.center = (self.x,self.y)
    
    def movement (self):
        keys = py.key.get_pressed()
        if keys [py.K_LEFT]:
            self.x -= self.vel
            self.image = self.capy2
        elif keys [py.K_RIGHT]:
            self.x += self.vel
            self.image = self.capy1
        if keys [py.K_UP]:
            self.y -= self.vel
        elif keys [py.K_DOWN]:
            self.y += self.vel

    def correction (self):
        if self.x - self.widht / 2 < 0 :
            self.x = self.widht / 2

        elif self.x + self.widht / 2 > WIDTH:
            self.x = WIDTH - self.widht / 2

        if self.y - self.height / 2 < 0 :
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

        


class mbp(py.sprite.Sprite):
    def __init__ (self,numero):
        super().__init__()
        if numero == 1:
            self.x = 380
            self.image = py.image.load ('mbappé.png')
            self.vel = -4
        else:
            self.x = 920
            self.image = py.image.load ('mbappé.png')
            self.vel = 5
        
        self.y = HEIGHT / 2
        self.widht = 100
        self.height = 150
        self.image = py.transform.scale(self.image,(self.widht,self.height))
        self.rect = self.image.get_rect()

    def update (self):
        self.movement()
        self.rect.center = (self.x, self.y)
    
    def movement (self):
        self.y += self.vel
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1
        
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1

class Tela(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imapa = py.image.load ('mapa1.png')
        self.iwin = py.image.load ('grama_na_direita.jpg')
        self.ilose = py.image.load ('grama_na_esquerda.jpg')

        self.imapa = py.transform.scale (self.imapa,(WIDTH,HEIGHT))
        self.iwin = py.transform.scale (self.iwin,(WIDTH,HEIGHT))
        self.ilose = py.transform.scale (self.ilose,(WIDTH,HEIGHT))

        self.image = self.imapa
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()

        def update (self):
            self.rect.topleft = (self.x,self.y)

class breja (py.sprite.Sprite):
    def __init__(self,numero):
        super().__init__()
        self.numero = numero
        if self.numero == 1:
            self.image = py.image.load ('cerveja.png')
            self.visible = False
            self.x = 50
        else:
            self.image = py.image.load ('cerveja.png')
            self.visible = True
            self.x = 580
        
        self.y = HEIGHT / 2
        self.image = py.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
    
    def update (self):
        if self.visible:
            self.rect.center = (self.x,self.y)


def pontodpl():
    ponto_texto = pontos_font.render(str(pontos) + ' / 5', True, (0,0,0))
    window.blit(ponto_texto,(255,10))  

WIDTH = 1280
HEIGHT = 720

py.init()

window= py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption ('Crossy Tiête')
clock = py.time.Clock ()

pontos = 0
pontos_font = py.font.SysFont ('comicsans', 50 , True)

fundo = Tela ()
screen_group = py.sprite.Group()
screen_group.add(fundo)

capy =capy()
capy_group = py.sprite.Group()
capy_group.add(capy)

mbappe_1 = mbp(1)
mbappe_2 = mbp(2)
group_mbp = py.sprite.Group()
group_mbp.add(mbappe_1,mbappe_2)



game = True

while game :
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    screen_group.draw(window)

    capy_group.draw(window)
    group_mbp.draw(window)
    capy_group.update()
    group_mbp.update()
    screen_group.update()
    pontodpl()

    py.display.update()
py.quit()
