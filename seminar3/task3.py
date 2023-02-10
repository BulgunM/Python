# Напишите программу для печати
# всех уникальных значений в словаре.

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
    "VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]

my_dict = {'key1': 1231, 'key2': 34235}

my_set = set()
my_set_key = set()

for item in list:
    for key, value in item.items():
        my_set.add(value.strip())
        my_set_key.add(key.strip())


print(list)
print(my_set)
print(my_set_key)
