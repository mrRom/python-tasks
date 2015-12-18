import unittest
import ForthInterpreter3

class Test(unittest.TestCase):

    def test_fucn_add(self):
        stack = [1, 2]
        ForthInterpreter3.func_add(stack)
        self.assertEqual(stack[0], 3)
        stack = [1]
        with self.assertRaises(Exception):
            ForthInterpreter3.func_add(stack)

    def test_fucn_put(self):
        stack = [1]
        ForthInterpreter3.func_put(stack, 2)
        self.assertEqual(stack[1], 2)
        with self.assertRaises(Exception):
            ForthInterpreter3.func_put(stack)

    def test_fucn_sub(self):
        stack = [1, 2]
        ForthInterpreter3.func_sub(stack)
        self.assertEqual(stack[0], 1)
        stack = [1]
        
        with self.assertRaises(Exception):
            ForthInterpreter3.func_sub(stack)

    def test_fucn_pop(self):
        stack = [1, 2]
        ForthInterpreter3.func_pop(stack)
        self.assertEqual(len(stack), 1)
        stack = []
        with self.assertRaises(Exception):
            ForthInterpreter3.func_pop(stack)

    def test_fucn_print(self):
        stack = [1, 2]
        ForthInterpreter3.func_print(stack)
        self.assertEqual(len(stack), 1)
        stack = []
        with self.assertRaises(Exception):
            ForthInterpreter3.func_print(stack)

    def test_ForthInterpreter_split_line(self):
        stack = []
        fi = ForthInterpreter3.ForthInterpreter(stack)
        self.assertEqual(fi.split_line("put 1"), ["put", "1"])
        self.assertEqual(fi.split_line("put   1"), ["put", "1"])
        self.assertEqual(fi.split_line("   put   1  "), ["put", "1"])
        self.assertEqual(fi.split_line('put "1"'), ['put', '1'])

    def test_ForthInterpreter_convert_value(self):
        stack = []
        fi = ForthInterpreter3.ForthInterpreter(stack)
        self.assertEqual(fi.convert_value(["1"]), [1])
        self.assertEqual(fi.convert_value(["1.5"]), [1.5])
        with self.assertRaises(ValueError):
            fi.convert_value("abc")
    
    def test_eval_forth(self):
        stack = []
        lines = ["put 2", "Put 3", " ADD", "put   4  ", "sub", "put 5", "pop", "print"]
        fi = ForthInterpreter3.ForthInterpreter(stack)
        fi.evaluate(lines)
        self.assertEqual(len(stack), 0)

if __name__ == "__main__":
    unittest.main()
