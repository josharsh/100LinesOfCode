import os

TITLE = "--- GHOSTCHAT: SECURE ENCRYPTED UTILITY ---"

def crypt_logic(text, key, mode):
    """Shifts characters using the key within printable ASCII (32-126)."""
    result = ""
    for i, char in enumerate(text):
        k_val = ord(key[i % len(key)])
        # Shift up for encryption, down for decryption
        shift = k_val if mode == "enc" else -k_val
        result += chr((ord(char) - 32 + shift) % 94 + 32)
    return result

# Clear screen and show title
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{TITLE.center(80)}\n")
shared_key = input("SYSTEM: Set Shared Secret Key (keep this private): ")

while True:
    print("\n" + "="*80)
    
    # 1. Handle Your Message (Encryption)
    print("") # spacing
    my_msg = input(f"{' '*40}me(decrypt): ")
    if my_msg.lower() in ['exit', 'quit']: break
    print(f"{' '*40}me(encrypt): {crypt_logic(my_msg, shared_key, 'enc')}")

    # 2. Handle Friend's Message (Decryption)
    friend_enc = input("sender(encrypt): ")
    if friend_enc.lower() in ['exit', 'quit']: break
    print(f"sender(decrypt): {crypt_logic(friend_enc, shared_key, 'dec')}")

