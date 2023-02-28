
# class Car:

#     # year = 2023

#     def __init__(self, model: str, color: str, volume: float):
#         self.model = model
#         self.color = color
#         self.volume = volume

#     def gas(self):
#         print('Брррррр!')

#     def present(self):
#         return f'Это машина {self.model}, {self.color} цвета и объем {self.volume}'

#     def __str__(self) -> str:
#         return f'Это машина {self.model}, {self.color} цвета и объем {self.volume}'


# ferrari = Car('F355', 'red', 6.0)
# bmw = Car('M3', 'black', 5.0)

# print(ferrari.color)
# print(bmw.color)

# bmw.color = 'green'

# print(ferrari.color)
# print(bmw.color)

# ferrari.sport = True

# print(ferrari.sport)
# print(bmw.sport)

# ferrari.gas()
# bmw.gas()

# print(ferrari.present())
# print(bmw.present())

# print(ferrari.year)
# print(bmw.year)

# print(ferrari)
# print(bmw)


class Calc:

    def __init__(self, a: int, b: int):
        ''' Это калькулятор. Принимает 2 числа и производит арифметические действия
        '''
        self.a = a
        self.b = b

    def summ(self):
        '''Возвращает сумму двух чисел
        '''
        return self.a + self.b

    def power(self):
        return self.a ** self.b


number = Calc(4, 5)

print(number.summ())
print(number.power())

# help(number)
