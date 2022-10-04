def sumodd(r1,r2):
    sum=0
    for i in range(r1,r2+1):
        if i%2!=0:
            sum+=i
    return sum
print(sumodd(40,80))