import re

rule = '^a[\w\W]*b$'
s = 'aHVvbnFGHhgb'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')

import re

rule1 = '[a-z]'
s1 = 'asdfasf'
matcher = re.fullmatch(rule1, s1)
if matcher is not None:
    print('valid')
else:
    print('not valid')
