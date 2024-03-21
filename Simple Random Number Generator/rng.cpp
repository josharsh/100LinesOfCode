#include <iostream>
#include <string>

int main() {
	std::cout << "Please enter the lower limit (inclusive): ";
	size_t in1 {0}, in2 {0}, in3 {0}, x {1};
	std::cin >> in1;
	
	std::cout << "Please enter the upper limit (inclusive): ";
	std::cin >> in2;
	std::cout << "How many times would you like to roll?: ";
	std::cin >> in3;

	x = in3;
	std::string s {" times"};
	if (x == 1) {
		s = " time";
	}
	
	srand((unsigned) time(NULL));
	if (in1 > in2) {size_t h = in1; in1 = in2; in2 = h;}
	std::cout << std::endl << "Rolling between " << in1 << " and " << in2 << " for " << x << s << ":" << std::endl;
	size_t range = in2-in1+1;
	
	for (int i {0}; i < x; ++i) {
	std::cout << "(" << i+1 << ") " << in1 + (rand() % range) << std::endl;
	}
	
	return 0;
}
