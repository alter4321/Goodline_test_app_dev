n = int(input('n='))
m = int(input('m='))
x = int(input('x='))
y = int(input('y='))
xr = 0
yr = 0
f = 0
g = 0

# Проверка наличия Яши в пределах бассейна
if x > n:
    print("Недопустимое условие")
    sys.exit()
elif y > m:
    print("Недопустимое условие")
    sys.exit()

# Выявление ближнего бортика на одной оси
xr = n - x
yr = m - y

if xr < 0:
    xr = abs(xr)
if yr < 0:
    yr = abs(yr)

if x <= xr:
    f = x
else:
    f = xr

if y <= yr:
    g = y
else:
    g = yr
# Выбор самого ближнего бортика
if f < g:
    print(f)
else:
    print(g)
