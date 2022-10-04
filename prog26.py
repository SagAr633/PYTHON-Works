import re
rule='A-Z{1}a-z{5,9}0-9{1}[@][g][m][a][i][l][.][c][o][m]'
s=input('Enter You G-mail Id')
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('VALID')
else:
    print('NOT VALID')