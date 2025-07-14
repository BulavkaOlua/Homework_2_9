from lesson_11_12_tests.average_function import average

import unittest

#def average(numbers):
    #if len(numbers) == 0:
        #return 0
   # return sum(numbers) / len(numbers)

class TestAverageFunction(unittest.TestCase):

    def test_average_regular_list(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)

    def test_average_empty_list(self):
        self.assertEqual(average([]), 0)

    def test_average_single_element(self):
        self.assertEqual(average([10]), 10.0)

    def test_average_negative_numbers(self):
        self.assertEqual(average([-1, -2, -3]), -2.0)

    def test_average_mixed_numbers(self):
        self.assertEqual(average([-1, 0, 1]), 0.0)

    def test_average_floats(self):
        self.assertAlmostEqual(average([1.5, 2.5, 3.0]), 2.3333333333333335)

    def test_average_large_numbers(self):
        self.assertEqual(average([1000000, 2000000, 3000000]), 2000000.0)

    def test_average_zeros(self):
        self.assertEqual(average([0, 0, 0]), 0.0)

    def test_average_duplicates(self):
        self.assertEqual(average([4, 4, 4, 4]), 4.0)

    def test_average_mixed_integers_and_floats(self):
        self.assertAlmostEqual(average([1, 2.5, 3]), 2.1666666666666665)


# Запуск тестів
if __name__ == '__main__':
    unittest.main()
