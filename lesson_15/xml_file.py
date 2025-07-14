import os
import json
import logging

your_second_name = "Biriukova"
log_file_name = f"json__{your_second_name}.log"

# Налаштування логера
logging.basicConfig(filename=log_file_name, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_json_files(directory_path):
    """
    Перевіряє всі файли у вказаній директорії на валідність JSON.
    Логує помилки для невалідних файлів.
    """
    print(f"Починаємо перевірку файлів у директорії: {directory_path}")
    found_json_files = False

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # Перевіряємо, чи це файл і чи має він розширення .json
        if os.path.isfile(filepath) and filename.endswith('.json'):
            found_json_files = True
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    json.load(f)  # Спроба завантажити JSON
                print(f"Файл '{filename}' є валідним JSON.")
            except json.JSONDecodeError as e:
                error_message = f"Файл '{filename}' не є валідним JSON. Помилка: {e}"
                logging.error(error_message)
                print(error_message)
            except Exception as e:
                # Обробка інших можливих помилок (наприклад, проблем з кодуванням)
                error_message = f"Не вдалося прочитати файл '{filename}'. Помилка: {e}"
                logging.error(error_message)
                print(error_message)
        elif os.path.isfile(filepath):
            print(f"Файл '{filename}' не є JSON файлом (пропущено).")

    if not found_json_files:
        print("У вказаній директорії не знайдено жодного JSON файлу для перевірки.")


# Шлях до папки з файлами
# Використовуємо наданий вами шлях
folder_to_check = r'C:\Users\user\PycharmProjects\Homework_2_9\automation_qa-main\ideas_for_test\work_with_json'

if __name__ == "__main__":
    if os.path.exists(folder_to_check) and os.path.isdir(folder_to_check):
        validate_json_files(folder_to_check)
        print(f"\nПеревірку завершено. Деталі про невалідні файли дивіться у лог-файлі: {log_file_name}")
    else:
        print(f"Помилка: Папка '{folder_to_check}' не знайдена або не є директорією.")
        print("Будь ласка, переконайтесь, що шлях до папки вказано правильно і вона існує.")