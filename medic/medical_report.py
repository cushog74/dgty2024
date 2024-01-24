import pandas as pd

def find_patient_by_surname_and_date(surname, date):
    data = pd.read_csv("patient_data.csv")
    filtered_data = data[(data["Фамилия"] == surname) & (data["Дата обращения"] == date)]
    return filtered_data

def build_yearly_disease_table(data):
    data["Дата обращения"] = pd.to_datetime(data["Дата обращения"]).dt.year
    yearly_disease_counts = data.groupby("Дата обращения").size()
    yearly_disease_counts.index = yearly_disease_counts.index.astype(str)
    return yearly_disease_counts

def main():
    surname = input("Введите фамилию пациента: ")
    date = input("Введите дату обращения: ")
    patient_record = find_patient_by_surname_and_date(surname, date)

    if not patient_record.empty:
        yearly_disease_counts = build_yearly_disease_counts(patient_record)
        print("Число заболевших по дате рождения:")
        print(yearly_disease_counts)
    else:
        print("Записи с таким именем и датой обращения не найдены.")

if __name__ == "__main__":
    main()