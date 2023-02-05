# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

from random import randint

count_watermelon = int(input('Введите количество арбузов: '))

max_watermelon = 0  # идем от меньшего к большему
min_watermelon = 30000  # идем от большего к меньшему

for _ in range(1, count_watermelon + 1):
    weight_watermelon = randint(1, 30000)
    print(weight_watermelon)
    if weight_watermelon > max_watermelon:
        max_watermelon = weight_watermelon
    if weight_watermelon < min_watermelon:
        min_watermelon = weight_watermelon

print(max_watermelon, min_watermelon)
