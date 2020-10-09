import base64
import binascii

message = input("Please enter the text you would like to encrypt or decrypt: ")
option = input("Please select the method you'd like to use: base64/morse/hex/caesar cipher: ")
while option == 'base64' or option == 'morse' or option == 'hex' or option == 'caesar cipher':
    if option == 'base64':
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print("Encrypted Message:" + base64_message)


    if option == 'morse':
        Morse_Dict = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}   
    def encryption(message):
            cipher = ' '
            for letter in message:
                if letter != ' ':
                    cipher += Morse_Dict[letter] + ' '
                else:
                    cipher += ' '
            print(cipher)
            encryption(message)
    if option == 'hex':
        print(message.encode("utf-8").hex())
    if option == 'caesar cipher':
        s = int(input("Please enter the shift number you'd like (Exmaple: 4): "))
        def encrypt(message,s):
            result = ""
            # transverse the plain text
            for i in range(len(message)):
                char = message[i]
                # Encrypt uppercase characters in plain text
                
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            print(result)
        encrypt(message, s)
    break

