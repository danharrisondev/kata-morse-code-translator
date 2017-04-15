from morse.text import morse_to_text, text_to_morse
from morse.sound import play_morse

def main():
    message = input('msg> ')

    morse_message = text_to_morse(message)
    print("morse: " + morse_message)
    play_morse(morse_message)

    original_message = morse_to_text(morse_message)
    print("original: " + original_message)

if __name__ == '__main__':
    main()
