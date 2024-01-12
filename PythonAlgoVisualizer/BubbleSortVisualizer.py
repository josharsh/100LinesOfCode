import pygame, sys, random

def Draw_rects(list_of_ints, state, RED, GREEN, WHITE,HEIGHT, window, width_of_bars):
    for i in range(len(list_of_ints)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN  
        else:
            color = WHITE
        pygame.draw.rect(window, color, pygame.Rect(int(i*width_of_bars), HEIGHT - list_of_ints[i], width_of_bars, list_of_ints[i]))

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# screen dimensions
WIDTH = 400
HEIGHT = 500
window_size = (WIDTH, HEIGHT)

# intializing pygame
pygame.init()

# initializing screen
window = pygame.display.set_mode(window_size)

# title 
pygame.display.set_caption('Bubble Sort Visualization')

clock = pygame.time.Clock()
clock.tick(40) # runs program at 40 frames per second

font=pygame.freetype.SysFont(None, 34)

width_of_bars = 1
range_of_bars = int(WIDTH/width_of_bars)

#initializing lists with random integers
list_of_ints = list(range(1,400)) # list of integers from 1 to 400
random.shuffle(list_of_ints) # shuffling integers
#intializing lists for keeping track of state of integers
state = [1] * len(list_of_ints)



# Bubble Sort Implementation
n = len(list_of_ints)
swap_made = False
counter = n
for i in range(n):
    counter -= 1
    for j in range(0, n-i-1):
        window.fill((10, 10, 10))
        state[j] = 0
        state[j+1] = 0
        if list_of_ints[j] > list_of_ints[j+1]:
            swap_made = True
            list_of_ints[j], list_of_ints[j+1] = list_of_ints[j+1], list_of_ints[j]

        ticks=pygame.time.get_ticks()
        seconds=round(float(ticks/1000), 3)
        time_str = f"{seconds}s"
        font.render_to(window, (34, 34), time_str, WHITE)

        Draw_rects(list_of_ints, state, RED, GREEN, WHITE, HEIGHT, window, width_of_bars)
        pygame.display.flip()
        state = [1] * n
        state[counter:] = [2 for x in state[counter:]]
        

    if swap_made is False:
        state = [2] * len(list_of_ints)
        break

Draw_rects(list_of_ints, state, RED, GREEN, WHITE, HEIGHT, window, width_of_bars)
pygame.display.flip()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
