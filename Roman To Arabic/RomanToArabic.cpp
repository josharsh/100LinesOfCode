#include <iostream>

int romanCharToValue(char roman_char) {
  switch (roman_char) {
    case 'I': return 1;
    case 'V': return 5;
    case 'X': return 10;
    case 'L': return 50;
    case 'C': return 100;
    case 'D': return 500;
    case 'M': return 1000;
    default: return 0;
  }
}

bool isValidRomanNumeral(const std::string& roman_numeral) {
  if (roman_numeral.empty()) return false;
  for (char c : roman_numeral) {
    if (romanCharToValue(c) == 0) return false;
  }
  return true;
}

int romanToArabic(const std::string& roman_numeral) {
  if (!isValidRomanNumeral(roman_numeral)) {
    return -1;
  }

  int arabic_number = 0;
  int prev_value = 0;

  for (char c : roman_numeral) {
    int current_value = romanCharToValue(c);
    arabic_number += current_value;

    if (prev_value < current_value) {
      arabic_number -= 2 * prev_value;
    }

    prev_value = current_value;
  }

  return arabic_number;
}

int main() {
  std::string roman_numeral;
  std::cout << "Enter a Roman numeral: ";
  std::cin >> roman_numeral;

  int arabic_number = romanToArabic(roman_numeral);
  if (arabic_number == -1) {
    std::cerr << "Invalid Roman numeral" << std::endl;
    return 1;
  }

  std::cout << "The Arabic number is: " << arabic_number << std::endl;
  return 0;
}