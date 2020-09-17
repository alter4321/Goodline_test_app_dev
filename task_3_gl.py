quantity = int(input('Количество элементов массива'))
numbers = [int(i) for i in input('Введите значения через пробел').split(' ')]

if quantity != len(numbers):
    print('Указанное количество элементов не соответсвует фактическому')
else:
    pass

sign = []
result = []

for el in numbers:
    if el not in sign:
        sign.append(el)
        result.append(el)
    else:
        if el in result:
            i = result.index(el)
            del result[i]

print(' '.join(str(i) for i in result))
