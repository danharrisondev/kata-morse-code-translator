from morse.text import morse_to_text, text_to_morse
from morse.sound import play_morse

def main():
    message = text_to_morse('HELLO WORLD', separator='/')

    play_morse(message)

    print(message)

if __name__ == '__main__':
    main()
