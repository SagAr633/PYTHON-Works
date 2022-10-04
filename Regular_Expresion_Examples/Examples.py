import re
count=0
# x='[abc]'  #either a b or c
# x='[^abc]' #except abc...count all elements except abc
# x='[a-z]' #a to z.. counts only small letters excludes space a upper case letters
# x='\s' # only counts space
# x='\w' #all charecters excepts special character(spaces,@\)
# x='\d' #counts only digits
x='\D' #counts all element except digits
matcher=re.finditer(x,'abc hello hai ABC@abraham')
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print('Total Count Is',count)

# .finditer:- to find an element in a string
# .start:- to find the index(postion) of the element in string
# .group:- to print the element we are searching