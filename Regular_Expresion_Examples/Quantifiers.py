# x='a+' a including group(min 1 to unlimited)
# x='a*' count including zero number of a:- count the postion where there's no a
# x='a?' count a as individual elements including zero no of a
# x='a{2}' count only 2 no of a's together(aa)
# x='a{2,3}' counts minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a
import re
count=0
x='a$'
matcher=re.finditer(x,'acdc aaabcd asbbdsia aabca')
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print('total count is',count)