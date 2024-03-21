import cv2
import numpy as np

class TicTacToe:
    def __init__(self):
        self.window_size = (600, 600)
        self.grid_size = 3
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player = 'O'
        self.winner_flag = 0
        self.check_flag = self.grid_size**2

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.img = np.zeros((self.window_size[0], self.window_size[1], 3), np.uint8)

        self.draw_grid()

    def draw_grid(self):
        for i in range(1, self.grid_size):
            thickness = 5
            cv2.line(self.img, (i * (self.window_size[0] // self.grid_size), 0),
                     (i * (self.window_size[0] // self.grid_size), self.window_size[1]), (0, 255, 0), thickness)
            cv2.line(self.img, (0, i * (self.window_size[1] // self.grid_size)),
                     (self.window_size[0], i * (self.window_size[1] // self.grid_size)), (0, 255, 0), thickness)

    def switch_player(self):
        self.player = 'X' if self.player == 'O' else 'O'

    def put_game(self, row, col):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = self.player
            self.draw_mark(row, col)
            self.check_win()
            self.check_draw()
            self.switch_player()

    def draw_mark(self, row, col):
        x, y = col * (self.window_size[0] // self.grid_size), row * (self.window_size[1] // self.grid_size)
        x, y = self.getxy(x, y)
        cv2.putText(self.img, self.player, (x, y), self.font, 9, (255, 0, 0), 3)

    def getxy(self, x, y):
        x = (x // (self.window_size[0] // self.grid_size)) * (self.window_size[0] // self.grid_size)
        y = (y // (self.window_size[1] // self.grid_size)) * (self.window_size[1] // self.grid_size)
        return x, y

    def check_win(self):
        for i in range(self.grid_size):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == self.player:
                self.winner_flag = 1
                return
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == self.player:
                self.winner_flag = 1
                return
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == self.player:
            self.winner_flag = 1
            return
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == self.player:
            self.winner_flag = 1

    def check_draw(self):
        self.check_flag = sum(1 for row in self.grid for cell in row if cell == ' ')
        if self.check_flag == 0:
            self.winner_flag = 2

    def place(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            col, row = x // (self.window_size[0] // self.grid_size), y // (self.window_size[1] // self.grid_size)
            self.put_game(row, col)
            if self.winner_flag == 1:
                print(f"{self.player} WINS!\n\n")
            elif self.check_flag == 0:
                print("Game is a draw.")

    def run(self):
        cv2.namedWindow("Tic-Tac-Toe", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("Tic-Tac-Toe", self.place)

        while True:
            cv2.imshow("Tic-Tac-Toe", self.img)
            key = cv2.waitKey(1)
            if key == 27 or self.winner_flag == 1 or self.check_flag == 0:
                break

        cv2.destroyWindow("Tic-Tac-Toe")

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
