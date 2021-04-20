def is_int(v):
    try:
        int(v)
        return True

    except ValueError:
        return False

def caesar_encrypt(realText, step):
    output = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = ord(eachLetter) - 65
            caesar_int = (index + step) % 26
            newLetter = uppercase[caesar_int]
            output.append(newLetter)

        elif eachLetter in lowercase:
            index = ord(eachLetter) - 97
            caesar_int = (index + step) % 26
            newLetter = lowercase[caesar_int]
            output.append(newLetter)

        elif is_int(eachLetter):
            temp_int = int(eachLetter) + step
            if temp_int > 9:
                while temp_int > 9:
                    temp_int -= 10
            elif temp_int < 0:
                while temp_int < 0:
                    temp_int += 10
            output.append(str(temp_int))

        elif eachLetter not in uppercase or eachLetter not in lowercase:
            output.append(eachLetter)
    return output


try:
    message = input('Enter the message you want to encrypt: ')
    shift = int(input('Enter the amount you want to shift by: '))
    code = caesar_encrypt(message, shift)
    print(''.join(code))

except ValueError:
    print('Something went wrong, try again with proper values or just numbers (no units)')
