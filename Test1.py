import unittest
def sum_low_numbers(a):
    return sum(sorted(a)[:2])

class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum_low_numbers([1, 2, 3]), 3, "Should be 3")
        self.assertEqual(sum_low_numbers([1000, 2000, 3000]), 3000, "Should be 3000")
        self.assertEqual(sum_low_numbers([-7234123, -857322, 115]), -8091445, "Should be 8091445")
    
    def test_pick(self):
        self.assertEqual(sum_low_numbers([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]), 3, "Should be 3")
        self.assertEqual(sum_low_numbers([-10, 1, 9, -2, 8, -3, 7, 4, -6, -5]), -16, "Should be -16")

    def test_empty(self):
        self.assertIsNone(sum_low_numbers, "Is empty")

if __name__ == '__main__':
    unittest.main()