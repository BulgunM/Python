def print_menu():
    print('Это телефонный справочник. Выберите действие, которое нужно совершить: \n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакт\n'
          '5. Изменить контакт\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
    data = int(input('Введите номер необходимого действия: '))
    return data


while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print('Открыть файл')
        case 2:
            print('Сохранить файл')
        case 3:
            print('Показать контакты')
        case 4:
            print('Добавить контакт')
        case 5:
            print('Изменить контак')
        case 6:
            print('Найти контакт')
        case 7:
            print('Удалить контакт')
        case 8:
            print('Выход')
            break
