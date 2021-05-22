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
paddle = pygame.image.load("assets/paddle.png")
paddle_y = 560
paddle_x = 325
paddle_right = False
paddle_left = False

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = -5

# Variable for the following while loop
game_loop = True
fps = pygame.time.Clock()

while game_loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        
        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle_right = True
            if event.key == pygame.K_LEFT:
                paddle_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle_right = False
            if event.key == pygame.K_LEFT:
                paddle_left = False
        

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

    # paddle right movement
    if paddle_right:
        paddle_x += 5
    else:
        paddle_x += 0

    # paddle 1 left movement
    if paddle_left:
        paddle_x -= 5
    else:
        paddle_x += 0

    # ball collision with upper wall
    if ball_y <= 40:
        ball_dy *= -1

    # ball collision with floor
    if ball_y >= 590:
        ball_dy *= -1
    
    # ball collision with left wall
    if ball_x <= 0:
        ball_dx *= -1
    
    # ball collision with right wall
    if ball_x >= 790:
        ball_dx *= -1

    # ball collision with the player 1 's paddle
    if ball_y >= 545 :
        if paddle_x + 85 < ball_x or paddle_x - 85 > ball_x:
            ball_dy *= -1


    screen.blit(paddle, (paddle_x, paddle_y))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.flip()
    
    fps.tick(60)

pygame.quit()
