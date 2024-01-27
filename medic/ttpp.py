import csv
def search_record(surname, date):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == surname and row[3] == date:
                return row
    return None
def print_sick_leave(record):
    if record is None:
        print('Запись не найдена')
    else:
        print('Фамилия И.О. пациента:', record[0])
        print('Пол:', record[1])
        print('Возраст:', record[2])
        print('Дата обращения:', record[3])
        print('Причина обращения в медпункт:', record[4])
        print('Больничный лист:')

def build_table():
    years = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            year = row[2].split('.')[-1]
            if year not in years:
                years.append(year)
    years.sort()
    table = '| Год | Число заболевших |\n'
    table += '|-----|-----------------|\n'
    for year in years:
        count = 0
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[2].split('.')[-1] == year:
                    count += 1
        table += f'| {year} | {count} |\n'
    return table

record = search_record('Иванов', '01.01.2022')
print_sick_leave(record)
table = build_table()
print(table)
