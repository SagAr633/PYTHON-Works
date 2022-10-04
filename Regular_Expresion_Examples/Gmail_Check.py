import re

rule = '[a-z0-9\.]+[@][g][m][a][i][l][.][c][o][m]'
s = input('Enter Gmail Id')
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')
