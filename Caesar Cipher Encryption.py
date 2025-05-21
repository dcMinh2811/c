from string import ascii_lowercase
letters = [letter for letter in ascii_lowercase]

while True:
    message = input("Message: ").strip()
    shift = int(input("Shift: "))

    def caesar_encrypt(message, shift):
        encrypted_message = ""
        for char in message:
            is_uppercase = False if char == char.lower() else True
            char = char.lower()
            if char in letters:
                try:
                    newChar = letters[letters.index(char) + shift]
                except IndexError:
                    index = abs(len(letters) - (letters.index(char) + shift))
                    newChar = letters[index]
            else:
                newChar = char
            encrypted_message += newChar.upper() if is_uppercase else newChar
        
        return print(encrypted_message if len(encrypted_message) > 0 else print("Empty"))
    
    caesar_encrypt(message,shift)