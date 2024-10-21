import pygame

pygame.init()
clock = pygame.time.Clock()

#color
RED = (255,0,0); GREEN = (0,255,0)
BLUE = (0,0,255); WHITE = (255,255,255)
BLACK = (0,0,0)
#screen
SCR_WIDTH, SCR_HEIGHT = 800,600

#snake
SNAKE_SIZE = 20
snake_pos_x  = SCR_WIDTH/2 - SNAKE_SIZE/2
snake_pos_y  = SCR_HEIGHT/2 - SNAKE_SIZE/2
snake_posx_change = 0
snake_posy_change = 0

screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("Snake Game ver 1.0")


running = True
while running:
    for event in pygame.event.get() :
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_posx_change = 0
                snake_posy_change = -10
            if event.key == pygame.K_DOWN:
                snake_posx_change = 0
                snake_posy_change = 10
            if event.key == pygame.K_LEFT:
                snake_posx_change = -10
                snake_posy_change = 0
            if event.key == pygame.K_RIGHT:
                snake_posx_change = 10
                snake_posy_change = 0
                
    snake_pos_x += snake_posx_change
    snake_pos_y += snake_posy_change
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [snake_pos_x,
                            snake_pos_y,
                            SNAKE_SIZE,
                            SNAKE_SIZE])
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
