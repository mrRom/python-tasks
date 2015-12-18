import unittest
import AONDecoding

class Test(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(AONDecoding.decode("#"), "")
        self.assertEqual(AONDecoding.decode("##"), "")
        self.assertEqual(AONDecoding.decode("11"), "1")
        self.assertEqual(AONDecoding.decode("#1"), "")
        self.assertEqual(AONDecoding.decode("111222"), "12")
        self.assertEqual(AONDecoding.decode("11##"), "11")
        self.assertEqual(AONDecoding.decode("11##1"), "11")
        self.assertEqual(AONDecoding.decode("####11####"), "11")
        self.assertEqual(AONDecoding.decode("####1####"), "")
        self.assertEqual(AONDecoding.decode("####111222####333"), "1223")
        self.assertEqual(AONDecoding.decode("11####111222####333"), "111223")

if __name__ == "__main__":
    unittest.main()

