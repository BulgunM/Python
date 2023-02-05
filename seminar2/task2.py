# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

number = int(input('Введите натуральное число: '))

fibonacci_1 = 0
fibonacci_2 = 1
fibonacci_sum = 0
i = 3

while fibonacci_sum < number:
    fibonacci_sum = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_sum
    if number == fibonacci_sum:
        print(f'Число {number} является {i} по счету')
        break
    i += 1
else:
    print(-1)
