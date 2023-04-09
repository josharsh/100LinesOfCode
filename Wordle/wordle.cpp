#include <iostream>
#include <fstream>
#include <string>
#include <random>

using namespace std;

string getWord(ifstream& wordFile) {
    int lines = 0; string line;
    while(wordFile >> line) lines++;

    random_device rd; mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, lines);
    int rand_line = dis(gen);

    wordFile.clear(); wordFile.seekg(0, ios::beg);
    int curr_line = 0; string word;
    while (wordFile >> word) {
        curr_line++;
        if (curr_line == rand_line) break;
    }
    return word;
}

struct myStruct {
    string letter;
    int state;
};

void printBoard(myStruct board[6][5]) {
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 5; j++) {
            if (board[i][j].state == 0) cout << "\033[37m";
            else if (board[i][j].state == 1) cout << "\033[33m";
            else cout << "\033[32m";
            cout << board[i][j].letter;
        }
        cout << "\n";
    }
    cout << "\033[0m";
}

bool validInput(string input, ifstream& wordFile) {
    wordFile.clear(); wordFile.seekg(0, ios::beg);
    string word;
    while(wordFile >> word) {
        if (input == word) return true;
    }
    return false;
}

void processInput(string input, string word, myStruct board[6][5], int attempt) {
    for (int i = 0; i < 5; i++) {
        board[attempt][i].letter = input[i];
    }

    for (int i = 0; i < 5; i++) {
        if(word.find(input[i]) != string::npos) {
            if (input[i] == word[i]) {
                board[attempt][i].state = 2;
            } else {
                board[attempt][i].state = 1;
            }
        }
    }
}

int main() {
    ifstream wordFile("words.txt");
    string word = getWord(wordFile);
    
    myStruct board[6][5];
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 5; j++) {
            board[i][j].letter = "\u25A1";
            board[i][j].state = 0;
        }
    }

    for (int attempt = 0; attempt < 6; attempt++) {
        printBoard(board);
        string input; cin >> input;
        while(!validInput(input, wordFile)) {
            cout << "Word not in list, try again\n";
            cin >> input;
        } cout << '\n';
        processInput(input, word, board, attempt);
        if (input == word) {
            printBoard(board);
            cout << "You guessed the word in " << attempt + 1 << " attempt(s).\n Congratulations!\n";
            return 0;
        }
    }
    
    printBoard(board);
    cout << "You've run out of attempts.\n The word was: " << word << endl;

    return 0;
}