def decode(line):
    """At first it removes all single chars from str.
        Then it replaces two and more chars in a row with single char
        And then it replaces sharps with last occurring char.
        
    """
    line = replaceSharps(replaceDoubles(removeSingleCharacters(line)))
    return line

def removeSingleCharacters(line):
    """Removes all single chars from str.
    
    """
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
    """Replaces two and more chars in a row with single char
    
    """
    lst = list(line)
    for i in range(len(lst)-1):
        if (lst[i] == lst[i+1]):
            lst[i] = ""
    line = ''.join(lst)
    print line
    return line
    
def replaceSharps(line):
    """Replaces sharps with last occurring char.
    
    """
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
    print line
