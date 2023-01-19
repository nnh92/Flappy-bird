import pygame
import random

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 336,550
        linkBackground = './Data/background_night.png'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))

        pygame.display.set_caption('Flappy bird!')
        self.background = pygame.image.load(linkBackground).convert()
        self.background = pygame.transform.scale(self.background,(self.xScreen, self.yScreen))
        linkIcon = pygame.image.load('./Data/Bird.png').convert()
        pygame.display.set_icon(linkIcon)
        #Thong so game
        self.gamerunning = True
        self.gravity = 0.15
        self.Move = 0
        self.Clock = pygame.time.Clock()
        self.Floor_x_Pos = 0
        self.Col_x_pos = 0
        self.Col_y_pos = 100
        #Thong so Floor
        self.Floor = pygame.image.load('./Data/Floor.png').convert()
        #Thong so bird
        self.BirdImg = pygame.image.load('./Data/yellowbird-midflap.png').convert()
        self.Bird = pygame.transform.scale(self.BirdImg, (50,50))
        self.Bird_x_Pos, self.Bird_y_Pos = 40, self.yScreen/2
        #Thong so Column
        self.Col_Img = pygame.image.load('./Data/tube2.png').convert()
        
    def Bird_Move(self):
        self.Move += 0.5 * self.gravity
        self.bird_rect.centery += self.Move
        self.screen.blit(self.Bird, self.bird_rect)

    def Draw_Column(self, pos):
        self.screen.blit(self.Col_Img, pos)

    def Draw_Floor(self):
        self.screen.blit(self.Floor,(self.Floor_x_Pos,450))
        self.screen.blit(self.Floor,(self.Floor_x_Pos+self.xScreen,450))

    def run(self):
        self.bird_rect = self.Bird.get_rect(center = (50,self.yScreen/2))
        while self.gamerunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamerunning = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.Move = 0
                        self.Move -= 4

            self.screen.blit(self.background,(0,0))
            self.Bird_Move()
            #Ve Column
            self.Col_x_pos -= 2
            
            if self.Col_x_pos <= -self.xScreen-52:
                self.Col_y_pos = random.randrange(50,300,25)
                self.Col_x_pos = 0
            self.Col_Pos = (336+self.Col_x_pos, 150 + self.Col_y_pos)
            self.Draw_Column(self.Col_Pos)
            # Ve ground
            self.Floor_x_Pos -= 2
            self.Draw_Floor()
            if self.Floor_x_Pos <= -self.xScreen:
                self.Floor_x_Pos = 0
            #pygame.display.flip()
            pygame.display.update()
            self.Clock.tick(120)

        pygame.quit()

if __name__ == '__main__':
    bird = Bird()
    bird.run()