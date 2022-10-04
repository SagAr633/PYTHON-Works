#Exception_Handling

u=int(input('enter num1'))
u2=int(input('enter num2'))
try:
    print(u/u2) #if num1 is 6 & num2 is 0 the output
    #will be an error,so we use try & excep to remove
    #that error from output.
    #Try block works all the time while Except works only
    #when there's an error in try block.
    #Try and Except must use together
except Exception as e:
    print(e)
finally:
    print('Inside finally') #not that important
    #When there's an error or not, it will always work.