def rev(word):
    str=''
    index=len(word)
    while index>0:
        str+=word[index-1]
        index=index-1
    return str
print(rev('johnrambo1234'))


