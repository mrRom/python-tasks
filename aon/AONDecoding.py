import sys

def decode(line):

    result = ''
    previous_char = ''
    previous_added_char = ''
    added = False

    for ch in line:
        if (ch == '#'):
            if previous_char == '#':
                if added == False:
                    result += previous_added_char
                    added = True
            else:
                previous_char = ch
                added = False
        else:
            if previous_char == ch:
                if added == False:
                    result += ch
                    previous_added_char = ch
                    added = True
            else:
                previous_char = ch
                added = False
    return result

if __name__ == '__main__':
    line = "##311122234###55##3"
    #line = arguments = sys.argv[1]
    newline = decode(line)
    print newline
