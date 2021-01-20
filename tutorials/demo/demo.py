import sys, pygame

pygame.init()
fpsClock = pygame.time.Clock()

size = width, height = 800, 600
speed = [5,5]
background = pygame.Color(100, 149, 237)

screen = pygame.display.set_mode(size)
sprites01 = pygame.image.load("sprite-01.jpg")
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(ball, ballrect)
    screen.blit(sprites01, (0, 0), (32, 0, 32, 32))

    pygame.display.flip()
    fpsClock.tick(120)
