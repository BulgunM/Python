phone_book = []


def open_phone_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        print('Файл открыт')
        return phone_book


def save_phone_book():
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(i)


def show_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст!')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')))


def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст!')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append('\n' + user_info)


def change_phone_book():
    user_info = input('Введите номер контакта, который хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новые данные контакта: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)


def search_phone_book():
    user_input = input('Введите данные контакта, по которому будем искать: ')
    results = [i for i in phone_book if user_input in i]
    if len(results) == 0:
        print('Ничего не найдено!')
    else:
        for result in results:
            print(' '.join(result.split(';')))


def delete_phone_book():
    user_info = input('Введите номер контакта, который хотите удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            phone_book.pop(i)
            break
    else:
        print('Контакт не найден!')


phone_book = open_phone_book()
save_phone_book()
show_phone_book()
add_phone_book()
change_phone_book()
search_phone_book()
delete_phone_book()
