#include <iostream>
#include <cstdlib>
#include <time.h>
#include <iomanip>
using namespace std;

int main() {
    srand(time(nullptr));
    int instructions;
    int bits;
    cout << "How many bits each instruction should have?" << endl;
    cin >> bits;
    cout << "How many instruction you want to generate per line?" << endl;
    cin >> instructions;
    for (int i = 0; i < 100; ++i) {
        for (int k = 0; k < instructions; ++k) {
            for (int j = 0; j < bits; ++j) {
                cout << rand() % 2;
            }
            cout << " ";
        }
        cout << endl;
    }
    cout << "I hope it doesn't have any bugs!";
    return 0;
}
