a=[1,2,3]
i=int(input('Enter Index'))
try:
    print(a[i])
except Exception as error: #To find what error has occured
    #we use Exception module,which can find all types of error
    #and we store it to a variable.
    # (here the variable is 'error')
    print(error)