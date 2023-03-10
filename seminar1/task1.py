"""
За день машина проезжает n километров. 
Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

**Input:**

n = 700

m = 750
"""

import math

dist_per_day = int(input('Машина проезжает за день(километров): '))
total_dist = int(input('Нужно проехать(километров): '))

# ceil округляет в большую сторону
days = math.ceil((total_dist + dist_per_day) / dist_per_day - 1)
print(f'Потребуется {days} дней')
