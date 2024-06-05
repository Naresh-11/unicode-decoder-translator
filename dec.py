import re
import os

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("deep-translator module not found. Please install it using 'pip install deep-translator'")
    exit()

def unicode_decoder(unicode_str):
    # Check if the string contains Unicode escape sequences
    if re.search(r'\\u[0-9a-fA-F]{4}', unicode_str):
        try:
            # Attempt to decode the Unicode escape sequences
            decoded_str = unicode_str.encode('utf-8').decode('unicode_escape')
            return decoded_str
        except UnicodeDecodeError:
            return "Error: Unable to decode the provided message."
    else:
        return unicode_str

def translate_to_english(text):
    try:
        # Translate text to US English
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        return f"Error: Unable to translate the message. Details: {e}"

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        # Prompt the user to input the encrypted message
        encrypted_message = input("Please enter your encrypted message (or type 'exit' to quit): ")
        if encrypted_message.lower() == 'exit':
            break
        # Decode the encrypted message
        decoded_message = unicode_decoder(encrypted_message)
        # Translate the decoded message to English
        translated_message = translate_to_english(decoded_message)
        # Display the decoded and translated message
        print(f"Original: {decoded_message}\nTranslated (en): {translated_message}")
        # Wait for user input before clearing the screen and prompting again
        input("Press Enter to continue...")
        clear_screen()

# Run the main function
if __name__ == "__main__":
    main()
