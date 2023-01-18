import pygame

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
        self.gamerunning = True
        self.gravity = 2
        self.Move = 0

        self.Floor = pygame.image.load('./Data/Floor.png').convert()

        self.BirdImg = pygame.image.load('./Data/yellowbird-midflap.png').convert()
        self.Bird = pygame.transform.scale(self.BirdImg, (50,50))
        self.Bird_x_Pos, self.Bird_y_Pos = 40, self.yScreen/2
        
        self.Clock = pygame.time.Clock()
        self.Floor_x_Pos = 0

    def Bird_Move(self, Bird_rect):
        Bird_rect += self.Move
        self.screen.blit(self.Bird, (self.Bird_x_Pos, self.Bird_rect))


    def Draw_Floor(self):
        self.screen.blit(self.Floor,(self.Floor_x_Pos,450))
        self.screen.blit(self.Floor,(self.Floor_x_Pos+self.xScreen,450))

    def run(self):
        while self.gamerunning:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.gamerunning = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gravity = 0
                        self.gravity -= 10

            self.screen.blit(self.background,(0,0))

            # Ve Bird
            self.Move += self.gravity
            bird_rect = bird.get_rect(center = (100,300))
            self.Bird_Move(bird_rect)

            # Ve ground
            self.Floor_x_Pos -= 2
            self.Draw_Floor()
            if self.Floor_x_Pos <= -self.xScreen:
                self.Floor_x_Pos = 0
            
            pygame.display.flip()
            pygame.display.update()
            self.Clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    bird = Bird()
    bird.run()