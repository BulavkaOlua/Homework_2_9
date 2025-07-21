# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

# 2.Створіть генератор, який генерує послідовність Фібоначчі до певного числа N

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
for num in fibonacci(50):
    print(num)

# 3. Реалізуйте ітератор для зворотного виведення елементів списку.

def reverse_iter(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]

my_list = [10, 20, 30, 40]

for item in reverse_iter(my_list):
    print(item)

# 4. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)

#5. Напишіть декоратор, який логує аргументи та результати викликаної функції.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат функції '{func.__name__}': {result}")
        return result
    return wrapper
@logger
def add(a, b):
    return a + b
add(5, 7)

# 6. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка у функції '{func.__name__}': {e}")
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))


