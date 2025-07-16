import pandas as pd

# RAW-посилання на файли CSV з GitHub
url1 = "https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_csv/r-m-c.csv"
url2 = "https://raw.githubusercontent.com/dntpanix/automation_qa/main/ideas_for_test/work_with_csv/random-michaels.csv"

# Зчитування обох файлів
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)

# Об'єднання та видалення дублікатів
combined = pd.concat([df1, df2])
result = combined.drop_duplicates()

# Збереження результату у файл
result.to_csv("result_Biriukova.csv", index=False)

print("✅ Файл result_Biriukova.csv збережено без дублікатів.")
