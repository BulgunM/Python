# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

number = int(input('Введите целое число: '))

# i = 1
# fact = 1
# while i <= number:
#     fact *= i
#     i += 1
# print(f'Факториал числа {number} = {fact}')

fact = 1
for i in range(1, number + 1):
    fact *= i
print(f'Факториал числа {number} = {fact}')
