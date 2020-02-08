import unittest

from mathutils import half, double, facts, power

class Test_mathsutils(unittest.TestCase):

    def test_halving(self):
        input = 40
        expectedResult = 20

        result = half(input)

        self.assertEqual(expectedResult, result)
    def test_doubling(self):
        input = 3
        expectedResult = 6

        result = double(input)

        self.assertEqual(expectedResult, result)

    def test_doubling_2(self):
        input = 2
        expectedResult = 4

        result = double(input)

        self.assertEqual(expectedResult, result)

    def test_factors(self):
        input = 6
        expectedResult = 4

        result = facts(input)

        self.assertEqual(expectedResult, result)

    def test_factors_2(self):
        input = 12
        expectedResult = 6

        result = facts(input)

        self.assertEqual(expectedResult, result)

    def test_factors_3(self):
        input = 1
        expectedResult = 1

        result = facts(input)

        self.assertEqual(expectedResult, result)

    def test_power(self):
        base = 2
        exponent = 4
        expectedResult = 16

        result = power(base, exponent)

        self.assertEqual(expectedResult, result)