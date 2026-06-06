import keyboard, time, random, os

class Color:
    red, green, normal = '\033[31m', '\033[32m', '\033[0m'


class Snake:
    def __init__(self):
        self.x, self.y = random.randint(0, MAP_X_SIZE-1), random.randint(0, MAP_Y_SIZE-1)
        self.direction = None
        self.length = [(self.x, self.y)]

        self.key_map = { 'a': 'Left', 'd': 'Right', 'w': 'Up', 's': 'Down' }
        self.direction_map = { 'Left': (-1, 0), 'Right': (1, 0), 'Up': (0, -1), 'Down': (0, 1), None: (0, 0) }
        self.opposite = { 'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
    

    def new_direction(self, key):
        if (key in self.key_map) and (self.direction != self.opposite[self.key_map[key]]):
            self.direction = self.key_map[key]


    def move(self):
        dx, dy = self.direction_map[self.direction]
        self.length.append((self.x + dx, self.y + dy))

        self.x, self.y = self.length[-1]
        self.length.pop(0)


        if self.length[-1] in self.length[:-1]:
            print('Game Over!')
            exit()

        if (self.x < 0) or (self.x > MAP_X_SIZE-1) or (self.y < 0) or (self.y > MAP_Y_SIZE-1):
            print('Game Over!')
            exit()


class Apple:
    def place(self):
        while True:
            self.x, self.y = random.randint(0, MAP_X_SIZE-1), random.randint(0, MAP_Y_SIZE-1)

            if not (self.x, self.y) in snake.length: return


class Renderer:
    def __init__(self):
        self.score = 0


    def render(self):
        if (snake.x, snake.y) == (apple.x, apple.y):
            self.score += 1
            apple.place()
            snake.length.insert(0, 'SNAKE_GROWTH')
        snake.move()

        os.system('clear' if os.name == 'posix' else 'cls')     # Clears for the next render

        print('╔' + ('═' * MAP_X_SIZE * 2) + '╗')

        for y in range(MAP_Y_SIZE):
            row = '║'

            for x in range(MAP_X_SIZE):
                if (x, y) in snake.length:          row += f'{Color.green}[]{Color.normal}'
                elif (x, y) == (apple.x, apple.y):  row += f'{Color.red}(){Color.normal}'
                else:                               row += ' .'

            row += '║'
            print(row)
        
        print('╚' + ('═' * MAP_X_SIZE * 2) + '╝')
        print(f'Score: {self.score}')

        if self.score >= ((MAP_X_SIZE * MAP_Y_SIZE) - 1):
            print('You Win!')
            exit()


MAP_X_SIZE = MAP_Y_SIZE = 10

snake = Snake()
apple = Apple()
map = Renderer()

if __name__ == '__main__':
    apple.place()
    keyboard.on_press(lambda key_input: snake.new_direction(key_input.name))    # This always checks for input, even if it's not in a loop
    
    while True:
        map.render()
        time.sleep(0.15)