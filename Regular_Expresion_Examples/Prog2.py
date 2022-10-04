import re
rule='\d{1}[A-Z]+' # + means there's no limit on the letters
s=input('Enter String')
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("Valid")
else:
    print('Not Valid')