adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""



##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
print("task 01")
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("task 2")
adwentures_of_tom_sawer=adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)


# task 03 ==
print("task 3")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
import re
adwentures_of_tom_sawer=re.sub(r'\s+', ' ',adwentures_of_tom_sawer.strip())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("task 04")

kilkist_h=adwentures_of_tom_sawer.count("h")
print(kilkist_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("task_05")
Upper_case=[word for word in adwentures_of_tom_sawer.split()if word.istitle()]
print(len(Upper_case))


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("task_06")
First_place=adwentures_of_tom_sawer.find("Tom")
Second_place=adwentures_of_tom_sawer.find("Tom", First_place+1)
print(Second_place)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#adwentures_of_tom_sawer_sentences = None
print("task_07")
import re
adwentures_of_tom_sawer_sentences=re.split(r'(?<=[.!?]) +', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)



# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task_08")

if len(adwentures_of_tom_sawer)>=4:
    fourth_sentense=adwentures_of_tom_sawer_sentences[3].lower()
    print(fourth_sentense)
else:
    print("Четверте речння відсутнє")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("task_09")
start_by_the_time=any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print(start_by_the_time)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("task_10")
last_sentence=adwentures_of_tom_sawer_sentences[-1]
count_words=len(last_sentence.split())
print(count_words)