import pandas as pd

def search_patient_record(last_name, date):
    df = pd.read_csv('patients_data.csv')
    record = df[(df['ФИО'].str.contains(last_name)) & (df['Дата обращения'] == date)]
    return record

def generate_sick_count_table():
    df = pd.read_csv('patients_data.csv')
    df['Год рождения'] = pd.to_datetime(df['Дата обращения']).dt.year - df['Возраст']
    sick_count_table = df.groupby('Год рождения').size().reset_index(name='Число заболевших')
    return sick_count_table

if __name__ == "__main__":
    last_name = "Иванов"
    date = "2022-01-15"
    record = search_patient_record(last_name, date)
    print(f"Запись по пациенту {last_name} от {date}:\n{record}\n")

    sick_count_table = generate_sick_count_table()
    print("Таблица числа заболевших по дате рождения:\n", sick_count_table)

df = pd.read_csv('patients_data.csv')

def find_patient_record(last_name, date_of_visit):
    result = df[(df['ФИО'].str.contains(last_name, case=False)) & (df['Дата обращения'] == date_of_visit)]

    if not result.empty:
        print(result[['ФИО', 'Дата рождения', 'Возраст', 'Дата обращения', 'Причина обращения']])
    else:
        print("Запись не найдена.")


last_name_input = input("Введите фамилию пациента: ")
date_of_visit_input = input("Введите дату обращения (гггг-мм-дд): ")

find_patient_record(last_name_input, date_of_visit_input)