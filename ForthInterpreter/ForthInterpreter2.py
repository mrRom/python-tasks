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
            If line starts with "#" or line is empty - ignore!
            
        """
        for line in lines:
            line = line.strip()
            
            if line.startswith("#") or line == "":
                continue
            else:
                arguments = self.split_line(line)
                cmd = arguments[0].lower()
                params = self.convert_value(arguments[1:])
                if self.cmds.get(cmd) == None:
                    raise Exception("Unknown command: %s" %cmd)
                else:
                    command = self.cmds.get(cmd)(*params)
                    command.execute(self.stack) 

    def load_file(self, fpath):
        """Returns list of lines from the file
        
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
        result = []
        for argument in arguments:
            if argument == "":
                continue
            else: 
                if argument.startswith('"') and argument.endswith('"'):
                    argument = argument[1:-1]
                result.append(argument)
        return result

    def convert_value(self, params):
        """Converts strings from params into int or float type.
            Returns list of params with converted values
            Throws ValueError if parameter can't be converted.
            
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
    def __init__(self, *params):
        self.params = params

    def execute(self, stack):
        pass

#params in add, print and sub can be ignored and there is no need to raise exception. 
#They don't affect the stack itself.
#So, if there will be some mistake in the file and method execute receives 
#some parameters along with those commands, it will execute the command like it was without any parameters

class Add(Command):
    MINSTACKSIZE = 2
    def execute(self, stack):
        if len(stack) < self.MINSTACKSIZE:
            raise Exception('Not enough values in the stack for "add" operation!')
        stack.append(stack.pop() + stack.pop())

class Pop(Command):
    MINSTACKSIZE = 1
    def execute(self, stack):
        if len(stack) < self.MINSTACKSIZE:
            raise Exception('Not enough values in the stack for "pop" operation!')
        stack.pop()

class Put(Command):
    PARAMSCOUNT = 1
    def execute(self, stack):
        if len(self.params) != self.PARAMSCOUNT:
            raise Exception('Wrong number of parameters for "put" operation!')
        stack.append(self.params[0])

class Sub(Command):
    MINSTACKSIZE = 2
    def execute(self, stack):
        if len(stack) < self.MINSTACKSIZE:
            raise Exception('Not enough values in the stack for "sub" operation!')
        stack.append(stack.pop() - stack.pop())

class Print(Command):
    MINSTACKSIZE = 1
    def execute(self, stack):
        if len(stack) < self.MINSTACKSIZE:
            raise Exception('Not enough values in the stack for "print" operation!')
        print str(stack.pop())

def eval_forth(filepath):
    stack = []
    forth_interpreter = ForthInterpreter(stack)
    try:
        forth_interpreter.evaluate(forth_interpreter.load_file(filepath))
    except Exception, e:
        print "Can't process this file! %s" %e

if __name__ == '__main__':
    eval_forth("example.frt")
#     filepath = raw_input('Enter name of the file: ')
#     if filepath.endswith('.frt'):
#         eval_forth(filepath)
#     else:
#         raise Exception("Incorrect file type!")
