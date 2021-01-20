import pygame, os, sys

pygame.init()
fpsClock = pygame.time.Clock()

size = width, height = (800,600)
localDir = os.path.dirname(__file__)
mainSurface = pygame.display.set_mode(size)
pygame.display.set_caption('Bricks')

black = pygame.Color(0, 0, 0)
brick = None

def create_bricks(pathToImage, rows, cols):
    global brick
    brick = pygame.image.load(pathToImage)
    bricks = []
    brickWidth = brick.get_width()
    brickHeight = brick.get_height()

    for y in range(rows):
        brickY = (y * brickHeight) + 100
        for x in range(cols):
            brickX = (x * brickWidth) + 245
            rect = pygame.Rect(brickX, brickY, brickWidth, brickHeight)
            bricks.append(rect)
    
    return bricks

# bat init

bat = pygame.image.load(os.path.join(localDir, 'bat.png'))

playerY = 540
batRect = bat.get_rect()

mousex, mousey = (0, playerY)

# ball init
ball = pygame.image.load(os.path.join(localDir, 'ball.png'))
ballRect = ball.get_rect()

ballStartY = 200
ballSpeed = 3
ballServed = False

bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)

# bricks init
bricks = create_bricks(os.path.join(localDir, 'brick.png'), 5, 10)

while True:
    mainSurface.fill(black)

    # brick draw
    for b in bricks:
        mainSurface.blit(brick, b)

    # bat and ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)
    # events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and not ballServed:
            ballServed = True
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < width - 55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (width - 55, playerY)
    # main game logic

    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx, by)

    if (by <= 0):
        by = 0
        sy = -sy
    if (by >= height - ballRect.height):
        ballServed = False
        bx, by = (24, ballStartY)
        ballSpeed = 3
        sx, sy = (ballSpeed, ballSpeed)
        ballRect.topleft = (bx, by)

    if (bx <= 0):
        bx = 0
        sx = -sx

    if (bx >= width - ballRect.width):
        bx = width - ballRect.width
        sx = -sx

    if ballRect.colliderect(batRect):
        by = playerY - ballRect.width
        sy *= 1.001
        sx *= 1.001
        sy = -sy

    # collision detection
    brickHitIndex = ballRect.collidelist(bricks)

    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]

        mx = bx + 4
        my = by + 4
        if mx > hb.x + hb.width or mx < hb.x:
            sx = -sx
        else:
            sy = -sy

        del(bricks[brickHitIndex])

    pygame.display.update()
    fpsClock.tick(30)