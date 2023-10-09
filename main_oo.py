#object oriented version

import sys
import scanner_oo


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = scanner_oo.Scanner()
    lexer.build()

    
    # Give the lexer some input
    lexer.input(text)

    # Tokenize
    while True:
        tok = lexer.tokenize()
        if not tok: 
            break      # No more input
        print(tok)
