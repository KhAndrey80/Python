# "Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой."
from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    last_name = "Иванов"

    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue # перешли на новую иттерацию цикла


    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue # перешли на новую иттерацию цикла

    return [first_name, last_name, phone_number]

def create_file(file_name):
    # менеджер контекста 
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже существует")
            return
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def copy_row(file_name, row_number):
    rows = read_file(file_name)
    if row_number < 1 or row_number > len(rows):
        print("Неверный номер строки!")
        return

    row_to_copy = rows[row_number - 1]
    new_file_name = "copy_phone.csv"

    with open(new_file_name, "w", encoding='utf-8', newline='') as new_data:
        f_writer = DictWriter(new_data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerow(row_to_copy)

    print(f"Строка {row_number} скопирована в файл copy_phone.csv!")


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == "r":
            if not exists(file_name):
                print("Файл отсутствует, создайте его!")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его!")
                continue
            row_number = int(input("Введите номер строки для копирования: "))
            copy(file_name, row_number)

def copy(file_name, row_number):
    rows = read_file(file_name)
    if row_number < 1 or row_number > len(rows):
        print("Неверный номер строки!")
        return

    row_to_copy = rows[row_number - 1]
    new_file_name = "copy_phone.csv"

    with open(new_file_name, "w", encoding='utf-8', newline='') as new_data:
        f_writer = DictWriter(new_data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerow(row_to_copy)

    print(f"Строка {row_number} скопирована в файл copy_phone.csv!")


main()