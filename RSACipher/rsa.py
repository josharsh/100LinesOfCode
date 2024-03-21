from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    modulus_length = 1024
    key = RSA.generate(modulus_length)
    pub_key = key.publickey()
    return key, pub_key

def encrypt(plain, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(plain)
    print(f"Encrypted Message: {encrypted_msg}")
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(f"Base64 Encoded Message: {encoded_encrypted_msg}")
    return encoded_encrypted_msg

def decrypt(encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encrypted_msg)
    print(f"Decoded Encrypted Message: {decoded_encrypted_msg}")
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg

def main():
  private, public = generate_keys()
  print (private)
  message = b'RSA Cipher!'
  encoded = encrypt(message, public)
  message_decrypted = decrypt(encoded, private)
  print(f"Dectrypted Message: {message_decrypted}")

if __name__== "__main__":
  main()