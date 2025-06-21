print('task 1')
lier = """ Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1  # стартове значення множника

    while True:
        result = number * multiplier
        if result > 25:
            break  # якщо добуток більше 25 — зупиняємо цикл
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1  # збільшуємо множник

multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


print('task 2')
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

result = sum_two_numbers(a, b)
print("Сума чисел:", result)


print('task 3')
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

input_str = input("Введіть числа через пробіл: ")

numbers = list(map(float, input_str.split()))
result = average(numbers)
print("Середнє арифметичне:", result)

print('task 4')
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

user_input = input("Введіть рядок: ")

reversed_text = reverse_string(user_input)
print("Рядок у зворотному порядку:", reversed_text)


print('task 5')
"""Написати функцію, яка приймає список слів та повертає найдовше слово у списку."
"""
def find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

input_str = input("Введіть слова через пробіл: ")

word_list = input_str.split()

longest = find_longest_word(word_list)
print("Найдовше слово:", longest)

print('task 6')
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"

print(find_substring(str1, str2))

print('task 7')
#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-
#ськеморя разом?
def total_area(area1, area2):
    return area1 + area2

black_sea_area = 436402  # км²
azov_sea_area = 37800    # км²

result = total_area(black_sea_area, azov_sea_area)
print("Загальна площа Чорного та Азовського морів:", result, "км²")


print('task 8')
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
# необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.

def total_cost(monthly_payment, years):
    months = years * 12
    return monthly_payment * months

monthly_payment = 1179
years = 1.5

cost = total_cost(monthly_payment, years)
print("Вартість комп’ютера:", cost, "грн")

print('task 9')

# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі

def find_stock_counts(total, first_second, second_third):

    C = total - first_second
    B = first_second + second_third - total
    A = first_second - B

    return A, B, C

total_goods = 375291
first_second = 250449
second_third = 222950

A, B, C = find_stock_counts(total_goods, first_second, second_third)
print(f"Товари на першому складі: {A}")
print(f"Товари на другому складі: {B}")
print(f"Товари на третьому складі: {C}")

print('task 10')
#Ігор займається фотографією. Він вирішив зібрати всі свої 232
#фотографії та вклеїти в альбом. На одній сторінці може бути
#розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
#Ігорю, щоб вклеїти всі фото?

def pages_needed(total_photos, photos_per_page):
    pages = (total_photos + photos_per_page - 1) // photos_per_page
    return pages

total_photos = 232
photos_per_page = 8

pages = pages_needed(total_photos, photos_per_page)
print("Кількість сторінок, потрібних для всіх фото:", pages)