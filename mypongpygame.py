import pygame

pygame.init()

# Making new window 
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2021.05.21")

# Defining colors used in the game 

white = (255, 255, 255)
red = (255, 100, 0)
orange = (255, 100, 0)
yellow = (255,255,0)
black = (0, 0, 0)

score = 0
lives = 2

#Creating Paddle
paddle_1 = pygame.image.load("assets/paddle.png")
paddle_1_y = 560

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# Variable for the following while loop
keepplaying = True

# Controling game's fps
fps = pygame.time.Clock()

while keepplaying:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepplaying = False

    screen.fill(black)
    pygame.draw.line(screen, white, [0, 38],
                    [800, 38], 2)

    #Score and Number of lives at the bottom of screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # ball collision with upper wall
    if ball_y > 590:
        ball_dy *= -1

    # ball collision with upper wall
    if ball_y > 590:
        ball_dy *= -1
    
    # ball collision with upper wall
    if ball_y > 590:
        ball_dy *= -1


    screen.blit(paddle_1, (325, paddle_1_y))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.flip()
    
    fps.tick(60)

pygame.quit()







