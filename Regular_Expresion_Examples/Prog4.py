import re

rule = '[a-z]+[\d\W]'
s = input('Enter String')
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')
