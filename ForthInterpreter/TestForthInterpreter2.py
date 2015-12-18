import unittest
import ForthInterpreter2

#Learning, how to use unittest in Python

class Test(unittest.TestCase):

    def test_Add(self):
        stack = [1, 2]
        add = ForthInterpreter2.Add()
        add.execute(stack)
        self.assertEqual(stack[0], 3)
        stack = [1]
        add = ForthInterpreter2.Add()
        with self.assertRaises(Exception):
            add.execute(stack)

    def test_Put(self):
        stack = [1]
        put = ForthInterpreter2.Put(2)
        put.execute(stack)
        self.assertEqual(stack[1], 2)
        put = ForthInterpreter2.Put()
        with self.assertRaises(Exception):
            put.execute(stack)

    def test_Sub(self):
        stack = [1, 2]
        sub = ForthInterpreter2.Sub()
        sub.execute(stack)
        self.assertEqual(stack[0], 1)
        stack = [1]
        sub = ForthInterpreter2.Sub()
        with self.assertRaises(Exception):
            sub.execute(stack)

    def test_Pop(self):
        stack = [1, 2]
        pop = ForthInterpreter2.Pop()
        pop.execute(stack)
        self.assertEqual(len(stack), 1)
        stack = []
        pop = ForthInterpreter2.Pop()
        with self.assertRaises(Exception):
            sub.execute(stack)

    def test_Print(self):
        stack = [1, 2]
        printt = ForthInterpreter2.Print()
        printt.execute(stack)
        self.assertEqual(len(stack), 1)
        stack = []
        printt = ForthInterpreter2.Print()
        with self.assertRaises(Exception):
            printt.execute(stack)

    def test_ForthInterpreter_split_line(self):
        stack = []
        fi = ForthInterpreter2.ForthInterpreter(stack)
        self.assertEqual(fi.split_line("put 1"), ["put", "1"])
        self.assertEqual(fi.split_line('put "1"'), ['put', '1'])

    def test_ForthInterpreter_convert_value(self):
        stack = []
        fi = ForthInterpreter2.ForthInterpreter(stack)
        self.assertEqual(fi.convert_value(["1"]), [1])
        self.assertEqual(fi.convert_value(["1.5"]), [1.5])
        with self.assertRaises(ValueError):
            fi.convert_value("abc")

if __name__ == "__main__":
    unittest.main()
