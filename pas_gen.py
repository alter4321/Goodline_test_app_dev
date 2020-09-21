import random

"""
Объявляется функция генерации паролей. На
первом цикле добавляется по одному из необходимых
символов, на втором случайно добавляются символы, 
пока не наберется 12. В конце получившийся пароль
перемешивается.
"""


def generate_password():
    password = ''
    digit = '1234567890'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spesial = '!@#$%^&*()-+'

    var = 0

    while var < 5:
        i = var
        if i == 1:
            password += random.choice(digit)
        elif i == 2:
            password += random.choice(lower)
        elif i == 3:
            password += random.choice(upper)
        elif i == 4:
            password += random.choice(spesial)
        var += 1

    while var < 13:
        z = random.randint(1, 4)
        if z == 1:
            password += random.choice(digit)
        elif z == 2:
            password += random.choice(lower)
        elif z == 3:
            password += random.choice(upper)
        elif z == 4:
            password += random.choice(spesial)
        var += 1

    pass_list = list(password)
    random.shuffle(pass_list)
    shuffled_password = ''.join(pass_list)

    return shuffled_password


# Сама программа для анализа введенного пароля
# на соответсие требованиям.
while True:
    esc = 'Чтобы завершить введите "ok"\n'
    s = str(input('Придумайте пароль!'
                  '(Чтобы завершить введите "ok")\n'))
    if s == 'ok':
        break
    allow_digits = '1234567890'
    allow_lower = 'abcdefghijklmnopqrstuvwxyz'
    allow_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allow_specials = '!@#$%^&*()-+'
    attention = 'Ненадёжный пароль:'
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_special = 0
    bad_symbol = 0

    for a in s:
        if a.isupper():
            count_upper += 1
        if a.islower():
            count_lower += 1
        if a.isdigit():
            count_digit += 1
        for special in allow_specials:
            if a == special:
                count_special += 1
        if a not in (allow_digits + allow_lower +
                     allow_upper + allow_specials):
            bad_symbol += 1

    if count_digit < 1:
        attention += '\n-Необходимо добавить хотя бы 1 цифру!'

    if count_lower < 1:
        attention += '\n-Необходимо добавить хотя бы 1 букву'

    if count_upper < 1:
        attention += '\n-Необходимо добавить хотя бы 1 заглавную букву!'

    if count_special < 1:
        attention += '\n-Необходимо добавить хотя бы' \
                     ' 1 спецсимвол " ! @ # $ % ^ & * ( ) - + "'

    if len(s) < 12:
        attention += '\n-Необходимо, чтобы пароль был не короче 12 ' \
                     'символов! Ваш текущий пароль = '\
                     + str(len(s)) + ' символов!'

    if bad_symbol > 0:
        attention += '\n-Недопустимые символы! Используйте цифры 0-9,' \
                     ' латинские буквы \nи специальные символы ' \
                     '" ! @ # $ % ^ & * ( ) - + "!'

    if count_digit >= 1 and count_lower >= 1 and count_upper >= 1 \
            and count_special >= 1 and len(s) >= 12 and bad_symbol == 0:
        print('Этот пароль надёжный!')
        break

    else:
        print(attention + '\n\nРекомендуемый пароль: ' + generate_password())
