#object oriented version
import scanner_oo

if __name__ == '__main__':

    with open("example.txt", "r") as f:
        data = f.read()

    lexer = scanner_oo.Scanner()

    
    # Give the lexer some input
    lexer.input(data)


