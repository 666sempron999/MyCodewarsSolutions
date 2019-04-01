import pprint

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code = morse_code.strip()

    MORSE_CODE_DICT = { 
    'A':'.-', 
    'B':'-...', 
    'C':'-.-.',
    'D':'-..', 
    'E':'.', 
    'F':'..-.', 
    'G':'--.', 
    'H':'....', 
    'I':'..', 
    'J':'.---', 
    'K':'-.-', 
    'L':'.-..', 
    'M':'--', 
    'N':'-.', 
    'O':'---', 
    'P':'.--.', 
    'Q':'--.-', 
    'R':'.-.', 
    'S':'...', 
    'T':'-', 
    'U':'..-', 
    'V':'...-', 
    'W':'.--', 
    'X':'-..-', 
    'Y':'-.--', 
    'Z':'--..', 
    '1':'.----', 
    '2':'..---', 
    '3':'...--', 
    '4':'....-', 
    '5':'.....', 
    '6':'-....', 
    '7':'--...', 
    '8':'---..', 
    '9':'----.', 
    '0':'-----', 
    ', ':'--..--', 
    '.':'.-.-.-', 
    '?':'..--..',
    '!': '-.-.--', 
    '/':'-..-.', 
    '-':'-....-', 
    '(':'-.--.', 
    ')':'-.--.-',
    'SOS': '...---...'
    }

    CODE_REVERSED = {value:key for key,value in MORSE_CODE_DICT.items()}

    translatedString = ""

    words = morse_code.split("   ")
    
    for i in range(0, len(words)):
        simbols = words[i].split(" ")
#         if len(simbols) == 1:
#             return CODE_REVERSED.get(simbols[i])
#         else:
        for j in range(0, len(simbols)):
            translatedString += CODE_REVERSED.get(simbols[j])
        if i < len(words) - 1:
            translatedString += " "
    
    return translatedString

def main():
    print(decodeMorse("      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  "))

if __name__ == '__main__':
    main()