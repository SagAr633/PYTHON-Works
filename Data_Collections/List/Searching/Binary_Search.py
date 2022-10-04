# Binary Search
l=[7,4,8,2,9,1,5,7,2,6,1]
def binarysearch(u):
    l.sort()
    #u=int(input('Enter an Element')) #6
    lowerindex=0
    upperindex=len(l)-1 #11-1=10
    flag=0
    while lowerindex<=upperindex:
        mid=(lowerindex+upperindex)//2 #mid=10/2=5
        if u<l[mid]:
            upperindex=mid-1
        elif u>l[mid]:
            lowerindex=mid+1 #5+1=6
        elif u==l[mid]: #u=6=l[mid]=6
            flag=1 # yes
            break
    if flag==0:
        print('Not_Present')
    else:
        print('Present') #yes
binarysearch(9)
