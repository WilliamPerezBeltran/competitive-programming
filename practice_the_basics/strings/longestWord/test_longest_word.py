import unittest
from longest_word import LongestWord 

class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        longest_word = LongestWord()
        self.assertEqual(longest_word.method_1("ole la la kd lamas"),"lamas")
        self.assertEqual(longest_word.method_2("ole la la kd lamas"),"lamas")
        self.assertEqual(longest_word.method_3("ole la la kd lamas"),"lamas")
        self.assertEqual(longest_word.method_4("ole la la kd lamas"),"lamas")
        self.assertEqual(longest_word.method_5("ole la la kd lamas"),"lamas")


if __name__ == "__main__":
    unittest.main()

