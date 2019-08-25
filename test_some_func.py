import unittest
from some_func import sum_two_lowest_numbers
from some_func import sum_two_lowest_numbers_with_len_validation


class Test(unittest.TestCase):
    def test_sum_two_lowest_numbers(self):
        self.assertEqual(sum_two_lowest_numbers(
            [1, 2, 3]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers(
            [1000, 2000, 3000]), 3000, "Should be 3000")
        self.assertEqual(sum_two_lowest_numbers(
            [-7234123, 857322, 115]), -7234008, "Should be -7234008")

    def test_pick_two_lowest_numbers(self):
        self.assertEqual(sum_two_lowest_numbers(
            [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers(
            [-10, 1, 9, -2, 8, -3, 7, 4, -6, -5]), -16, "Should be -16")

    def test_sum_two_lowest_numbers_with_len_validation(self):
        self.assertEqual(sum_two_lowest_numbers_with_len_validation(
            [1, 2, 3]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers_with_len_validation(
            [1000, 2000, 3000]), 3000, "Should be 3000")
        self.assertEqual(sum_two_lowest_numbers_with_len_validation(
            [-7234123, 857322, 115]), -7234008, "Should be -7234008")

    def test_pick_two_lowest_numbers_with_len_validation(self):
        self.assertEqual(sum_two_lowest_numbers_with_len_validation(
            [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]), 3, "Should be 3")
        self.assertEqual(sum_two_lowest_numbers_with_len_validation(
            [-10, 1, 9, -2, 8, -3, 7, 4, -6, -5]), -16, "Should be -16")

    def test_raises_value_error_if_list_is_empty(self):
        self.assertRaises(ValueError,
                          sum_two_lowest_numbers_with_len_validation, [])
    def test_raises_value_error_if_list_is_contain_one_element(self):
        self.assertRaises(ValueError,
                          sum_two_lowest_numbers_with_len_validation, [1])


if __name__ == '__main__':
    unittest.main()
