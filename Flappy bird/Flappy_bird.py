import pygame
import random
import sys

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 336,550
        linkBackground = './Flappy bird/Flappy bird/Data/background_night.png'
        linkBackgroundEnd = './Flappy bird/Flappy bird/Data/Background2.png'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))

        pygame.display.set_caption('Flappy bird!')
        self.background = pygame.image.load(linkBackground).convert()
        self.background = pygame.transform.scale(self.background,(self.xScreen, self.yScreen))
        self.backgroundEnd = pygame.image.load(linkBackgroundEnd).convert()
        self.backgroundEnd = pygame.transform.scale(self.backgroundEnd,(self.xScreen, self.yScreen))
        linkIcon = pygame.image.load('./Flappy bird/Flappy bird/Data/Bird.png').convert()
        pygame.display.set_icon(linkIcon)
        #Thong so game
        self.gamerunning = True
        self.gravity = 0.15
        self.Move = 0
        self.Clock = pygame.time.Clock()
        self.Floor_x_Pos = 0
        self.Col_x_pos = 0
        self.Col_B_Height = 100
        self.distance = 150
        self.Col_Height = 500
        self.FPS = 60
        self.score = 0
        #Thong so Floor
        self.Floor = pygame.image.load('./Flappy bird/Flappy bird/Data/Floor.png').convert()
        self.Floor_Level = 500
        #Thong so bird
        self.Bird_Size = 50
        self.BirdImg = pygame.image.load('./Flappy bird/Flappy bird/Data/KL.png').convert()
        self.Bird = pygame.transform.scale(self.BirdImg, (self.Bird_Size,self.Bird_Size))
        self.Bird_x_Pos, self.Bird_y_Pos = 40, self.yScreen/2
        #Thong so Column
        self.Col_Img_Bot = pygame.image.load('./Flappy bird/Flappy bird/Data/tube2.png').convert()
        self.Col_Img_Bot = pygame.transform.scale(self.Col_Img_Bot, (45,self.Col_Height))
        self.Col_Img_Top = pygame.image.load('./Flappy bird/Flappy bird/Data/tube1.png').convert()
        self.Col_Img_Top = pygame.transform.scale(self.Col_Img_Top, (45,self.Col_Height))
    def Bird_Move(self):
        self.Move += 0.5 * self.gravity
        self.bird_rect.centery += self.Move
        self.screen.blit(self.Bird, self.bird_rect)

    def Draw_Floor(self):
        self.screen.blit(self.Floor,(self.Floor_x_Pos,self.Floor_Level))
        self.screen.blit(self.Floor,(self.Floor_x_Pos+self.xScreen,self.Floor_Level))

    def isGameOver(self, score):
        font = pygame.font.SysFont('consolas', 30)
        fontScore = pygame.font.SysFont('consolas', 20)
        headingSuface = font.render('GAMEOVER', True, (255,0,0))
        headingScore = fontScore.render('Score: ' + str(score), True, (255,255,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.backgroundEnd,(0,0))
            self.screen.blit(headingSuface, (100,200))
            self.screen.blit(headingScore, (100,250))
            pygame.display.update()

    def Score(self, score):
        font = pygame.font.SysFont('consolas', 20)
        headingSuface = font.render('Score: ' + str(score), True, (255,255,0))
        self.screen.blit(headingSuface, (50,50))

    def run(self):
        self.bird_rect = self.Bird.get_rect(center = (self.Bird_Size,self.yScreen/2))
        while self.gamerunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamerunning = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.Move = 0
                        self.Move -= 2.5
            if self.bird_rect.centery >= self.Floor_Level - self.Bird_Size/2 or self.bird_rect.centery < self.Bird_Size/2:
                self.isGameOver(self.score)
                
            self.screen.blit(self.background,(0,0))
            self.Bird_Move()
            #Ve Column
            self.Col_x_pos -= 2
            
            if self.Col_x_pos <= -self.xScreen-52:
                self.Col_B_Height = random.randrange(100,self.yScreen - self.distance - 50,25)
                self.Col_x_pos = 0
                self.score += 1
                if self.score % 10 == 0:
                    self.FPS += 5
            self.Col_Pos_B = (self.xScreen + self.Col_x_pos, self.yScreen - self.Col_B_Height)
            self.Col_Pos_T = (self.xScreen + self.Col_x_pos, self.yScreen - self.Col_B_Height - self.distance - self.Col_Height)
            self.screen.blit(self.Col_Img_Bot, self.Col_Pos_B)
            self.screen.blit(self.Col_Img_Top, self.Col_Pos_T)

            if self.bird_rect.centery + self.Bird_Size/2 > self.Col_Pos_B[1] and self.Bird_x_Pos + self.Bird_Size/2 >= self.Col_Pos_B[0]:
                self.isGameOver(self.score)
            if self.bird_rect.centery - self.Bird_Size/2 < self.Col_Pos_T[1] + self.Col_Height and self.Bird_x_Pos + self.Bird_Size/2 >= self.Col_Pos_T[0]:
                self.isGameOver(self.score)
            # Hien thi diem
            self.Score(self.score)
            # Ve ground
            self.Floor_x_Pos -= 2
            self.Draw_Floor()
            if self.Floor_x_Pos <= -self.xScreen:
                self.Floor_x_Pos = 0
            #pygame.display.flip()
            pygame.display.update()
            self.Clock.tick(self.FPS)

        pygame.quit()

if __name__ == '__main__':
    bird = Bird()
    bird.run()