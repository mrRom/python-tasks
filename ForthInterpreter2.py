class ForthInterpreter(object):
    """Interpreter of the Forth Language.
        Supports 5 commands: put, pop, add, sub, print.   
    """
    def __init__(self, stack):
        """Initializes:
             cmds - dict with command names as a key and supported class as a value
             stack - list where values will be stored 
        """
        self.stack = stack
        self.cmds = {'add': Add, 'pop': Pop, 'put': Put, 'sub': Sub, 'print': Print}

    def evaluate(self, lines):
        """Receives list of lines from the .frt file  
        
        """
        for line in lines:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            else:
                arguments = self.split_line(line)
                cmd = arguments[0]
                params = self.convert_value(arguments[1:])
                command = self.cmds.get(cmd)(*params)
                command.execute(self.stack)

    def load_file(self, fpath):
        """Returns list with lines from the file
        
        """
        lines = []
        with open(fpath, 'r') as ffile:
            for line in ffile:
                lines.append(line)
        return lines

    def split_line(self, line):
        """Splits line. 
            Returns list of arguments where first argument is a command 
            and all next arguments are parameters (parameter have to be numeric). 
             
        """
        arguments = line.split(" ")
        for argument in arguments:
            if argument.startswith('"') and argument.endswith('"'):
                argument = argument[1:-1]
        return arguments

    def convert_value(self, params):
        """Converts strings from params into int or float type.
            Returns list of params with converted values
            Throws ValueError if parameter cann't be converted.
            
        """
        result = []
        for val in params:
            try:
                result.append(int(val))
            except ValueError:
                result.append(float(val))
        return result

class Command(object):
    """Base class for all command classes
    
    """
    paramsCount = None
    minStackSize = None
    def __init__(self, *params):
        self.params = params
    def execute(self, stack):
        pass

class Add(Command):
    minStackSize = 2
    def execute(self, stack):
        if len(stack) < self.minStackSize:
            raise Exception('Not enough values for "add" operation!')
        stack.append(stack.pop() + stack.pop())

class Pop(Command):
    minStackSize = 1
    def execute(self, stack):
        if len(stack) < self.minStackSize:
            raise Exception('Not enough values for "pop" operation!')
        stack.pop()

class Put(Command):
    paramsCount = 1
    def execute(self, stack):
        if len(self.params) != self.paramsCount:
            raise Exception('Wrong number of parameters!')
        stack.append(self.params[0])

class Sub(Command):
    minStackSize = 2
    def execute(self, stack):
        if len(stack) < self.minStackSize:
            raise Exception('Not enough values for "sub" operation!')
        stack.append(stack.pop() - stack.pop())

class Print(Command):
    minStackSize = 1
    def execute(self, stack):
        print str(stack.pop())

def eval_forth(filepath):
    stack = []
    forth_interpreter = ForthInterpreter(stack)
    forth_interpreter.evaluate(forth_interpreter.load_file(filepath))

if __name__ == '__main__':
    filepath = raw_input('Enter name of the file: ')
    if filepath.endswith('.frt'):
        eval_forth(filepath)
    else:
        raise Exception("Incorrect file type!")
