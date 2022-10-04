import re

rule = '\d{2}[k][g]'
s = '24kg'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print('Valid')
else:
    print('Not_Valid')
