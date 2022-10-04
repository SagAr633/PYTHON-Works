import re
f1=open('Reg_Num.txt','r')
f2=open('PY_Reg_Num','w')
rule='[L][U][M][1][1][P][Y]\d{2}'
for i in f1:
    reg=i.rstrip('\n')
    matcher=re.fullmatch(rule,reg)
    if matcher is not None:
        f2.write(reg)
        f2.write('\n')

