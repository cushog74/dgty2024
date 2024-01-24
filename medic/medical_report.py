import pandas as pd

def find_patient_record(last_name, date):
    data = pd.read_csv('patient_data.csv')
    filtered_data = data[(data['Фамилия'] == last_name) & (data['Дата об-ращения'] == date)]
    if filtered_data.empty:
        return "Записи с таким именем и датой об-ращения не найдено."
    else:
        return filtered_data.to_string()

def build_birth_year_table():
    data = pd.read_csv('patient_data.csv')
    birth_years = data['Дата об-ращения'].apply(lambda x: x.split('-')[0])
    birth_year_count = birth_years.value_counts().sort_index()
    return birth_year_count.to_string()

if __name__ == '__main__':
    last_name = input("Введите фамилию пациента: ")
    date = input("Введите дату об-ращения: ")
    print(find_patient_record(last_name, date))
    print(build_birth_year_table())