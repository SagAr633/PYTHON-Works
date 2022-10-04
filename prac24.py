n = 24
for i in range(2, 5 + 1):
    if n % 2 == 0:
        print('Not Weird')
        break
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
        break
    elif n % 2 != 0:
        print('Weird')
        break
    for l in range(6, 20 + 1):
        print('Weird')
        break




