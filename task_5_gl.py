q_first_set = int(input('Количество элементов первого списка'))
numbers_first_set = {int(i) for i in input('Введите значения через пробел').split(' ')}
q_second_set = int(input('Количество элементов второго списка'))
numbers_second_set = {int(i) for i in input('Введите значения через пробел').split(' ')}
numbers_full_set = set()
numbers_full_set.update(numbers_first_set)
numbers_full_set.update(numbers_second_set)
same_digit_list = []

if q_first_set != len(numbers_first_set):
    print('Несовпадение указанного и фактического количества элементов')
else:
    pass
if q_second_set != len(numbers_second_set):
    print('Несовпадение указанного и фактического количества элементов')
else:
    pass


if len(numbers_first_set) > 100000 or len(numbers_second_set) > 100000:
    print('Неверное условие, количиство элементов одного списка более 100000')
    sys.exit()
else:
    pass


for i in numbers_full_set:
    if i in numbers_first_set and i in numbers_second_set:
        same_digit_list.append(i)

sorted(same_digit_list)

print(' '.join(str(i) for i in same_digit_list))
