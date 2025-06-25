#Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
# Наприклад:
#[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
#Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
#Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і
# вивести “Не можу це зробити!”

def sum_of_numbers_in_string(s):
    try:
        numbers = s.split(",")
        total = 0
        for num in numbers:
            total += int(num)
        return total
    except ValueError:
        return "Не можу це зробити!"

# список строк
strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# обробляємо кожен елемент списку
for s in strings:
    result = sum_of_numbers_in_string(s)
    print(result)