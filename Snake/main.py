import keyboard, time, random, os, threading

class Color: red, green, normal = '\033[31m', '\033[32m', '\033[0m'

class Snake:
    def __init__(self, x_pos, y_pos):
        self.x, self.y = x_pos, y_pos
        self.direction = None
        self.length = [(self.x, self.y)]
    
    def new_direction(self, key):
        if key == 'a' and self.direction != 'R': self.direction = 'L'
        elif key == 'd' and self.direction != 'L': self.direction = 'R'
        elif key == 'w' and self.direction != 'D': self.direction = 'U'
        elif key == 's' and self.direction != 'U': self.direction = 'D'
    
    def move(self):
        if self.direction == 'L': self.length.append((self.x-1, self.y))
        elif self.direction == 'R': self.length.append((self.x+1, self.y))
        elif self.direction == 'U': self.length.append((self.x, self.y-1))
        elif self.direction == 'D': self.length.append((self.x, self.y+1))
        elif self.direction == None: self.length.append((self.x, self.y))

        self.x, self.y = self.length[-1][0], self.length[-1][1]
        self.length.pop(0)

        if self.length[-1] in self.length[:-1]: print('Game Over!'), exit()
        if (self.x < 0) or (self.x > MAP_X_SIZE-1) or (self.y < 0) or (self.y > MAP_Y_SIZE-1): print('Game Over!'), exit()

class Apple:
    def __init__(self, x_pos, y_pos):
        self.x, self.y = x_pos, y_pos

        while (self.x, self.y) in snake.length:
            self.x = random.randint(0, MAP_X_SIZE-1)
            self.y = random.randint(0, MAP_Y_SIZE-1)
    
    def eaten(self):
        self.x = random.randint(0, MAP_X_SIZE-1)
        self.y = random.randint(0, MAP_Y_SIZE-1)

        while (self.x, self.y) in snake.length:
            self.x = random.randint(0, MAP_X_SIZE-1)
            self.y = random.randint(0, MAP_Y_SIZE-1)

class Renderer:
    def __init__(self):
        self.score = 0
    
    def render(self):
        if (snake.x == apple.x) and (snake.y == apple.y):
            self.score += 1
            apple.eaten()
            snake.length.insert(0, snake.length[0])
        snake.move()

        os.system('clear' if os.name == 'posix' else 'cls')

        print('╔' + '═'*(MAP_X_SIZE*2) + '╗')

        for y in range(MAP_Y_SIZE):
            row = ''
            row += '║'

            for x in range(MAP_X_SIZE):
                if (x,y) in snake.length: row += Color.green + '[]' + Color.normal
                elif (x == apple.x) and (y == apple.y): row += Color.red + '()' + Color.normal
                else: row += ' .'

            row += '║'
            print(row)
        
        print('╚' + '═'*MAP_X_SIZE*2 + '╝')
        print(f'Score: {self.score}')

        if self.score >= ((MAP_X_SIZE * MAP_Y_SIZE) - 1): print('You Win!'), exit()

MAP_X_SIZE = MAP_Y_SIZE = 10

snake = Snake(random.randint(0, MAP_X_SIZE-1), random.randint(0, MAP_Y_SIZE-1))
apple = Apple(random.randint(0, MAP_X_SIZE-1), random.randint(0, MAP_Y_SIZE-1))
map = Renderer()

def keyboard_handler():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN: snake.new_direction(event.name)

def map_renderer():
    while True:
        map.render()
        time.sleep(0.15)

threading.Thread(target=keyboard_handler, daemon=True).start()
map_renderer()