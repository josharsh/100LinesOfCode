#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int fromBaseAtoDecimal(const string& number, int b1) {
    int result = 0;
    int power = 1;

    for (int i = number.size() - 1; i >= 0; --i) {
        int digit = number[i] >= 'A' ? (number[i] - 'A' + 10) : (number[i] - '0');
        result += digit * power;
        power *= b1;
    }

    return result;
}

string fromDecimalToBaseB(int decimal, int b2) {
    string result;

    while (decimal > 0) {
        int r = decimal % b2;
        char digit = r >= 10 ? (r - 10 + 'A') : (r + '0');
        result.push_back(digit);
        decimal /= b2;
    }

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    int base1, base2;
    string num;

    cout << "Enter the source base (2-36): ";
    cin >> base1;
    cout << "Enter the target base (2-36): ";
    cin >> base2;
    cout << "Enter the number in source base: ";
    cin >> num;

    int decimal = fromBaseAtoDecimal(num, base1);
    string res = fromDecimalToBaseB(decimal, base2);

    cout << "The number " << num << " in base " << base1 << " is " << res << " in base " << base2 << "." << endl;
}