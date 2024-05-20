import pygame as py
import time

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
        self.mask= py.mask.from_surface(self.image)

    def update (self):
        self.movement()
        self.correction()
        self.Checaimpacto()
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

    def Checaimpacto(self):
        mbpC=py.sprite.spritecollide(self, group_mbp, False, py.sprite.collide_mask)
        if mbpC:
            explosao.explode(self.x, self.y)

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
        self.mask= py.mask.from_surface(self.image)

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
        self.iwin = py.image.load ('fuga_mbappé.png')
        self.ilose = py.image.load ('mbappé_te_pegou.png')

        self.imapa = py.transform.scale (self.imapa,(WIDTH,HEIGHT))
        self.iwin = py.transform.scale (self.iwin,(WIDTH,HEIGHT))
        self.ilose = py.transform.scale (self.ilose,(WIDTH,HEIGHT))

        self.image = self.imapa
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()

        def update (self):
            self.rect.topleft = (self.x,self.y)

class brj (py.sprite.Sprite):
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
            self.x = 1170
        
        self.y = HEIGHT / 2
        self.image = py.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.mask= py.mask.from_surface(self.image)
    
    def update (self):
        if self.visible:
            self.pegabrj()
            self.rect.center = (self.x,self.y) 

    def pegabrj(self):
        global pontos,capy

        pega_brj= py.sprite.spritecollide(self, capy_group, False, py.sprite.collide_mask)
        if pega_brj:
            self.visible= False
        
        if self.numero == 1:
            brj1.visible = True
            if pontos< 5:
                sobenivel()
            else:
                capy_group.empty()
                MataQualquer()
                TelaFim(1)
        else:
            brj2.visible= True

class explosao(object):
    def __init__(self):
        self.costume =1 
        self.width= 140 
        self.height= 140
        self.image=py.image.load('explosion'+ str(self.costume)+ '.png')
        self.image=py.transform.scale(self.image, (self.width, self.height))

    def explode(self,x,y):
        x= x-self.width/2
        y= y-self.height/2
        MataCapy()

        while self.costume < 9:
            self.image=py.image.load('explosion'+ str(self.costume)+ '.png')
            self.image=py.transform.scale(self.image, (self.width, self.height))
            window.blit(self.image, (x,y))
            py.display.update()

            self.costume += 1 
            time.sleep(0.1)

        MataQualquer()
        TelaFim(0)
        


def pontodpl():
    global jogo
    ponto_texto = pontos_font.render(str(pontos) + ' / 5', True, (0,0,0))
    window.blit(ponto_texto,(255,10))  

def checabreja():
    for brj in brjs:
        if not brj.visible:
            brj.kill()

        else:
            if not brj.alive():
                group_brj.add(brj)

def sobenivel():
    global pontos

    if  mbappe_1.vel < 0:
        mbappe_1.vel -=1

    else:
        mbappe_1.vel += 1 

    if  mbappe_2.vel < 0:
        mbappe_2.vel -=1

    else:
        mbappe_2.vel += 1 

    ponto += 1

def MataCapy():
    global capy

    capy.kill()
    screen_group.draw(window)
    capy_group.draw(window)
    group_brj.draw(window)
    screen_group.update()
    capy_group.update()
    group_brj.update()

    py.display.update()

def MataQualquer():
    capy_group.empty()
    group_brj.empty()
    group_mbp.empty()
    pontos.empty()

    brjs.clear()
    
def TelaFim(n):
    global jogo

    jogo= False
    if n == 0:
        fundo.image= fundo.ilose
    
    elif n ==1:
        fundo.image= fundo.iwin

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

brj1= brj(1)
brj2= brj(2)
group_brj=py.sprite.Group()
group_brj.add(brj1,brj2)
brjs= [brj1,brj2]

explosao= explosao()
jogo=True
game = True

while game :
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    screen_group.draw(window)

    pontodpl()
    checabreja()

    group_mbp.draw(window)
    capy_group.draw(window)
    group_brj.draw(window)
    group_mbp.update()
    capy_group.update()
    screen_group.update()
    group_brj.update()
    

    py.display.update()
py.quit()

