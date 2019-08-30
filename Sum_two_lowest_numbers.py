def sum_two_lowest_numbers(numbers):
    """Функция, возвращающая сумму двух минимальных элементов."""
    if len(numbers) < 2:
        raise ValueError("Not enough numbers")
    if numbers[0] > numbers[1]:
        a = numbers[0]
        b = numbers[1]
    else:
        a = numbers[1]
        b = numbers[0]

    for number in numbers[2:]:
        if a > number:
            a = number
            if a < b:
                a, b = b, a
    return (a + b)
