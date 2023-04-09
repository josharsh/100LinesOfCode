#include <iostream>
#include <vector>

using namespace std;

const int ROWS = 6, COLS = 7;
vector<vector<char>> board(ROWS, vector<char>(COLS, '-'));

void draw_board() {
    for (auto& row : board) {
        for (char cell : row) cout << cell << ' ';
        cout << '\n';
    }
    cout << "1 2 3 4 5 6 7\n";
}

bool is_valid_move(int col) {
    return board[0][col] == '-';
}

bool make_move(int col, char player) {
    if (!is_valid_move(col)) return false;
    for (int row = ROWS - 1; row >= 0; --row) {
        if (board[row][col] == '-') {
            board[row][col] = player;
            return true;
        }
    }
    return false;
}

bool check_win(char player) {
    for (int row = 0; row < ROWS; ++row) {
        for (int col = 0; col < COLS; ++col) {
            if (board[row][col] != player) continue;
            for (int dr = -1; dr <= 1; ++dr) {
                for (int dc = -1; dc <= 1; ++dc) {
                    if (dr == 0 && dc == 0) continue;
                    bool win = true;
                    for (int i = 1; i < 4; ++i) {
                        int r = row + i * dr, c = col + i * dc;
                        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] != player) {
                            win = false;
                            break;
                        }
                    }
                    if (win) return true;
                }
            }
        }
    }
    return false;
}

int main() {
    draw_board();
    int move_count = 0;
    while (true) {
        int col;
        char player = move_count % 2 == 0 ? 'X' : 'O';
        cout << "Player " << player << ", enter column (1-7): ";
        cin >> col;
        if (col < 1 || col > 7) {
            cout << "Invalid column. Try again.\n";
            continue;
        }
        if (make_move(col - 1, player)) {
            ++move_count;
            draw_board();
            if (check_win(player)) {
                cout << "Player " << player << " wins!\n";
                break;
            }
            if (move_count == ROWS * COLS) {
                cout << "It's a draw!\n";
                break;
            }
        } else {
            cout << "Column full. Try again.\n";
        }
    }
    return 0;
}