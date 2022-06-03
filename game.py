import pygame, sys
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("아마도 게임")
clock = pygame.time.Clock()

class character:
    def __init__(self):
        self.x = 50
        self.y = 50

    def draw(self):
        pygame.draw.rect(window, (255,0,0,), [self.x, self.y,20,20])
        
choco = character()

while True:
    window.fill((255,255,255))
    
    choco.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                choco.y -= 5
            if event.key == pygame.K_a:
                choco.x -= 5
            if event.key == pygame.K_s:
                choco.y += 5
            if event.key == pygame.K_d:
                choco.x += 5

    pygame.display.update()
    clock.tick(30)