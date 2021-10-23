import base64
import binascii

# ~~~~~~~~~~~~~~~~~~~~~~ Encryption ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
message = input("Please enter the text you would like to encrypt ")
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

# ~~~~~~~~~~~~~~~~~~~~~~ DECRYPTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
message = input("Please enter the text you would like to decrypt ")
option = input("Please select the method you'd like to use: base64/morse/hex/caesar cipher: ")
while option == 'base64' or option == 'morse' or option == 'hex' or option == 'caesar cipher':
    if option == 'base64':
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64decode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print("Encrypted Message:" + base64_message)
            break  


    if option == 'morse':
        Morse_Dict = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}   
        def decrypt(message):
            var = '' #variable for concatenating letters 
            decode = ''
            for letter in message: 
                if (letter != ' '): 
                    c = 0          #counter for spaces to keep letters separated
                    var += letter 
                else: 
                    c += 1
                    if c == 2:
                        decode += ' '
                    else: 
                        decode += list(Morse_Dict.keys())[list(Morse_Dict.values()).index(var)] 
                        var = ''
            return decode
        result = decrypt(message) 
        print (result) 
        break  

        
    if option == 'hex':
        hex_bytes = bytes.fromhex(message) 
        message_bytes = hex_bytes.decode('utf-8')
        result = message_bytes
        print(result)
        break

    if option == 'caesar cipher':
        s = int(input("Please enter the shift number you'd like (Exmaple: 4): "))
        def decrypt2(message,s):
            result = ""
            # transverse the plain text
            for i in range(len(message)):
                char = message[i]
                # Encrypt uppercase characters in plain text
                
                if (char.isupper()):
                    result += chr((ord(char) - s-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) - s - 97) % 26 + 97)
            print(result)
        decrypt2(message, s)
    break


        
