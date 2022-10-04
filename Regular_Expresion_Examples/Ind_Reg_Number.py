import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
s='KL11AZ6336'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('VALID')
else:
    print('NOT VALID')