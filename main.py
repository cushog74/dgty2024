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