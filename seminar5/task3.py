# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым

# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

number = int(input('Введите целое число: '))


def simple_number(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


if simple_number(number):
    print('Простое')
else:
    print('Не простое')
