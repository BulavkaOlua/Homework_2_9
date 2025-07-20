# test_my_function_2.py
# Тести з абсолютним імпортом для запуску з кореня проєкту

from my_function_2 import sum_of_numbers_in_string

def test_simple_sum():
    assert sum_of_numbers_in_string("1,2,3") == 6

def test_with_zero():
    assert sum_of_numbers_in_string("0,0,0") == 0

def test_with_negative_numbers():
    assert sum_of_numbers_in_string("-1,-2,3") == 0

def test_with_invalid_string():
    assert sum_of_numbers_in_string("abc,2,3") == "Не можу це зробити!"

def test_with_letters_inside_numbers():
    assert sum_of_numbers_in_string("1,2a,3") == "Не можу це зробити!"

