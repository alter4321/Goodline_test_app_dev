import re

ip = input('IP:')

check = re.match(r'(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])'
                 r'(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$', ip)

if check:
    print('YES')
else:
    print('NO')

