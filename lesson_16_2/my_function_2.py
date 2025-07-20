def sum_of_numbers_in_string(s):
    try:
        numbers = s.split(",")
        total = 0
        for num in numbers:
            total += int(num)
        return total
    except ValueError:
        return "Не можу це зробити!"
