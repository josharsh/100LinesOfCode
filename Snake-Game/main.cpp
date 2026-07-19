#include <iostream>
#include <vector>
#include <thread>
#include <atomic>
#include <algorithm>
#include <cstdlib>

constexpr int W = 20, H = 10;
enum Direction { LEFT, RIGHT, TOP, BOTTOM };
struct Point {
    int x;
    int y;
};
std::vector<Point> snake; 
std::atomic<Direction> dir(RIGHT);
bool game_over = false;

void input_listener() {
    while(!game_over) {
        char c;
        std::cin >> c; 
        c = tolower(c);

        // prevent 180 deg movement -> snake eating itself lol
        if(c == 'q') game_over = true; // exit
        if(c == 'w' && dir != BOTTOM) dir = TOP;
        if(c == 's' && dir != TOP) dir = BOTTOM;
        if(c == 'a' && dir != RIGHT) dir = LEFT;
        if(c == 'd' && dir != LEFT) dir = RIGHT;
    }
}

Point generate_fruit() {
    int fx, fy;
    do {
        fx = rand() % W;
        fy = rand() % H;
    } while (std::any_of(snake.begin(), snake.end(), [fx, fy](const Point& p) {
        return p.x == fx && p.y == fy;
    }));

    Point fruit = {fx, fy};
    return fruit;
}

int main() {
    snake = {{W/2, H/2}, {W/2-1, H/2}, {W/2-2, H/2}};

    std::thread input_thread(input_listener);
    Point fruit = generate_fruit();

    // game loop
    while(!game_over) {
        Point new_head = snake.front();
        if(dir == TOP) { new_head.y--; }
        if(dir == BOTTOM) { new_head.y++; }
        if(dir == RIGHT) { new_head.x++; }
        if(dir == LEFT) { new_head.x--; }

        // clip through walls
        if(new_head.x < 0) { new_head.x = W - 1; }
        if(new_head.x >= W) { new_head.x = 0; }
        if(new_head.y < 0) { new_head.y = H - 1; }
        if(new_head.y >= H) { new_head.y = 0; }

        // eating itself
        for (const auto& s : snake) if (s.x == new_head.x && s.y == new_head.y) game_over = true;

        // create head for moving effect
        snake.insert(snake.begin(), new_head);

        if (new_head.x == fruit.x && new_head.y == fruit.y) { fruit = generate_fruit(); } 
        else { snake.pop_back(); }

        system("cls");
        std::string frame = "";

        // rendering
        for(int i = 0; i < H; i++) {
            for(int j = 0; j < W; j++) {
                if(snake.front().x == j && snake.front().y == i) { frame += "O"; }
                else if(std::any_of(snake.begin(), snake.end(), [i, j](const Point& p) { return p.x == j && p.y == i; })) { frame += "o"; }
                else if(fruit.x == j && fruit.y == i) { frame += "X"; }
                else { frame += "."; }
            }
            frame += "\n";
        }
        std::cout << frame << std::flush;

        // 10 fps
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    input_thread.join();
    std::cout << "Game Over!\n";

    return 0;
}