import pygame

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 500,680
        linkBackground = './Data/Background.jpg'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))

        pygame.display.set_caption('Flappy bird!')
        self.background = pygame.image.load(linkBackground)
        linkIcon = pygame.image.load('./Data/Bird.png')
        pygame.display.set_icon(linkIcon)
        self.gamerunning = True

        self.Floor = pygame.image.load('./Data/Floor3.png')
        
        

    def run(self):
        while self.gamerunning:
            for event in pygame.event.get():
                self.screen.blit(self.background,(0,-500))
                self.screen.blit(self.Floor,(0,500))
                if event.type == pygame.QUIT:
                    self.gamerunning = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(1)

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    bird = Bird()
    bird.run()