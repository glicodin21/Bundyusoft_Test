import unittest
from Sum_two_lowest_numbers import sum_two_lowest_numbers


class Test(unittest.TestCase):
    def test_sum_two_lowest_numbers(self):
        self.assertEqual(sum_two_lowest_numbers(
            [1, 2, 3]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers(
            [1000, 2000, 3000]), 3000, "Should be 3000")
        self.assertEqual(sum_two_lowest_numbers(
            [-7234123, 857322, 115]), -7234008, "Should be -7234008")

    def test_pick_two_lowest_numbers_with_len_validation(self):
        self.assertEqual(sum_two_lowest_numbers(
            [10, 1, 9, 2]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers(
            [-10, 1, 9, -2]), -12, "Should be -12")
        self.assertEqual(sum_two_lowest_numbers(
            [0, 0, 0]), 0, "Should be 0")

    def test_raises_value_error_if_list_is_empty(self):
        self.assertRaises(ValueError,
                          sum_two_lowest_numbers, [])

    def test_raises_value_error_if_list_is_contain_one_element(self):
        self.assertRaises(ValueError,
                          sum_two_lowest_numbers, [1])


if __name__ == '__main__':
    unittest.main()
