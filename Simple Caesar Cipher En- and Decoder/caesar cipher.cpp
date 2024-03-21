#include <iostream>
#include <fstream>
#include <string>
char cr (char in, int i, int mode) {
    char ch {static_cast<char>((in))};
    if (in >= 65 && in <= 90 && mode == 1) {
        ch = static_cast<char>((in+i));
        if (ch > 90) ch = static_cast<char>(ch -=26); return ch;
    } else if (in >= 97 && in <= 122 && mode == 1) {
        if (in+i > 122) i-=26;
        ch = static_cast<char>((in+i)); 
        if (ch > 122) ch =  static_cast<char>(ch -=26); return ch;
    } else if (in >= 65 && in <= 90 && mode == 2) {
        ch = static_cast<char>((in-i));
        if (ch < 65) ch =  static_cast<char>(ch +=26); return ch;
    } else if (in >= 97 && in <= 122 && mode == 2) {
        ch = static_cast<char>((in-i));
        if (ch < 97) ch =static_cast<char>(ch +=26); return ch;
    } else {
        return in;
    }
}
void cc (std::string input, bool mode, int i, int c) {
    std::ofstream write_here("cc.txt");
    std::string line {}, bcc {};
    if (mode) {
        input+=".txt";
        std::ifstream read_this(input);
        while (getline(read_this, line)) {
            for (const auto& elem : line) {
                write_here << cr(elem, i, c);
            }
        } 
        read_this.close();
    }
    else {
        for (const auto& elem : input) {
            write_here << cr(elem, i, c);
        }
    }
    write_here.close(); 
    std::cout << "The Text has been ";
    c == 1 ?  std::cout << "encoded into the cc.txt file.\n" : std::cout << "decoded into the cc.txt file.\n";
}
int main() {
    std::string text {}, i1 {}, i2 {};
    int i {0}, c {0}, ch {0};
    std::cout << "---Caesar's Cypher Program---" << std::endl << "--Encode & Decode messages easily--" << std::endl << std::endl << "Select the shift-modifier (1-25): ", getline(std::cin, i1);;
    while (i == 0) {
        try {
            if (stoi(i1) > 0 && stoi(i1) < 26) {
                i = stoi(i1); 
            }
            else {
                std::cout << "Please enter a valid shift-modifier (Number between 1 and 25 (inclusive)): ", getline(std::cin, i1);
            }
        }
        catch (...) {
            i1 = "";
            std::cin.clear();
            std::cout << "Please enter a valid shift-modifier (Number between 1 and 25 (inclusive)): ", getline(std::cin, i1);
        }
    }
    std::cout << "Do you want to [1]encode or [2]decode the text?: ", getline(std::cin, i2);
      while (c == 0) {
        if (i2 == "1") {
            c = 1;
        }
        else if (i2 == "2") {
            c = 2;
        }
        else {
            std::cin.clear();
            std::cout << "Please choose one of the two. Type 1 to [encode] or type 2 to [decode]: ", getline(std::cin, i2);
        }
    }
    std::cout << "Do you want to [1]read in from a .txt file or [2]type the text yourself: ", getline(std::cin, i2);
      while (ch == 0) {
        if (i2 == "1") {
            ch = 1;
        }
        else if (i2 == "2") {
            ch = 2;
        }
        else {
            std::cin.clear();
            std::cout << "Please choose one of the two. Type 1 to [type the text yourself] or type 2 to [read in from a .txt file]: ", getline(std::cin, i2);
        }
    }
    if (ch == 2) {
        std::cout << "Enter your text:\n", getline(std::cin, text);
        cc(text, false, i, c);
    }
    else {
        std::cout << "Enter the filename without the extension (has to be a txt file):\n", getline(std::cin, text);
        cc(text, true, i, c);
    }
    return 0;
}
