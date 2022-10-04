import re

rule = '[\dA-Z]{5,8}'
s = 'ASFDF32'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')
