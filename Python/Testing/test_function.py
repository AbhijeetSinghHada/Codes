from unittest import TestCase
from function import divide, multiply


class TestFunctions(TestCase):
    def test_dvide_result(self):
        divident = 15
        divisor = 3
        expected = 5.0  # 4.0 Failed

        self.assertAlmostEqual(divide(divident, divisor),
                               expected, delta=0.0001)

    def test_divide_negative(self):
        divident = 15
        divisor = -3
        expected = -5.0  # 4.0 Failed

        self.assertAlmostEqual(divide(divident, divisor),
                               expected, delta=0.0001)

    def test_divide_dividend_zero(self):
        divident = 0
        divisor = 5
        expected = 0  # 4.0 Failed

        self.assertEqual(divide(divident, divisor), expected)

    def test_divide_error_on_zero(self):
        # self.assertRaises(ValueError,lambda: divide(25,0)) # both are same
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_result_with_zero(self):
        inputs = (3, -5, 0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_result_with_negative(self):
        inputs = (3, -5, 2)
        expected = -30
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_result_floats(self):
        inputs = (3.0, 5, 2)
        expected = 30
        self.assertEqual(multiply(*inputs), expected)
