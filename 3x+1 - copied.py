from random import randrange

a = randrange(1, 9)
print(a)
if (a % 2) == 0:
    y = a / 2
while True:
    if (y % 2) == 0:
        y = y / 2
        print(y)
    else:
        b = (a * 3) + 1
while True:
    if (b % 2) == 0:
        b = b / 2
    else:
        b = (a * 3) + 1
    print(b)
