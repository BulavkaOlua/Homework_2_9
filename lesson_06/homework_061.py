#Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

stroka = input("Введіть строку: ")
count_unique_chars = set(stroka)
print(len(count_unique_chars) > 10)