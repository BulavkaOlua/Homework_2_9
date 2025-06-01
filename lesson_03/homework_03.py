#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
#task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
print("\n task 01")
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
print(alice_in_wonderland)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

print("\n task 02")

ap_counter=0
for character in alice_in_wonderland:
    if character=="'":
        print("O, я знайшла апостроф !!! -", character)
        ap_counter=ap_counter+1
print("Усього я знайшла ", ap_counter, "апострофа)")


# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\n task 03")
print(alice_in_wonderland)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("\n task 04")
S_Black_sea=436402
S_Azov_sea=37800
S_total=S_Black_sea+S_Azov_sea
print(S_total, " км2 займають Чорне та Азовське моря разом")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\n task 05")

total_sum_warehouse=375291
sum_first_and_second_warehouse=250449
sum_second_and_third_warehouse=222950

second_warehouse=sum_first_and_second_warehouse+sum_second_and_third_warehouse-total_sum_warehouse
first_warehouse=sum_first_and_second_warehouse-second_warehouse
third_warehouse=sum_second_and_third_warehouse-second_warehouse

print("На першому складі перебуває ", first_warehouse, " товарів")
print("На другому складі перебуває ", second_warehouse, " товарів")
print("На третьому складі перебуває ", third_warehouse, " товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

print("\n task 06")
months=18
payment=1179
vaztist=payment*months
print("Вартість комп’ютера становить ", vaztist, " гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print("\n task 07")

print("a) 8019 % 8 =",8019 % 8)
print("b) 9907 % 9 =",9907 % 9)
print("c) 2789 % 5 =",2789 % 5)
print("d) 7248 % 6 =",7248 % 6)
print("e) 7128 % 5 =",7128 % 5)
print("f) 19224 % 9 =",19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

print("\n task 08")

pizza_1_total=274*4
pizza_2_total=218*2
juice_total=35*4
cake_total=350*1
watter_total=21*3
party_cost_total=pizza_1_total+pizza_2_total+juice_total+cake_total+watter_total
print("Замовлення буде коштувати ", party_cost_total, " грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("\n task 09")

photos_total=232
one_page_photos=8
pages_all=photos_total//one_page_photos

remainder=pages_all%one_page_photos

if remainder>0:
    pages_all=pages_all+1
print(pages_all, " cрінок знадобиться Ігорю, щоб вклеїти всі фото")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

print("\n task 09")

distance=1600
spending_100=9
volume=48

volume_gas_1=distance/100*9
stop_need=distance/volume_gas_1
volume_gas_2=distance%volume_gas_1
if volume_gas_2>0:
    stop_need=stop_need+1

print(volume_gas_1, "літрів бензину знадобиться для такої подорожі")

print("родині необхідно заїхати на заправку", stop_need, "разів")


