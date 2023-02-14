# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# *Пример: *

# [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]
print(numbers)

new_list = []

my_dict = {}

for i in numbers:
    my_dict[i] = my_dict.get(i, 0) + 1

for j in my_dict:
    if my_dict.get(j) == 1:
        new_list.append(j)

print(f'Уникальные элементы: {new_list}')
