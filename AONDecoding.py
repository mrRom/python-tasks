def decode(line):
    """At first it removes all single chars from str.
        Then it replaces two and more chars in a row with single char
        And then it replaces sharps with last occurring char.
        
    """
    line = replace_sharps(replace_doubles(remove_single_characters(line)))
    return line

def remove_single_characters(line):
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
    return line

def replace_doubles(line):
    """Replaces two and more chars in a row with single char
    
    """
    lst = list(line)
    for i in range(len(lst)-1):
        if (lst[i] == lst[i+1]):
            lst[i] = ""
    line = ''.join(lst)
    return line
    
def replace_sharps(line):
    """Replaces sharps with last occurring char.
    
    """
    lst = list(line)
    for i in range(1, len(lst)):
        if (lst[i] == "#"):
            lst[i] = lst[i-1]
    if lst[0] == "#":
        lst[0] = ""
    line = ''.join(lst)
    return line
    
if __name__ == '__main__':
    line = "##311122234###55##3"
    print line
    newline = decode(line)
    print newline
