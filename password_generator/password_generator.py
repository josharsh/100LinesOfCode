# @author Akash Kummar

import string
import random
import sys

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_random_password(self, min_length=8, max_length=16, fixed_length=8, lowercase=False, uppercase=False, digits=False, special_characters=False):
        """
        Method to generate a random password
        :param lowercase:
        :param min_length:
        :param max_length:
        :param fixed_length:
        :param uppercase:
        :param numbers:
        :param special_characters:
        :return:
        """

        try:
            string_size = random.randint(min_length, max_length)
            combination = ''
            if lowercase: combination += string.ascii_lowercase
            if uppercase: combination += string.ascii_uppercase
            if digits: combination += string.digits
            if special_characters: combination += string.punctuation

            # print(combination)

            # using random.choices()
            # generating random strings
            password = ''.join(random.choices(combination, k=string_size))

            return password

        except:
            return "Error: No options selected"


if __name__ == "__main__":
    print(PasswordGenerator().generate_random_password())