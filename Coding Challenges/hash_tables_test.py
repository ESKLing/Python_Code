import unittest

from hash_tables import checkMagazine

class TestCheckMagazine(unittest.TestCase):

    def test_one(self):
        result = checkMagazine('give me one grand today night', 'give one grand today')
        self.assertEqual(True, result)

    def test_two(self):
        result = checkMagazine('ive got a lovely bunch of coconuts', 'ive got some coconuts')
        self.assertEqual(False, result)

    def test_three(self):
        result = checkMagazine('two times three is not four', 'two times two is four')
        self.assertEqual(False, result)

    def test_four(self):
        result = checkMagazine('a', 'a')
        self.assertEqual(True, result)

    def test_five(self):
        result = checkMagazine('a', 'A')
        self.assertEqual(False, result)