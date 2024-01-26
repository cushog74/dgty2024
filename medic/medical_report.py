import csv
def search_record(surname, date):
    with open('patients.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == surname and row[3] == date:
                return row
        return None
def print_sick_leave(record):
    if record:
        print("Больничный лист:")
        print(f"Фамилия И.О. пациента: {record[0]}")
        print(f"Пол: {record[1]}")
        print(f"Возраст: {record[2]}")
        print(f"Дата обращения: {record[3]}")
        print(f"Причина обращения в медпункт: {record[4]}")
    else:
        print("Запись не найдена")
def build_birthdate_table():
    birthdates = {}
    with open('patients.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            year = row[2].split('.')[-1]
            if year in birthdates:
                birthdates[year] += 1
            else:
                birthdates[year] = 1
    print("Таблица числа заболевших по дате рождения:")
    for year, count in birthdates.items():
        print(f"Год рождения: {year}, Количество заболевших: {count}")


record = search_record('Абрамович', '01.01.2022')
print_sick_leave(record)

build_birthdate_table()
