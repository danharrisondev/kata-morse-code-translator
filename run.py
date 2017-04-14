from morse.text import morse_to_text, text_to_morse

def main():
    message = text_to_morse('HELLO WORLD', separator='/')

    print(message)

if __name__ == '__main__':
    main()
