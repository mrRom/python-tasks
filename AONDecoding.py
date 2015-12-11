def decode(line):
    line = replaceSharps(replaceDoubles(removeSingleCharacters(line)))
    return line

def removeSingleCharacters(line):
    lst = list(line)
    for i in range(1, len(lst)-1):
        if (lst[i] != lst[i+1] and lst[i] != lst[i-1]):
            lst[i] = ""
    if (lst[len(lst)-1] != lst[len(lst)-2]):
        lst[len(lst)-1]= ""
    if (lst[0] != lst[1]):
        lst[0]= ""
    line = ''.join(lst)
    print line
    return line

def replaceDoubles(line):
    lst = list(line)
    for i in range(len(lst)-1):
        if (lst[i] == lst[i+1]):
            lst[i] = ""
    line = ''.join(lst)
    print line
    return line
    
def replaceSharps(line):
    lst = list(line)
    for i in range(len(lst)):
        if (lst[i] == "#"):
            lst[i] = lst[i-1]
    line = ''.join(lst)
    print line
    return line
    
if __name__ == '__main__':
    line = "311122234###55###3"
    print line
    newline = decode(line)