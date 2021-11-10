#include "compute.hpp"

void evaluate_speed()
{
	std::string content = "Type this and see if you do it fast enough. We consider all input including space and special character, even 12345 numbers are evaluated. If you are able to type all of this fast enough. Kudos! to you.";
	std::cout << content << std::endl;
	int counter = 0;
	int correct_chars = 0;
	char input_char;
	std::cout << std::fixed << std::setprecision(9) << std::left;
	std::chrono::time_point start_time = std::chrono::high_resolution_clock::now();
	do
	{
		input_char = getchar();
		if(input_char == content[counter])
		{
			correct_chars++;
		}
		counter++;
		
	}while((input_char != '\n') &&  counter < content.length()); 
	std::chrono::duration<double> time_taken = std::chrono::high_resolution_clock::now() - start_time ;

	std::cout << "You got " << correct_chars << " characters correct out of " << counter << " characters\n";
	std::cout << "You took " << time_taken.count() << " seconds\n";
	std::cout << "Your rate of typing (correct input/time taken) is " << correct_chars/time_taken.count() << std::endl;
}
int main(int argc, char** argv)
{
	std::cout << "********Typing Speed Calculator*********\n";
	std::cout << "Hit Enter to get content to type and type it to calculate your speed\n";
	if(std::cin.get() == '\n')
	{
		evaluate_speed();
	}
	else
	{
		std::cout << "Exiting....\n";
	}
	return 0;
}
