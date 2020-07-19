#include <iostream>
#include <cstdlib>
#include <time.h>
#include <iomanip>

int main() {
    std::srand(time(nullptr));
    int instructions;
    int bits;
    std::cout << "How many bits each instruction should have?" << std::endl;
    std::cin >> bits;
    std::cout << "How many instruction you want to generate per line?" << std::endl;
    std::cin >> instructions;
    for (int i = 0; i < 100; ++i) {
        for (int k = 0; k < instructions; ++k) {
            for (int j = 0; j < bits; ++j) {
                std::cout << rand() % 2;
            }
            std::cout << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "I hope it doesn't have any bugs!";
}
