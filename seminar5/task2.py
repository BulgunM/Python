# Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.

from random import randint

count_grades = int(input('Введите количество оценок: '))
grades = []

for _ in range(count_grades):
    grades.append(randint(2, 5))
print(grades)

for i in range(len(grades)):
    if grades[i] == max(grades):
        grades[i] = min(grades)
print(grades)
