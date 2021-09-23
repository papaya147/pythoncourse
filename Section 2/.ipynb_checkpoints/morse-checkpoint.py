letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}

morse_to_letter = {}
        
for letter, morse in letter_to_morse.items():
    morse_to_letter[morse] = letter

class EnglishMessage:
    def __init__(self, message):
        self.message = message
        
    def encode(self):
        morse = []

        for letter in self.message.lower():
            morse_letter = letter_to_morse[letter]
            morse.append(morse_letter)

        # We need to join together Morse code letters with spaces
        morse_message = " ".join(morse)
        return morse_message

    # We need to invert the dictionary. This will create a dictionary
    # that can go from the morse back to the letter
    morse_to_letter = {}
    for letter in letter_to_morse:
        morse = letter_to_morse[letter]
        morse_to_letter[morse] = letter

class MorseMessage:
    def __init__(self, message):
        self.message = message
        
    def decode(self):
        english = []

        # Now we cannot read by letter. We know that morse letters are
        # separated by a space, so we split the morse string by spaces
        morse_letters = self.message.split(" ")

        for letter in morse_letters:
            english_letter = morse_to_letter[letter]
            english.append(english_letter)

        # Rejoin, but now we don't need to add any spaces
        english_message = "".join(english)

        return english_message