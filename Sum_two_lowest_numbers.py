def sum_two_lowest_numbers(numbers):
    """Функция, возвращающая сумму двух минимальных элементов."""
    return sum(sorted(numbers)[:2])


def sum_two_lowest_numbers_with_len_validation(numbers):
    """Функция, возвращающая сумму двух минимальных элементов.

    С учетом возможности списка оказаться пустым
    или состоящим из одного элемента"""
    if len(numbers) < 2:
        raise ValueError("Not enough numbers")
    return sum(sorted(numbers)[:2])
