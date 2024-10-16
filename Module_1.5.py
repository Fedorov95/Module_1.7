print('Кортежи')
Immutable_var = 1, 'tea', [1, 2], False
print(Immutable_var)
print(type(Immutable_var))
Immutable_var[2][1] = 'cold_tea'  # Кортеж относится к неизменяемым типам данных, изменить значения неизменяемых элементов кортежа можно только, если преобразовать кортеж или элемент кортежа в тип данных список (list)
print(Immutable_var)
print('Список')
mutable_list = [1, 'moon', 'sakura']
print(mutable_list)
print(type(mutable_list))
mutable_list.append(True)
print(mutable_list)
mutable_list[1] = 3
print(mutable_list)

Print = "Для чего нужна команда print()?"
print(type(Print))