"""Provides methods for converting between morse code and latin text"""

from .dictionary import LATIN_TO_MORSE_LOOKUP, MORSE_TO_LATIN_LOOKUP

def morse_to_text(morse, separator):
    """Converts morse to latin text"""
    morse_characters = morse.split(separator)
    letters = []
    for character in morse_characters:
        letters.append(MORSE_TO_LATIN_LOOKUP[character])
    return ''.join(letters)


def text_to_morse(text, separator):
    """Converts latin text to morse"""
    morse_code = []
    for character in text:
        morse_code.append(LATIN_TO_MORSE_LOOKUP[character])
        morse_code.append(separator)
    return ''.join(morse_code)
 