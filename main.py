# Thanks to this project, I reviewed the previous classes and recalled what I had learnt before.
# I had fun when I completed this assignment
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
}

Converting_mode = input("Would you like to translate your morse code (1) or convert your message to a morse code (2)? Please answer by typing 1 or 2!\n")
if Converting_mode == "1":
    Sentence = input("Please write the secret message you want to send!\n")

    Sentence = Sentence.split(' ')

    morsecode = ""

    for word in Sentence:
        for letter in word:
            key = morse_code.get(letter.upper())
            morsecode = morsecode + key + " "
        morsecode = morsecode + '\ '

    print(f'Your morse code is {morsecode}')

elif Converting_mode == "2":

    morsecode = input("Please write the coded message you received!\n")

    morsecode = morsecode.split(" ")

    coded_text = ""

    for j in morsecode:
        if j == "":
            pass
        elif j =="\\":
            coded_text = coded_text + " "
        else:
            for letter, code in morse_code.items():
                if code == j:
                    coded_text = coded_text + letter

    print(coded_text.lower())
