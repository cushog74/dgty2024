import pandas as pd

data = pd.read_csv("patients.csv", delimiter=";")

surname = input("Введите фамилию пациента: ")
date = input("Введите дату обращения (в формате дд.мм.гггг): ")
filtered_data = data[(data["Фамилия И.О."] == surname) & (data["Дата обращения"] == date)]

if len(filtered_data) > 0:
    print("Больничный лист:")
    print(filtered_data)
else:
    print("Запись не найдена")

birth_dates = pd.to_datetime(data["Дата обращения"]).dt.year
count_by_year = birth_dates.value_counts().sort_index()
table = pd.DataFrame(count_by_year, columns=["Число заболевших"])
print("Таблица числа заболевших по дате рождения:")
print(table)