quantity = int(input('Количество элементов массива'))
numbers = [int(i) for i in input('Введите значения через пробел').split(' ')]

# Проверка соответсвия указанного и фактического количества элементов массива
if quantity != len(numbers):
    print('Указанное количество элементов не соответсвует фактическому')
else:
    pass

sign = []
result = []

# Каждый новый элемент попадает в 2 списка, если он уже
# есть в списке 'sign', тогда удаляется по индексу из
# результирующего списка
for el in numbers:
    if el not in sign:
        sign.append(el)
        result.append(el)
    else:
        if el in result:
            i = result.index(el)
            del result[i]

print(' '.join(str(i) for i in result))
