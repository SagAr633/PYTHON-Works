# +91(10 digits)
# vehicle registration number (KL11(az)4343)

# import re
# rules='[+][9][1]\d{10}'
# s=input('Enter Your Mobile Number')
# matcher=re.fullmatch(rules,s)
# if matcher is not None:
#     print('VALID')
# else:
#     print('NOT VALID')

import re
rule = '[a-z0-9\.]+[@][g][m][a][i][l][.][c][o][m]'
mail = input('enter mail')
matcher = re.fullmatch(rule,mail)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')