def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher


def decrypt(string, shift):
 
  decipher = ''
  for char in string: 
    if char == ' ':
      decipher = decipher + char
    elif  char.isupper():
      decipher = decipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      decipher = decipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return decipher