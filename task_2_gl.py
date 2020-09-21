v = int(input('V='))
t = int(input('T='))
res = 0

# Проверка условий задачи
if 0 <= t <= 1000:
    pass
else:
    print('Недопустимые условия')
    sys.exit()

if -1000 <= v <= 1000:
    pass
else:
    print('Недопустимые условия')
    sys.exit()
# Формула рассчета
res = (v * t) % 109

print(res)
