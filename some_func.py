def sum_two_lowest_numbers(numbers):
    return sum(sorted(numbers)[:2])


def sum_two_lowest_numbers_with_len_validation(numbers):
    if len(numbers) < 2:
        raise ValueError("Not enough numbers")
    return sum(sorted(numbers)[:2])
