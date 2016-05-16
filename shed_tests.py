from shed import valid_card
import unittest


class ShedTestSuite(unittest.TestCase):
    def test_valid_card(self):
        self.assertTrue(valid_card([9])) # a number on its own can be played at the start
        self.assertTrue(valid_card([2, 3])) # higher number allowed on lower number
        self.assertFalse(valid_card([2, 1])) # lower number not allowed on higher number
        self.assertTrue(valid_card([2, 2])) # same number allowed on same number
        self.assertTrue(valid_card([7, 6])) # seven means play lower
        self.assertFalse(valid_card([7, 8])) # seven means dont play higher
        self.assertTrue(valid_card([7, 10])) # ten should over rule 7


unittest.main()
