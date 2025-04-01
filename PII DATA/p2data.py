import re

def load_text(file_path):
    """Reads the content of the file and returns it line by line."""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def find_pii(text_lines):
    """Scans each line for PII data such as emails, phone numbers, and SSNs."""
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    ssn_regex = r"\b\d{3}-\d{2}-\d{4}\b"

    for line in text_lines:
        search_and_print("email", email_regex, line)
        search_and_print("phone number", phone_regex, line)
        search_and_print("SSN", ssn_regex, line)

def search_and_print(data_type, pattern, text):
    """Searches for a pattern in the text and prints any matches found."""
    matches = re.findall(pattern, text)
    for match in matches:
        print(f"Found {data_type}: {match}")

def main():
    print("Welcome to PII Data Detector!")
    file_path = input("Enter the file path to scan for PII data: ").strip()

    text_lines = load_text(file_path)
    if text_lines:
        find_pii(text_lines)
    else:
        print("No content to scan.")

if __name__ == "__main__":
    main()
