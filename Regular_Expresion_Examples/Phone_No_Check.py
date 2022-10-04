import re
f=open('Phone_NO.txt','r')
rule='[+][9][1]\d{10}'
for i in f:
    num=i.rstrip()
    matcher=re.fullmatch(rule,num)
    if matcher is not None:
        print(num)