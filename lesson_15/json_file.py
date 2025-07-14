import os
import json
import logging

# Налаштування логера
logging.basicConfig(
    filename="json__Olha.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Шлях до папки з json-файлами
folder_path = r"C:\Users\user\PycharmProjects\Homework_2_9\automation_qa-main\ideas_for_test\work_with_json"

# Перевірка кожного .json файлу
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)  # спроба зчитати JSON
        except json.JSONDecodeError as e:
            logging.error(f"{filename} - Невалідний JSON: {e}")
        except Exception as e:
            logging.error(f"{filename} - Інша помилка: {e}")
