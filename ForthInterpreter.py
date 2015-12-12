def evaluate(lines):
    stack = []
    for line in lines:
        line = line.strip()
        if line.startswith("#") or line =="":
            continue
        else:
            arguments = split_line(line)
            cmd = arguments[0]
            if cmd == "put":
                val = arguments[1]
                stack.append(convertValue(val))
            elif cmd == "pop":
                stack.pop()
            elif cmd == "add":
                stack.append(stack.pop() + stack.pop())
            elif cmd == "sub":
                stack.append(stack.pop() - stack.pop())
            elif cmd == "print":
                print str(stack.pop())
                
def load_file(fpath):
    lines = []
    with open(fpath, 'r') as ffile:
        for line in ffile:
            lines.append(line)
    return lines

def split_line(line):
    arguments = line.split(" ")
    if len(arguments) > 2:
        raise Exception("Not valid line!: " + line)
    for a in arguments:
        if a.startswith('"') and arg.endswith('"'):
            a = a[1:-1]
    return arguments

def convertValue(val):
    try:
        result = int(val)
    except ValueError:
        result = float(val)
    return result

def eval_forth(fl):
    evaluate(load_file(fl))

if __name__ == '__main__':
    fpath = raw_input('Enter name of the file: ')
    if fpath.endswith('.frt'):
        eval_forth(fpath)
    else:
        raise Exception ("Incorect file type!")
