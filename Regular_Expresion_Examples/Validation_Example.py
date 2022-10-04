# use .fullmatch for validation insted of .finditer

import re
rule='\d{10}'
s=input('Enter Phone Number To Validate')
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('Number is Valid')
else:
    print('Number is Not Valid')