# Дан список чисел. Определите, сколько в нем встречается различных чисел.

import random

my_list = []
for _ in range(15):
    my_list.append(random.randint(0, 9))
print(my_list)
print(set(my_list))
