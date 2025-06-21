#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

input_str = input("Введіть числа розділяючи їх між собою за допомогою пробілу: ")

numbers = input_str.split()

total_sum = 0

for x in numbers:
    num = int(x)
    if num % 2 == 0:
        total_sum += num

if total_sum > 0:
    print("Сума парних чисел:", total_sum)
else:
    print("Парних чисел немає ")