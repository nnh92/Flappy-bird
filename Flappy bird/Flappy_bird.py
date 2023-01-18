import pygame

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 400,600
        linkBackground = './Data/Background.jpg'
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))

        pygame.display.set_caption('Flappy bird!')
        self.background = pygame.image.load(linkBackground)
        

        self.gamerunning = True
        
        

    def run(self):
        while self.gamerunning:
            for event in pygame.event.get():
                self.screen.blit(self.background,(0,-500))
                if event.type == pygame.QUIT:
                    self.gamerunning = False

                

            pygame.display.flip()
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    bird = Bird()
    bird.run()