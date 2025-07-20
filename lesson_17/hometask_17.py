#--- 1. Власна функція ---
from my_function_3 import find_longest_word

result = find_longest_word()
print("Найдовше слово:", result)


# --- 2–6. Вбудовані модулі ---
import os
import sys
import math as m
from datetime import datetime
from collections import Counter

# --- 7–10. Вбудовані модулі з різними формами імпорту ---
from random import randint, choice
from functools import reduce as red
from json import *
import re

# --- 11–15. Популярні зовнішні бібліотеки (інстальовані у venv/Lib) ---
import numpy as np
from pandas import DataFrame
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

# --- 16–20. Інші приклади ---
import statistics
from pathlib import Path
from typing import List, Dict
from itertools import combinations as comb
from operator import itemgetter

# ----------------------------

# Використання імпортованих елементів:
words = ["сонце", "дерево", "комп'ютер", "ніч"]
print("Найдовше слово:", find_longest_word(words))

print("Поточна дата:", datetime.now())
print("Випадкове число:", randint(1, 100))
print("Сума [1, 2, 3]:", red(lambda x, y: x + y, [1, 2, 3]))
print("Квадратний корінь з 16:", m.sqrt(16))

sample_text = "тест тест тест код код"
print("Лічильник:", Counter(sample_text.split()))

print("Перевірка шаблону:", re.findall(r"\bкод\b", sample_text))

# Інші — просто щоб були використані:
_ = np.array([1, 2, 3])
_ = DataFrame({"a": [1, 2], "b": [3, 4]})
_ = Flask(__name__)
_ = requests.get("https://example.com")
_ = BeautifulSoup("<html></html>", "html.parser")
_ = Path(".").resolve()
_ = comb([1, 2, 3, 4], 2)
_ = itemgetter(0, 1)(("a", "b", "c"))
