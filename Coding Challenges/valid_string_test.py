import unittest

from valid_string import isValid

class TestValidString(unittest.TestCase):

    def test_one(self):
        result = isValid('a')
        self.assertEqual(True, result)

    def test_two(self):
        result = isValid('abc')
        self.assertEqual(True, result)

    def test_three(self):
        result = isValid('abbc')
        self.assertEqual(True, result)

    def test_four(self):
        result = isValid('abbbc')
        self.assertEqual(False, result)

    def test_five(self):
        result = isValid('abbbcc')
        self.assertEqual(False, result)

    def test_six(self):
        result = isValid('abcdefghhgfedecba')
        self.assertEqual(True, result)

    def test_seven(self):
        result = isValid('aabbccddeefghi')
        self.assertEqual(False, result)
