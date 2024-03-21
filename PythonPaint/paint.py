import pygame

background = (255, 255, 255)
(screenWidth, screenHeight) = (800,600)

tool = 'pencil'
color = (0,0,0)

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('paint')
screen.fill(background)
pygame.display.flip()

def renderToolbar():
    # tool switcher buttons
    screen.blit(pygame.image.load('pencil.png'), (0,0))
    screen.blit(pygame.image.load('eraser.png'), (100,0))
    screen.blit(pygame.image.load('screenshot.png'), (200,0))

    # color changer buttons
    pygame.draw.rect(screen, (0, 0, 0), (300,0,100,20)) # black
    pygame.draw.rect(screen, (255, 0, 0), (400,0,100,20)) # red
    pygame.draw.rect(screen, (0, 255, 0), (500,0,100,20)) # green
    pygame.draw.rect(screen, (0, 0, 255), (600,0,100,20)) # blue
    pygame.draw.rect(screen, (255, 0, 255), (700,0,100,20)) # magenta

renderToolbar() # initial rendering

def drawLine(surface, color, start, end, radius):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = start[0] + i / distance * dx
        y = start[1] + i / distance * dy
        pygame.draw.circle(surface, color, (x, y), radius)
    renderToolbar()

running = True
drawing = False
radius = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

            # toolbar
            if (event.pos[0] < 100 and event.pos[1] < 20):
                tool = 'pencil'
            if (event.pos[0] < 200 and event.pos[0] > 100 and event.pos[1] < 20):
                tool = 'eraser'
            if (event.pos[0] < 300 and event.pos[0] > 200 and event.pos[1] < 20):
                rect = pygame.Rect(0, 20, screenWidth, screenHeight-20)
                pygame.image.save(screen.subsurface(rect), "your_art.jpeg")
            if (event.pos[0] < 400 and event.pos[0] > 300 and event.pos[1] < 20):
                color = (0,0,0)
            if (event.pos[0] < 500 and event.pos[0] > 400 and event.pos[1] < 20):
                color = (255,0,0)
            if (event.pos[0] < 600 and event.pos[0] > 500 and event.pos[1] < 20):
                color = (0,255,0)
            if (event.pos[0] < 700 and event.pos[0] > 600 and event.pos[1] < 20):
                color = (0,0,255)
            if (event.pos[0] > 700 and event.pos[1] < 20):
                color = (255,0,255)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == 'pencil':
                    pygame.draw.circle(screen, color, event.pos, radius)
                    drawLine(screen, color, lastPos, event.pos, radius)
                if tool == 'eraser':
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)
                    drawLine(screen, (255,255,255), lastPos, event.pos, radius)
            lastPos = event.pos
    pygame.display.flip()
