# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

list = [1, 2, 3, 4, 5]
number = int(input('Введите число, на которое сдвинем массив: '))

for _ in range(number):
    temp = list.pop(len(list)-1)
    list.insert(0, temp)

print(list)
