import pygame
from pygame.locals import *
import funcions
from funcions import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inicialização o pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.flip()
pygame.display.set_caption("Snake")

# Criação da cobra
#          x    y      x    y      x    y
snake = [(200, 200)]
snake_skin = pygame.Surface((15,15))
snake_skin.fill((255,255,255)) #Branco

# Criação da maça
apple_pos = gridRandom()
apple = pygame.Surface((15,15))
apple.fill((255,0,0)) # Full vermelho

clock = pygame.time.Clock()

my_direction = LEFT
my_direction = UP
my_direction = DOWN
my_direction = RIGHT


while True:
    clock.tick(20)
    # Isto são eventos que acontecem no game  
    for event in pygame.event.get():
        if event.type == QUIT:
            break

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT    
        
    if collision(snake[0], apple_pos):
        apple_pos = gridRandom()
        snake.append(snake[-1])
    
    if snake[0][0] == 700 or snake [0][1] == 700 or snake[0][0] < 0 or snake[0][1] < 0:
        text()
        clock.tick(1)
        pygame.quit()
        exit()

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            text()
            clock.tick(1)
            pygame.quit()
            exit()

    for i in range(len(snake)- 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i][1])        

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])     
    
    color = (0,50,0)
    screen.fill(color)
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()