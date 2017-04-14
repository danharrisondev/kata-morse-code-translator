"""Provides a method to play a morse message through the computer's beep function"""

import winsound

FREQUENCY = 500
DASH_LENGTH = 300
DOT_LENGTH = 100

def play_morse(morse_message):
    """Plays a morse message"""
    for character in morse_message:
        if character == '-':
            winsound.Beep(FREQUENCY, DASH_LENGTH)
        elif character == '.':
            winsound.Beep(FREQUENCY, DOT_LENGTH)
