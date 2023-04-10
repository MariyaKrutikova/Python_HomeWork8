# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер # телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Функция считывания тел.книги
def read_phonebook(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        book = []
        for line in data:
            res = line.strip('\n').split(' ')
            book.append(res)
    return book

# Функция открывающая тел.книгу
def open_phonebook(filename):
    data = read_phonebook(filename)
    fields = ["Фамилия", "Имя", "Отчество", "Телефон", "Комментарий"]
    for line in data:
        res = dict(zip(fields, line))
        print(" Фамилия: ", res["Фамилия"], '\n', "Имя: ", res["Имя"], '\n', "Отчество: ", res["Отчество"], '\n',"Телефон: ", res["Телефон"], '\n', "Комментарий: ", res["Комментарий"], '\n')
    return res

def add_contact(filename):
    with open(filename, 'a', encoding='utf=8') as book:
        contact = input("Укажите данные контакта, который необходимо добавить в формате фамилия имя отчество телефон комментарий через пробел: ").split(',')
        book.write('\n' + ' '.join(contact))
    return book

# Функция нахождения абонента по фамилии
def find_by_last_name(filename):
    last_name = input("Укажите фамилию: ")
    data = read_phonebook(filename)
    for line in data:
        for name in line:
            if last_name == name:
                print(" Фамилия: ", line[0], '\n', "Имя: ", line[1], '\n', "Отчество: ", line[2], '\n',"Телефон: ", line[3], '\n', "Комментарий: ", line[4], '\n')
            
# Функция нахождения абонента по телефону
def find_by_phone_number(filename):
    phone_number = input("Укажите номер телефона: ")
    data = read_phonebook(filename)
    for line in data:
        for name in line:
            if phone_number == name:
                print(" Фамилия: ", line[0], '\n', "Имя: ", line[1], '\n', "Отчество: ", line[2], '\n',"Телефон: ", line[3], '\n', "Комментарий: ", line[4], '\n')

# Функция удаления абонента
def delete_contact(filename):
    contact_ditails = input("Укажите данные абонента, которого необходимо удалить или чьи данные необходимо изменить: ")
    data = read_phonebook(filename)
    for line in data:
        for name in line:
            if contact_ditails == name:
                data.remove(line)
    return data

# Функция изменения данных абонента
def change_contact(filename):
    newdata = delete_contact(filename)
    data = open('myphonebook.txt', 'w', encoding='utf=8')
    for list in newdata:
        newd = ' '.join(list)
        data.write(newd + '\n')
    data.close()
    data = add_contact(filename)
    return data

option = 0
while option != '7':
    print(' ')
    print('1 - вывести все контакты;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - добавить контакт;\n5 - удалить контакт;\n6 - изменить контакт;\n7 - завершить работу.')

    option = input('Укажите номер операции со справочником, которую необходимо выполнить:')
    print('  ')
    if option == '1':
        open_phonebook('myphonebook.txt')

    elif option == '2':
        find_by_last_name('myphonebook.txt')

    elif option == '3':
        find_by_phone_number('myphonebook.txt')

    elif option == '4':
        add_contact('myphonebook.txt')

    elif option == '5':
        newdata = delete_contact('myphonebook.txt')
        data = open('myphonebook.txt', 'w', encoding='utf=8')
        for list in newdata:
            newd = ' '.join(list)
            print(newd)
            data.write(newd + '\n')
        data.close()

    elif option == '6':
        change_contact('myphonebook.txt')
        
    else:
        print('Работа с телефонной книгой завершена.')

