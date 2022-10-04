import re
rule='\d[\w\W]{3,8}\d'
s=input('Enter String')
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('Valid')
else:
    print('Not Valid')