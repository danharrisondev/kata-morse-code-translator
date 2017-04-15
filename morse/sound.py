"""Provides a method to play a morse message through the computer's beep function"""

from .dictionary import DASH, DOT
import winsound

FREQUENCY = 500
DASH_LENGTH = 300
DOT_LENGTH = 100

def play_morse(morse_message):
    """Plays a morse message"""
    for character in morse_message:
        if character == DASH:
            winsound.Beep(FREQUENCY, DASH_LENGTH)
        elif character == DOT:
            winsound.Beep(FREQUENCY, DOT_LENGTH)
