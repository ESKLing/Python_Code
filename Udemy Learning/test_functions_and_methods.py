import unittest

from functions_and_methods import vol, ran_bool, multiply, palindrome, ispangram
#or import functions_and_methods if there is only one function on that file/ to call specific functions

class Test_functions_and_methods(unittest.TestCase):

    def test_volume(self):
        input = 2
        expectedResult = 33.51

        result = vol(input)

        self.assertEqual(expectedResult, result)

    #or
    #     def test_volume(self):
    #         input = 2
    #         result = functions_and_methods.vol(input)
    #
    #         self.assertEqual(33.51, result)
    # if __name__== '__main__':
    #     unittest.main()


    def test_volume_2(self):
        input = 15
        expectedResult = 14137.17

        result = vol(input)

        self.assertEqual(expectedResult, result)

    def test_check(self):
        num = 5
        low = 2
        high = 7
        expectedResult = True

        result = ran_bool(num,low,high)

        self.assertEqual(expectedResult, result)

    def test_check_2(self):
        num = 300
        low = 2
        high = 100
        expectedResult = False

        result = ran_bool(num,low,high)

        self.assertEqual(expectedResult, result)

    def test_sum(self):
        input = [1, 2, -3]
        expectedResult = -6

        result = multiply(input)

        self.assertEqual(expectedResult, result)

    def test_sum_2(self):
        input = [5, 6, 0]
        expectedResult = 0

        result = multiply(input)

        self.assertEqual(expectedResult, result)

    def test_palindrome(self):
        input = 'nurses run'
        expectedResult = True

        result = palindrome(input)

        self.assertEqual(expectedResult, result)

    def test_palindrome_2(self):
        input = 'hello'
        expectedResult = False

        result = palindrome(input)

        self.assertEqual(expectedResult, result)

    def test_pangram(self):
        input = 'nurses run'
        expectedResult = False

        result = ispangram(input)

        self.assertEqual(expectedResult, result)

    def test_pangram_2(self):
        input = 'The quick brown fox jumps over the lazy dog'
        expectedResult = True

        result = ispangram(input)

        self.assertEqual(expectedResult, result)