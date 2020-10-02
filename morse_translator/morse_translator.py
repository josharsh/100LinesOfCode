# python program to implement Morse code translator

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
# message encryption function
def encrypt(message):
    code = ''
    for letter in message:
        if letter != ' ':
            code += MORSE_CODE_DICT[letter] + ' '
        else:
            code += ' ' 
    return code

# message decryption function
def decrypt(code):
    code = code.strip()
    code+= ' '
    decipher = ''
    morse_word = ''
    for letter in code:
        # print("Letter is", letter)
        if letter!=' ':
            i = 0;
            morse_word += letter
        else:
            i+=1
            
            if i==2:
                decipher+=' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_word)] 
                morse_word = ''
    return decipher

if __name__ == "__main__":
    c = 0
    while c>=0:
        print("Choose:\n1.Encrypt\t2.Decrypt\t3.Exit")
        c = int(input())
        if c==1:    
            s = input("Enter your message\n")
            res = encrypt(s.upper())
            print("Encrypted message is:\n",res)
        elif c==2:
            s = input("Enter your message\n")
            res = decrypt(s)
            print("decrypted message is:\n",res)
        elif c==3:
            break
        else:
            print("Invalid choice")        
    
