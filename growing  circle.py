import pygame
pygame.init()

WIDTH = 900
HEIGHT = 900

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("sky blue")


class Circle:
    def __init__(self,color,pos,r,w):
        self.color=color
        self.pos=pos
        self.r=r
        self.w=w
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.r,self.w)

    def growcircle(self,r):
        self.r = self.r+r
        pygame.draw.circle(self.screen,self.color,self.pos,self.r,self.w)

c1 = Circle("blue",(450,450),20,0)



while True:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("sky blue")
            c1.draw()
            pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill("sky blue")  
            c1.growcircle(20)
            pygame.display.update()
            
        elif event.type==pygame.QUIT:
            pygame.quit



    pygame.display.update()



