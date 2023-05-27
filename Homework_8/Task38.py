def print_help():
    print("  -= Телефонный справочник =-")
    print("1 - Показать всю книгу")
    print("2 - Найти контакт по фамилии, имени или телефону")
    print("3 - Изменить контакт")
    print("4 - Удалить контакт")
    print("5 - Добавить контакт")
    print("6 - Выход с сохранением")
    print("7 - Выход без сохранения")

def print_book():
    for n in data:
        print(n)


def find_cont():
    find_date = input("Введите данные для поиска - ")
    for n in data:
        if find_date in n:
            print(n)


def change_cont():
    find_date = input("Введите контакт для изменения - ")
    for n in range(len(data)):
        if find_date in data[n]:
            print(data[n])
            ch_date = input("Введите новые данные через пробел - Имя Фамилия Телефон (Enter - пропустить)")
            if ch_date == "":
                pass
            else:
                data[n] = ch_date


def del_cont():
    find_date = input("Введите контакт для удаления - ")
    for n in range(len(data)):
        if find_date in data[n]:
            print(data[n])

            if input("Для удаления контакта нажмите 1") == "1":
                data.pop(n)
                break


def add_cont():
    new_date = input("Введите новый контакт через пробел - Имя Фамилия Телефон (Enter - пропустить)")
    if new_date == "":
        pass
    else:
        data.append(new_date+"\n")


def exit_save():
    file_base = open("C:/Git/GB_Python_Homework/Homework_8/base.txt", "w")
    for n in data:
        file_base.write(n)
    file_base.close()
    print("Пока!")
    exit()


file_base = open("C:/Git/GB_Python_Homework/Homework_8/base.txt", "r")
data = file_base.readlines()
file_base.close()

print_help()

while True:
    command = input("Введите команду (Enter - help)")
    if command == "":
        print_help()
    if command == "1":
        print_book()
    if command == "2":
        find_cont()
    if command == "3":
        change_cont()
    if command == "4":
        del_cont()
    if command == "5":
        add_cont()
    if command == "6":
        exit_save()
    if command == "7":
        print("Пока!")
        exit()
